"""

"""
from declib import DeclibCli

from .api import RenderApi

class MainCli(DeclibCli):

    def __init__(self, config):
        """


        """
        super().__init__(config)

        self.operations = {
            'render': {
                'aliases': ['r'],
                'handler': self.render,
                'help': "Do the thing"
            }
        }
        self.no_matching_args_operation = 'render'

    def render(self, args):

        data_name = args.pop(0)
        tmpl_name = args.pop(0)

        api = RenderApi(self.config)
        api.render(tmpl_name, data_name, f"{data_name}-{tmpl_name}")

        # docx_out_path = os.path.join(self.config['docx_out_dir'], f"{docx_out_name}.docx")
        # api.generate_pdf(self.config['docx_out_dir'], self.config['pdf_out_dir'])
