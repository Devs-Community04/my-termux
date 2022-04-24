import os, sys, time
from time import sleep

try:
  import lolcat
except:
  os.system("pkg up -y; pkg i python -y; pip install lolcat")
def logo():
  os.system("clear")
  os.system("echo '\t██████╗░░█████╗░░█████╗░░░██╗██╗\n\t██╔══██╗██╔══██╗██╔══██╗░██╔╝██║\n\t██║░░██║██║░░╚═╝██║░░██║██╔╝░██║\n\t██║░░██║██║░░██╗██║░░██║███████║\n\t██████╔╝╚█████╔╝╚█████╔╝╚════██║\n\t╚═════╝░░╚════╝░░╚════╝░░░░░░╚═╝' | lolcat")
  slog = "\t Make Google Your Best Friend!\n"
  for x in slog:
    sleep(0.1)
    sys.stdout.write(x)
    sys.stdout.flush()
  os.system("echo '=============================================='|lolcat")
  
def update ():
  logo ()
  print("Termux Update and Upgrading.......")
  os.system("pkg up -y; clear")
  
def bpkg ():
  logo ()
  os.system("pkg i git python python2 php ruby rust openssl openssh wget curl nano unzip tar zip bash clang namp figlet toilet zsh -y")
def pip ():
  logo ()
  os.system("pip install bs4 requests mechanize lolcat myspeed; pip2 install requests bs4 lolcat mechanize")
  
def menu ():
  os.system("termux-open-url https://www.facebook.com/groups/2078563798832259/?ref=share")
  logo ()
  os.system("echo '\n\t[01] PKG UPDATE & UPGRADE \n\t[02] BASIC PKG INSTALL\n\t[03] PIP INSTALL\n\t[04] INSTALL P10K\n\t[05] INSTALL KALI\n\t[06] CONTACT\n\t[07] EXIT\n'|lolcat")
  x = str(input("\t\033[32mSELECT OPTION : "))
  if x == "1":
    update ()
  elif x == "2":
    bpkg ()
  elif x == "3":
    pip ()
  elif x == "4":
    os.system (". <(curl -L git.io/zsh.sh)")
  elif x == "5":
    os.system("pkg update -y && pkg upgrade  -y && pkg in git  ncurses-utils proot -y && cd $HOME && git clone https://github.com/BDhaCkers009/proot-distro.git  && cd ~/proot-distro && bash install.sh && cd $HOME && rm -rf ~/proot-distro && clear &&  proot-distro install kali")
  elif x == "6":
    os.system("termux-open-url https://www.facebook.com/groups/2078563798832259/?ref=share")
    menu ()
  elif x == "7":
    sys.exit()
  else:
    menu ()
menu ()
