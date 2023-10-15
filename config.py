########################################################################
#### >>>      Guardian Angel V1.00                              <<< ####
#### >>>      Author: Arnaud "Frenchy" Prevot                   <<< ####
#### >>>      https://github.com/FrenchyArnaud/GuardianAngel    <<< ####
########################################################################

########################################################################
#### >>>        CONFIGURATION FILE                              <<< ####
#### >>>        TUNE TO YOUR NEEDS                              <<< ####
########################################################################


# If you mess up badly, 
# simply delete this file
# and reboot the App.
# A fresh copy of this file will be generated 




                #### >>>#########################<<< ####
                #### >>>     SETTING UP LIMITS   <<< ####
                #### >>>#########################<<< ####

#       priority H or L,  min val, max val : CaSe SeNsItIvE
#       if left empty, will be set to  = ["L","",""]
#       and will use default hard coded values.
#       You can monitor between values, exclude values, or set a limit

#       Example :
#       limits_rain = ["H","","10"]
#       will trigger a high priority alert as soon as a value of 10 is reached

#       Example :
#       limits_Press = ["L","1010","1025"]
#       will trigger a low priority alert if the atmospheric pressure
#       gets outside of the 1010-1025 range

#       Example :
#       limits_percent  = ["H","21",""]
#       will trigger a high priority alert if the laptop battery falls to 20% charge
#       and another one if the battery reaches 100% charge


#       Example :
#       limits_Z  = ["H","270","90"] -- note that 270 > 90 --
#       will trigger a high priority alert if the OTA 
#       is sloped more than 90deg or less than 270deg aka going upside down
#       with counte weights above OTA
#       (Possible because the gyroscope understands that 0 = 360 so 360 > 270 and 360 < 90)


limits_tmpDHT = ["L","-40","60"]
#temperature as read from humidiy sensor, Celsius
# Should be left as default.

limits_tmpBMP = ["L","-40","60"]
# temperature as read from barometer sensor, Celsius
# Should be left as default.

limits_tmpGYR = ["L","-40","60"]
# temperature as read from gyroscope, Celsius
# Should be left as default.

limits_Hum = ["L","15","85"]
# relative humidity, 0% to 100%

limits_Press = ["L","101000","102600"]
# barometric (atmospheric) pressure in HectoPascals (typically = 1013)

limits_X = ["L","-180","180"]
# angle of the OTA on the X axis in deg

limits_Y = ["L","-180","180"]
# angle of the OTA on the Y axis in deg

limits_Z = ["L","-180","180"]
# angle of the OTA on the Z axis in deg

limits_gx = ["L","-1","1"]
# angular speed of the OTA on the X axis in deg/min

limits_gy = ["L","-1","1"]
# angular speed of the OTA on the Y axis in deg/min

limits_gz = ["L","-1","1"]
# angular speed of the OTA on the Z axis in deg/min

limits_rain = ["H","0","5"]
# value returned by the sensor, should be in the range 0-1024
# but this varies with the droplet plate. See
# docs for calibration and recommended values.

limits_tmpAVG = ["L","-5","24"]
# Air temperature considered by the system for weather calculations.
# CALCULATED, NOT MEASURED.
# you can change the reading priority with the value tmpAVG_src
# usefull if you are at risk for frost for instance.

limits_dewpt = ["L","3",""]
# NEGATIVE DIFFERENCE between air temperature and dew point.
# CALCULATED, NOT MEASURED.
# This does not consider the maxValue but uses only the minValue.
# example:
# limits_dewpt = ["L","2",""]
# will trigger an alert if the difference between dew point
# and air temperature is less than 2 degrees.
# Dew point is by definition inferior to air temperature
# and tends to increase.
# when dewpt is almost equal to air temp,
# it is raining or there is fog.
# Useful to start or strengthen dew heaters.

limits_percent  = ["H","15","100"]
# Alert trigger for the computer battery charge in %.
# REPORTED BY OS, NOT MEASURED.

limits_secsleft = ["L","600",""]
# Alert trigger for the computer battery charge in seconds of power left.
# REPORTED BY OS, NOT MEASURED.
# For instance, use limits_secsleft = ["H","900",""] to receive a high priority notification
# when the computer has less than 15mins of charge left.

limits_power_plugged = ["H","0","1"]
# Is the computer plugged in?
# REPORTED BY OS, NOT MEASURED.
# There is no conceivable scenario where this value should be changed.


                #### >>>#########################<<< ####
                #### >>>    SETTING UP OPTIONS   <<< ####
                #### >>>#########################<<< ####


muteNotif = 90
# minimum time in seconds between successive notifications.
# value recommended is 90 but anything is suitable.
# However, consider that if a dew point alert for instance is triggered, it will also prevent
# rain or power alerts to go through for the same duration. 

freq = 15
# frequency of refresh. I.E. if freq = 7, data will be transmitted once every 7 seconds.
# For all intents and purposes, 10 to 30 is more than often enough.
# values under 5 seconds are ignored by the system and a 5 secs value is used.
# Think that smaller values (high refresh frequencies) can generate massive log files.
# Unless you have a specific reason to change this value, you should not.
# increasing it will not notably decrease the CPU load and
# decreasing it lengthens the calculation lag exponentially
# Tests show that there is virtually no difference in input smoothness between 12 and 30. 

priorityAlert = "L"
# Default priority value
# L for LOW, H for HIGH.
# With the recommended notification service settings, 
# HIGH repeats until acknowledged even with the phone on SILENT.
# LOW does not repeat and obeys the SILENT rule of the phone.
# HIGH sends an ALARM, LOW sends an ALERT

