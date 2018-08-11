#!/usr/bin/env python3

import os

from jinja2 import Template
import yaml

base_dir = os.path.expanduser("~/var/docs/resume/")
data_file = os.path.join(base_dir, "resume-data.yaml")
template_file = os.path.join(base_dir, "content.xml.j2")
content_file = os.path.join(base_dir, "content.xml")

with open(data_file) as fh:
    resume_data = yaml.load(fh)

with open(template_file) as fh:
    template = Template(fh.read())

content = template.render(**resume_data)

with open(content_file, 'w') as fh:
    fh.write(content)