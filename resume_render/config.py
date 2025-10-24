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
            'out_dir': "~/.config/resume-render/out"
        }
        path_opts = ['tmpl_dir', 'data_dir', 'out_dir']

        super().__init__("resume-render", extra_defaults, path_opts)
