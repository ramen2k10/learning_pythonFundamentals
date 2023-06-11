import os
class CountWords_In_Dict:

    def displayWordCount_dict(self, filePath):
        wordsCount = dict()
        fhandle = open(filePath)
        for line in fhandle:
            str = line.rstrip()
            listData = str.split()
            for item in listData:
                if item not in wordsCount:
                    wordsCount[item] = 1
                else:
                    wordsCount[item] = wordsCount[item]+1

        print(wordsCount)




file_path  = input("Enter a file path:")
if os.path.exists(file_path):
    print(f"The file {file_path} exists in the folder.")
else:
    print(f"The file {file_path} does not exist in the folder.")
    exit()
object = CountWords_In_Dict()
object.displayWordCount_dict(file_path)
