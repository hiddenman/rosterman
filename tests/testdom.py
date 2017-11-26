#!/usr/bin/python
# добавлять нового пользователя и уведомлять всех об этом или только того, кому добавили?
from xml.dom.minidom import *

jids=[]
dom = parse("./abel.xml")
elements = dom.getElementsByTagName("item")
for element in elements:
    jids.append(element.getAttribute('name'))

print (jids)



