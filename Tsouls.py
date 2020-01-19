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

elif choose == 1:
	os.system("apt install nmap")

elif choose == 2:
	os.system("git clone https://github.com/sherlock-project/sherlock.git")

elif choose == 3:
	os.system("git clone https://github.com/Pure-L0G1C/Instagram.git")
	os.system("git clone https://github.com/Mebus/cupp.git")

elif choose == 4:
	os.system("git clone https://github.com/tchelospy/termux-ngrok.git")
os.system("clear")
print(Fore.BLUE+"Загрузка прошла успешно, удачного хакинга (В ознакомительных целях конечно же(:)"+Style.RESET_ALL)