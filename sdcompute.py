#!/usr/bin/python3
# Date: Mon 24 Jun 2019 17:37:37 CEST
# Author: Nicolas Flandrois
# Description: The Compute class regroup all necessary computing functions,
# needed in stardate.

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

    def ask_integer(self, range, error_message: str = ""):
        """
        This function's purpose is to ask and verify an Integer.
        """
        var = None
        while True:
            try:
                var = int(input(self))
                if var in range:
                    return var
            except KeyboardInterrupt:
                break

            except:
                print(error_message)

    def leapyr(self):
        """"
        This function defines if the year is
        a Leap year (366 days)
        or a Normal year (365 days).
        Then it will to the variable n the value of 366 or 365, accordingly.
        """
        return 366 if self % 400 == 0 or self % 4 == 0 and self % 100 != 0 else 365

    def nowearthdate():
        """Will generate automaticaly a tuple datetime object, for now time"""
        nowdate = datetime.datetime.now()
        return nowdate.timetuple(), nowdate.strftime('%A, %Y %B %d. %H:%M:%S')

    def sdconvert(self):
        """
        Stardate calculator
        t = Time  (cf 'datetime.datetime.now().timetuple()' format)
        Compute.config()["earthdate"] = Earthdate Year reference point
        Compute.config()["stardate"] = Stardate Yaer reference point
        Compute.leapyr(t.tm_year) = number of days leap year/not (365 or 366)
        """
        return format(
            (
                Compute.config()["stardate"]
                + 1000 * (self.tm_year - Compute.config()["earthdate"])
            )
            + (
                1000
                / (Compute.leapyr(self.tm_year) * 1440.0)
                * (
                    (
                        (((self.tm_yday - 1.0) * 1440.0) + self.tm_hour * 60.0)
                        + self.tm_min
                    )
                )
            ),
            '.2f',
        )

    def sdtranslate(self):
        """
        Stardate translator
        sd = Stardate Time  (cf float, stardate format)
        Compute.config()["earthdate"] = Earthdate Year reference point
        Compute.config()["stardate"] = Stardate Yaer reference point
        Compute.leapyr(t.tm_year) = number of days leap year/not (365 or 366)
        """
        print("Stardate  : ", self)

        ed_year = int(
            (self - Compute.config()["stardate"]) // 1000
            + Compute.config()["earthdate"]
        )
        ed_time = (
            (self - Compute.config()["stardate"])
            % 1000
            / (1000 / (1440 * Compute.leapyr(ed_year)))
        )
        ed_day = (ed_time//1440)+1
        dlist = [ed_year, int(ed_day)]
        ed_hour = (ed_time-((ed_day-1)*1440))//60
        dlist.append(int(ed_hour))
        ed_min = ed_time % 60
        dlist.append(int(ed_min))
        # NOTE: This calculation has 2 min leap from real date
        dstring = " ".join([str(i) for i in dlist])

        return datetime.datetime.strptime(dstring, '%Y %j %H %M').strftime(
            '%A, %Y %B %d. %H:%M:%S')
