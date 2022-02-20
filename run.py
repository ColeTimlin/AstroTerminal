import os
from termcolor import cprint
from pyfiglet import figlet_format

version = "1.2"
year = "2022"

os.system("title Astro Terminal " + version)
cprint(figlet_format('Astro Terminal', font='big'),
       'blue', attrs=['bold'])

print("Version " + version + " " + year)

help = "-Commands-\n \nhelp (shows all commands)\nping (pings a certain web address and/or IP)\ncd (gets current directory of this application)\npip (allows you to install pip packages, straight from our terminal)\nipconfig (shows you your IP configuration)\ntaskmanager (opens the task manager application on your computer, making it easy to check your computer's performance)"

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
    