import pexpect
import time
import sys

ssh = pexpect.spawn('ssh manager@192.168.0.43')
ssh.expect('We.*password')
ssh.sendline('Sommer123!')
ssh.expect('.*Press any key to continue.*')
ssh.sendline('')
ssh.sendline('show interfaces transceiver detail')
ssh.expect ('show interfaces transceiver detail')
sys.stdout.flush()
time.sleep(5)

print ssh.before[460:]
