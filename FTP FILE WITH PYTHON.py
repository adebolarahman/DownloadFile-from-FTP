#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import ftplib
# import os
# ftp_srv = '196.46.20.7'
# ftp_usr = 'Access-Oyesanmi'
# ftp_pass = '2R{HqbO!$<'
# port=23
# ftp = ftplib.FTP(ftp_srv,'anonymous')
# ftp.login(ftp_usr, ftp_pass)


# In[3]:


from ftplib import FTP
import os
import paramiko
import os
import datetime
from datetime import datetime
from FTP_Credentials import *


# In[4]:


import paramiko
transport = paramiko.Transport((host, port))
transport.connect(username = username, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)
print ("Connected.")


# In[5]:


sftp.listdir_attr()[1]


# In[6]:


sftp.listdir()[1]


# In[7]:


from datetime import datetime, time, timedelta

# today_midnight = datetime.combine(datetime.today(), time.min)
# yesterday_midnight = today_midnight - timedelta(days=1)
# yesterday_midnight


# In[8]:


# latest = 0
# latestfile = None
# for file in sftp.listdir():
#     if file.startswith('ACCESS DAILY APPROVED') and datetime.datetime.strptime(file,"ACCESS DAILY APPROVED *_%Y-%m-%d.xlsx"):
#         latest = fileattr.st_mtime
#         latestfile = fileattr.filename
#         print(latestfile)
            


# In[9]:


from datetime import datetime, timedelta
Yesterday_date =datetime.strftime(datetime.now() - timedelta(1), '%Y_%m_%d')
Yesterday_date


# In[10]:


from datetime import datetime, timedelta
Yesterday_date_alternative =datetime.strftime(datetime.now() - timedelta(1), '%d_%m_%Y')
Yesterday_date_alternative


# In[11]:


# if 'Access Approved Daily Transx with RRN_Domestic 2020_07_19.xlsx'[-15:-5] == Yesterday_date:
#     print("yes")


# In[13]:


import fnmatch
import os
import glob
from datetime import datetime
path =r'\\abp-filesvr06\general\eric\pos\settlement\INTERSWITCH'+'\\'
for file in sftp.listdir():
     if  file.lower().startswith('access approved daily')and file[-15:-5]==Yesterday_date and file.endswith('.xlsx'):
            print(file)
            file_local = path + file
            sftp.get(file,file_local)
            
     elif file.lower().startswith('access approved daily')and file[-15:-5]==Yesterday_date_alternative and file.endswith('.xlsx'):
        print(file)
        sftp.get(file,file)


# In[36]:


# path =r'\\abp-filesvr06\general\eric\pos\settlement\INTERSWITCH'+'\\'+file
# for file in sftp.listdir():
#     if  file.lower().startswith('access approved daily')and file[-15:-5]==Yesterday_date and file.endswith('.xlsx'):
#         print(file)
#         sftp.get(file,path)


# In[25]:


"Access Approved Daily Transx with RRN_Domestic 21_07_2020.xlsx"


# In[26]:


def prior_day(Yesterday_date=datetime.now()):
    return datetime.strftime(datetime.now() - timedelta(1), '%Y/%m/%d')


# In[27]:


prior_day(datetime.now())


# In[ ]:




