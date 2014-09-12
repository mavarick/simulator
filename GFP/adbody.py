#!/usr/bin/env python
#encoding:utf8

import pdb
"""
这个地方的逻辑应该是：
1，如果发现当前竞价的广告价格增加了，那么进行全局搜索进行竞价；
2，如果发现当前竞价的广告价格不变，那么找小于自己竞价的最大价格进行竞价；
"""

PRICE_CHANGE_STEP = 0.1
class AdBody(object):
    def __init__(self, name, income):
        self.name = name
        self.income = income

        self.current_bid = {"bid": None, "price": None}

    def get_cur_best_choice(self, status):
        # the status came from outside to support the body make decision
        best_choice = None
        for bid_id, bid_cond in status.iteritems():
            name = bid_cond['name']
            click = bid_cond["click"]
            price = bid_cond["price"]

            if self.name == name:
                new_price, _name= self.find_max_plantorm_price(price, status)
                new_price = new_price if name==_name else new_price + PRICE_CHANGE_STEP
            else:
                new_price = price + PRICE_CHANGE_STEP
            bef = self.cal_benefit(click, new_price)
            if not best_choice:
                best_choice = (bid_id, new_price, bef)
            if bef > best_choice[2]:
                best_choice = (bid_id, new_price, bef)
        return best_choice

    def find_max_plantorm_price(self, price, status):
        bids_sort = sorted(status.values(), key=lambda x:x["price"])
        prices = [t["price"] for t in bids_sort]
        index = prices.index(price)
        index = index if index ==0 else index - 1
        return prices[index], bids_sort[index]['name']

    def cal_benefit(self, click, price):
        # find the most benefit under self condition and outside condition
        bef = (self.income - price) * click
        return bef

    def bid(self, plat_form):
        # update the plat_form the decision this body has made
        status = plat_form.get_status()
        cur_best_choice = self.get_cur_best_choice(status)
        #print "%s # %s # %s" % (self.name, cur_best_choice, status)
        bid_id, price, bef = cur_best_choice
        if bef < 0:
             bid_id = None
             price = 0
        plat_form.update(self.name, bid_id, price)

