#!/usr/bin/python
#

import pwd,grp,string,re,os,include;
from pwdgrp import *;

def build_roster_by_user(users='',groups='',domain=include.domain,raw=include.false):
    """ Build full roster and return it """
    if (users==''):
        users=pwd.getpwall();
    if (groups==''):
        groups=grp.getgrall();
    ure=re.compile(include.excludeusers);
    if (raw):
        roster=''
    else:
        roster=include.rosterstart;
    for user in users:
        if ((ure.match(user[0])!=None) or (int(user[2])<include.minuid)):
            if (include.debug):
                print 'Skip user %s' % str(user[0])
            continue
        if (include.debug):
            print 'Add user %s to roster' % str(user[0])                    
        uname=(get_uname(user[0],users).decode('cp1251').encode('utf-8'));
        ugroups=get_ugroups(user[0],groups);
        for ugroup in ugroups:
            if (ugroup==""):
                continue
            roster+="<item jid='"+user[0]+'@'+domain+"' name='"+uname \
                     +"' subscription='both'><group>"+(ugroup.decode('cp1251').encode('utf-8'))+"</group><autoauth/></item>";
    if (not raw):
        roster+=include.rosterend;
    return roster;

