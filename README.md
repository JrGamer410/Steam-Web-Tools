# Steam Web Tools
 A simple Python library to get information about Steam apps using their webpage

 # Installation
 To install the library, run the following command:
 ```
pip install steam-web-tools
```
Once installed, use the following command to import it into your script:
```
from steamwebtools import *
```
# Commands
Here are all the commands included in the library: <br>
Note: If you encounter an error with this library, you may need to convert the returned value into a string. <br> Example:
```
vac = isvacenabled(440) # Using App ID 440 (Team Fortress 2) as an example
vac = str(vac)
print(vac)
```
__isvacenabled(app_id)__
```
vac = isvacenabled(440) # Using App ID 440 (Team Fortress 2) as an example
print(vac)
```
Response:
```
Yes
```
__hasinapppurchases(app_id)__
```
purchases = hasinapppurchases(440) # Using App ID 440 (Team Fortress 2) as an example
print(purchases)
```
Response:
```
Yes
```
__hasleveleditor(app_id)__
```
leveleditor = hasleveleditor(440) # Using App ID 440 (Team Fortress 2) as an example
print(leveleditor)
```
Response:
```
Yes
```
__hassteamworkshop(app_id)__
```
workshop = hassteamworkshop(440) # Using App ID 440 (Team Fortress 2) as an example
print(workshop)
```
Response:
```
Yes
```
__hassourcesdk(app_id)__
```
sdk = hassourcesdk(440) # Using App ID 440 (Team Fortress 2) as an example
print(sdk)
```
Response:
```
No
```
__hasachievements(app_id)__
```
achievements = hasachievements(440) # Using App ID 440 (Team Fortress 2) as an example
print(achievements)
```
Response:
```
Yes
```
__usessteamcloud(app_id)__
```
steamcloud = usessteamcloud(440) # Using App ID 440 (Team Fortress 2) as an example
print(steamcloud)
```
Response:
```
No
```
__supportsfamilysharing(app_id)__
```
familysharing = supportsfamilysharing(440) # Using App ID 440 (Team Fortress 2) as an example
print(familysharing)
```
Response:
```
No
```
__hassingleplayer(app_id)__
```
singleplayer = hassingleplayer(440) # Using App ID 440 (Team Fortress 2) as an example
print(singleplayer)
```
Response:
```
No
```
__hasonlinecoop(app_id)__
```
coop = hasonlinecoop(440) # Using App ID 440 (Team Fortress 2) as an example
print(coop)
```
Response:
```
No
```
__hastradingcards(app_id)__
```
tradingcards = hastradingcards(440) # Using App ID 440 (Team Fortress 2) as an example
print(tradingcards)
```
Response:
```
Yes
```
__hassplitscreenpvp(app_id)__
```
splitscreenpvp = hassplitscreenpvp(440) # Using App ID 440 (Team Fortress 2) as an example
print(splitscreenpvp)
```
Response:
```
No
```
__haslanpvp(app_id)__
```
lanpvp = haslanpvp(440) # Using App ID 440 (Team Fortress 2) as an example
print(lanpvp)
```
Response:
```
No
```
__hasstats(app_id)__
```
stats = hasstats(440) # Using App ID 440 (Team Fortress 2) as an example
print(stats)
```
Response:
```
Yes
```
__hasdlc(app_id)__
```
dlc = hasdlc(440) # Using App ID 440 (Team Fortress 2) as an example
print(dlc)
```
Response:
```
No
```
__hascommentary(app_id)__
```
commentary = hascommentary(440) # Using App ID 440 (Team Fortress 2) as an example
print(commentary)
```
Response:
```
Yes
```
__hasstats(app_id)__
```
crossplatformmultiplayer = hascrossplatformmultiplayer(440) # Using App ID 440 (Team Fortress 2) as an example
print(crossplatformmultiplayer)
```
Response:
```
Yes
```
__hasadditionalhighqualityaudio(app_id)__
```
additionalhighqualityaudio = hasadditionalhighqualityaudio(440) # Using App ID 440 (Team Fortress 2) as an example
print(additionalhighqualityaudio)
```
Response:
```
No
```
__supportssteaminputapi(app_id)__
```
steaminputapi = supportssteaminputapi(440) # Using App ID 440 (Team Fortress 2) as an example
print(steaminputapi)
```
Response:
```
No
```
__supportsremoteplayontv(app_id)__
```
remoteplayontv = supportsremoteplayontv(440) # Using App ID 440 (Team Fortress 2) as an example
print(remoteplayontv)
```
Response:
```
No
```
