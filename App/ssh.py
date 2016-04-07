import pxssh
import pexpect
import getpass

def connect(host, login, password, ssh_key):
	status = 0

	connection = pxssh.pxssh()

	try:	
		connection.login (host, login, password, ssh_key=ssh_key)

		status = 1

		msg = "Connection to lomonosov.parallel.ru opened"
		connection.sendline('module add slurm')
		connection.prompt()
		connection.sendline('cd _scratch')
		connection.prompt()
		connection.sendline('mkdir tavis')
		connection.prompt()

		command = "scp -i lomonosov.ppk H alexfmsu_1616@lomonosov.parallel.ru:_scratch/tavis/"
		child = pexpect.spawn(command)
		child.expect(':\s*$')
		child.sendline(password)
		child.wait()
		child.close()
	except:
		msg = "Connection to lomonosov.parallel.ru failed"
		status = -1
		
	return msg, status, connection


def init_ssh(obj):
 	obj.host.setText('lomonosov.parallel.ru')
 	obj.login.setText('alexfmsu_1616')
 	obj.password.setText('alexfmsu321678')