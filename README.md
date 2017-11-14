# pyIpCountryWhitelist
A python program that gets IP blocks by country and makes an ipset then add the set to iptables.

The program pulls from public sources.  It also allows RFC1918 by default.  You can change this,
but just make sure you dont lose connection to the device if you arent in a console session(duh).

