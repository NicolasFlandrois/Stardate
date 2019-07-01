#!/usr/bin/python3
# Date: Mon 24 Jun 2019 17:36:07 CEST
# Author: Nicolas Flandrois
# Description:View's class will regroup all displays and questions inputs,
# needed in Stardate.

import datetime
import os
import platform
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
        View.clean()
        print("STARDATE\n")
        View.show_today_stardate()
        print('\n')
        while True:
            responce = input("Do you want to do some other Stardate operation?\n\
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
                        View.clean()
                        View.show_today_stardate()
                        print('\n')
                    elif responce.strip().lower() == '2':
                        View.clean()
                        date = View.ask_date()
                        stardate = Compute.sdconvert(date[0])
                        View.show_stardate(stardate, date[1])
                        print('\n')
                    elif responce.strip().lower() == '3':
                        View.clean()
                        print("\nEarthdate : ", translate(View.ask_stardate()))
                        print('\n')
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

        View.clean()
        dstring = " ".join([str(i) for i in dlist])

        res_date = datetime.datetime.strptime(dstring, '%Y %m %d %H %M')

        return res_date.timetuple(), res_date.strftime(
            '%A, %Y %B %d. %H:%M:%S')

    def ask_stardate():
        """
        Ask and return for the float's stardate number.
        """
        stardate = float(input("What Stardate do you wish to translate? : "))
        View.clean()
        return stardate

    def show_date(earthdate):
        """
        Displays a date object, in a User Experience readable format.
        """
        return earthdate()[1]

    def show_stardate(stardate, date):
        """
        Displays Date's Stardate.
        """
        print("Earthdate : ", date)
        print("\nStardate  : ", stardate)

    def show_today_stardate():
        """
        Displays Today's now()'s Stardate.
        """
        print("Today\'s Earthdate : ", View.show_date(Compute.nowearthdate))
        print("\nToday\'s Stardate  : ", Compute.sdconvert(
              datetime.datetime.now().timetuple()))
