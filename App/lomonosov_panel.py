import re

from ssh import *

def onConnectButton(obj):
    host = obj.host.text()
    login = obj.login.text()
    password = obj.password.text()
    ssh_key = 'lomonosov.ppk'

    msg, obj.status, obj.connection = connect(host, login, password, ssh_key)
    	
    obj.textEdit.setText(msg)

    if obj.status == 1:	
	   	obj.connect_btn.setEnabled(False)
	   	obj.disconnect_btn.setEnabled(True)

	   	obj.host.setEnabled(False)
	   	obj.login.setEnabled(False)
	   	obj.password.setEnabled(False)	    	

	   	obj.test_btn.setEnabled(True)
	   	obj.regular4_btn.setEnabled(True)
	   	obj.regular6_btn.setEnabled(True)

def onDisconnectButton(obj):
    	obj.connection.logout()
    	obj.status = 0

    	obj.connect_btn.setEnabled(True)
    	obj.disconnect_btn.setEnabled(False)

    	obj.host.setEnabled(True)
    	obj.login.setEnabled(True)
    	obj.password.setEnabled(True)

    	obj.test_btn.setEnabled(False)
    	obj.regular4_btn.setEnabled(False)
    	obj.regular6_btn.setEnabled(False)

    	obj.textEdit.setText("Connection to lomonosov.parallel.ru closed")


def onTestButton(obj):
	if obj.status == 1:
		cn = obj.connection
			
		msg = ''
			
		command = "squeue -p test"
		cn.sendline(command)
		cn.prompt()
			
		answer = str(cn.before)
		answer = re.sub('^.+?' + command, '', answer)
		answer = re.sub(r'\\r\\n', '\n', answer)
		answer = re.sub('\'$', '', answer)
			
		msg += str(answer)
			
		obj.textEdit.setText(msg)

	return

def onRegular4Button(obj):
	if obj.status == 1:
		cn = obj.connection
			
		msg = ''

		command = "squeue -p regular4"
		cn.sendline(command)
		cn.prompt()
			
		answer = str(cn.before)
		answer = re.sub('^.+?' + command, '', answer)
		answer = re.sub(r'\\r\\n', '\n', answer)
		answer = re.sub('\'$', '', answer)
			
		msg += str(answer)
			
		obj.textEdit.setText(msg)

	return

def onRegular6Button(obj):
	if obj.status == 1:
		cn = obj.connection
			
		msg = ''

		command = "squeue -p regular6"
		cn.sendline(command)
		cn.prompt()

		answer = str(cn.before)
		answer = re.sub('^.+?' + command, '', answer)
		answer = re.sub(r'\\r\\n', '\n', answer)
		answer = re.sub('\'$', '', answer)
			
		msg += str(answer)
		  
		obj.textEdit.setText(msg)
	
	return
