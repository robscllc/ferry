#!/usr/bin/env bash

wget -O - http://www.wsdot.com/ferries/vesselwatch/Vessels.ashx | \
jq '.vessellist | map(select(.route == "SEA-BI" and .aterm_abbrev == "BBI")) | .[0] | .eta + .etaAMPM' | \
grep -v null | \
xargs -I foo php -r 'echo floor((strtotime("foo") - strtotime("now"))/60);' | \
xargs -I foo -0 espeak --stdout -a 300 -s 125 "rob, please leave for the ferry in foo minutes" | play -
