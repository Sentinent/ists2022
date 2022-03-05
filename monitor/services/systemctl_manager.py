import subprocess
from .util import *

class SystemctlManager:
    def __init__(self, services):
        self.services = services

    def check(self):
        ns = subprocess.run(['netstat', '-lpn'], stdout=subprocess.PIPE)
        ns_output = ns.stdout.decode('utf-8').split('\n')
        ns_header = next(x for x in ns_output if x.startswith('Proto'))
        ns_output = [x for x in ns_output if 'LISTEN' in x]
        print(ns_header)

        for service in self.services:
            print('[{}]'.format(service.name))

            ### netstat

            ns_line = [x for x in ns_output if str(service.port) in x]
 
            for l in ns_line:
                print(colorize(l, { str(service.port): COLOR.Green }))
            
            if len(ns_line) == 0:
                print('WARNING: Port {} is not listening.'.format(service.port))

            ### systemctl

            systemctl = subprocess.run(['systemctl', 'status', service.name], stdout=subprocess.PIPE)
            systemctl_output = systemctl.stdout.decode('utf-8').split('\n')
            try:
                systemctl_output = next(x.strip() for x in systemctl_output if 'Active' in x)
                print(colorize(systemctl_output, { 'running': COLOR.Green, 'exited': COLOR.Red }))

                if 'exited' in systemctl_output:
                    journalctl = subprocess.run(['journalctl', '-u', service.name, '-n', '10', '--reverse'], stdout=subprocess.PIPE)
                    journalctl_output = journalctl.stdout.decode('utf-8').split('\n')[1:] # first line is "logs begin at ..."
                    # reverse
                    journalctl_output.reverse()
                    print('\n'.join(journalctl_output))
            except StopIteration:
                print('ERROR: systemctl command failed.\n{}'.format('\n'.join(systemctl_output)))

            print()


class SystemctlService:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.port = kwargs['port']
