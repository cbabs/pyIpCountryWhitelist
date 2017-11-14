#!/usr/bin/python3

import os, sys
import math
import urllib3
import requests


##For multiple countries uncomment and add the countries you want
#arinCountryList=['US','CA']

##For a single country define here 
arinCountryList='US'

http = urllib3.PoolManager()



#This file is where all output is logged
#timestamp = time.ctime().replace(':', '.')
#logfile = open(timestamp + '-Awesome-SSHlog.txt', 'w')


class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        timestamp = time.ctime().replace(':', '.')
        self.logfile = open(timestamp + '-Awesome-SSHlog.txt', 'w')

    def write(self, message):
        self.terminal.write(message)
        self.logfile.write(message)   
         
class whitelistIp():
    
    def arinCountryIPs(self):
        url ='http://ftp.arin.net/pub/stats/arin/delegated-arin-extended-latest'
        
        os.system("wget " + url)
        
        f = open("delegated-arin-extended-latest", "r")    
        lines=f.readlines() 
        
        print("Trying loop now")
        subnets = []
        for line in lines:
            if (('ipv4' in line) & ('US' in line)) :
                s=line.split("|")
                net=s[3]
                cidr=float(s[4])
                subnets.append("%s/%d" % (net,(32-math.log(cidr,2))))
        
        print("IPv4 entries " + str(len(subnets)))
        
        #Close file and delete
        f.close
        os.system("rm ./delegated-arin-extended-latest")
        
        return subnets
   
    def ipset(self):
        
        ##Uncomment this line if you want a log of activity
        #sys.stdout = Logger() 
        
        #Allow RFC1918 address space
        rfc1918=['10.0.0.0/8','172.16.0.0/12','192.168.0.0/16']
        os.system("ipset create RFC1918 hash:net")
        for privNet in rfc1918:
            os.system("ipset add RFC1918 " + privNet)
            
        os.system("iptables -I INPUT -m set --match-set RFC1918 src -j ACCEPT")
        
        #Allow 22 from everywhere and established connections
        os.system("iptables -I INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT")
        os.system("iptables -I INPUT -p tcp -m tcp --dport 22 -j ACCEPT")
        
        
        print("Gettings lists from ARIN of US public subnets from arinCountryIPs()")
        ipList = whitelistIp.arinCountryIPs(self)
        
        
        os.system("ipset flush whiteList")
        print("Creating a new list")
        os.system("ipset create whiteList hash:net")
        os.system("iptables -I INPUT -p tcp -m tcp --dport 22 -j ACCEPT")
        for subnet in ipList:  
            #print(subnet)
            if '#' in subnet:
                continue 
            else:
                os.system("ipset add whiteList " + subnet)
                
        print("Installing ipset whiteList into iptables and setting INPUT policy to DROP")
        os.system("iptables -A INPUT -m set --match-set whiteList src -j ACCEPT")
        os.system("iptables -P INPUT DROP")
        
def main():   
    execProg = whitelistIp()
    execProg.ipset()
    #execProg.arinCountryIPs()

if __name__ == "__main__":
