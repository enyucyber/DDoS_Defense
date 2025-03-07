import subprocess

print(" ")
subprocess.run('del tempHistory.txt', shell=True)
subprocess.run('type nul > tempHistory.txt', shell=True)

print("The content of temHistory.txt has been cleared")

subprocess.run('del blackList.txt', shell=True)
subprocess.run('type nul > blackList.txt', shell=True)

print("The content of blackList.txt has been cleared")


subprocess.run('del stoppedTraffic.txt', shell=True)
subprocess.run('type nul > stoppedTraffic.txt', shell=True)

print("The content of stoppedTraffic.txt has been cleared")

print(" ")