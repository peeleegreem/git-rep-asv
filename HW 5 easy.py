__author__ = 'Вертипрахов Александр Сергеевич'

 # Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil
# creating of directories
print('Creating of directories')
for i in range(1, 10):
    try:
        os.mkdir('dir_' + str(i))
        print("Directory dir_" + str(i) + " is created")
    except FileExistsError:
        print('The directory (dir_' + str(i) + ") is exists")
# deleting of directories
print('Deleting of directories')
dir_del = input('Are You sure? (Please, print Y or N without space)')
if dir_del  == 'Y':
    for i in range(1, 10):
        os.rmdir('dir_' + str(i))
        print("dir_" + str(i) + " is deleted")
else:
    print("It's Your decision. All directories are still there")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print('List of files in current directory')
for i in os.listdir():
    print(i)
	

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

os.path.realpath(__file__)
Name = str(__file__)
print('Original file : ', Name)
NewFileName = (Name + '.copy')
NewFile = shutil.copy(__file__, NewFileName)
print("It's a copy : ", NewFile) 