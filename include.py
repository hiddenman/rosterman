#!/usr/bin/python

from utils import *
#from seqdict import seqdict
from ordereddict import oDict
# some constants
false=0
true=1

# where is ssh
ssh='/usr/bin/ssh'



# exclude matching groups from roster
excludegroups='^Domain|^Admin|^Schem|^Enter|^Group|^Dns|^Пользователь|^topol|^sales|^eva5|^pos|^guest';

# exclude matching users from roster
excludeusers='^Domain|^Admin|^topol|^admin|^guest|^iusr_|^iwam_|^tsinternet|^kassa|^kostya';

# replace matching groups
replacegroups=oDict(
    {
    'evaadmins':'Супермаркет Варус1::ИТ',
    'security':'Супермаркет Варус1::Безопасность',
    'purchase':'Супермаркет Варус1::Менеджеры',
    'accounting':'Супермаркет Варус1::Бухгалтерия',
    'personal':'Супермаркет Варус1::Кадры',
    'operationist':'Супермаркет Варус1::Операционисты',
    'administration':'Супермаркет Варус1::Управление',
    'brigadiers':'Супермаркет Варус1::Бригадиры',                    
    'secretary':'Супермаркет Варус1::Секретариат',
    'development':'Супермаркет Варус1::Отдел Развития',
    'Тополь':'Супермаркет Варус1::Офис',
    'Buhgalter':'Супермаркет Варус2::Бухгалтерия',
    'evausers':'Супермаркет Варус1::Офис',
    'Manager':'Супермаркет Варус2::Менеджеры',
    'of_buh':'Супермаркет Варус2::Офис::Бухгалтерия',
    'of_opr':'Супермаркет Варус2::Офис::Операционисты',
    'of_pro':'Супермаркет Варус2::Офис::Отдел продаж',
    'of_top':'Супермаркет Варус2::Офис::Дирекция',
    'of_zak':'Супермаркет Варус2::Офис::Отдел закупок',
    'Ohrana':'Супермаркет Варус2::Безопасность',
    'Operator':'Супермаркет Варус2::Операционисты',
    'sklad':'Супермаркет Варус2::Кладовщики',
    'st1':'Центральный склад',
    'Top':'Супермаркет Варус2::Дирекция',
    'zaladmin':'Супермаркет Варус2::Администраторы торгового зала',
    'zal':'Супермаркет Варус2::Операторы торгового зала',                                            
    'Магазин Варус2':'Супермаркет Варус2::Офис',
    'Отдел ИТ':'',
    'Офис::$':'',    
    'Отдел ПО':'Офис::Отдел ИТ::Отдел ПО',
    'Отдел ТО':'Офис::Отдел ИТ::Отдел ТО',
    'Отдел СО':'Офис::Отдел ИТ::Отдел СО',
    'Техподдержка':'Офис::Отдел ИТ::Техподдержка'
    }
    )
    

# add predicate groups for matchins groups
predicategroups=oDict(
    {   
    '^Магазин Ева':'Магазины::Ева::',
    '^Супермаркет Планета':'Супермаркеты::Планета::',
    '^Супермаркет ПГТ':'Супермаркеты::ПГТ::',        
    '^Варус':'Супермаркеты::Варус::',
    '^Супермаркет Варус':'Супермаркеты::Варус::',        
    '(?!^Магазин|^Варус|^Супермаркет|^Центральный склад|^Офис)':'Офис::'
    }
    )
    

# add matching users to groups
replaceusersgroups=oDict(
    {
    'aid':'Офис::Отдел ИТ',        
    'sh.*a':'Магазины::Ева::Управляющие',
    'sh.*b':'Магазины::Ева::Кладовщики',
    'sh.*c':'Магазины::Ева::Менеджеры по инвентаризации',
    'pgt.*a':'Супермаркеты::ПГТ::Управляющие',
    'pgt.*b':'Супермаркеты::ПГТ::Кладовщики',
    'pgt.*c':'Супермаркеты::ПГТ::Менеджеры по инвентаризации',    
    'sh2c':'Магазины::Ева::Управляющие'
    }
    )
    
    

# start UID from this
minuid=501;

# start GID from this
mingid=501;

# default jid domain for local users
domain='jabber.office.eva.dp.ua'
# e-mail domain for e-mails in jud
emaildomain='eva.dp.ua'

# xml stuff
rosterstart="<xdb><query xmlns='jabber:iq:roster' xdbns='jabber:iq:roster'>";
rosterend="</query></xdb>";

judstart="<xdb><foo xdbns='jabber:jud:users' xmlns='jabber:jud:users'>"
judend="</foo></xdb>"

authstart="<xdb><password xmlns='jabber:iq:auth' xdbns='jabber:iq:auth'>";
authend="</query><query xmlns='jabber:iq:last' last='0000000000' xdbns='jabber:iq:last'>Disconnected</query></xdb>";


#  company name
company='ООО РУШ'


# debug?
debug=1

