import os

basePath = "C:/Users/Lucas/Downloads"

for file in os.listdir(basePath):
    if os.path.isfile(os.path.join(basePath, file)):
        print(file)
