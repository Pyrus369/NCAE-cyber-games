# Activity 1
## Goals:
- Configure your IP to the given IP Address: 172.19.\*.\*
## How To:
- Network file located in /etc/sysconfig/network-service/ifcfg-eth0
- Edit with the command below
```bash
sudo vi /etc/sysconfig/network-service/ifcfg-eth0
```
- Replace current "IPADDR= " with the given IP Address

# Activity 2
## Goals:
- Part 1:
    - Using Bill account, create a privileged account for yourself. Set username to 'cyberuser' username and create a password. Add the new account to the group 'wheel' when creating.
- Part 2:
    - Disable, but do **NOT** delete the bill account.
 ## How To:
 - Create your own account with 'cyberuser##' and assing a new password
 ```bash
 sudo useradd -g wheel cyberuser##
 sudo passwd cyberuser##
 ```
 
   - Edit /etc/passwd to not allow Bill to log-in.
```bash
sudo vi /etc/passwd
```
   - Change "bill:X:1000:1000::/home/bill:*/bin/bash*" 
   - to "bill:X:1000:1000::/home/bill:*/sbin/nologin*"
   - Now sign into your new account.
 
 ```bash
 su cyberuser##
 ```
 
 # Activity 3
 ## Goals:
 - Create multiple new employee accounts.
 ## How To:
 - To pull just the username and password of the new accounts run the following code.
 ```bash
 cat username.txt | awk '{ print $3, $4 }' > users.txt
 ```
 - Now edit and change users.txt from 
 ```text
 lmyers collectBEAUTIFULwin
 jmckee volcanoAIRfrog
 glozano cupMONTHgodly
 ...etc
 ```
 - To the following syntax for the command 'newusers'
 ```text
 lmyres:collectBEAUTIFULwind:1002:1002::/home/lmyres:/bin/bash
 jmckee:volcanoAIRfrog:1003:1003::/home/jmckee:/bin/bash
 glozano:volcanoAIRfrog:1004:1004::/home/glozano:/bin/bash
 ...etc
 ```
 #### There will also be a python script added that will create the new file for you.
 - If you made the file with python script to run use the following:
 ```bash
 python newUsers.py
 ```
 - Once the new file is created run the following command to create the new users all at once:
 ```bash
 sudo newusers new_users.txt
 ```
 - You can verify the creation of the accounts by looking at /etc/passwd.
 
 # Activity 4
 ## Goals:
 - Part 1:
  - Create a new priviledged account "jrice" on the server belonging to 'wheel' group.
 - Part 2:
  - Allow jrice to login via ssh by download and adding his is_rsa_jrice.pub to his authorized_keys file. (Don't worry about giving the account a password)
 ## How To:
 - Create "jrice" user.
 ```bash
 sudo useradd -g wheel jrice
 ```
 - Curl to download the id_rsa_jrice.pub file.
 ```bash
 curl -k https://172.19.0.1/data/id_rsa_jrice.pub > jrice.pub
 ```
 - Within the users home directory you need to create a new directory '.ssh' and a new file 'authorized_keys'
 ```bash
 sudo mkdir /home/jrice/.ssh
 sudo touch /home/jrice/.ssh/authorized_keys
 ```
 - Now move the contents of jrice.pub into authorized_keys and change ownership of the users .ssh directory and the authorized_keys file.
 ```bash
 sudo cat jrice.pub >> /home/jrice/.ssh/authorized_keys
 sudo chown jrice:wheel /home/jrice/.ssh
 sudo chown jrice:wheel /home/jrice/.ssh/authorized_keys
 ```
 
 # Activity 5
 ### TODO
 
 # Activity 6
 ### TODO
 
 # Activity 7
 ### TODO
 
 

