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
