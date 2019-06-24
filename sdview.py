#!/usr/bin/python3
#Date: Mon 24 Jun 2019 17:36:07 CEST
#Author: Nicolas Flandrois
#Description:View's class will regroup all displays and questions inputs, needed in Stardate.

import datetime
import os, platform
from sdcompute import Compute

class View(object):
    """
    View's class will regroup all displays and questions inputs.
    """

    def clean():
        """
        This function will clear the terminal's screen. The command is 
        automaticaly detected according to the system OS you run it.
        Compatible with Windows, OSx, and Linux.
        """
        os.system("cls" if platform.system() == "Windows" else "clear")

    def menu(convert, translate):
        """menu docstring"""
        print("STARDATE.\n\n")
        View.show_today_stardate()
        print('\n\n')
        while True:
            responce = input("Do you want to do some other operation?\n\
press:\n\
        1 : Compute Today\'s Stardate.\n\
        2 : To convert a Date into Stardate.\n\
        3 : To Translate a Stardate into a Date.\n\
        R : Return to main menu.\n\
        Q : To Quit.\n\n")
            View.clean()

            try:
                if responce.strip().lower() in ['r', 'q', '1', '2', '3']:
                    if responce.strip().lower() == 'r':
                        continue
                    elif responce.strip().lower() == 'q':
                        break
                    elif responce.strip().lower() == '1':
                        View.show_today_stardate()
                        print('\n\n')
                    elif responce.strip().lower() == '2':
                        date = View.ask_date()
                        date[1]
                        print(convert(date[0]))
                        print('\n\n')
                    elif responce.strip().lower() == '3':
                        print(translate(View.ask_stardate()))
                        print('\n\n')
                    else:
                        raise
                else:
                    raise          
            except:
                print("We couldn't understand your choice. Please try again.")

            
    def ask_date():
        """
        Ask input and return for the date object.
        """
        dlist = []
        dlist.append(Compute.ask_integer("Earth Year? (YYYY format) ",
                                         range(-10000000, 10000000)))
        dlist.append(Compute.ask_integer("Earth Month? (from 01 to 12) ",
                                         range(1, 13)))
        dlist.append(Compute.ask_integer("Day of the month? (from 01 to 31) ",
                                         range(1, 32)))
        dlist.append(Compute.ask_integer("Hour? (from 00 to 23) ",
                                         range(0, 24)))
        dlist.append(Compute.ask_integer("Minutes? (from 00 to 59) ",
                                         range(0, 60)))

        dstring = " ".join([str(i) for i in dlist])

        res_date = datetime.datetime.strptime(dstring, '%Y %m %d %H %M')

        return  res_date.timetuple(), res_date.strftime('%A, %Y %B %d. %H:%M:%S')

    def ask_stardate():
        """
        Ask and return for the float's stardate number.
        """
        return float(input("What Stardate do you wish to convert? : "))

    def show_date(earthdate):
        """
        Displays a date object, in a User Experience readable format.
        """
        return earthdate()[1]

    def show_today_stardate():
        """
        Displays Today's now()'s Stardate.
        """
        print("Today is : ", View.show_date(Compute.nowearthdate))
        print("Stardate : ", Compute.sdconvert(datetime.datetime.now().timetuple()))

# TEST
# print(View.ask_date()) # OK > time.struct_time(tm_year=2019, tm_mon=1, tm_mday=1, tm_hour=1, tm_min=1, tm_sec=0, tm_wday=1, tm_yday=1, tm_isdst=-1), 'Tuesday, 2019 January 01. 01:01:00')
# print(View.ask_stardate()) # OK > What Stardate do you wish to convert? : 7974.96 > 7974.96
# print(View.show_date(Compute.nowearthdate)) # OK > Monday, 2019 June 24. 16:06:50
