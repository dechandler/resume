
import logging
import os

import docxtpl
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


    def render(self, tmpl_name, data_name, docx_out_name):

        tmpl_path = os.path.join(self.config['tmpl_dir'], f"{tmpl_name}.docx")
        docx_out_path = os.path.join(self.config['docx_out_dir'], f"{docx_out_name}.docx")

        tmpl = docxtpl.DocxTemplate(tmpl_path)
        tmpl.render(self.get_data(data_name), autoescape=True)

        tmpl.save(docx_out_path)


    def generate_pdf(self, docx_path, out_dir):

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
