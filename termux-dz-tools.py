import os,sys,time

def jalan(z):
	for e in z +'\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
        
        
print("\031[1;31m")
logo = """
          န์์์์์ััััััััััุุุุุุุุุุุุุุุุืืืืื้้้้ 
                  ♛⇝Source⇝: Termux dz

                  ♛⇝Telegram⇝: https://t.me/Termux_DZ_Hacker
        
                  ♛ ⇝youtube⇝: termux_dz_kali_linux                                             
   န์์์์์ััััััััััุุุุุุุุุุุุุุุุืืืืื้้้้้้้              
                                                                          န์์์์์ััััััััััุุุุุุุุุุุุุุุุืืืืื้      
         န์์์์์ััััััััััุุุุุุุุุุุุุุุุืืืืื้ 
                                               န์์์์์ััััััััััุุุุุุุุุุุุุุุุืืืืื้้้้้้้้่่

──▄────▄▄▄▄▄▄▄────▄───
─▀▀▄─▄█████████▄─▄▀▀──
─────██─▀███▀─██──────
───▄─▀████▀████▀─▄────
─▀█────██▀█▀██────█▀──
                                                                       န์์์์์ััััััััััุุุุุุุุุุุุุุุุืืืืื้้้้้้้้่่่่่

                                                                     န์์์์์ััััััััััุุุุุุุุุุุุุุุุืืืืื้้้้้้้้่่่่่


       န์์์์์ััััััััััุุุุุุุุุุุุุุุุืืืืื้้้้้้้้่่่่่      
"""

os.system('clear')


jalan("\033[1;33m█████████")
jalan("\033[1;33m█▄█████▄█")
jalan("\033[1;33m█\033[1;31m▼▼▼▼▼")
jalan("\033[1;33m█ \033[1;35mTermux🇩🇿")
jalan("\033[1;33m█\033[1;31m▲▲▲▲▲")
jalan("\033[1;33m█████████")
jalan("\033[1;33m██   ██")


time.sleep(3)
os.system('clear')
print(logo)

def list():
	print("\033[1;32m[1] \033[1;32mbasics termux")
	print("\033[1;32m[2] \033[1;32mngrok")
	print("\033[1;32m[3] \033[1;32mmetasploit")
	print("\033[1;32m[4] \033[1;32mtermux root")
	print("\033[1;32m[5] \033[1;32mTelegram")
	print("\033[1;32m[6] \033[1;32mtermux dz")
	print("\033[1;32m[0] \033[1;32mExit")
print("")
list()
print("")

choose = input("\033[1;36m[?] \033[1;32mchoose :")

print(" \033[1;37m")

if choose =="1":
	os.system("pkg update && upgrade;pkg install x11-repo -y;pkg install unstable-repo -y;pkg install root-repo -y;pkg install grep -y;pkg install perl -y;pkg install proot -y;pkg install w3m -y;pkg install clang -y;pkg install unrar -y;pkg install net-tools -y;pkg install zip -y;pkg install wgetrc -y;pkg install openssh -y;pkg install tar -y;pkg install tor -y;pkg install curl -y;pkg install lolcat -y;pkg install cowsay -y;pkg install toilet -y;pkg install havij -y;pkg install host -y;pkg install golang -y;pkg install ruby -y;pkg install wget -y;pkg install python -y;pkg install python2 -y;pkg install git;pkg install nano -y;pkg install php -y;pkg install unzip;pkg install lolcat;pkg install figlet -y")
	jalan("\033[1;33mupdated")
	time.sleep(2)
	os.system('python termux-dz-tools.py')


elif choose =="2":
	os.system("pkg update -y;pkg upgrade -y;pkg install git;git clone https://github.com/Dhiyae/Ngrok-termux-dz.git ;cd Ngrok-termux-dz ; python Ngrok-termux-dz.py")
	jalan("\033[1;33mtermux-dz")
	time.sleep(2)
	os.system('python termux-dz-tools.py')
	
elif choose =="3":
	os.system("pkg update -y;pkg upgrade -y;pkg install git -y;git clone https://github.com/Dhiyae/metasploit-termux-dz.git;cd metasploit-termux-dz;python metasploit-termux-dz.py")
	jalan("\033[1;33mtermux-dz")
	time.sleep(2)
	os. system('python termux-dz-tools.py')
	
elif choose =="4":
	os.system("apt upgrade -y;apt update -y;apt install git -y;git clone https://github.com/Bhayou/Root-Termux/;cd Root-Termux;bash root21.sh")
	jalan("\033[1;33mtermux-dz")
	time.sleep(2)
	os. system('python termux-dz-tools.py')
	
elif choose =="5":
	os.system("xdg-open https://t.me/Termux_DZ_Hacker ")
	
elif choose =="6":
	os.system("xdg-open https://youtube.com/channel/UCt8pMJ2iq9WNPEGtD5YCvfg ")

elif choose =="0":
	os.system('exit')

else:
	jalan("\033[1;35mplaese choose 1 or 2 or 3 or 0 for exit")
	os. system('python termux-dz-tools.py')
	

	

	
	
	


	
	

