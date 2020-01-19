import os
try:
	from colorama import Fore, Back, Style
except:
	os.system("pip install colorama")
	from colorama import Fore, Back, Style
	
os.system("clear")
print(Fore.YELLOW + ''' ________    _____     ____     __    __   _____        _____  
(___  ___)  / ____\   / __ \    ) )  ( (  (_   _)      / ____\ 
    ) )    ( (___    / /  \ \  ( (    ) )   | |       ( (___   
   ( (      \___ \  ( ()  () )  ) )  ( (    | |        \___ \  
    ) )         ) ) ( ()  () ) ( (    ) )   | |   __       ) ) 
   ( (      ___/ /   \ \__/ /   ) \__/ (  __| |___) )  ___/ /  
   /__\    /____/     \____/    \______/  \________/  /____/'''+Fore.RED+'''

00) Превратить ваше устройство в хакинг машину'''+Fore.GREEN+'''

01) Nmap (web сканирование) 

02) Sherlock (Поиск ников по разным соц-сетям

03) Instagram + cupp (Брут паролей инстаграм + создание словаря)

04)termux-ngrok (создание публичных url)

05)CAM-HACKERS (Получение ip различных камер)

06)metasploit-framework (Тут я в двух словах не обьясню, придется гуглит)

ps. В случае ошибков порыскайте в инете

07)PhoneInfoga (Информация о владельце номера)

8)SayHello (Заполучение снимка лица человека находившегося в вашей точке доступа)
''')

choose = int(input(Fore.YELLOW+"Выберите число: "+Style.RESET_ALL))
os.system("clear")
if choose == 0:
	#1
	os.system("apt install nmap")
	#2
	os.system("git clone https://github.com/sherlock-project/sherlock.git")
	#3
	os.system("git clone https://github.com/Pure-L0G1C/Instagram.git")
	os.system("git clone https://github.com/Mebus/cupp.git")
	#4
	os.system("git clone https://github.com/tchelospy/termux-ngrok.git")
	#5
	os.system("git clone https://github.com/AngelSecurityTeam/Cam-Hackers")
	#6
	os.system("pkg install root-repo")
	os.system("pkg install perl")
	os.system("pkg install ruby")
	os.system("apt update && apt upgrade")
	os.system("pkg uodate && pkg upgrade")
	os.system("pkg install metasploit")
	#7
	os.system("git clone https://github.com/sundowndev/PhoneInfoga")
	#8
	os.system("git clone https://github.com/thelinuxchoice/saycheese")

elif choose == 1:
	os.system("apt install nmap")

elif choose == 2:
	os.system("git clone https://github.com/sherlock-project/sherlock.git")

elif choose == 3:
	os.system("git clone https://github.com/Pure-L0G1C/Instagram.git")
	os.system("git clone https://github.com/Mebus/cupp.git")

elif choose == 4:
	os.system("git clone https://github.com/tchelospy/termux-ngrok.git")

elif choose == 5:
	os.system("git clone https://github.com/AngelSecurityTeam/Cam-Hackers")

elif choose == 6:
	os.system("pkg install root-repo")
	os.system("pkg install perl")
	os.system("pkg install ruby")
	os.system("apt update && apt upgrade")
	os.system("pkg uodate && pkg upgrade")
	os.system("pkg install metasploit")
	
elif choose == 7:
	os.system("git clone https://github.com/sundowndev/PhoneInfoga")

elif choose == 8:
	os.system("git clone https://github.com/thelinuxchoice/saycheese")

os.system("clear")
print(Fore.BLUE+"Загрузка прошла успешно, удачного хакинга (В ознакомительных целях конечно же)"+Style.RESET_ALL)
