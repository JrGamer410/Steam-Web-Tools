import requests

def isvacenabled(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Valve Anti-Cheat enabled" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response

def hasinapppurchases(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "In-App Purchases" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    
def hasleveleditor(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Includes level editor" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response

def hassteamworkshop(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Steam Workshop" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    
def hassourcesdk(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Includes Source SDK" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    
def hasachievements(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Steam Achievements" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    
def usessteamcloud(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Steam Cloud" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    
def supportsfamilysharing(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Family Sharing" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    
def hassingleplayer(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Single-player" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    
def hasonlinecoop(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Online co-op" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    
def hastradingcards(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Steam Trading Cards" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    
def hassplitscreenpvp(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Shared/Split Screen PvP" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response

def hasonlinepvp(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Online PvP" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    
def haslanpvp(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "LAN PvP" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    
def hasstats(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Stats" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    
def hasdlc(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Downloadable Content" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    
def hascommentary(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Commentary available" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    
def hascrossplatformmultiplayer(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Cross-Platform Multiplayer" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    
def hasadditionalhighqualityaudio(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Additional High-Quality Audio" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    
def supportssteaminputapi(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Steam Input API" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    
def supportsremoteplayontv(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Remote Play on TV" in steam_response.text:
        steam_app_response = "Yes"
        steam_app_response = str(steam_app_response)
        return steam_app_response
    else:
        steam_app_response = "No"
        steam_app_response = str(steam_app_response)
        return steam_app_response