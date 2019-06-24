#!/usr/bin/python3
#Date: Mon 24 Jun 2019 17:37:37 CEST
#Author: Nicolas Flandrois
#Description: The Compute class regroup all necessary computing functions, needed in stardate.

import datetime
import json

class Compute(object):
    """
    The Compute class regroup all necessary computing functions.
    """

    def config():
        """
        Returns a Tuple from config.json reference points: 
        (Earthdate, Stardate)
        """
        with open("sdconfig.json") as f:
            return json.load(f)

    def ask_integer(message:str, range, error_message:str = ""):
        """
        This function's purpose is to ask and verify an Integer.
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

    def leapyr(year:int):
        """" 
        This function defines if the year is 
        a Leap year (366 days) 
        or a Normal year (365 days).
        Then it will to the variable n the value of 366 or 365, accordingly.
        """
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            n = 366
            print("The year is a Leap year.\n")

        else:
            n = 365
            print("The year is a normal year.\n")

        return n

    def nowearthdate():
        """Will generate automaticaly a tuple datetime object, for now time"""
        nowdate = datetime.datetime.now()
        return  nowdate.timetuple(), nowdate.strftime('%A, %Y %B %d. %H:%M:%S')

    def sdconvert(t):
        """ 
        Stardate calculator
        t = Time  (cf 'datetime.datetime.now().timetuple()' format)
        Compute.config()["earthdate"] = Earthdate Year reference point
        Compute.config()["stardate"] = Stardate Yaer reference point
        Compute.leapyr(t.tm_year) = number of days leap/normal year (365 or 366)
        """
        return format(((Compute.config()["stardate"]+
            (1000*(t.tm_year - Compute.config()["earthdate"])))+
            ((1000/((Compute.leapyr(t.tm_year))*1440.0))*(((t.tm_yday - 1.0)*1440.0)+
                (t.tm_hour*60.0) + t.tm_min))), '.2f')

    def sdtranslate(sd):
        """ 
        Stardate translator
        sd = Stardate Time  (cf float, stardate format)
        Compute.config()["earthdate"] = Earthdate Year reference point
        Compute.config()["stardate"] = Stardate Yaer reference point
        Compute.leapyr(t.tm_year) = number of days leap/normal year (365 or 366)
        """
        dlist = []
        ed_year = int(((sd - Compute.config()["stardate"])//1000) + Compute.config()["earthdate"])
        dlist.append(int(ed_year))
        ed_time = (((sd - Compute.config()["stardate"])%1000)/(1000/(1440*Compute.leapyr(ed_year))))
        ed_day = (ed_time//1440)+1
        dlist.append(int(ed_day))
        ed_hour = (ed_time-((ed_day-1)*1440))//60
        dlist.append(int(ed_hour))
        ed_min = ed_time%60
        dlist.append(int(ed_min))
        #NOTE: This calculation has 2 min leap from real date
        dstring = " ".join([str(i) for i in dlist])
        
        return datetime.datetime.strptime(dstring, '%Y %j %H %M')
        

# TEST
# print(Compute.leapyr(2019)) # OK > The year is a normal year. > 365
# print(Compute.sdconvert(datetime.datetime.now().timetuple())) # OK > 97079.72
# print(Compute.sdtranslate(7974.96)) # OK > The year is a normal year. > 1930-05-17 10:08:00
# print(Compute.config()) # OK > (2019, 96601.2)
# print(Compute.nowearthdate()) # > (time.struct_time(tm_year=2019, tm_mon=6, tm_mday=24, tm_hour=15, tm_min=49, tm_sec=28, tm_wday=0, tm_yday=175, tm_isdst=-1), 'Monday, 2019 June 24. 15:49:28')
