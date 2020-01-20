import os
import time
import random
import sys
try:
	from colorama import Fore, Back, Style
except:
	os.system("pip install colorama")
	from colorama import Fore, Back, Style

var = 1
choose = 1
a=0
b=0
while b == 0:
	lang = input("Choose language:\n1)English\n2)Русский\n")
	try:
		lang = int(lang)
		b=1
	except:
		n=3
		for i in range(3):
			print("Please enter a number")
			print(n)
			n-=1
			time.sleep(1)
			os.system("clear")

if lang == 2:
	os.system("clear")
	ban = Style.BRIGHT+''' ________    _____     ____     __    __   _____        _____  
(___  ___)  / ____\   / __ \    ) )  ( (  (_   _)      / ____\ 
    ) )    ( (___    / /  \ \  ( (    ) )   | |       ( (___   
   ( (      \___ \  ( ()  () )  ) )  ( (    | |        \___ \  
    ) )         ) ) ( ()  () ) ( (    ) )   | |   __       ) ) 
   ( (      ___/ /   \ \__/ /   ) \__/ (  __| |___) )  ___/ /  
   /__\    /____/     \____/    \______/  \________/  /____/'''

	while var == 1:
	 
		colors = list(vars(Fore).values())
		colored_chars = [random.choice(colors) + ban]
		print(''.join(colored_chars))
		print(Fore.RED+'''

00) Превратить ваше устройство в хакинг машину'''+Fore.GREEN+'''

01)Nmap (web сканирование) 

02)Sherlock (Поиск ников по разным соц-сетям)

03)Instagram + cupp (Брут паролей инстаграм + создание словаря)

04)termux-ngrok (создание публичных url)

05)CAM-HACKERS (Получение ip различных камер)

06)metasploit-framework (Тут я в двух словах не обьясню, придется гуглить)

ps. В случае ошибок порыскайте в инете

07)PhoneInfoga (Информация о владельце номера)

08)SayHello (Заполучение снимка лица человека находившегося в вашей точке доступа)

09)Morpheus (Создание mitm (man-in-the-middle) атак)

10)RED_HAWK (Сканирование сетей)
'''+Fore.RED+'''
99)ВЫХОД (Какое должно быть описание у выхода?)
''')

		choose = input(Fore.YELLOW+"Выберите число: "+Style.RESET_ALL)
		os.system("clear")
		try:
			choose = int(choose)
			var = 0
		except:
			var = 1
			S = 3
			for i in range(3):
				print("Введите пожалуйста число...")
				print(S)
				S -= 1
				time.sleep(1)
				os.system("clear")
			
			time.sleep(1)
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
		#9
		os.system("git clone https://github.com/r00t-3xp10it/morpheus.git")
		#10
		os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')

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

	elif choose == 9:
		os.system("git clone https://github.com/r00t-3xp10it/morpheus.git")

	elif choose == 10:
		os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')



	elif choose == 666:
		a=1
		print(Fore.RED+'''
            ______              
       .d$$$******$$$$c.        
    .d$P"            "$$c      
   $$$$$.           .$$$*$.    
 .$$ 4$L*$$.     .$$Pd$  '$b   
 $F   *$. "$$e.e$$" 4$F   ^$b  
d$     $$   z$$$e   $$     '$. 
$P     `$L$$P` `"$$d$"      $$ 
$$     e$$F       4$$b.     $$ 
$b  .$$" $$      .$$ "4$b.  $$ 
$$e$P"    $b     d$`    "$$c$F 
'$P$$$$$$$$$$$$$$$$$$$$$$$$$$  
 "$c.      4$.  $$       .$$   
  ^$$.      $$ d$"      d$P    
    "$$c.   `$b$F    .d$P"     
      `4$$$c.$$$..e$$P"        
          `^^^^^^^
''')
		print("Что тебе надо, смертный?")
		choose2 = input("Что бы дойти до зоветной пасхалки тебе надо сюда вписать секретный пароль: ")
	
		try:
			choose2 = int(choose2)
		except:
			print("Я не прощаю ошибок")
			time.sleep(3)
			sys.exit()
		if choose2 == 25:
			print("Хах, просто угадал")
			choose2 = input("Пароль: ")
		
			try:
				choose2 = int(choose2)
			except:
				print("Я не прощаю ошибок")
				time.sleep(3)
				sys.exit()
			if choose2 == 1:
				print("Ты точно смертный?")
				choose2 = input("Пароль: ")
			
				try:
					choose2 = int(choose2)
				except:
					print("Я не прощаю ошибок")
					time.sleep(3)
					sys.exit()
				if choose2 == 14:
					print("Не может быть")
					choose2 = input("Пароль: ")
				
					try:
						choose2 = int(choose2)
					except:
						print("Я не прощаю ошибок")
						time.sleep(3)
						sys.exit()
					if choose2 == 16:
						print("Что ты такое?")
						choose2 = input("Пароль: ")
					
						try:
							choose2 = int(choose2)
						except:
							print("Я не прощаю ошибок")
							time.sleep(3)
							sys.exit()
						if choose2 == 5:
							print("Невозможно")
							choose2 = input("Пароль: ")
						
							try:
								choose2 = int(choose2)
							except:
								print("Я не прощаю ошибок")
								time.sleep(3)
								sys.exit()
							if choose2 == 11:
									print("НЕЕЕЕЕЕЕТ*пшик*")
									time.sleep(2)
									os.system("clear")
									s = 10
									for l in range(10):
										print(Fore.GREEN+"https://t.me/joinchat/AAAAAFZH_cXHs8d78bakTg")
										print("Копируй быстрее")
										print(s)
										s -= 1
										time.sleep(1)
										os.system("clear")
									sys.exit()
	elif choose == 99:
		sys.exit()
	if a==0:
		os.system("clear")
		print(Fore.BLUE+"Загрузка прошла успешно, удачного хакинга (В ознакомительных целях конечно же)"+Style.RESET_ALL)
elif lang == 1:
	print("Cooming soon")