yourEmail = "frenchyarnaud@gmail.com"
# STRONGLY RECOMMEND CREATING AN EMAIL ACCOUNT SPECIFICALLY FOR THIS APP
# MUST BE A GMAIL ACCOUNT, WITH APP PASSWORD ENABLED,
# SEE : https://support.google.com/mail/?p=InvalidSecondFactor

password = 'fqxo sjoh hnto raki'
# APP PASSWORD ENABLED FOR GMAIL ACCOUNT
# SEE : https://support.google.com/mail/?p=InvalidSecondFactor

lowPriorityAlertEmail = "5bi3shodgt@pomail.net"
# LOW PRIORITY >>> LOW AND HIGH CAN BE THE SAME

highPriorityAlertEmail = "ib51porqqq@pomail.net"
# HIGH PRIORITY  >>> LOW AND HIGH CAN BE THE SAME

subject00 = "Telescope Alert"
#   Default header for low priority notifications
#   This can be set to anything entertaining such as :
#   "Message from JWST"

subject01 ="!! TELESCOPE ALARM !!"
#   Default header for high priority notifications
#   This can be set to anything entertaining such as :
#   "Beam me up out of bed, Scotty!"


                #### >>>#########################<<< ####
                #### >>>     ADVANCED OPTIONS    <<< ####
                #### >>>#########################<<< ####

                #### >>>#########################<<< ####
                #### >>> YOU SHOULD NOT EDIT THIS<<< ####
                #### >>> UNLESS YOU UNDERSTAND IT<<< ####
                #### >>>#########################<<< ####

useLowPass = "Y"
#Yes, No, Auto > Y N A

lowPass = "M"
# Weak, Medium, Strong > W M S
# Used if uselowPass = A
# this sets customLowPass and customLowPassCal at recommanded values automatically
# with customLowPass based on 50,75 or 100% of max delay as freq / (1 - customLowPass)
# and with customLowPassCal = customLowPass * 1.100

customLowPass = 0.833
# scale is 0.000 > 1.000
# Applies only on MEASURED values, not CALCULATED nor REPORTED
# formula is Val = [{Val * (1 - customLowPass)} + (previousVal * customLowPass)] then previousVal = Val.
# so that new Val is integrated for (1 - customLowPass) at each cycle.
# recommand high customLowPass (0.850+) at high refresh rates (under 15 secs)
# recommand low customLowPass (0.350-) at low refresh rates (over 60 secs)
# normalisation delay can be calculated by : delay = freq / (1 - customLowPass)
# take it into account so that normalisation happens before any relevant change
# can happen during the imaging session. 

#example 1:
# freq = 12
# customLowPass = 0.666
# delay = 12 / (1.000- 0.666) = 36 secs.
# this is ok, under 45secs latency will not change much.
# You probably can push the value up to 0.750.

#example 2:
# freq = 30
# customLowPass = 0.975
# delay = 30 / (1.000- 0.975) = 1200 secs.
# this is not ok, a heavy summer shower has enough time to totally submerge the OTA in 20 mins.

# as a rule of thumb you want the normalisation delay to be just less than the muteNotif
# that you have set as this is the time you consider safe.
# for instance if you have muteNotif = 120
# and freq = 20, you probably want customLowPass = 0.830 maximum 
# because 20 / (1 - 0.830) = 117 seconds (about 6 cycles)
# and  customLowPass = 0.666 minimum
# because 20 / (1 - 0.666) = 60 seconds (about 3 cycles)
# so a safe and efficient value would be around the half way point, that's about 0.745.

customLowPassCal = 0.915
# Same as customLowPass but applies only on Calculated and Reported Values.

trace = 1
# Log level. Change to 2 or 3 only if there are crashes or need for debug.
# 0 = no log, 1 = logging datas, 2 = logging errors, 3 = logging datas + errors

tmpAVG_src = "235"
#   all 3 sensors in equal weight, recommended value
#   2 = DHT11, 3 = BMP, 5 = GYRO.
#   if you suspect a sensor is off by too much you can exclude it and give more weight to another.
#   for instance, if you think the dht11 (designated 2) temperature is erratic,
#   you can deactivate it and give more weight to the value returned by the gyroscope (5)
#   for this, use : tmpAVG_src = "355"
#   Order is irrelevant : "523" is equivallent to "235", "553" to "355" and "535".
#   To use a specific sensor only, simply make it unique : "333" will force
#   the use of the temperature sensor of the BMP180 ONLY and discard the others.
#   Useful if one of your sensor is calibrated.


# the following values are the thresholds for trigger when a vale derives from
# the initial set of values too much.
# The App evaluates the sensor returns on their own (for instance "rain detected")
# but it also evaluates the evolution of values(for instance, "barometer dropping fast and humidity increasing fast"
# meaning rain is arriving very shortly. 
# For instance, comp_tmpAVG = 5 means that if tmpAVG varies by more than +5 or -5 degree Celsius,
# a trigger is generated.
# Changing these values is probably a bad idea and can lead to unpredictable results.
comp_tmpDHT = 5.000
comp_tmpBMP = 5.000
comp_tmpGY = 5.000
comp_Hum = 10
comp_Press = 6.000
comp_X = 0.650
comp_Y = 0.650
comp_Z = 0.650
comp_gx = 0.120
comp_gy = 0.120
comp_gz = 0.12
comp_rain = 1
comp_tmpAVG = 5.000
comp_dewpt = 2.750
comp_percent = 10
comp_secsleft = 60
comp_power_plugged = 0.001




























