#!/usr/bin/env python

import os
import sys

import urllib2
import json
import datetime

lastdock = sys.argv[1] if len(sys.argv) > 1 else 'BBI' # 'BRE'
routes = dict(BBI="SEA-BI", BRE="SEA-BR")

req = urllib2.Request("http://www.wsdot.com/ferries/vesselwatch/Vessels.ashx")
opener = urllib2.build_opener()
f = opener.open(req)
v = json.load(f)

bi = [v for v in v["vessellist"] if v["route"] == routes[lastdock] and v['lastdock_abbrev'] == lastdock]
t = bi[0]["eta"]
try:
    dt = datetime.datetime
    t = dt.strptime("%s%s" % (bi[0]["eta"], bi[0]["etaAMPM"]), '%I:%M%p')
    eta = dt.today().replace(hour=t.hour,minute=t.minute)
    t = eta - dt.now()
    t = "Next boat from %s arrives %d minutes from now" % (lastdock, t.seconds / 60.0)
    os.system("osascript -e 'display notification \"{}\" with title \"Ferry\"'".format(t))
except:
    print("No ETA ... next boat's still docked")
    sys.exit(1)
