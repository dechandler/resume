"""


"""
import logging

from declib import DeclibConfig


log = logging.getLogger("resume-render")


class RenderConfig(DeclibConfig):

    def __init__(self):

        extra_defaults = {
            'tmpl_dir': "~/.config/resume-render/templates",
            'data_dir': "~/.config/resume-render/resume-data",
            'docx_out_dir': "~/.config/resume-render/docx-out",
            'pdf_out_dir': "~/.config/resume-render/pdf-out"
        }
        path_opts = ['tmpl_dir', 'data_dir', 'docx_out_dir', 'pdf_out_dir']

        super().__init__("resume-render", extra_defaults, path_opts)
