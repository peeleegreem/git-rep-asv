# coding: utf-8

import os
import sys
import shutil
import psutil


def duplicate_file(filename):
	if os.path.isfile(filename):
		newfile = filename + '.dupl'
		shutil.copy(filename, newfile)
		if os.path.exists(newfile):
			print("File ", newfile, " was create")
			return True
		else:
			print("Its a problem of copying")
			return False


def del_duplicates(dirname):
	file_list = os.listdir(dirname)
	double_count = 0
	for f in file_list:
		fullname = os.path.join(dirname, f)
		if fullname.endswith('.dupl'):
			os.remove(fullname)
			if not os.path.exists(fullname):
				double_count += 1
				print("File", fullname, "is delete")
	return double_count

def double_files(dirname):
	file_list = os.listdir(dirname)
	i = 0
	while i < len(file_list):
		duplicate_file(file_list[i])
		i += 1

def sys_info():
	print("What I know about system:")
	print("Number of processors: ", psutil.cpu_count())
	print("Platforms: ", sys.platform)
	print("Coding of file system: ", sys.getfilesystemencoding)
	print("Directory: ", os.getcwd())
	print("User: ", os.getlogin())

def main():
	print("Great Python Program!")
	print("Hello world!")
	name = input("Your name: ")
	print(name, ", Welcome to world of Python")

	answer =''
	while answer != 'Q':
		answer = input("Let's work? (Y/N/Q)")
		if answer == 'Y':
			print(name, "Ok!")
			print("I can:")
			print(" [1] - output file sheet")
			print(" [2] - output os info")
			print(" [3] - output sheet of processes")
			print(" [4] - duplicate files in directory")
			print(" [5] - duplicate file")
			print(" [6] - delete duplicate files in directory")

			do = int(input("Select your action"))

			if do == 1:
				print(os.listdir())
			elif do == 2:
				sys_info()
			elif do == 3:
				print(psutil.pids())
			elif do == 4:
				print("=duplicate files in directory=")
				double_files('.')
			elif do == 5:
				print("=duplicate file=")
				filename = input("Choose the file")
				duplicate_file(filename)
			elif do == 6:
				print("=delete duplicate files in directory=")
				dirname = input("Choose the directory")
				count = del_duplicates(dirname)
				print("-- Delete number of files: ", count)
			else:
				pass
		elif answer == 'N':
			print("Goodbye!")
		else:
			print("N/a")


if __name__ == "__main__":
	main()


# Comment


