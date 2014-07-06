#   Return a list of subscribers for the specific module

STEREOLIVE = 1
NIGHTCULTURE = 2
EASTBAY = 3
FINISHLINE = 4
NIKE = 5

STEVEN_EMAIL = 'stevennguyendao@gmail.com'
STEVEN_PHONE = '7135384209@messaging.sprintpcs.com'


class subscriber:
    def __init__(self, module):
        self.STEVEN_PHONE = STEVEN_PHONE
        if module == 'SL':
            self.list = [STEVEN_EMAIL]
        if module == 'NC':
            self.list = [STEVEN_EMAIL]