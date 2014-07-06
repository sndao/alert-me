from BeautifulSoup import BeautifulSoup, SoupStrainer
from timekeeper import timekeeper
from logger import logger
from environment import environment
from mailer import mailer
from subscriber import subscriber
import os
import urllib2
import re


class nightculture:
    def __init__(self):
        self.module = 'NC'
        self.env = environment()
        self.tk = timekeeper()
        self.mail = mailer()
        self.sub = subscriber(self.module)
        self.log = logger(self.env, self.module)
        self.eventbrite_raw = []
        self.eventbrite_links = []

    def scan(self):
        self.tk.start_time()

        pageFile = urllib2.urlopen('http://nightculture.com/upcoming-events/')
        pageHtml = pageFile.read()
        pageFile.close()
        soup = BeautifulSoup("".join(pageHtml))
        soup.find()
        sAll = soup.findAll("a")
        self.eventbrite_raw = soup.findAll("a")


        stereo_file = []
        artist_list = []


        if not os.path.exists(self.env.historydir + "nightculture.txt"):
            f = file(self.env.historydir + "nightculture.txt", "w")
            f.close()

        if not os.path.exists(self.env.historydir + "nightculture_links.txt"):
            f = file(self.env.historydir + "nightculture_links.txt", "w")
            f.close()

        with open(self.env.historydir + "nightculture.txt", 'r+') as f:
            nc = f.readlines()
            flag = False
            #print stereo_file

            for x in sAll:
                x = str(x)
                if 'Houston' in x and '<a title="' in x:
                    x = x.replace('<a title="', '')
                    #print x
                    artist = x[:x.index('" h')-12]
                    #print artist

                    if (artist + '\n') not in nc:
                        flag = True
                        send_line = artist + '" @NightCulture \n\nhttp://nightculture.com/upcoming-events/'
                        print send_line
                        f.write(artist + '\n')
                        for i in xrange(2):
                            self.mail.compose('', send_line, self.sub.list)
            if flag:
                self.tk.end_time()
                self.log.log(self.tk)
                print self.tk.timing
                return True

        self.tk.end_time()
        self.log.log(self.tk)
        print self.tk.timing
        return False


    def get_eventbrite(self):

        with open(self.env.historydir + "nightculture_links.txt", 'r+') as f:
            stereo_links = f.readlines()

            for s in self.eventbrite_raw:
                try:
                    match = re.search(r'href=[\'"]?([^\'" >]+)', str(s))
                    if match and 'eventbrite' in str(s):
                        matched_link = str(match.group(1)).strip()
                        print matched_link
                        self.eventbrite_links.append(matched_link)

                        if matched_link not in str(stereo_links):
                            f.write(matched_link + '\n')

                except:
                    print "Could not get EventBrite link."
                    pass

        return self.eventbrite_links
