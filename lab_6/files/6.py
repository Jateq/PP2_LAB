
import os,shutil

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

folder = input('Enter foldername: ')
if not os.path.exists(folder):
    os.mkdir(folder)

dst = os.getcwd() + '\\' + folder
for i in range(len(alphabet)):
    if not os.path.exists(alphabet[i]):
        file = open(alphabet[i],'w')
        file.close()
        file = open(alphabet[i],mode = 'a')
        file.write(alphabet[i])
        file.close()
        src = os.getcwd() + '\\' + str(alphabet[i])
        shutil.move(src, dst)