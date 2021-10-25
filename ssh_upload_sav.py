#-*- coding: utf-8 -*-
import paramiko

import sys,time
import os

reload(sys)
sys.setdefaultencoding('utf-8')

# send file which in linux server to windows server

try:
	cli = paramiko.SSHClient()
	cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
	# windows server account
	cli.connect('0.0.0.0', port=22, username='user', password='password')
	# replace test.raw(which is already exits in windows server) into old_test.raw
	stdin, stdout, stderr = cli.exec_command("cd C:\WORK & Ren test.raw old_test.raw")
	time.sleep(3)

	sftp = cli.open_sftp()
	# send new file as test.raw
	sftp.put('/usr/share/jhmin/test.raw', os.path.join('C:\WORK', 'test.raw'))
	print('Success')
except Exception as ex:
	print(ex)
	print('Failed')
finally:
	cli.close()
