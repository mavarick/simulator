#!/usr/bin/env python
#encoding:utf8
import pdb

from adbody import AdBody
from platform import PlatForm

import time
def simu():
    b1 = AdBody(1, 10)
    b2 = AdBody(2, 4)
    b3 = AdBody(3, 2)

    bids = {}
    bids["bid1"] = {"click": 200, "price": 0, "name": None}
    bids["bid2"] = {"click": 100, "price": 0, "name": None}
    pf = PlatForm(bids)

    n = 100
    while n>0:
        #pdb.set_trace()
        b1.bid(pf)
        b2.bid(pf)
        b3.bid(pf)

        print "%s   %s" % (n, str(pf))
        n -= 1

simu()






