import csv

with open('Secret_Santa.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    hash1 = {}
    hash2 = {}
    #nicknames = []
    #names = []
    for row in readCSV:
        name = row[1]
        nickname = row[2]
        email = row[3]
        hash1[nickname] = name
        hash2[nickname] = email 
        #nicknames.append(nickname)
        #names.append(name)

    #print(nicknames)
    #print(names)

    print hash1

    whatName = raw_input('Whose name do you wish to know?\n->')
    #coldex = names.index(whatName)
    #theNickname = nicknames[coldex]
    print('The name of ' + whatName + ' is: ' + hash1[whatName])
    print('The email of ' + whatName + ' is ' + hash2[whatName])