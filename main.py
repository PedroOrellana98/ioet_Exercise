# Arrays used to store multiple results.
listData = []
resulLitsCount = []
resulLitsNames = []

# Variable to enter the name of the .txt file.
print("\nEnter the name of the TXT file: \n")
path = input()

# Function to read the .txt file and generate some strings.
with open(path, 'r') as data:
    for line in data:
        data = line.replace('=', ',').replace(
            '\n', '').replace(' ', '').split(',')
        listData.append(data)

# Method to assign the names of the couples to a list.
def appendList(listName, value):
    for i in listData[value][0]:
        listName.append(i)
    return listName

# Method to verify the similarity between arrays according to the date that the people coincided.
def averageList(listData, valX, valY):
    listAverage = []
    for i in listData[valX]:
        for j in listData[valY]:
            if i == j:
                listAverage.append(i)
    return listAverage

#  Method to compare the hours and assign the hours and days that the people coincide in addition to printing the result.
def compareHours():
    for x in range(len(listData)):
        for y in range(x+1, len(listData)):

            listAverage = []
            listName1 = []
            listName2 = []

            listName1 = appendList(listName1, x)
            listName2 = appendList(listName2, y)

            resulLitsNames.append(''.join(listName1) +
                                  '-' + ''.join(listName2) + ":")

            listAverage = averageList(listData, x, y)

            resulLitsCount.append(len(listAverage))

    print("\n------OUTPUT------\n")

    for v in zip(*(resulLitsNames, resulLitsCount)):
        print(*v)


compareHours()
