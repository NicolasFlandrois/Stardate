#!usr/bin/python3
#Convert Stardate into Earthdate.

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

#Date: Fri 18 Jan 2019 03:51:33 PM CET - Stardate: 96649.58
#Author: Nicolas Flandrois
#Description: This program intend to convert a given Stardate, 
#into an Earthdate, using customized reference points for calculation:
# stardate = c + [1000*(y-b)] + 
#            [(1000/(n*1440))*((iso_day_of_year - 1)+time_in_minutes)]
#To date, this script has a 2 min leap error from translation.
#Version: 1.0

import datetime

t = float(input("What Stardate do you wish to convert? : "))

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
#Reference point variables can be customized. 
#Please refer to the reference dates document.

n = 1

print("")
print("Stardate: ", t)

def leapyr(year):
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

dlist = []
ed_year = int(((t-c)//1000) + b)
dlist.append(int(ed_year))
leapyr(ed_year)
ed_time = (((t-c)%1000)/(1000/(1440*n)))
ed_day = (ed_time//1440)+1
dlist.append(int(ed_day))
ed_hour = (ed_time-((ed_day-1)*1440))//60
dlist.append(int(ed_hour))
ed_min = ed_time%60
dlist.append(int(ed_min))
#NOTE: This calculation has 2 min leap from real date
dstring = " ".join([str(i) for i in dlist])
d = datetime.datetime.strptime(dstring, '%Y %j %H %M')
d_display = d.strftime('%A, %Y %B %d. %H:%M:%S')
print('Earthdate : ', d_display)
