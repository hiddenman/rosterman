#!/usr/bin/python

import pwd,grp,string,re,os,include;


def get_remote_users(host):
    """ Return remote user list """
    users=[];
    try:
        fd=os.popen(include.ssh+' '+host+' getent passwd');
        users_t=fd.readlines();
        for user in users_t:
            users.append(tuple(string.split(user,':')));
    except:
        print 'Error while executing remote command'
    
    return users;

def get_remote_groups(host):
    """ Return remote group list """
    groups=[];
    try:
        fd=os.popen(include.ssh+' '+host+' getent group');
        groups_t=fd.readlines();
        for group in groups_t:
            groups.append(tuple(string.split(group,':')));
    except:
        print 'Error while executing remote command'
    
    return groups;

def get_uname(login,users):
    """ Return full username by login """
    uname='';
    for user in users:
        if (login==user[0]):
            uname=user[4];
            break;
    if (uname==''):
        return login
    else:
        return user[4]
    
def get_fluname(uname):
    """ Return first and last username """
    uname_s=string.split(uname,' ');
    if (len(uname_s)==3):
        return (uname_s[0],uname_s[2])
    elif (len(uname_s)==2):
        return (uname_s[0],uname_s[1])
    else:
        return (uname_s[0],uname_s[0])

def get_ugroups(login,groups=''):
    """ Return user group by login """
    ugroups=[];
    gre=re.compile(include.excludegroups);
    if (groups==''):
        groups=grp.getgrall();        
    if (include.debug):
        print 'User '+login       
    for group in groups:
        if (login in group[3]):
            if ((gre.match(group[0])!=None) or (int(group[2])<include.mingid)):
                if (include.debug):                
                    print 'Skip group '+group[0]                
                continue;            
            ugroup=group[0];
            for replace in include.replacegroups:
                rgre=re.compile(replace);                
                if (rgre.match(ugroup)!=None and ugroup!=''):
                    if (include.debug):
                        print 'Replace is '+replace
                        print 'Group '+ugroup+' is replaced with '+str(include.replacegroups[replace])
                    ugroup=include.replacegroups[replace];                    
            for predicate in include.predicategroups:
                grpe=re.compile(predicate);
                if ((grpe.match(ugroup))!=None and ugroup!=''):
                    if (include.debug):
                        print 'Predicate is '+predicate
                        print 'Group '+ugroup+' is predicated with '+str(include.predicategroups[predicate])                    
                    ugroup=include.predicategroups[predicate]+ugroup;
            for ureplace in include.replaceusersgroups:
                urgre=re.compile(ureplace);
                print ureplace
                if (urgre.match(login)!=None and ugroup!=''):
                    if (include.debug):
                        print 'UserReplace is '+ureplace                        
                        print 'Group '+ugroup+' is replaced with personal user group '+str(include.replaceusersgroups[ureplace])
                    ugroup=include.replaceusersgroups[ureplace];          

            # FIXME                
            # ugroups.append(ugroup.decode('cp1251').encode('utf-8'));
            if (ugroup!=''):
                ugroups.append(ugroup);
#            if (include.debug):
#                print 'User '+login+' added to group '+ugroups[0];

    if (include.debug):
        print 'User '+login+' has '+str(len(ugroups))+' groups:'
        for ugroup in ugroups:
            print ugroup
    return ugroups
