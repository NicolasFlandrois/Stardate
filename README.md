# STARDATE - v2.0

**Date**: Mon 24 Jun 2019 17:41:36 CEST  - **Stardate** 97079.93

**Author**: Nicolas Flandrois

**Licence**: MIT License - Copyright (c) 2019 - Nicolas Flandrois

-----------------------------------------
## Script description:

From launch, the program will automatically display the current Stardate (cf: Stardate Now), followed by a main menu:

1. Compute Today's Stardate. (cf: Stardate Now)
2. To convert a Date into Stardate. (cf: Stardate Convertor)
3. To Translate a Stardate into a Date. (cf:Stardate Translator)
4. Return to main menu.
5. To Quit.


### Stardate Now:

This script intend to compute Stardate, according to current time defined by the user computer. It is using customized reference points for calculation, according to [STO [^6] Stardate generator](https://www.stoacademy.com/tools/stardate.php).
If the user wants to set up customized reference points, he/she needs to modify (b, c) variables in the sdconfig.json file. [^1]

- Current date and time, Earthdate (defined by user computer).
- Whether the current year is a Leap Year or a Normal Year.
- Current Stardate

### Stardate Convertor:
    
This script intend to convert an Earthdate into a Stardate. It is using customized reference points for calculation, according to [STO Stardate generator](https://www.stoacademy.com/tools/stardate.php).
If the user wants to set up customized reference points, he/she needs to modify (b, c) variables in the sdconfig.json file. [^1]
    
It will ask the user for inputs, related to the date we want to translate:
    
- Year
- Month (Number of)
- Day of the month
- Hour
- Minutes
    
It will display on your consol:
    
- Earthdate (the date the user inputed, as a reminder).
- Whether the current year is a Leap Year or a Normal Year.
- Corresponding Stardate.

### Stardate Translator:
    
This script intend to translate a Stardate into an Earthdate. It is using customized reference points for calculation, according to [STO Stardate generator](https://www.stoacademy.com/tools/stardate.php).
If the user wants to set up customized reference points, he/she needs to modify (b, c) variables in the sdconfig.json file. [^1]

> **Note**: Due to the nature of a Stardate and approximation (rounding at 2 decimals), the translation of the stardate has a leap error of 2 minutes.

It will ask the user to inputs the stardate we want to translate:

- Stardate

It will display in your consol:

- Stardate (the date the user inputed, as a reminder).
- Whether the current year is a Leap Year or a Normal Year.
- Corresponding Earthdate.

---------------------------------------------------
## Requirements:
+ Python 3.7 and above.
+ No other requirements, all modules are part of Python's standard Library.

---------------------------------------------------
# taH pagh taHbe <<< To continue or to not continue >>>

## Why? How? And a few thoughts to consider.

A stardate is a fictional system of time measurement developed for the television and film series Star Trek. In the series, use of this date system is commonly heard at the beginning of a voiceover log entry such as: 

> "Captain's log, stardate 41153.7. Our destination is planet Deneb IV..." 

While the general idea resembles the Julian day currently used by astronomers, writers and producers have selected numbers using different methods over the years, some more arbitrary than others. This makes it impossible to convert all stardates into equivalent calendar dates, especially since stardates were originally intended to disguise the precise era of Star Trek.


From *'Star Treck: The Next Generation'* Stardates became more formalized.
Today, the following algorythm is admited in Star Trek fan univers, to convert a date:


> c + (1000*(y-b)) + ((1000/n)*(m + d -1)) = Stardate
> 
> c = Stardate reference point
> 
> b = Earthdate reference point
> 
> y = Earth Year to convert
> 
> n = Either 365 or 366, depending if the year to convert is a leap year or not.
> 
> m = Earth Month to convert
> 
> d = Earth Day to convert

> ***Nota Benne***: (m+d) = ISO-8601 day of the year's number. e.g. June 10th, 2018 = Year 2018, Day 161

The most important piece of information: **1 Earth Year = 1000 Stardate units**.

The MMORPG, [Star Trek Online (STO)](https://www.stoacademy.com/tools/stardate.php), uses this algorythm in their online date converter.

They are kind of the reference online.

However, I will attract your attention to ***1967's instructions regarding Stardates***, when the original TV series was created.

> **[Star Trek Guide (April 17, 1967, p. 25)](https://en.wikipedia.org/wiki/Stardate)**:
>
> We invented "Stardate" to avoid continually mentioning Star Trek's century (actually, about two hundred years from now), and getting into arguments about whether this or that would have developed by then. Pick any combination of four numbers plus a percentage point, use it as your story's stardate. For example, 1313.5 is twelve o'clock noon of one day and 1314.5 would be noon of the next day. Each percentage point is roughly equivalent to one-tenth of one day. The progression of stardates in your script should remain constant but don't worry about whether or not there is a progression from other scripts. Stardates are a mathematical formula which varies depending on location in the galaxy, velocity of travel, and other factors, can vary widely from episode to episode. [^2]

So! Star Trek creators defined themselves that stardates vary according to MULTIPLE Factors:

> - Mathematical Calculation
> 
> - Location in the Galaxy
>
> - Velocity of space travel (usually in FTL - Faster than light speed)
>
> - Traveling through the Galaxy
>
> - Travel point of origin
>
> - Travel Destination
>
> - etc... etc... etc... and lots of unknow factors.

I, personnaly, especially appreciate:

> "Stardates in YOUR script should remain consistant. But don't worry whether or not there is a progression in other scripts.
> [...][A stardate] can vary wildely from episod to episode [, as the crew travels between episodes, through the Galaxy, at upper than light speed... and other unknown factors into play... and messed up the stardate count]."
   
And on that matter, all Star Trek writters did wonders!
Stardates are MESSED UP! Well if you went to follow stardates in a linear Earth-like chronological order.
And we are not even talking about Alernative timelines, yet. Which seem to happen frequently in Star Trek Univers- STU [^5].

Actually, my point is:

- Consider that YOU are the writter of your own (STU) story.
- You are in a relative fixed location in the Galaxy, and within a (stable) linear timeline.

In Consequences, and from above description [***Giving you PERMISSION !***] from STU creators themselves:

- Choose your own stardate reference point. One that Suits you, and your needs.
- Be consistent with yourself.
- Do whatever you want with it! They did! So Why not us?

Still, that's *not a reason to do crazy stuff*.
In this repository, you will also find a .txt documents offering few reference points.

There is an exemple, to choose and use a stardate reference point.

1. Let say/consider, that you want to incarnate your alternet self in the STU.
1. What timeline do you want to be contemporary with?
1. Would you like to be in the same period of time as the UFP (United Federation of Planets) creation?
1. Or, would you prefer to be in the same timeline as your vavorit Star Trek character?

1. Now that you chose your timeline, lets crossreference and reverse engineer a few reference points.

1. In my exemple, I want to be born the same year as *Captain J.L. Picard*.
1. As *real life* birth year = 1970 *(Arbitrary & random exemple)*
1. JL PIcard's birthdate = July 13th 2305 (Earthdate) = Unknown Stardate.
1. We take as reference point: SD 2263.02 = 02 JAN 2305 [^3]

1. So the Delta between our reference point and Picard's year of birth is 42 Earth Years = 42000 Stardate units.
1. Consequently, we can deduce [or reverse engineer], that Picard's Stardate of birth is 44791.77.

1. Now back to the our *Alternate-STU-Ego*'s birth Year = *1970* [^4]
1. Simply use "1970" as Earth date reference point and "*44263*" as Stardate reference point.
    + **b = 1970**
    + **c = 44263**

1. Now use/compute those reference points *{b:1970, c:44263}* [^1], launch the python script.
1. It will give you the current (*real time*) Stardate.

> ***Note***: if not modified, the script will give a Stardate in STO reference point. [^1]

If you prefer to calculate your Stardate every time by hand, that's cool too! You are free to have fun!

# Qapla'

------------------------
[^1]: To change the reference points, please modify the ***sdconfig.json*** file.

[^2]: source: [Wikipedia Stardate](https://en.wikipedia.org/wiki/Stardate)

[^3]: As it's a major (also very tragic) reference point in all STU. Who dosn't like Vulcans, and would like to give them homage?

[^4]: In my exemple I arbitrary use that date, you can use the year you prefer.. according to your liking or the meaning it has e.g. Wedding Anniversary, the first time you kissed a boy/girl, the first "on air" release date of Star Trek original series's first episode, or any event in Earth history!

[^5]: STU = Star Trek Univers

[^6]: STO = [Star Trek Online](https://www.stoacademy.com)