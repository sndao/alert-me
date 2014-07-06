from BeautifulSoup import BeautifulSoup, SoupStrainer
from timekeeper import timekeeper
from logger import logger
from environment import environment
from mailer import mailer
from subscriber import subscriber
import os
import urllib2


class nightculture:
    def __init__(self):
        self.module = 'NC'
        self.env = environment()
        self.tk = timekeeper()
        self.mail = mailer()
        self.sub = subscriber(self.module)
        self.log = logger(self.env, self.module)


    def scan(self):
        self.tk.start_time()

        pageFile = urllib2.urlopen('http://nightculture.com/upcoming-events/')
        pageHtml = pageFile.read()
        pageFile.close()
        soup = BeautifulSoup("".join(pageHtml))
        soup.find()
        sAll = soup.findAll("a")
        stereo_file = []
        artist_list = []

        if not os.path.exists(self.env.historydir + "nightculture.txt"):
            f = file(self.env.historydir + "nightculture.txt", "w")
            f.close()

        with open(self.env.historydir + "nightculture.txt", 'r+') as f:
            nc = f.readlines()
            #print stereo_file

            for x in sAll:
                x = str(x)
                if 'Houston' in x and '<a title="' in x:
                    x = x.replace('<a title="', '')
                    #print x
                    artist = x[:x.index('" h')-12]
                    #print artist

                    if (artist + '\n') not in nc:
                        send_line = artist + '" @NightCulture \n\nhttp://nightculture.com/upcoming-events/'
                        print send_line
                        f.write(artist + '\n')
                        for i in xrange(3):
                            self.mail.compose('', send_line, self.sub.list)

        self.tk.end_time()
        self.log.log(self.tk)
        print self.tk.timing
