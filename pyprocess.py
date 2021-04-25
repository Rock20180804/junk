import psutil
import time

import subprocess
import sys

print('executable is ', sys.executable)

p = subprocess.Popen(['/bin/sh', '-c', 'while true; do echo "a"; sleep 1; done'])

pid = p.pid
print('pid is ', pid)

time.sleep(10)
ps = psutil.Process(pid)
ps.kill()

print('process ', pid, ' is killed')
