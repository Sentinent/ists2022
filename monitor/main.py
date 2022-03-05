import os
import subprocess
import time
from services import ICMPManager
from services import SystemctlManager, SystemctlService

SERVICES = [
    SystemctlService(name='ssh', port=22),
    # SystemctlService(name='ntp', port=22),
    SystemctlService(name='apache2', port=80),
    SystemctlService(name='nginx', port=80),
]

service_manager = SystemctlManager(SERVICES)
# icmp_manager = ICMPManager()

os.system('clear')
while True:
    service_manager.check()
    subprocess.run(['w'])

    time.sleep(15)
    os.system('clear')
