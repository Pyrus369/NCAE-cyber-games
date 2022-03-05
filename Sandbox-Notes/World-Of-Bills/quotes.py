# CURRENTLY BEING TESTED

csvFile = open('quotes.csv', 'r')

Lines = csvFile.readlines()

for line in Lines:
    quote, aurthor, topic = line.split(';')
    if aurthor.split()[0].lower == 'user1firstname':
        f1 = open('/home/user1/quotes/smile.txt', 'at')
        f2 = open('/home/user1/quotes/topics.txt', 'at')
        f1.write(line)
        f2.write(topic)
        f2.write('\n')
    elif aurthor.split()[0].lower() == 'user2firstname':
        f1 = open('/home/user2/quotes/smile.txt', 'at')
        f2 = open('/home/user2/quotes/topics.txt', 'at')
        f1.write(line)
        f2.write(topic)
        f2.write('\n')
    '''
        Continue creating elif statements until all users are accounted for.
    '''
    else:
        continue
