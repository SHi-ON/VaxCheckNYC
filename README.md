## VAX Check NYC 
Check COVID-19 vaccine appointments availability and notifies the user by sending email.
The script runs every 3 seconds and request the website of state-run vaccination centers in NY.

### Usage
Change `PROVIDER_IDS` in `vax_check.py` to your 
desired vaccine center ID according to the provided table below. Run the 
script `python vax_check.py` and enjoy the automation!

#### Send Email
You need to create a file `secrets.env` similar to the provided example 
having your email credentials.


### Providers IDs
List of vaccine centers and their corresponding IDs **as of April 9, 2021** 
(subject to change):

| Provider Name | Provider ID |
| ------------- | ----------- | 
|SUNY Corning Community College |  1025 |
|Rochester Dome Arena |  1012 | 
|SUNY Binghamton |  1009 |
|Plattsburgh International Airport |  1008 |
|SUNY Potsdam  |  1006 |
|State Fair Expo Center: NYS Fairgrounds  |  1002 |
|SUNY Polytechnic Institute |  1010 |
|**Washington Avenue Armory - Albany, Schenectady, Troy  |  1016 |
|SUNY Albany |  1003 |
|Suffolk CCC - Brentwood |  1028 |
|Bronx - Bay Eden Senior Center |  1024 |
|**Medgar Evers College - Brooklyn |  1014 |
|**Delavan Grider Community Center - Buffalo |  1018 |
|University at Buffalo South Campus |  1011 |
|SUNY Old Westbury |  1029 |
|**York College - Health and Physical Education Complex - Queens |  1013 |
|SUNY Orange |  1031 |
|Ulster Fairgrounds in New Paltz |  1033 |
|Javits Center |  1019 |
|Javits Center |  1000 |
|The Conference Center Niagara Falls |  1026 |
|SUNY Oneonta |  1030 |
|Queensbury Aviation Mall - Sears |  1034 |
|**Former Kodak Hawkeye Parking Lot - Rochester |  1017 |
|**Former Kodak Hawkeye Parking Lot - Rochester | 1027 |
|Aqueduct Racetrack  |  1007 |
|Stony Brook - Southampton |  1032 |
|SUNY Stony Brook  |  1005 |
|SUNY Rockland Community College |  1035 |
|State Fair Expo Center: NYS Fairgrounds |  1020 |
|Jones Beach - Field 3  |  1001 |
|Westchester County Center |  1004  |
|**New York National Guard Armory - Yonkers and Mount Vernon |  1015 |
