# pyIpCountryWhitelist
A python program that gets IP blocks by country and makes an ipset then add the set to iptables.

The program pulls from public sources.  It also allows RFC1918 by default and established connections.  You can change this,
but just make sure you dont lose connection to the device if you arent in a console session(duh).

Please feel very free to make improvements.  No ego here.  Happy to make it better and take suggestions.

A few of many limitations:

This was made to only allow connections from the USA.  This means the database is from ARIN.  ARIN only covers the US, Canada and Carribbean.  Feel free to add other regional registrars(links below).    If you want to add others, clean it up, add other functionalty, and dont want to do it yourself, let me know.  We can make it happen for $1,000,000 or less(prob less).

Also this is dependent on ARIN continuing to publish IPs from the URL they currently publish to, in the format they use.  If they stop or change, it's all over.

Last thing is a little preachy.  Whitelists are a layer in security.  They are easily defeated by say a USA(or insert your fav country here) proxy, TOR exit in the USA(same really), or hacking a device in the USA.  Good security should have many layers at different layers.  

Enjoy!


Links to all ip DBs:

ftp://ftp.arin.net/pub/stats/arin/delegated-arin-extended-latest

ftp://ftp.ripe.net/ripe/stats/delegated-ripencc-latest

ftp://ftp.afrinic.net/pub/stats/afrinic/delegated-afrinic-latest

ftp://ftp.apnic.net/pub/stats/apnic/delegated-apnic-latest

ftp://ftp.lacnic.net/pub/stats/lacnic/delegated-lacnic-latest
