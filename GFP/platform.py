#!/usr/bin/env python
#encoding:utf8

"""
这个地方的逻辑是：
如果发现有bid在新的广告位上竞价，那么之前此用户的竞价作废，归零
"""

import copy

class PlatForm(object):
    def __init__(self, bids):
        self.bids = copy.deepcopy(bids)

    def update(self, body_name, bid_id, price):
        # body name
        # bid = (bid_id, price, bef)
        if bid_id is None:
            self.erase(body_name)
            return
        self.bids[bid_id]['price'] = price
        self.bids[bid_id]['name'] = body_name
        for _bid_id in self.bids:
            if _bid_id == bid_id:
                continue
            if self.bids[_bid_id]['name'] == body_name:
                self.bids[_bid_id]["name"] = None
                self.bids[_bid_id]["price"] = 0

    def erase(self, body_name):
        ''' erase the body bidding in self.bids
        '''
        for bid_id, bid_info in self.bids.iteritems():
            if bid_info['name'] == body_name:
                self.bids[bid_id]['name'] = None
                self.bids[bid_id]['price'] = 0

    def get_status(self):
        return copy.deepcopy(self.bids)

    def __str__(self):
        p_lst = []
        for k, v in self.bids.iteritems():
            v_str = k+'['+'|'.join("%s:%s"%(_k,_v) for _k, _v in v.iteritems())+']'
            p_lst.append(v_str)
        return '\t'.join(p_lst)

