#!/usr/bin/python

import include,re

for ureplace in include.replaceusersgroups:
    print ureplace;
    urgre=re.compile(ureplace);                
    if (urgre.match('sh1a')!=None):
        print 'match'
