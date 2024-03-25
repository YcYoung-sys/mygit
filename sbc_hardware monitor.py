#! /usr/bin/python
import sys
import os
import paramiko
import time
import re

host = '10.254.173.112'
username = 'weiqyang'
password = '8$3|tB+l'
port = 22

command = 'show environment \n'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host,username=username, password=password, port=port, look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh.exec_command(command)
output = stdout.readlines()
#print(' '.join(map(str, output)))
Env = (' '.join(map(str, output)))
#print(Env)

file1 = open('/export/home/weiqyang/SBC/me01peesb088/Env.txt', 'w+')
file2 = open('/export/home/weiqyang/SBC/me01peesb088/CiscoEnv.txt', 'w')
print(Env,file=file1 )

with open('/export/home/weiqyang/SBC/me01peesb088/Env.txt','r',encoding = 'utf-8') as fr,open('/export/home/weiqyang/SBC/me01peesb088/CiscoEnv.txt','w',encoding = 'utf-8') as fd:
    for text in fr.readlines():
        if text.split():
            fd.write(text)
    print('输出成功....')

f = open('/export/home/weiqyang/SBC/me01peesb088/CiscoEnv.txt', 'r')
f3 = open('/export/home/weiqyang/SBC/me01peesb088/alarms.txt', 'w+')

import linecache
text1=linecache.getline(r'/export/home/SBC/me01peesb088/CiscoEnv.txt',1)
text2=linecache.getline(r'/export/home/SBC/me01peesb088/CiscoEnv.txt',2)
text3=linecache.getline(r'/export/home/SBC/me01peesb088/CiscoEnv.txt',3)
print(text1)
print(text2)
print(text3)

a = re.search(r'\d+',text1).group()
print(a)
if a == '0':
    print('success')
else:
    f3.write(str(text1))

b = re.search(r'\d+',text2).group()
print(b)
if b == '0':
    print('success')
else:
    f3.write(str(text2))

c = re.search(r'\d+',text2).group()
print(c)
if c == '0':
    print('success')
else:
    f3.write(str(text3))
