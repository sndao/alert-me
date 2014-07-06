from pastebin_python import pastebin
from environment import environment

class publish_pb:
    def __init__(self):
        self.env = environment()
        self.key = self.env.pastebin_key


    def get_paste(self, links):
        links_str = ''
        for link in links:
            links_str += str(link).strip() + '\n'

        pasteBin = pastebin.PastebinPython(api_dev_key=self.key)
        url = pasteBin.createPaste(api_paste_code=links_str,
                          api_paste_name='Eventbrite Links',
                          api_paste_format='text',
                          api_paste_private=0,
                          api_paste_expire_date='1D')

        return url


