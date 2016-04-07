import re

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
