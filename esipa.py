'''
DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
                    Version 2, December 2004 
Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 
Everyone is permitted to copy and distribute verbatim or modified 
copies of this license document, and changing it is allowed as long 
as the name is changed. 
           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
 TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

1. You just DO WHAT THE FUCK YOU WANT TO.

         ///\\\  ( Have Fun )
        / ^  ^ \ /
      __\  __  /__
     / _ `----' _ \
     \__\   _   |__\
      (..) _| _ (..)
       |____(___|     Mynameisv_ 2016
_ __ _ (____)____) _ _________________________________ _

/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
 ____  ____  __  ____   __  
(  __)/ ___)(  )(  _ \ / _\ 
 ) _) \___ \ )(  ) __//    \
(____)(____/(__)(__)  \_/\_/

\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
                          
EsIPa stands for Empire's Stager IP and Port Alterer
'''
#
##
###
################################################################
## Parameters and Prerequisites
################################
# Version, name, author...
iVersionMinor = 1;
iVersionMajor = 0;
sScriptName = "EsIPa";
sAuthor = "Mynameisv_"; # that looks to be me :-)
#
##
###
###########################################################
# Python Imports
#############################
import base64
import re
import sys
#
##
###
###########################################################
# Functions
#############################
# [ What ]
#  Decode a base64 encoded unicode-empire-stager
# [ Returns ]
#  An ascii empire stager
def stagerDecode(
		sStagerB64,	# Base64 encoded stager
	):
	# To avoid checking if the input is good, I use "try", yeah \o/
	try:
		sStagerUnicode = base64.b64decode(sStagerB64)
		# A way to remove the unicode \0x00
		sStagerAscii = ''
		for i in range (0,len(sStagerUnicode)):
			if (i%2==0):
				sStagerAscii+=sStagerUnicode[i]
		return sStagerAscii
	except Exception, e:
		print "\n [!] Stager is not base64 encoded or badly.\n"
		sys.exit(1)
#end - stagerDecode(
#############################
# [ What ]
#  Transform an ascii-empire-stager to unicode and base64-encode it
#  No revolution here, it's Empire style
# [ Returns ]
#  An unicode-empire-stager, base64 encoded
def stagerEncode(
		sStagerAscii,	# Ascii stager
	):
	# To avoid checking if the input is good, I use "try", yeah \o/
	return base64.b64encode("".join([char + "\x00" for char in unicode(sStagerAscii)]))
#end - stagerEncode(
#############################
# [ What ]
#  Replace IP address and Port in a ascii-empire-stager
# [ Returns ]
# An ascii empire stager
def stagerReplace(
		sStagerAscii, # Ascii stager
		sIP, # IP address to replace
		sPort # TCP Port to replace
	):
	# Here is the worst part, with my worst dev
	sTag1 = '://' # work with http and https
	sTag2 = '/'
	iPos1 = sStagerAscii.find(sTag1)
	if iPos1==-1:
		print "\n [!] Error finding the IP address in the stager, tag={"+sTag1+"}.\n"
		sys.exit()
	iPos2 = sStagerAscii.find(sTag2, iPos1+len(sTag1))
	if iPos1==-1:
		print "\n [!] Error finding the TCP Port in the stager, tag={"+sTag1+"}.\n"
		sys.exit()
	return sStagerAscii[0:iPos1+len(sTag1)]+sIP+':'+sPort+sStagerAscii[iPos2:]
#end - stagerReplace(
#
##
###
################################################################
## Main / Entrypoint
################################
#
# Hello  \o
print "\n"+sScriptName+" "+str(iVersionMajor)+"."+str(iVersionMinor)+" / "+sAuthor
print "License: Do what the fuck you want to public license\n"
#
# Set up here your stager
sStagerB64 = raw_input("Paste your base64 encoded stager: ")
# Set up here your ip and port
sIP = raw_input("Type your new IP address: ")
sPort = raw_input("Type your new TCP Port: ")
# An option. What ? Command line with params !!? don't know ;-)
sVerbose = raw_input("Type anything for Verbose or just 'Enter': ")

# A line
sLine='';
for i in range(0,70):
	sLine+='-';

# Decode
sStagerAscii = stagerDecode(sStagerB64)
if len(sVerbose)!=0:
	print "\n - Decoded Stager ---------------"
	print sStagerAscii
	print sLine

# Replace
sStagerNew = stagerReplace(sStagerAscii, sIP, sPort)
if len(sVerbose)!=0:
	print "\n - Replaced Stager ---------------"
	print sStagerNew
	print sLine

# Reencode
sStagerFinal = stagerEncode(sStagerNew)
print "\n - Final Reencoded Stager ---------------"
print sStagerFinal
print sLine

raw_input("\nPress any key to exit...")