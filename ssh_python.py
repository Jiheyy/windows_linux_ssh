#-*- coding: utf-8 -*-
import paramiko
import sys,time

# run python file (test.py : which write result in test.txt) in windows server and get result (test.txt).

reload(sys)
sys.setdefaultencoding('utf-8')

number_list = sys.argv[1:] 
args_msg= ' '.join(number_list)

path="cd C:\Users\jhmin\Documents\test & test.py "+str(args_msg)

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# windows server info
cli.connect('0.0.0.0', port=22, username='user', password='password')
# run python
stdin, stdout, stderr = cli.exec_command(path)

time.sleep(10)
# read result
path='type "C:\Users\jhmin\Documents\test.txt"'
stdin, stdout, stderr = cli.exec_command(path)


msg = stdout.read()
print(msg)
cli.close()
