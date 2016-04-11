#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib, re, datetime
# import re

def get_external_ip():
    site = urllib.urlopen("http://checkip.dyndns.org/").read()
    grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', site)
    address = grab[0]
    return address

if __name__ == '__main__':
  ip = ( get_external_ip() )

date = datetime.datetime.now().time()


with open("Output.txt", "w") as text_file:
    text_file.write("Dış IP Adresi: %s" % ip + " Tarih: %s" % date)