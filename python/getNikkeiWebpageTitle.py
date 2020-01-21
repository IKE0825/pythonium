# coding: UTF-8
import requests
res = requests.get('https://daiseki-eco.cybozu.com/g/message/view.csp?cid=&rid=&mid=976&nid=3755120&module_id=grn.message/')
#print(res.tesxt)
with open('tonari-it.html','w')as file:
    file.write(res.text)