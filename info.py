'''
Information Gathering Tools Classes
'''
import os  
from colorama import Fore, Back, Style, init
from pegase import *
class informationGatheringMenu:

    def __init__(self):
        clearScr()
        logo()

        print("  {1}--Nmap - Network Mapper")
        print("  {2}--Setoolkit")
        print("  {3}--Host To IP")
        print("  {4}--WPScan")
        print("  {5}--CMSmap")
        print("  {6}--XSStrike")
        print("  {7}--Doork")
        print("  {8}--Crips\n  ")
        print("  {99}-Back To Main Menu \n")
        choice2 = input(pegasePrompt)
        clearScr()
        if choice2 == "1":
            nmap()
        elif choice2 == "2":
            setoolkit()
        elif choice2 == "3":
            host2ip()
        elif choice2 == "4":
            wpscan()
        elif choice2 == "5":
            CMSmap()
        elif choice2 == "6":
            XSStrike()
        elif choice2 == "7":
            doork()
        elif choice2 == "8":
            crips()
        elif choice2 == "99":
            main()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        input("Completed, click return to go back")
        self.__init__()

class setoolkit:
    def __init__(self):
        self.installDir = "setoolkit"
        self.gitRepo = "https://github.com/trustedsec/social-engineer-toolkit.git"

        if not self.installed():
            self.install()
            self.run()
        else:
            print(alreadyInstalled)
            self.run()
        response = input(continuePrompt)    

    def installed(self):
        return (os.path.isfile("/usr/bin/setoolkit"))

    def install(self):
        os.system("apt-get --force-yes -y install git apache2 python-requests libapache2-mod-php \
            python-pymssql build-essential python-pexpect python-pefile python-crypto python-openssl")
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("cd %s && python setup.py install" % self.installDir)

    def run(self):
        os.system("setoolkit")

class wpscan:

    def __init__(self):
        self.installDir = "wpscan"
        self.gitRepo = "https://github.com/wpscanteam/wpscan.git"

        if not self.installed():
            self.install()
        clearScr()
        logo()
        target = input("   Enter a Target: ")
        self.menu(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone --depth=1 %s %s" +
                  (self.gitRepo))

    def menu(self, target):
        clearScr()
        logo()
        print("   WPScan for: %s\n" % target)
        print("   {1}--Username Enumeration [--enumerate u]")
        print("   {2}--Plugin Enumeration [--enumerate p]")
        print("   {3}--All Enumeration Tools [--enumerate]\n")
        print("   {99}-Return to information gathering menu \n")
        response = input(pegasePrompt)
        clearScr()
        logPath = "../../logs/wpscan-" + \
            strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".txt"
        wpscanOptions = "--no-banner --random-agent --url %s" % target
        try:
            if response == "1":
                os.system(
                    "ruby tools/wpscan/wpscan.rb %s --enumerate u --log %s" % (wpscanOptions, logPath))
                response = input(continuePrompt)
            elif response == "2":
                os.system(
                    "ruby tools/wpscan/wpscan.rb %s --enumerate p --log %s" % (wpscanOptions, logPath))
                response = input(continuePrompt)
            elif response == "3":
                os.system(
                    "ruby tools/wpscan/wpscan.rb %s --enumerate --log %s" % (wpscanOptions, logPath))
                response = input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)



class host2ip:

    def __init__(self):
        clearScr()
        logo()
        host = input("   Enter a Host: ")
        ip = socket.gethostbyname(host)
        print("   %s has the IP of %s" % (host, ip))
        response = input(continuePrompt)

class nmap:

    def __init__(self):
        self.gitRepo = "https://github.com/nmap/nmap.git"

        self.targetPrompt = "   Enter Target IP/Subnet/Range/Host: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/nmap") or os.path.isfile("/usr/local/bin/nmap"))

    def install(self):
        os.system("git clone --depth=1 %s %s" 
                  (self.gitRepo))
        os.system("cd %s && ./configure && make && make install")

    def run(self):
        clearScr()
        logo()
        target = input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        logo()
        print("   Nmap scan for: %s\n" % target)
        print("   {1}--Simple Scan [-sV]")
        print("   {2}--Port Scan [-Pn]")
        print("   {3}--Operating System Detection [-A]\n")
        print("   {99}-Return to information gathering menu \n")
        response = input(pegasePrompt)
        clearScr()
        logPath = "logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        try:
            if response == "1":
                os.system("nmap -sV -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "2":
                os.system("nmap -Pn -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "3":
                os.system("nmap -A -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

informationGatheringMenu()