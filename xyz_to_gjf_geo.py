#Convert XYZ files to GJF files
#9/6/21

try:
	import os
	import argparse

except ModuleNotFoundError:
	print("[Error] - Missing modules not found")
	exit()

headingsList = ["%LindaWorkers=in-cn0541\n",
	       "%NProcShared=32\n",
	       "%Mem=64gb\n",
	       "%chk=ts12.chk\n",
	       "#wB97XD/def2TZVP Int(grid=ultrafine) opt freq=noraman\n"
	       "",
	       "\n",
	       ""]

def createFiles(inNumXYZ): #prepare new files by adding heading
	
	File = open(str(inNumXYZ) + ".gjf", "w+")

	for i in range(0, 8):

		if (i == 3):
			File.write("%chk=" + str(inNumXYZ) + ".chk\n")

		elif (i == 6):
			File.write(str(inNumXYZ) +"\n\n")
		
		elif (i == 7):
			File.write("0 1\n")

		else:
			File.write(headingsList[i])

	return File

def openXYZ(inPathTo, inFileNumber):

	with open(inPathTo + "//" + str(inFileNumber) + ".xyz", "r") as xyz:
		
		lineCount = 0
		File = createFiles(inFileNumber)

		for line in xyz:
			
			if (lineCount > 1):
				File.write(line)
		
			lineCount = lineCount + 1
		File.write('\n')
		File.close()

	print("[Info] - File generation finished successfully for xyz file " + str(inFileNumber))
	

def getFileNumber(inFullPath):

	head, tail = os.path.split(inFullPath)
	currentDir = head
	fileNumber = tail.split('.')
	return head, fileNumber[0]

if __name__ == '__main__':

	#add cmd arguments
	parser = argparse.ArgumentParser(description="Convert XYZ files to GJF files")
	parser.add_argument("--file", help="path to single xyz file")
	parser.add_argument("--dir", help="path to directory of xyz files (all will be used in generation)")
	args = parser.parse_args()

	if (args.file != None):
		
		if (os.path.isfile(args.file) != True):
			print("[Error] - Path to single file does not exist")
			exit()

		pathTo, fileNumber = getFileNumber(args.file)
		openXYZ(pathTo, fileNumber)

	elif (args.dir != None):

		if (os.path.isdir(args.dir) != True):
			print("[Error] - Path to directory does not exist")
			exit()

		found = False
		for xyz in os.listdir(args.dir):
	 
			if (xyz.endswith(".xyz")):
				found = True
				fullPath = os.path.join(args.dir, xyz)
				pathTo, fileNumber = getFileNumber(fullPath)
				openXYZ(pathTo, fileNumber)

		if (found != True):
			print("[Error] - No xyz files found in given directory")
			exit()
		
	else:
	
		print("[Error] - Must supply a single file or a directory of xyz files")
		exit()

	
	
