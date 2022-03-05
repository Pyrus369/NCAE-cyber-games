file1 = open('names.txt', 'r')
file2 = open('users.txt', 'at')

Lines = file1.readlines()
i = 1002

for line in Lines:
    username, password = line.split()
    text = username + ':' + password + ':' + str(i) + ':' + str(i) + '::' + '/home/' + username + ':' + '/bin/bash\n'
    f2.write(text)
    i += 1
