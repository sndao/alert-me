import os

class environment:
    def __init__(self):
        self.environment = os.path.dirname(os.path.realpath(__file__))
        self.pastebin_key = '2577c46b7a098facc631429e3304f1d3'

        if '/Users/stevendao' in str(self.environment):
            self.workingdir = '/Users/stevendao/Dropbox/Programming/alert-me/'
            self.logdir = '/Users/stevendao/Dropbox/Programming/alert-me/log/'
            self.historydir = '/Users/stevendao/Dropbox/Programming/alert-me/history/'
            self.credentials_file = '/Users/stevendao/Documents/Credentials/credentials.txt'


        if '/home/stevendao' in str(self.environment):
            self.workingdir = '/home/stevendao/alerter/'
            self.logdir = '/home/stevendao/webapps/sdao/log/'
            self.historydir = '/home/stevendao/alerter/history/'
            self.credentials_file = '/home/stevendao/credentials/credentials.txt'


        with open(self.credentials_file, 'r') as file:
            creds = file.readlines()
            for x in creds:
                x = x.strip()
                if 'reddit_username' in x:
                    self.reddit_username = x[x.index('=')+1:]
                if 'reddit_password' in x:
                    self.reddit_password = x[x.index('=')+1:]

        if not os.path.exists(self.workingdir):
            os.makedirs(self.workingdir)

        if not os.path.exists(self.logdir):
            os.makedirs(self.logdir)

        if not os.path.exists(self.historydir):
            os.makedirs(self.historydir)


if __name__ == '__main__':

    env = environment()
    print env.reddit_username
    print env.reddit_password