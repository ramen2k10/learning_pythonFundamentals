import os

class Maxcount_bigword:
    def get_maxcount_bigword(self, filepath):
        fhandle = open(filepath)
        wordsDict = dict()
        for line in fhandle:
            words = line.split()
            for word in words:
                wordsDict[word] = wordsDict.get(word, 0) +1

        bigCount = None
        bigWord = None
        for  word, count in wordsDict.items():
            if bigCount is None or count > bigCount:
                bigCount = count
                bigWord = word

        print("Big word is: ", bigWord, "Big count is: ", bigCount)




file_path  = input("Enter a file path:")
if os.path.exists(file_path):
    print(f"The file {file_path} exists in the folder.")
else:
    print(f"The file {file_path} does not exist in the folder.")
    exit()
object = Maxcount_bigword()
object.get_maxcount_bigword(file_path)
