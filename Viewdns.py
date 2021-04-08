#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup

print(""" 
    
DDDDD   NN   NN  SSSSS   CCCCC  HH   HH EEEEEEE  CCCCC  KK  KK EEEEEEE RRRRRR  
DD  DD  NNN  NN SS      CC    C HH   HH EE      CC    C KK KK  EE      RR   RR 
DD   DD NN N NN  SSSSS  CC      HHHHHHH EEEEE   CC      KKKK   EEEEE   RRRRRR  
DD   DD NN  NNN      SS CC    C HH   HH EE      CC    C KK KK  EE      RR  RR  
DDDDDD  NN   NN  SSSSS   CCCCC  HH   HH EEEEEEE  CCCCC  KK  KK EEEEEEE RR   RR     
    
                                                           Powered By The Serum    
    
""")

while True:
    dns = raw_input("Sorgulamak Istediginiz Web Adresini Giriniz: ")

    headers1 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36 Opera/9.80 "}
    url = "https://viewdns.info/reverseip/?host={}&t=1".format(dns)
    r = requests.get(url, headers=headers1)
    soruce = BeautifulSoup(r.content,"html.parser")
    site = soruce.find_all("table",{"border":"1"})
    for i in site:
        siteler = i.text
        bol = siteler.split(" ")
        bol.remove("Date")
        bol.remove("Resolved")
        bol.remove("DomainLast")
        for r in bol:
            a = len(str(r)) - 10
            dosya = open("list.txt","a")
            dosya.write(r[0:a]+"\n")
            dosya.close
