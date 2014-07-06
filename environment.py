import os

class environment:
    def __init__(self):
        self.environment = os.path.dirname(os.path.realpath(__file__))

        if '/Users/stevendao' in str(self.environment):
            self.workingdir = '/Users/stevendao/Dropbox/Programming/alerter/'
            self.logdir = '/Users/stevendao/Dropbox/Programming/alerter/log/'
            self.historydir = '/Users/stevendao/Dropbox/Programming/alerter/history/'

        if '/home/stevendao' in str(self.environment):
            self.workingdir = '/home/stevendao/alerter/'
            self.logdir = '/home/stevendao/webapps/sdao/log/'
            self.historydir = '/home/stevendao/alerter/history/'

        if not os.path.exists(self.workingdir):
            os.makedirs(self.workingdir)

        if not os.path.exists(self.logdir):
            os.makedirs(self.logdir)

        if not os.path.exists(self.historydir):
            os.makedirs(self.historydir)