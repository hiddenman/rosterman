#!/usr/bin/python
# переделать все как на cvs
# убирать пробелы и прочее в начале/конце
# экранировать всякую фигню

import pwdgrp,os,base64,string
#os.makedirs('ldap');
ldif=file('ldap/rush.ldif','w+');


# office
users=pwdgrp.get_remote_users('192.168.1.200');
for user in users:
    if (int(user[2])<=500):
        continue
    login=user[0]
    uname=user[4]
    if (uname==''):
        uname=login
    (fname,lname)=pwdgrp.get_fluname(uname)
    uname=((fname+' '+lname).decode('cp1251').encode('utf-8'))
    fname=base64.encodestring(fname.decode('cp1251').encode('utf-8'))
    lname=base64.encodestring(lname.decode('cp1251').encode('utf-8'))    
    dn=string.replace((base64.encodestring('cn='+uname+',ou=int,ou=addressbook,ou=office,o=eva,dc=dp,dc=ua')),'\n','')+'\n'
    ldif.write('dn:: '+dn)
    ldif.write('objectClass: officePerson\n')
    ldif.write('cn:: '+base64.encodestring(uname))
    ldif.write('sn:: '+lname)
    ldif.write('givenName:: '+fname)
    ldif.write('mail: '+login+'@eva.dp.ua\n')
    ldif.write('o:: '+base64.encodestring('ООО "РУШ"'.decode('cp1251').encode('utf-8')))        
    ldif.write('\n')
    
# varus1    
users=pwdgrp.get_remote_users('192.168.100.1');
for user in users:
    if (int(user[2])<500):
        continue
    login=user[0]
    uname=user[4]
    if (uname==''):
        uname=login
    (fname,lname)=pwdgrp.get_fluname(uname)        
    uname=((fname+' '+lname).decode('cp1251').encode('utf-8'))    
    fname=base64.encodestring(fname.decode('cp1251').encode('utf-8'))
    lname=base64.encodestring(lname.decode('cp1251').encode('utf-8'))
    dn=string.replace((base64.encodestring('cn='+uname+',ou=int,ou=addressbook,ou=office,o=eva,dc=dp,dc=ua')),'\n','')+'\n'
    ldif.write('dn:: '+dn)
    ldif.write('objectClass: officePerson\n')
    ldif.write('cn:: '+base64.encodestring(uname))
    ldif.write('sn:: '+lname)
    ldif.write('givenName:: '+fname)
    ldif.write('mail: '+login+'@v1.varus.dp.ua\n')
    ldif.write('o:: '+base64.encodestring('ООО "ОМЕГА"'.decode('cp1251').encode('utf-8')))        
    ldif.write('\n')
    
# varus2
users=pwdgrp.get_remote_users('192.168.102.253');
for user in users:
    if (int(user[2])<500):
        continue
    login=user[0]
    uname=user[4]
    if (uname==''):
        uname=login
    (fname,lname)=pwdgrp.get_fluname(uname)        
    uname=((fname+' '+lname).decode('cp1251').encode('utf-8'))    
    fname=base64.encodestring(fname.decode('cp1251').encode('utf-8'))
    lname=base64.encodestring(lname.decode('cp1251').encode('utf-8'))
    dn=string.replace((base64.encodestring('cn='+uname+',ou=int,ou=addressbook,ou=office,o=eva,dc=dp,dc=ua')),'\n','')+'\n'
    ldif.write('dn:: '+dn)
    ldif.write('objectClass: officePerson\n')
    ldif.write('cn:: '+base64.encodestring(uname))
    ldif.write('sn:: '+lname)
    ldif.write('givenName:: '+fname)
    ldif.write('mail: '+login+'@v2.varus.dp.ua\n')
    ldif.write('o:: '+base64.encodestring('ООО "БЭТТА"'.decode('cp1251').encode('utf-8')))    
    ldif.write('\n')


ldif.close();

ldif=file('ldap/suppliers.ldif','w+');
csv=file('suppliers.csv','r')
users=csv.readlines()
csv.close()
for user in users:
    fields=string.split(user,',')
    if (string.count(fields[4],'@')==0):
        print 'Invalid string '+user
        continue
    email=fields[4]
    fname=fields[0]
    lname=fields[1]
    if (fname==''):
        fname=email
    if (lname==''):
        lname=email        
    uname=((fname+' '+lname).decode('cp1251').encode('utf-8'))    
    fname=string.replace(base64.encodestring(fname.decode('cp1251').encode('utf-8')),'\n','')+'\n'
    lname=string.replace(base64.encodestring(lname.decode('cp1251').encode('utf-8')),'\n','')+'\n'
    dn=string.replace((base64.encodestring('cn='+uname+',ou=ext,ou=addressbook,ou=office,o=eva,dc=dp,dc=ua')),'\n','')+'\n'
    cn=string.replace(base64.encodestring(uname),'\n','')+'\n'
    ldif.write('dn:: '+dn)
    ldif.write('objectClass: officePerson\n')
    ldif.write('cn:: '+cn)
    ldif.write('sn:: '+lname)
    ldif.write('givenName:: '+fname)
    ldif.write('mail: '+email+'\n')
    ldif.write('\n')

ldif.close()
