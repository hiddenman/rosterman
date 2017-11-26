#!/usr/bin/python
#

import pwd,grp,string,re,os,include,utils;
from roster import *;
from jud import *;
from pwdgrp import *;

def build_users_xml_by_user(template='./template_login.xml',xmldir='./private',rosterdir='./roster',otherdir='./other',judfile='./global.xdb',withjud=include.true,domains=[]):
    """ Build full xml with settings for user and return it """
    users=[];
    if (domains==[]):
        raw=include.false;
        users.append((pwd.getpwall(),grp.getgrall(),include.domain))
    else:
        raw=include.true;
        for tuple in range(len(domains)):
            host=domains[tuple][0]
            domain=domains[tuple][1]
            rusers=get_remote_users(host)
            rgroups=get_remote_groups(host)
            users.append((rusers,rgroups,domain))
            
        users.insert(0,(pwd.getpwall(),grp.getgrall(),include.domain))
        
    
    ure=re.compile(include.excludeusers);
    try:
        os.makedirs(xmldir);
        os.makedirs(rosterdir);
        os.makedirs(otherdir);                
    except:
        pass
    try:
        tfd=file(template,'r');
        tplbuf=tfd.read();
        tfd.close();
    except:
        print 'Error opening template file [%s] for reading' % str(template);
        return -1;

    if (withjud):
        jud=build_jud_by_user(users[0][0]);
    
        try:
            jfd=file(judfile,'w+')
            jfd.write(jud);
            jfd.close();
        except:
            print 'Error creating JUD XML file [%s] ' % str(judfile);

    
    roster=include.rosterstart;
    for users_t in users:
        roster+=build_roster_by_user(users=users_t[0],groups=users_t[1],domain=users_t[2],raw=include.true);
    roster+=include.rosterend;
    
    for user in users[0][0]:
        if ((ure.match(user[0])!=None) or (int(user[2])<include.minuid)):
            if (include.debug):
                print 'Skip user %s' % str(user[0])            
            continue
        if (include.debug):
            print 'Creating user %s' % str(user[0])
        try:
            xfd=file(xmldir+'/'+user[0]+'.xml','w+')
        except:
            print 'Error creating user XML file [%s] ' % str(xmldir+'/'+user[0]);
            continue
        try:
            rfd=file(rosterdir+'/'+user[0]+'.xml','w+')            
        except:
            print 'Error creating user XML file [%s] ' % str(rosterdir+'/'+user[0]);
            continue
        try:
            ofd=file(otherdir+'/'+user[0]+'.xml','w+')            
        except:
            print 'Error creating user XML file [%s] ' % str(otherdir+'/'+user[0]);
            continue


        ofd.write(include.authstart+user[0] \
                  +"</password><query xmlns='jabber:iq:register' xdbns='jabber:iq:register'><username>" \
                  +user[0]+"</username><x xmlns='jabber:x:delay' stamp='"+str(utils.get_datetime_stamp())+"'>registered</x>" \
                  +include.authend);
        ofd.close();
                  
       
        replaces={};

        #uname=(get_uname(user[0],users[0][0]).decode('cp1251').encode('utf-8'));
        uname=(get_uname(user[0],users[0][0]));        
        (funame,luname)=get_fluname(uname);
        
        replaces['TEMPLATE_LOGIN']=user[0];
        replaces['TEMPLATE_PASSWORD']=user[0];
        replaces['TEMPLATE_NICK']=user[0];
        replaces['TEMPLATE_FIRSTNAME']=funame;
        replaces['TEMPLATE_LASTNAME']=luname;
        replaces['TEMPLATE_COMPANY']=include.company;
        replaces['TEMPLATE_DEPARTMENT']=get_ugroups(user[0]).decode('cp1251').encode('utf-8');
        replaces['TEMPLATE_EMAIL']=user[0]+'@'+include.emaildomain;

        rep_keys=replaces.keys();
        rep_keys.sort(lambda a, b: cmp(len(b), len(a)));
        tplbuf_t=tplbuf;
        for r in rep_keys:
            tplbuf_t = tplbuf_t.replace(r, str(replaces[r]).decode('cp1251').encode('utf-8'));
        xfd.write(tplbuf_t);
        xfd.close();

        rfd.write(roster);
        rfd.close()
