import os
import fortnite_api
from termcolor import cprint
from pyfiglet import figlet_format
import urllib.request
import json


version = "1.2"
year = "2022"

def stats(user):
    print("----- Stats for player: "+ user + "-----\n")
    print(fn.stats.fetch_by_name(user))

os.system("title Astro Terminal " + version)
cprint(figlet_format('Astro Terminal', font='big'),
       'blue', attrs=['bold'])

print("\033[1;37;40mVersion " + version + " " + year + " (type 'help' for a list of commands)")

help = "\033[1;33;40m=====\033[1;37;40mCommands\033[1;33;40m=====\033[1;37;40m\n \nhelp (shows all commands)\nping (pings a certain web address and/or IP)\ncd (gets current directory of this application)\npip (allows you to install pip packages, straight from our terminal)\nipconfig (shows you your IP configuration)\ntaskmanager (opens the task manager application on your computer, making it easy to check your computer's performance)\nfnstats (allows you to use the fortnite-api.com API to find any Fortnite player's stats; you need to supply your own API key)\ncrcards (shows a list of all cards in Clash Royale and their max level; you need to supply your own API key)"

while True:

    command= input(" >>> ")
    if command == "help":
        print(" \n" + help + " \n")
    if command == "pinger":
        ipInput = input("IP Address to be pinged: ")
        n = input("The IP is going to be pinged [100] times. Continue [y/n]: ")
        if n == "y":
            ip_list = [ipInput]
            for ip in ip_list:
                for x in range(100):
                    response = os.popen(f"ping {ip}").read()
                    if "Received = 4" in response:
                        print("\033[1;32;40m UP " + "\033[1;37;40m" f"{ip} Ping Successful")
                    else:
                        print("\033[1;31;40m DOWN " + "\033[1;37;40m" + f"{ip} Ping Unsuccessful")
                    pass
    if command == "cd":
        print(f"Current Directory: {os.getcwd()}")
    if command == "color":
        print("Colors:")
        print("-\033[1;32;40mGreen\n\033[1;37;40m-\033[1;31;40mRed\033[1;37;40m\n-\033[1;34;40mBlue\033[1;37;40m\n-\033[1;35;40mPurple\033[1;37;40m\n-\033[1;37;40mWhite")
        c = input("Select color: ")
        c = c.upper()

        if c.upper() == "RED" or c.upper() == "BLUE" or c.upper() == "GREEN" or c.upper() == "PURPLE" or c.upper() == "WHITE":
            print("\033[1;32;40mValid Color!")

            if(c == "GREEN"):
                print("\033[1;32;40mGreen Selected!")
            if(c == "RED"):
                print("\033[1;31;40mRed Selected!")
            if(c == "BLUE"):
                print("\033[1;34;40mBlue Selected!")
            if(c == "PURPLE"):
                print("\033[1;35;40mPurple Selected!")
            if(c == "WHITE"):
                print("\033[1;37;40mWhite Selected!")
        else:
            print("\033[1;31;40mInvalid Color!\033[1;37;40m")
    if command == "pip":
        cmd = input("What would you like to install in PIP?: ")
        py = input("What is the directory of the folder where the python.exe file is located?: ")
        os.system(f'cmd /c "{py}\python.exe -m pip install {cmd}"')
    if command == "ipconfig":
        os.system('cmd /c "ipconfig"')
    if command == "taskmanager":
        os.system("start Taskmgr")
    if command == "fnstats":
        fileName = "key"
        print("Add API key in 'key.txt'. Retrieve it at https://www.fortnite-api.com")
        file = open(f"{fileName}.txt",encoding='latin-1')
        full_text = file.read()
        fn = fortnite_api.FortniteAPI(full_text)
        user = input("Player Epic Games Account: ")
        stats(user)
    if command == "crcards":
        input("You must first supply an API key in the 'crkey.txt' file. Retrieve a key at https//api.clashroyale.com. Click enter when key is supplied")
        with open("crkey.txt") as f:
            key = f.read().rstrip("\n")
            url = "https://api.clashroyale.com/v1/"
            endpoint = "cards"
        
        

            request = urllib.request.Request(
                        url+endpoint,
                        None,
                        {
                            "Authorization": "Bearer %s" % key
                        }
            )
            response = urllib.request.urlopen(request).read().decode("utf-8")
            data = json.loads(response)

            for item in data["items"]:
                print("\n%s \n[Max Level: %d]" % (item["name"], item["maxLevel"]))