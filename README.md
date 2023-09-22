# GuardianAngel
Watchdog DIY (hardware+firmware) for Astrophotography and Astronomy
Ok, so first, the name "Guardian Angel" is temporary - I was not able to come up with anything better since I started this DIY project a few weeks ago. 
The idea is to have an independant "observer" or "monitor", that is able to take measurements in real time of all the basic stuff you would normally do by hand while doing AP, and raise an alert, an alarm, or simply write a log, should anything go wrong with the pier,  like an obvious discrepancy between slew position and actual position of the OTA, unexpected rain etc. 
It's currently being developped and is well on its way. The core is an Arduino Nano paired with a GSM module (SIM800L) and a microSD card module on a protoPCB, which takes measures as soon as the pier is powered on. 
These measures are provided by : 
- A rain detector (LM393 / FR-04  50mm*40mm)
- A gyroscope (MPU6050)
- A vibration detector (SW420)
- A barometer (BMP180)
- A temp/humidity sensor (DHT11)
As it stands now , the Guardian is able to detect when:
- the weather is about to degrade unexpectedly (for instance, increase in temp and humidity + drop of atm. pressure indicating the approach of a local thunderstorm) 
- something is interfering with the OTA (animal, wind, snag..)
- rain, snow or excess condensation are appearing (and can differentiate using weather computations based on baro/temp/humidity values)
- the slew is noticeably different from theoretical values (every once in a while my scope will point straight up and stick there for no obvious reason)
- a meridian flip went haywire
- the scope stops moving but is not in park position,
etc.
It also automatically sends a handshake sms to my phone when I power the pier on, to confirm that all systems and probes (and the GSM link itself) have booted normally, and (will) interface with NINA to send a GoodNight message with a status report once NINA has finished its nightly sequence. 
When any of these happen,  the severity of the issue is evaluated, and depending on the situation, the Guardian will simply log the event, send a text to my phone with the basic data/infos (and wait for an answer and instructions) and, if no response arrives within 10 minutes, it will either send another text or, if there is an emergency (noticeable rain for instance) , it will call my phone (which rings with an alarm ringtone for this specific contact even if my phone is on silent) 
Basically, this gadget will do all the basic monitoring to avoid wasting a full night for a stupid thing that is easily detected but would require to stay up at night or to half sleep  with an eye on the computer from the bed. 
If anyone is interested, I'll post the schematics, parts list, firmware, software and docs here when it is sufficiently stable and complete. For now, it's only an advanced prototype. NB : it POINTS OUT issues and pulls you out of bed if needed, it does not take any action - for now. As a second phase of dev, I am considering having it able to cut all electrics on the pier (for emergency stops) either in response to a command (sent by SMS) or off its own initiative, using a master relay., and a few other possibilities of direct action.
It is standalone and does not require USB/WIFI connexion because its main function is to be a totally redundant system that oversees the physical reality of the pier's behaviour independantly of what the session manager and the telescope controller are doing or believing they are doing. 
Any input, remark, suggestion or question welcome.
