from environment import environment
from scan_stereolive import stereolive
from scan_nightculture import nightculture

env = environment()

sl = stereolive()
sl.scan()

nc = nightculture()
nc.scan()
