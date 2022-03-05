# CURRENTLY BEING TESTED

csvFile = open('quotes.csv', 'r')

Lines = csvFile.readlines()

userFirstName = {'user1FirstName':'/home/user1/quotes/', 'user2FirstName':'/home/user2/quotes/'} # Add all users first name in lowercase

for line in Lines:
    quote, aurthor, topic = line.split(';')
    if aurthor.split()[0].lower in userFirstName.keys():
        directory1 = userFirstName.get(aurthor.split()[0].lower()) + 'smile.txt'
        directory2 = userFirstName.get(aurthor.split()[0].lower()) + 'topics.txt'
        f1 = open(directory1, 'at')
        f2 = open(directory2, 'at')
        f1.write(line)
        f2.write(topic)
        f2.write('\n')
    else:
        continue
