#!/usr/bin/python
import pexpect
import time

ssh = pexpect.spawn('ssh manager@192.168.0.43')
ssh.expect('We.*password')
ssh.sendline('Sommer123!')
ssh.expect('.*Press any key to continue.*')
ssh.sendline('')
ssh.expect('#')
ssh.sendline('show lldp info local-device')
ssh.expect('Control-C')
print ssh.before # an dieser Stelle nach der Chassis Id matchen
