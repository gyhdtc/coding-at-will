import os, sys

FilePathRoot = "D:\\Github_File\\coding-at-will\\xjysb\\peer"
FileName = input("Input File Name : ")
FilePath = FilePathRoot + FileName
for file in os.listdir(FilePath):
    print("Del file : ", file)
    os.remove(FilePath + "\\" + file)