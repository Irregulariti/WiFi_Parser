# file or directory
file = open(r"C:\Users\user\Desktop\myResultsOfScan.txt", "r")

# temporary text
text = [x.replace("\n\n", "") for x in "".join(file.readlines()).split("\n\n\n")]
# print(text) #for test

listNames = []
listDictsOfLevels = []

for line in text:
    dictOfLevels = {}
    if ":" in line:
        name, strOfLevels = line.split(":")  # name and str of levels
        name = name.replace("\n", "")
        if name not in listNames:  # exclude name repetitions
            listOfLevels = strOfLevels.split("\n")
            for i in range(1, len(listOfLevels) - 1):
                dictOfLevels[listOfLevels[i].split(" - ")[0]] = int(listOfLevels[i].split(" - ")[1])  # SSID to level
            if dictOfLevels != {}:  # exclude empty scans
                listNames.append(name)
                listDictsOfLevels.append(dictOfLevels)

# lastTest

# the corresponding point and the SSID to level dictionary are on the same indices
print(listNames)
print(listDictsOfLevels)


# toKotlin :-)
list = str(listNames).replace("\'", "\"")[1:]
list = list[:-1]
print(list)
