import os
from bingobango import BingoBangoThread

threads = []

for team_num in range(1, 16):
    if os.environ['TEAM'] == str(team_num):
        continue  # dont destroy ourselves bruh

    t = BingoBangoThread(team_num)
    t.start()
    threads.append(t)
