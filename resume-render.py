#!/usr/bin/env python3

import json
import logging
import os
import sys

from collections import OrderedDict
from subprocess import Popen

import yaml

import docxtpl


name = "David Chandler"

log = logging.getLogger('resume-render')

def read_data_file(path):

    with open(path) as fh:
        doc_lines = fh.read().splitlines()

    data = {
        'name': 'root',
        'data_path': [],
        'header_depth': 0,
        'content': None,
        'children': OrderedDict(),
        'render_children_as_list': False
    }

    previous = data
    block_lines = []
    for line in doc_lines:

        # Skip if comment line
        if line.startswith("//"):
            continue

        # If not a header line, add to block and move on to next line
        if not line.startswith("#"):
            block_lines.append(line)
            continue

        # Load previous block lines into content 
        previous['content'] = yaml.safe_load('\n'.join(block_lines))


        # Parse header line
        split_line = line.split()
        header_depth = len(split_line.pop(0))
        render_children_as_list = False
        if split_line and split_line[0] == "-":
            render_children_as_list = True
            split_line.pop(0)

        element_name = ' '.join(split_line)

        if header_depth > previous['header_depth']:
            # Going deeper - entry is child of previous
            parent = previous

        else:
            # Moving up or sibling
            # Start from root and follow path of children to find parent
            parent = data
            for node_name in previous['data_path']:
                node = parent['children'][node_name]
                if header_depth <= node['header_depth']:
                    break
                parent = node

        parent['children'][element_name] = {
            'name': element_name,
            'data_path': [ *parent['data_path'], element_name ],
            'header_depth': header_depth,
            'content': None,
            'children': OrderedDict(),
            'render_children_as_list': render_children_as_list
        }

        block_lines = []
        previous = parent['children'][element_name]

    # Load content into last element
    previous['content'] = yaml.safe_load('\n'.join(block_lines))

    print(data)

    restructured = restructure_data(data)
    print(restructured)
    return restructured

def restructure_data(data):

    if type(data['content']) is dict:
        data['content']['name'] = data['name']

    if not data['children']:
        return data['content']


    cleaned_data = OrderedDict()
    if data['content']:
        if type(data['content']) is dict:
            cleaned_data.update(data['content'])
        else:
            cleaned_data['content'] = data['content']

    for child in data['children'].values():
        child_data = restructure_data(child)

        cleaned_data[child['name']] = child_data

    if data['render_children_as_list']:
        cleaned_data = [ *cleaned_data.values() ]

    return cleaned_data


def generate_pdf(docx_path, out_dir):

    cmd = [
        "soffice",
        "--convert-to", "pdf",
        "--outdir", out_dir,
        docx_path
    ]
    Popen(cmd).communicate()


if __name__ == "__main__":

    resume_dir = os.path.dirname(os.path.abspath(
        sys.argv.pop(0)
    ))
    if not sys.argv:
        sys.argv = ["print", "default"]
    resume_type = sys.argv.pop(0)

    if not sys.argv:
        sys.argv = ["default"]
    data_doc = sys.argv.pop(0)

    data_file = os.path.join(resume_dir, "data", f"{data_doc}.md")
    tmpl_file = os.path.join(resume_dir, "templates", f"{resume_type}.docx")
    docx_out_file = os.path.join(
        resume_dir, f"{'-'.join(name.split())}_resume-{resume_type}.docx"
    )
    # pdf_out_file = os.path.join(
    #     resume_dir, f"{'-'.join(name.split())}_resume-{resume_type}.pdf"
    # )

    data = read_data_file(data_file)

    tmpl = docxtpl.DocxTemplate(tmpl_file)
    tmpl.render(data, autoescape=True)
    tmpl.save(docx_out_file)

    # commented until & manual step is cleaned up
    #generate_pdf(docx_out_file, resume_dir)
