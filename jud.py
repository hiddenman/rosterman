#!/usr/bin/python
#

import pwd,grp,string,re,os,include;
from pwdgrp import *;

def build_jud_by_user(users='',raw=include.false):
    """ Build full jud and return it """
    if (users==''):
        users=pwd.getpwall();
    ure=re.compile(include.excludeusers);
    if (raw):
        jud=''
    else:
        jud=include.judstart;
    for user in users:
        if ((ure.match(user[0])!=None) or (int(user[2])<include.minuid)):
            continue
        uname=(get_uname(user[0],users).decode('cp1251').encode('utf-8'));
        uname_s=string.split(uname,' ');
        (funame,luname)=get_fluname(uname);
        jud+="<item jid='"+user[0]+'@'+include.domain+"'><name>"+uname \
                 +"</name><first>"+funame+"</first><last>"+luname+"</last><nick>"+user[0] \
                 +"</nick><email>"+user[0]+"@"+include.emaildomain+"</email></item>";
    if (not raw):
        jud+=include.judend;
    return jud;
