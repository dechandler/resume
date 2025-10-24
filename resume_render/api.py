
import logging
import os

import docxtpl
import jinja2
import yaml

from declib import DeclibApi

from .data import RenderDataLoader


log = logging.getLogger("resume-render")


class RenderApi(DeclibApi):

    def __init__(self, config):

        super().__init__(config)


    def get_data(self, data_name):

        data_path = os.path.join(self.config['data_dir'], f"{data_name}.md")
        return RenderDataLoader(data_path).data


    def render(self, tmpl_name, data_name, out_name):

        data = self.get_data(data_name)

        template_files = os.listdir(self.config['tmpl_dir'])
        for f in template_files:
            fname, extension = os.path.splitext(f)
            if fname == tmpl_name:
                tmpl_path = os.path.join(self.config['tmpl_dir'], f)
                break

        out_path = os.path.join(self.config['out_dir'], f"{out_name}{extension}")
        os.makedirs(self.config['out_dir'], exist_ok=True)

        if extension == ".docx":
            self.render_docx(tmpl_path, data, out_path)

        elif extension == ".md":
            self.render_markdown(tmpl_path, data, out_path)


    def render_markdown(self, tmpl_path, data, md_out_path):

        with open(tmpl_path) as fh:
            tmpl = jinja2.Template(fh.read())

        out = tmpl.render(**data)

        with open(md_out_path, 'w') as fh:
            fh.write(out)

    def render_docx(self, tmpl_path, data, out_path):

        tmpl = docxtpl.DocxTemplate(tmpl_path)
        tmpl.render(data, autoescape=True)
        tmpl.save(out_path)


    def docx_to_pdf(self, docx_path, out_dir):

        log.info(f"Converting {docx_path} into a PDF file in {out_dir}")
        self.run_command(
            [
                "soffice",
                "--convert-to", "pdf",
                "--outdir", out_dir,
                docx_path
            ],
            print_stdout=False, log_stdout=True,
            print_stderr=False, log_stderr=True

        )
