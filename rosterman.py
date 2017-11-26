#!/usr/bin/python
#
# ToDo:

import pwd,grp,string,re,os,include,xml;


        
        



domains=[('192.168.100.1','v1.varus.dp.ua'),('192.168.102.253','v2.varus.dp.ua')]
#domains=[]
xml.build_users_xml_by_user(domains=domains,xmldir='./private/jabber.office.eva.dp.ua',
                            rosterdir='./roster/jabber.office.eva.dp.ua',
                            otherdir='./other/jabber.office.eva.dp.ua',
                            judfile='./private/users.jabber.office.eva.dp.ua/global.xdb');



