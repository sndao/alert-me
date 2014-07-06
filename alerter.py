from environment import environment
from scan_stereolive import stereolive
from scan_nightculture import nightculture
from publish_pastebin import publish_pb
from mailer import mailer
from subscriber import subscriber

env = environment()
sl = stereolive()
nc = nightculture()
mail = mailer()

if sl.scan():
    print 'Stereo Live'
    sub = subscriber('SL')
    links = sl.get_eventbrite()
    pb = publish_pb()
    pb_str = str(pb.get_paste(links))
    mail.compose(subj='', message='StereoLive: ' + pb_str, to_list=sub.list)

if nc.scan():
    print 'Nightculture'
    sub = subscriber('NC')
    links = nc.get_eventbrite()
    pb = publish_pb()
    pb_str = str(pb.get_paste(links))
    mail.compose(subj='', message='Nightculture: ' + pb_str, to_list=sub.list)