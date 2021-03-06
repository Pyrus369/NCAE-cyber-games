eth0-external
eth1-internal


# ROUTER SETTINGS
/etc/sysconfig/netwowork-scripts/eth0-1

***external settings***
BOOTPROTO=static
ONBOOT=yes
IPPADDR=$iprange
ZONE=external
NETMASK=255.255.0.0

***internal settings***
BOOTPROTO=static
ONBOOT=yes
IPPADDR=$iprange
ZONE=internal
NETMASK=255.255.255.0

# Portforwarding

```bash
sudo firewall-cmd --zone=external --permanent --add-forward-port=port=80:proto=tcp:toport=80:toaddr=192.168.#.2
```
```bash
firewall-cmd --reload
firewarll-cmd --list-all --zone=external
```

# Create Multiple Users in Linux
- create 'names.txt'
- user1:user1password:userID:groupID:comment:homeDIR:shell
- user2:user2password:userID:groupID:comment:homeDIR:shell
- example:
- ***tcole:password123!:1002:1002::/home/tcole:/bin/bash***
- ***sfilly:!321drowssap:1003:1003::/home/sfilly:/bin/bash***
- change permission on file
```bash
sudo chmod 0600 names.txt
sudo newusers names.txt
```
- verify /etc/passwd

