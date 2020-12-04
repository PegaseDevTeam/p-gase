import os  
from pegase import *


class sniffingSpoofingMenu:
    def __init__(self):
        clearScr()
        logo()
        print(
            "   {1}--SEToolkit - Tool aimed at penetration testing around Social-Engineering")
        print("   {2}--SSLtrip - MITM tool that implements SSL stripping  attacks")
        print(
            "   {3}--pyPISHER - Tool to create a mallicious website for password pishing")
        print("   {4}--SMTP Mailer - Tool to send SMTP mail\n ")
        print("   {99}-Back To Main Menu \n")
        choice6 = input(pegasePrompt)
        clearScr()
        if choice6 == "1":
            setoolkit()
        elif choice6 == "2":
            ssls()
        elif choice6 == "3":
            pisher()
        elif choice6 == "4":
            smtpsend()
        elif choice6 == "99":
            main()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        input("Completed, click return to go back")
        self.__init__()

def smtpsend():
    os.system("wget http://pastebin.com/raw/Nz1GzWDS --output-document=smtp.py")
    clearScr()
    os.system("python smtp.py")
    
def pisher():
    os.system("wget http://pastebin.com/raw/DDVqWp4Z --output-document=pisher.py")
    clearScr()
    os.system("python pisher.py")

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


def ssls():
    print('''sslstrip is a MITM tool that implements Moxie Marlinspike's SSL stripping
    attacks.
    It requires Python 2.5 or newer, along with the 'twisted' python module.''')
    if yesOrNo():
        os.system("git clone --depth=1 https://github.com/moxie0/sslstrip.git")
        os.system("apt-get install python-twisted-web")
        os.system("python sslstrip/setup.py")
    else:
        sniffingSpoofingMenu.completed("SSlStrip")


sniffingSpoofingMenu()