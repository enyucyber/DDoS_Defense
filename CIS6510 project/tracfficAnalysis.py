import subprocess

checkList = []
blackList = []
with open('blackList.txt',  'r') as file:
    for line in file:
        Aline = line.strip()
        blackList.append(Aline)


with open('tempHistory.txt',  'r') as file:
    for line in file:
        Aline = line.strip()
        if Aline in checkList and Aline not in blackList:
            with open('blackList.txt', 'a') as file:
                file.write(Aline+'\n')
        if Aline not in checkList:
            checkList.append(Aline)
print(" ")
print("---------------Analysis Done---------------")
print(" ")
subprocess.run('del tempHistory.txt', shell=True)
subprocess.run('type nul > tempHistory.txt', shell=True)

