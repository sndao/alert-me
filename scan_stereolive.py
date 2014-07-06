from BeautifulSoup import BeautifulSoup, SoupStrainer
from timekeeper import timekeeper
from logger import logger
from environment import environment
from mailer import mailer
from subscriber import subscriber
import os
import urllib2


class stereolive:
    def __init__(self):
        self.module = 'SL'
        self.env = environment()
        self.tk = timekeeper()
        self.mail = mailer()
        self.sub = subscriber(self.module)
        self.log = logger(self.env, self.module)

    def scan(self):
        self.tk.start_time()
        pageFile = urllib2.urlopen('http://stereolivehouston.com/events/')
        pageHtml = pageFile.read()
        pageFile.close()
        soup = BeautifulSoup("".join(pageHtml))
        soup.find()
        sAll = soup.findAll("span")
        stereo_file = []
        artist_list = []

        if not os.path.exists(self.env.historydir + "stereo.txt"):
            f = file(self.env.historydir + "stereo.txt", "w")
            f.close()

        with open(self.env.historydir + "stereo.txt", 'r+') as f:
            stereo_file = f.readlines()
            #print stereo_file

            for x in sAll:
                #print x
                x = str(x)
                if '<span class="artist">' in x:
                    artist = x.replace('<span class="artist">','').replace('</span>','').strip()
                    artist_list.append(artist)

                    if (artist + '\n') not in stereo_file:
                        send_line = artist + ' @StereoLive \n\nhttp://stereolivehouston.com/events/'
                        print send_line
                        f.write(artist + '\n')
                        for i in xrange(3):
                            self.mail.compose('', send_line, self.sub.list)
        self.tk.end_time()
        self.log.log(self.tk)
        print self.tk.timing
