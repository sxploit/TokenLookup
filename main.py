import requests
from colorama import Fore

token = input("> ")
ly = Fore.LIGHTYELLOW_EX
w = Fore.WHITE

headers = {
    "Authorization": token,
    "Content-Type": "application/json"
}
r = requests.get("https://discord.com/api/v10/users/@me", headers=headers)
if r.status_code == 200:
    user_data = r.json()
    print(f"{ly}Username{w}⋮ {user_data['username']}")
    print(f"{ly}ID{w}⋮ {user_data['id']}")
    print(f"{ly}Email{w}⋮ {user_data.get('email', 'Unkown Error')}")
    print(f"{ly}Phone{w}⋮ {user_data.get('phone', 'Phone not found')}")
    print(f"{ly}2Fa{w}⋮ {'Yes' if user_data['mfa_enabled'] else "No"}")
    print(f"{ly}CREATOR{w}⋮ github.com/sxploit")
else:
    print(f"Error: {r.status_code}, {r.text}")
