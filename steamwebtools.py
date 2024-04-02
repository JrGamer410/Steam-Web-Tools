import requests

def isvacenabled(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Valve Anti-Cheat enabled" in steam_response.text:
        return "Yes"
    else:
        return "No"

def hasinapppurchases(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "In-App Purchases" in steam_response.text:
        return "Yes"
    else:
        return "No"
    
def hasleveleditor(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Includes level editor" in steam_response.text:
        return "Yes"
    else:
        return "No"

def hassteamworkshop(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Steam Workshop" in steam_response.text:
        return "Yes"
    else:
        return "No"
    
def hassourcesdk(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Includes Source SDK" in steam_response.text:
        return "Yes"
    else:
        return "No"
    
def hasachievements(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Steam Achievements" in steam_response.text:
        return "Yes"
    else:
        return "No"
    
def usessteamcloud(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Steam Cloud" in steam_response.text:
        return "Yes"
    else:
        return "No"
    
def supportsfamilysharing(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Family Sharing" in steam_response.text:
        return "Yes"
    else:
        return "No"
    
def hassingleplayer(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Single-player" in steam_response.text:
        return "Yes"
    else:
        return "No"
    
def hasonlinecoop(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Online co-op" in steam_response.text:
        return "Yes"
    else:
        return "No"
    
def hastradingcards(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Steam Trading Cards" in steam_response.text:
        return "Yes"
    else:
        return "No"
    
def hassplitscreenpvp(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Shared/Split Screen PvP" in steam_response.text:
        return "Yes"
    else:
        return "No"

def hasonlinepvp(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Online PvP" in steam_response.text:
        return "Yes"
    else:
        return "No"
    
def haslanpvp(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "LAN PvP" in steam_response.text:
        return "Yes"
    else:
        return "No"
    
def hasstats(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Stats" in steam_response.text:
        return "Yes"
    else:
        return "No"
    
def hasdlc(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Downloadable Content" in steam_response.text:
        return "Yes"
    else:
        return "No"
    
def hascommentary(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Commentary available" in steam_response.text:
        return "Yes"
    else:
        return "No"
    
def hascrossplatformmultiplayer(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Cross-Platform Multiplayer" in steam_response.text:
        return "Yes"
    else:
        return "No"
    
def hasadditionalhighqualityaudio(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Additional High-Quality Audio" in steam_response.text:
        return "Yes"
    else:
        return "No"
    
def supportssteaminputapi(app_id):
    steam_url = f"https://store.steampowered.com/app/{app_id}"
    steam_response = requests.get(steam_url)
    if "Steam Input API" in steam_response.text:
        return "Yes"
    else:
        return "No"