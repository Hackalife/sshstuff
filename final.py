import pexpect
import string
import time
import re


f = open('ipliste.txt')


a = 0
r = open('results.txt','w')

r.write('results:'+'\n')
for a in range (0, 2):
    str = f.readline()

    r.write('\n'+str)

    ssha = pexpect.spawn('ssh manager@'+str)
    ssha.expect('We.*password')
    ssha.sendline('Sommer123!')
    ssha.expect('.*Press any key to continue.*')
    ssha.sendline('')
    ssha.sendline('show lldp info local-device')
    ssha.expect('Control-C')
    chassid = ssha.before[502:550]
    r.write(chassid+'\n')

    ssh = pexpect.spawn('ssh manager@'+str)
    ssh.expect('We.*password')
    ssh.sendline("Sommer123!")
    ssh.expect('.*Press any key to continue.*')
    ssh.sendline('')
    ssh.expect('.')
    ssh.buffer = ''
    ssh.sendline('show interfaces transceiver')
    ssh.expect('.')
    time.sleep(1)
    lines = string.split(ssh.buffer, '\r\n')
    for line in lines:
        match = re.match("^.(\d+)\W+1000.X", line)
        if match:
            print match.group(1)
            ssh.buffer = ''
            ssh.sendline('show interface transceiver ' + match.group(1) + ' detail')
            ssh.expect('in ' + match.group(1))
            ssh.expect('Rx')
            power = re.match('(.+dBm)', ssh.buffer).group(1)
            r.write(power+'\n')

    a = a + 1
