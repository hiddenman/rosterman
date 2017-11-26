#!/usr/bin/python

from datetime import datetime;
from UserDict import UserDict

def get_datetime_stamp():
    """ Return datetime stamp """
    now=datetime.now();
    return now.strftime('%Y%m%dT%k:%M:%S')
#20041202T19:20:20

