#!usr/bin/python3

#################################################################################
# MIT License
#
# Copyright (c) 2019 - Nicolas Flandrois
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#################################################################################

#Thu 17 Jan 2019 04:25:27 PM CET  - Stardate: 96649.65
#Author: Nicolas Flandrois
#Description: This program intend to convert a given Earthdate into Stardate,
#it is using customized reference points for calculation:
# stardate = c + [1000*(y-b)] + 
#            [(1000/(n*1440))*((iso_day_of_year - 1)+time_in_minutes)]
#Version: 1.0

import datetime

def ask_integer(message:str, range, error_message:str = ""):
    """
    Le but de cette fonction
    est de demander un entier à l'utilisateur
    avec un message personnalisé
    Répéter l'opération si l'entrée n'est pas un entier
    avec un message d'erreur personnalisé
    L'entier sera vérifié par la fonction passée en paramètres
    """
    var = None
    while True:
        try:
            var = int(input(message))
            if var in range:
                return var
                raise
                
        except KeyboardInterrupt:
            break
            
        except:
            print(error_message)

dlist = []
dlist.append(ask_integer("Earth Year? (YYYY format) ", range(-10000000, 10000000)))
dlist.append(ask_integer("Earth Month? (from 01 to 12) ", range(1, 13)))
dlist.append(ask_integer("Day of the month? (from 01 to 31) ", range(1, 32)))
dlist.append(ask_integer("Hour? (from 00 to 23) ", range(0, 24)))
dlist.append(ask_integer("Minutes? (from 00 to 59) ", range(0, 60)))

dstring = " ".join([str(i) for i in dlist])

d = datetime.datetime.strptime(dstring, '%Y %m %d %H %M')

t = d.timetuple()

ed_display = d.strftime('%A, %Y %B %d. %H:%M:%S')
print('Earthdate : ', ed_display)

#The following reference points are from 
#the MMORPG Star Trek Online (STO). 
#This STO referncial was determined from their online converter:
# 2019/01/01 00:00 = 96601.20 stardate units
#https://www.stoacdemy.com/tools/stardate.php
#STO online converter uses differnt round parameters, 
#and I discovered they don't take leap year into account. 
#They apply n = 365, even during a leap year of 366 days.
b = 2019
c = 96601.20
#Referents point variables can be customized. 
#Please refer to the reference dates document.

n = 1

def leapyr(year:int):
	"""" 
	This function defines if the year is 
	a Leap year (366 days) 
	or a Normal year (365 days).
	Then it will to the variable n the value of 366 or 365, accordingly.
	"""
	global n
	if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
		n = 366
		print("The year is a Leap year.")

	else:
		n = 365
		print("The year is a normal year.")

leapyr(t.tm_year)

def stardate(b:int, c:float, t, n=365):
	""" 
	Stardate calculator
	b = Earthdate Year reference point
	c = Stardate Yaer reference point, corresponding to b
	t = Time  (cf 'datetime.datetime.now().timetuple()' format)
	n = number of days leap/normal year 
	"""
	
	sd = ((c+(1000*(t.tm_year-b)))+
		((1000/(n*1440.0))*(((t.tm_yday-1.0)*1440.0)+
			(t.tm_hour*60.0)+t.tm_min)))

	print("Stardate : ", format(sd, '.2f'))

print("")
stardate(b, c, t, n)
