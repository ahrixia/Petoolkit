#!/usr/bin/env python3

import os
import subprocess
import sys
import socket
import datetime
import webbrowser
from termcolor import colored

Tool_directory = os.path.dirname(os.path.abspath(__file__)) + '/'

def pentest():
    Sclear()
    global startbanner,banner1,banner2,banner3,banner4,banner5,banner6,banner7,bannernet,bannerweb,quitbanner,cmd 
    startbanner = '''    
PPPPPPPPPPPPPPPPP  EEEEEEEEEEEEEEEEEEEEETTTTTTTTTTTTTTTTTTTTTTT                            lllllllkkkkkkkk            iiii         tttt          
P::::::::::::::::P E::::::::::::::::::::T:::::::::::::::::::::T                            l:::::lk::::::k           i::::i     ttt:::t          
P::::::PPPPPP:::::PE::::::::::::::::::::T:::::::::::::::::::::T                            l:::::lk::::::k            iiii      t:::::t          
PP:::::P     P:::::EE::::::EEEEEEEEE::::T:::::TT:::::::TT:::::T                            l:::::lk::::::k                      t:::::t          
  P::::P     P:::::P E:::::E       EEEEETTTTTT  T:::::T  TTTTTooooooooooo     ooooooooooo   l::::l k:::::k    kkkkkkiiiiiittttttt:::::ttttttt    
  P::::P     P:::::P E:::::E                    T:::::T     oo:::::::::::oo oo:::::::::::oo l::::l k:::::k   k:::::ki:::::t:::::::::::::::::t    
  P::::PPPPPP:::::P  E::::::EEEEEEEEEE          T:::::T    o:::::::::::::::o:::::::::::::::ol::::l k:::::k  k:::::k  i::::t:::::::::::::::::t    
  P:::::::::::::PP   E:::::::::::::::E          T:::::T    o:::::ooooo:::::o:::::ooooo:::::ol::::l k:::::k k:::::k   i::::tttttt:::::::tttttt    
  P::::PPPPPPPPP     E:::::::::::::::E          T:::::T    o::::o     o::::o::::o     o::::ol::::l k::::::k:::::k    i::::i     t:::::t          
  P::::P             E::::::EEEEEEEEEE          T:::::T    o::::o     o::::o::::o     o::::ol::::l k:::::::::::k     i::::i     t:::::t          
  P::::P             E:::::E                    T:::::T    o::::o     o::::o::::o     o::::ol::::l k:::::::::::k     i::::i     t:::::t          
  P::::P             E:::::E       EEEEEE       T:::::T    o::::o     o::::o::::o     o::::ol::::l k::::::k:::::k    i::::i     t:::::t    tttttt
PP::::::PP         EE::::::EEEEEEEE:::::E     TT:::::::TT  o:::::ooooo:::::o:::::ooooo:::::l::::::k::::::k k:::::k  i::::::i    t::::::tttt:::::t
P::::::::P         E::::::::::::::::::::E     T:::::::::T  o:::::::::::::::o:::::::::::::::l::::::k::::::k  k:::::k i::::::i    tt::::::::::::::t
P::::::::P         E::::::::::::::::::::E     T:::::::::T   oo:::::::::::oo oo:::::::::::ool::::::k::::::k   k:::::ki::::::i      tt:::::::::::tt
PPPPPPPPPP         EEEEEEEEEEEEEEEEEEEEEE     TTTTTTTTTTT     ooooooooooo     ooooooooooo  lllllllkkkkkkkk    kkkkkkiiiiiiii        ttttttttttt  '''
    banner1 = '''
dP          .8888b                                         dP   oo                       .88888.             dP   dP                         oo                   
88          88   "                                         88                           d8'   `88            88   88                                              
88 88d888b. 88aaa  .d8888b. 88d888b. 88d8b.d8b. .d8888b. d8888P dP .d8888b. 88d888b.    88        .d8888b. d8888P 88d888b. .d8888b. 88d888b. dP 88d888b. .d8888b. 
88 88'  `88 88     88'  `88 88'  `88 88'`88'`88 88'  `88   88   88 88'  `88 88'  `88    88   YP88 88'  `88   88   88'  `88 88ooood8 88'  `88 88 88'  `88 88'  `88 
88 88    88 88     88.  .88 88       88  88  88 88.  .88   88   88 88.  .88 88    88    Y8.   .88 88.  .88   88   88    88 88.  ... 88       88 88    88 88.  .88 
dP dP    dP dP     `88888P' dP       dP  dP  dP `88888P8   dP   dP `88888P' dP    dP     `88888'  `88888P8   dP   dP    dP `88888P' dP       dP dP    dP `8888P88 
                                                                                                                                                              .88 
                                                                                                                                                          d8888P  '''
    banner2 = '''
.d88888b                                      oo                   
88.    "'                                                          
`Y88888b. .d8888b. .d8888b. 88d888b. 88d888b. dP 88d888b. .d8888b. 
      `8b 88'  `"" 88'  `88 88'  `88 88'  `88 88 88'  `88 88'  `88 
d8'   .8P 88.  ... 88.  .88 88    88 88    88 88 88    88 88.  .88 
 Y88888P  `88888P' `88888P8 dP    dP dP    dP dP dP    dP `8888P88 
                                                               .88 
                                                           d8888P   '''
    banner3 = '''
 88888888b                   dP          oo   dP              dP   oo                   
 88                          88               88              88                        
a88aaaa    dP.  .dP 88d888b. 88 .d8888b. dP d8888P .d8888b. d8888P dP .d8888b. 88d888b. 
 88         `8bd8'  88'  `88 88 88'  `88 88   88   88'  `88   88   88 88'  `88 88'  `88 
 88         .d88b.  88.  .88 88 88.  .88 88   88   88.  .88   88   88 88.  .88 88    88 
 88888888P dP'  `dP 88Y888P' dP `88888P' dP   dP   `88888P8   dP   dP `88888P' dP    dP 
                    88                                                                  
                    dP                                                                   '''
    banner4 = '''
 888888ba                      dP       88888888b                   dP          oo   dP              dP   oo                   
 88    `8b                     88       88                          88               88              88                        
a88aaaa8P' .d8888b. .d8888b. d8888P    a88aaaa    dP.  .dP 88d888b. 88 .d8888b. dP d8888P .d8888b. d8888P dP .d8888b. 88d888b. 
 88        88'  `88 Y8ooooo.   88       88         `8bd8'  88'  `88 88 88'  `88 88   88   88'  `88   88   88 88'  `88 88'  `88 
 88        88.  .88       88   88       88         .d88b.  88.  .88 88 88.  .88 88   88   88.  .88   88   88 88.  .88 88    88 
 dP        `88888P' `88888P'   dP       88888888P dP'  `dP 88Y888P' dP `88888P' dP   dP   `88888P8   dP   dP `88888P' dP    dP 
                                                           88                                                                  
                                                           dP                                                                      '''
    banner5 = '''
 888888ba                                                                dP     a88888b.                            dP       oo                   
 88    `8b                                                               88    d8'   `88                            88                            
a88aaaa8P' .d8888b. .d8888b. .d8888b. dP  dP  dP .d8888b. 88d888b. .d888b88    88        88d888b. .d8888b. .d8888b. 88  .dP  dP 88d888b. .d8888b. 
 88        88'  `88 Y8ooooo. Y8ooooo. 88  88  88 88'  `88 88'  `88 88'  `88    88        88'  `88 88'  `88 88'  `"" 88888"   88 88'  `88 88'  `88 
 88        88.  .88       88       88 88.88b.88' 88.  .88 88       88.  .88    Y8.   .88 88       88.  .88 88.  ... 88  `8b. 88 88    88 88.  .88 
 dP        `88888P8 `88888P' `88888P' 8888P Y8P  `88888P' dP       `88888P8     Y88888P' dP       `88888P8 `88888P' dP   `YP dP dP    dP `8888P88 
                                                                                                                                              .88 
                                                                                                                                          d8888P      '''
    banner6 = '''
.d88888b           oo .8888b .8888b oo                         d88b       .d88888b                             .8888b oo                   
88.    "'             88   " 88   "                            8`'8       88.    "'                            88   "                      
`Y88888b. 88d888b. dP 88aaa  88aaa  dP 88d888b. .d8888b.       d8b        `Y88888b. 88d888b. .d8888b. .d8888b. 88aaa  dP 88d888b. .d8888b. 
      `8b 88'  `88 88 88     88     88 88'  `88 88'  `88     d8P`8b             `8b 88'  `88 88'  `88 88'  `88 88     88 88'  `88 88'  `88 
d8'   .8P 88    88 88 88     88     88 88    88 88.  .88     d8' `8bP     d8'   .8P 88.  .88 88.  .88 88.  .88 88     88 88    88 88.  .88 
 Y88888P  dP    dP dP dP     dP     dP dP    dP `8888P88     `888P'`YP     Y88888P  88Y888P' `88888P' `88888P' dP     dP dP    dP `8888P88 
                                                     .88                            88                                                 .88 
                                                 d8888P                             dP                                             d8888P      '''
    banner7 = '''
 888888ba                                        dP   oo                   
 88    `8b                                       88                        
a88aaaa8P' .d8888b. 88d888b. .d8888b. 88d888b. d8888P dP 88d888b. .d8888b. 
 88   `8b. 88ooood8 88'  `88 88'  `88 88'  `88   88   88 88'  `88 88'  `88 
 88     88 88.  ... 88.  .88 88.  .88 88         88   88 88    88 88.  .88 
 dP     dP `88888P' 88Y888P' `88888P' dP         dP   dP dP    dP `8888P88 
                    88                                                 .88 
                    dP                                             d8888P      '''
    bannernet = '''
888888ba             dP                                dP             d88b        888888ba                      dP      .d88888b                                      oo                   
88    `8b            88                                88             8`'8        88    `8b                     88      88.    "'                                                          
88     88 .d8888b. d8888P dP  dP  dP .d8888b. 88d888b. 88  .dP        d8b        a88aaaa8P' .d8888b. 88d888b. d8888P    `Y88888b. .d8888b. .d8888b. 88d888b. 88d888b. dP 88d888b. .d8888b. 
88     88 88ooood8   88   88  88  88 88'  `88 88'  `88 88888"       d8P`8b        88        88'  `88 88'  `88   88            `8b 88'  `"" 88'  `88 88'  `88 88'  `88 88 88'  `88 88'  `88 
88     88 88.  ...   88   88.88b.88' 88.  .88 88       88  `8b.     d8' `8bP      88        88.  .88 88         88      d8'   .8P 88.  ... 88.  .88 88    88 88    88 88 88    88 88.  .88 
dP     dP `88888P'   dP   8888P Y8P  `88888P' dP       dP   `YP     `888P'`YP     dP        `88888P' dP         dP       Y88888P  `88888P' `88888P8 dP    dP dP    dP dP dP    dP `8888P88 
                                                                                                                                                                                       .88 
                                                                                                                                                                                   d8888P      '''
    bannerweb = '''
dP   dP   dP          dP          .d88888b                                      oo                   
88   88   88          88          88.    "'                                                          
88  .8P  .8P .d8888b. 88d888b.    `Y88888b. .d8888b. .d8888b. 88d888b. 88d888b. dP 88d888b. .d8888b. 
88  d8'  d8' 88ooood8 88'  `88          `8b 88'  `"" 88'  `88 88'  `88 88'  `88 88 88'  `88 88'  `88 
88.d8P8.d8P  88.  ... 88.  .88    d8'   .8P 88.  ... 88.  .88 88    88 88    88 88 88    88 88.  .88 
8888' Y88'   `88888P' 88Y8888'     Y88888P  `88888P' `88888P8 dP    dP dP    dP dP dP    dP `8888P88 
                                                                                                 .88 
                                                                                             d8888P      '''
    quitbanner = '''
 ___       ___ 
|__  \_/ |  |  
|___ / \ |  |  
                   '''
    cmd = colored("    PET ~# ", 'red')

    Sclear()
    print('''\n\n    A Penetration Test, also known as a pen test, is a simulated cyber attack against your computer system to check for exploitable vulnerabilities.
    Pen testing can involve the attempted breaching of any number of application systems, (e.g., application protocol interfaces (APIs),
    frontend/backend servers) to uncover vulnerabilities, such as unsanitized inputs that are susceptible to code injection attacks.\n
    The Main phases of Penetration Testing are :
    
    1. Information Gathering - Information gathering it's the 1st and a very important step for a successful penetration testing. 
                               Information gathering face is where you collect as much as information about a target auto client 
                               system which will lead to finding vulnerabilities in the target system much easily.

    2. Scanning - Scanning searches for weaknesses and vulnerabilities in a system and These scanning techniques are automated and 
                 they will provide a better picture of what can be exploited.

    3. Exploitation - Exploitation phase in penetration testing solely focuses on gaining access to a system or network by getting 
                      past security and firewall. Exploitation phase’s precision and result depends on Vulnerability scanning phase.

    
    4. Post-Exploitation - The main aim of post exploitation is to figure out all the best exploits and vulnerabilities of target 
                           system with a motive to gain access and escalate privileges without getting detected. 

    
    5. Report 
    

    Few more Important Stages that need to be performed in able to qualify Pen testing as well as for CTFs Events are :
    
    Password cracking - Password checking itself process of retrieving passwords of a system or an account by using certain tools 
                        and data that has been transmitted through a computer which will be in a scrambled form.

    Sniffing and Spoofing - There are two types of Internet security breaches Sniffing and Spoofing. Sniffing is art of intercepting 
                            and investigating packets using a sniffer to obtain valuable information about the target system. 
                            Spoofing is art of impersonation or falsifying identification where the attacker poses as someone else to gain information.

    ''')
    input("    Press Enter key to continue")
    Sclear()
    
    while(True):
        print('''\n\nDisclaimer:All the information on this Toolkit is published in good faith and for general information purpose only.
           This platform does not make any warranties about the completeness, reliability and accuracy of this information.
           Any action you take upon the information you find on this Toolkit, is strictly at your own risk.
        ''')
        ans = input("Do you agree to use it for Right purpose? (y/n): ")
        if (ans.lower() == 'y'):
            pet()
        elif (ans.lower() == 'n'):
            print(quitbanner)
            print('\nThanks. We appreciate your kindness...')
            sys.exit(0) 

class pet:
    def __init__(self):
        Sclear()
        now = datetime.datetime.now()
        nowstamp = now.strftime('%H:%M:%S %A, %d %B , %Y')
        print( startbanner + '\n\n    ' + nowstamp + '\n' )
        print( "    1   . Information Gathering" )
        print( "    2   . Scanning" )
        print( "    3   . Exploitation" )
        print( "    4   . Post Exploitation" ) 
        print( "    5   . Password Cracking" )
        print( "    6   . Sniffing & Spoofing" )
        print( "    7   . Reporting" )
        print( "    0   . Exit" )
        choice = input(cmd)
        try:
            if choice == '1':
                infogath()
            elif choice == '2':
                scann()
            elif choice == '3':
                exploit()
            elif choice == '4':
                postexploit()
            elif choice == '5':
                pwdcrack()
            elif choice == '6':
                sniffsnoof()
            elif choice == '7':
                report()
            elif choice == '0':
                Sclear()
                print(quitbanner)
                print('\nThanks For Choosing Our PEToolkit Platform! Have a Great Day :)\n')
                sys.exit(0)
            else:
                self.__init__()
        except KeyboardInterrupt:
            print('\nForce Quitting...Hello user you have pressed ctrl-C button.')
            sys.exit(0) 

class infogath():
     def __init__(self):
        Sclear()
        print(banner1)
        print('    1   -  Host to IP ')
        print('    2   -  NslookUp ')
        print('    3   -  Recong-ng ')
        print('    4   -  theHarvester ')
        print('    5   -  Discover ')
        print('    6   -  Shodan on Internet Browser ')
        print('    7   -  Censys on Internet Browser ')
        print('    0   -  Back to Main Menu')
        choice = input(cmd)
        if choice == '1':
            host2ip()
        elif choice == '2':
            nslookup()
        elif choice == '3':
            recon()
        elif choice == '4':
            theharv()
        elif choice == '5':
            discover()
        elif choice == '6':
            Sclear()
            webbrowser.open('https://www.shodan.io/', new = 2)
            input("Press any key to continue")
            infogath()
        elif choice == '7':
            Sclear()
            webbrowser.open('https://censys.io/', new = 2)
            input("Press any key to continue")
            infogath()
        elif choice == '0':
            pet()
        else:
            self.__init__()


class scann():
    def __init__(self):
        Sclear()
        print(banner2)
        print('    1   - Network and Port Scanning')
        print('    2   - Web Scanning')
        print('    3   - Full Recon and Scan ')
        print('    0   - Back to Main Menu')
        choice = input(cmd)
        if choice == '1':
            netport()
        elif choice == '2':
            webscan()
        elif choice == '3':
            fulrecon()
        elif choice == '0':
            pet()
        else:
            self.__init__()

class netport():
    def __init__(self):
        Sclear()
        print(bannernet)
        print('    1   - Nmap')
        print('    2   - Hping3')
        print('    3   - MassScan')
        print('    0   - Back to Scanning Menu')
        choice = input(cmd)
        if choice == '1':
            nmap()
        elif choice == '2':
            hping3()
        elif choice == '3':
            masscan()
        elif choice == '0':
            scann()
        else:
            self.__init__()

class webscan():
    def __init__(self):
        Sclear()
        print(bannerweb)
        print('    1   - Nikto')
        print('    2   - SQLMap')
        print('    3   - WPScan')
        print('    4   - Dirb')
        print('    5   - SkipFish')
        print('    0   - Back to Main Menu')
        choice = input(cmd)
        if choice == '1':
            nikto()
        elif choice == '2':
            sqlmap()
        elif choice == '3':
            wpscan()
        elif choice == '4':
            dirb()
        elif choice == '5':
            skipfish()
        elif choice == '0':
            scann()
        else:
            self.__init__()

class fulrecon():
    def __init__(self):
        host = input(" Enter the target IP or URL : ")
        self.menu(host)

    def menu(self, host):
        Sclear()
        print('    3klCon Project v1.0 by eslam3kl')
        print('    1   -  Full Recon and Scanning')
        print('    0   -  Back to Main Menu')
        choice = input(cmd)
        if choice == '1': 
            os.system("python 3klcon.py -t %s" % host)
            input("\nPress Enter key to continue")
            fulrecon()
        elif choice == '0':
            scann()
        else:
            self.menu(host)

class exploit():
    def __init__(self):
        Sclear()
        print(banner3)
        print('    OWASP TOP 10 ')
        print('    1   -  Injection')
        print('    2   -  Broken Authentication')
        print('    3   -  Sensitive Data Exposure')
        print('    4   -  XML Enternal Entities XXE')
        print('    5   -  Broken Access Control')
        print('    6   -  Security Misconfiguration')
        print('    7   -  Cross-Site Scripting XSS')
        print('    8   -  Insecure Deserialization')
        print('    9   -  Using Components with Known Vulnerabilities')
        print('    10  - Insufficient Logging & Monitoring')
        print('    99  - Searchsploit')
        print('    0   -  Back to Main Menu')
        choice = input(cmd)
        if choice == '1':
            inject()
        elif choice == '2':
            broauth()
        elif choice == '3':
            sensdata()
        elif choice == '4':
            xxe()
        elif choice == '5':
            broacc()
        elif choice == '6':
            secmisconf()
        elif choice == '7':
            xxs()
        elif choice == '8':
            insecdes()
        elif choice == '9':
            kwnvuln()
        elif choice == '10':
            lognmoni()
        elif choice == '99':
            Sclear()
            service = input(' Enter the Service Name/Version:')
            os.system("searchsploit %s" % service)
            input("\nPress Enter key to continue")
            exploit()
        elif choice == '0':
            pet()
        else :
            self.__init__()        

class postexploit():
    def __init__(self):
        Sclear()
        print(banner4)

class pwdcrack():
    def __init__(self):
        Sclear()
        print(banner5)
        print('    1   -  BruteX')
        print('    2   -  Hydra')
        print('    3   -  JohnThRipper')
        print('    4   -  Hashcat')
        print('    5   -  Ncrack')
        print('    0   -  Back to Main Menu')
        choice = input(cmd)
        if choice == '1':
            brutex()
        elif choice == '2':
            hydra()
        elif choice == '3':
            jtr()
        elif choice == '4':
            hashcat()
        elif choice == '5':
            ncrack()
        elif choice == '0':
            pet()
        else :
            self.__init__()

class sniffsnoof():
    def __init__(self):
        Sclear()
        print(banner6)
        print('    1   -  Setoolkit')
        print('    2   -  Macchanger')
        print('    0   -  Back to Main Menu')
        choice = input(cmd)
        if choice == '1':
            setoolkit()
        elif choice == '2':
            macchanger()
        elif choice == '0':
            pet()
        else :
            self.__init__()

class report():
    def __init__(self):
        Sclear()
        print(banner7)
        print('\n')
        print( "    1   . Information Gathering Report" )
        print( "    2   . Scanning Report" )
        print( "    3   . Metasploit")
        print( "    4   . Wireshark")
        print( "    5   . Burp Suite")
        print( "    6   . Maltego")
        print( "    7   . Metagoofil")
        print( "    99  . Read Report" )
        print( "    0   . Back" )
        choice = input(cmd) 
        if choice == '1':
            inforeport()
        elif choice == '2':
            scanreport()
        elif choice == '3':
            metasploit()
        elif choice == '4':
            wireshark()
        elif choice == '5':
            burpsuite()
        elif choice == '6':
            maltego()
        elif choice == '7':
            metagoofil()
        elif choice == '99':
            Sclear()
            filename = input('Enter the report Name with location: ')
            # a = open(filename, "r")
            temp = open(filename,'r').read().split('\n')
            print (temp)
            input(" \n\n Press Enter to continue...")
            report()
        elif choice == '0':
            pet()
        else :
            self.__init__()

class host2ip():
    def __init__(self):
        Sclear()
        print('''Host2ip- Host2IP helps to convert hostname to IP Address.\n''')
        host = input("HOST:")
        ip = socket.gethostbyname(host)
        print(" %s has the IP of %s" % (host,ip))
        input("\nPress Enter key to continue")
        infogath()

class nslookup():
    def __init__(self):
        Sclear()
        print('''Nslookup- The NsLookup tool allows you to query DNS servers for resource records.\n''')
        host = input("HOST: ")
        os.system("nslookup %s" % host)
        input("\nPress Enter key to continue")
        infogath()

class recon():
    def __init__(self):
        if not self.installed():
            self.install()      
        Sclear()
        print('''Recon-Ng - Recon-ng is a full-featured Web Reconnaissance framework written in Python. Complete with independent modules, database interaction, \nbuilt in convenience functions, interactive help, and command completion, Recon-ng provides a powerful environment in which \nopen source web-based reconnaissance can be conducted quickly and thoroughly.''')
        input("\n\nPress Enter key to continue")
        print('''

        ''')
        self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/recon-ng") or os.path.isfile("/usr/local/bin/recon-ng"))

    def install(self):
        os.system("sudo apt-get install recon-ng")
        
    def run(self):   
        os.system("recon-ng")
        input("\n\nPress Enter key to continue")
        infogath()

class theharv():
    def __init__(self):
        self.Install_directory = Tool_directory + "theHarvester"
        self.gitRepo = "https://github.com/laramies/theHarvester.git"
        if not self.installed():
            self.install()
        Sclear()     
        print('''
        The objective of this program is to gather emails, subdomains, hosts, employee names, open ports and 
        banners from different public sources like search engines, PGP key servers and SHODAN computer database.''')
        host = input("HOST: ")
        self.run(host)

    def installed(self):
        return (os.path.isdir(self.Install_directory))

    def install(self):
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.Install_directory))
        os.system("cd %s && python3 -m pip install -r requirements/base.txt" % self.Install_directory)

    def run(self,host):
        lists = input("List Results (>1): ")
        source = input("Data Source(baidu, bing, google, google-profiles, linkedin, pgp, twitter, virustotal, netcraft, yahoo) : ")
        shodan = input("If Shodan Queries (type '-h') : ")
        os.system("python3 %s/theHarvester.py -d %s -l %s -b %s %s" % (self.Install_directory,host,lists,source,shodan))
        input("\n\nPress Enter key to continue")
        infogath()

class discover(): 
    def __init__(self):
        self.Install_directory = Tool_directory + "discover"
        self.gitRepo = "https://github.com/leebaird/discover.git"
        if not self.installed():
            self.install()
        Sclear()
        print('''Discover- Custom bash scripts used to automate various penetration testing tasks including recon, \nscanning, parsing, and creating malicious payloads and listeners with Metasploit.''')
        input("\n\nPress Enter key to continue")
        self.run()
    
    def installed(self):
        return (os.path.isdir(self.Install_directory))

    def install(self):
        os.system("git clone --depth=1 %s %s" %(self.gitRepo, self.Install_directory))
        os.system("%s/./update.sh" % self.Install_directory)
        
    def run(self):
        os.system("%s/./discover.sh" % self.Install_directory)
        input("\n\nPress Enter key to continue")
        infogath()

class nmap():
    def __init__(self):
        self.Install_directory = Tool_directory + "nmap"
        self.gitRepo = "https://github.com/nmap/nmap.git"
        if not self.installed():
            self.install()
        Sclear()
        print('''
        Nmap - Nmap is used to discover hosts and services on a computer network by sending packets and analyzing the responses.
        Nmap provides a number of features for probing computer networks, including host discovery and service and operating 
        system detection. These features are extensible by scripts that provide more advanced service detection, vulnerability 
        detection, and other features.\n''')
        host = input(" Enter the target IP or URL : ")
        self.menu(host)

    def installed(self):
        return (os.path.isfile("/usr/bin/nmap") or os.path.isfile("/usr/local/bin/nmap"))

    def install(self):
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.Install_directory))
        os.system("cd %s && ./configure && make && make install" %self.Install_directory)

    def menu(self, host):
        print(" NMAP : %s\n" % host)
        print(" 1   . Simple Scan ")
        print(" 2   . Port Scan ")
        print(" 3   . Operating System Scan ")
        print(" 4   . All port Scan ")
        print(" 99  . Manual Scan")
        print(" 0   . Back on Network and Port Scanning ")
        choice = input(cmd)
        if choice == '1':  
            os.system("nmap -sV -F %s" % host)
            input("\nPress Enter key to continue")
            netport()
        elif choice == '2':
            os.system("nmap -Pn %s" % host)
            input("\nPress Enter key to continue")
            netport()
        elif choice == '3':
            os.system("nmap -A %s" % host)
            input("\nPress Enter key to continue")
            netport()
        elif choice == '4':
            os.system("nmap -p- %s" % host)
            input("\nPress Enter key to continue")
            netport()
        elif choice == '99':
            os.system("nmap --help")
            port = input(" Enter only Flag : ")
            os.system("nmap %s %s " % (port,host))
            input("\nPress Enter key to continue")
            netport()
        elif choice == '0':
            netport()
        else:
            self.menu(host)

class hping3():
    def __init__(self):
        if not self.installed():
            self.install()
        Sclear()
        print('''
        hping is a command-line oriented TCP/IP packet assembler/analyzer. The interface is inspired to the ping(8) unix command, but 
        hping isn’t only able to send ICMP echo requests. It supports TCP, UDP, ICMP and RAW-IP protocols, has a traceroute mode, the 
        ability to send files between a covered channel, and many other features.\n''')
        host = input(" Enter the target IP or URL : ")
        self.menu(host)

    def installed(self):
        return (os.path.isfile("/usr/bin/hping3") or os.path.isfile("/usr/local/bin/hping3"))

    def install(self):
        os.system("sudo apt-get install hping3 -y")

    def menu(self, host):
        print(" HPING3 : %s\n" % host)
        print(" 1   . Scan Mode")
        print(" 2   . TraceRoute Mode ")
        print(" 3   . Verbose Scan ")
        print(" 4   . SYN FLood ")
        print(" 99  . Manual Scan")
        print(" 0   . Back on Network and Port Scanning ")
        choice = input(cmd)
        if choice == '1':  
            os.system("sudo hping3 --scan 1-100 -S %s" % host)
            input("\nPress Enter key to continue")
            netport()
        elif choice == '2':
            os.system("sudo hping3 --traceroute -S %s" % host)
            input("\nPress Enter key to continue")
            netport()
        elif choice == '3':
            os.system("sudo hping3 -V -S %s" % host)
            input("\nPress Enter key to continue")
            netport()
        elif choice == '4':
            os.system("sudo hping3 -S --flood -V %s" % host)
            input("\nPress Enter key to continue")
            netport()
        elif choice == '99':
            os.system("hping3 --help")
            port = input(" Enter only Flag : ")
            os.system("hping3 %s %s " % (port,host))
            input("\nPress Enter key to continue")
            netport()
        elif choice == '0':
            netport()
        else:
            self.menu(host)
        
class masscan():
    def __init__(self):
        self.Install_directory = toolDir + "masscan"
        self.gitRepo = "https://github.com/robertdavidgraham/masscan.git"
        if not self.installed():
            self.install()
        Sclear()
        print('''
        This is the fastest Internet port scanner. It can scan the entire Internet in under 6 minutes, transmitting 10 million packets per second.
        It produces results similar to nmap, the most famous port scanner. Internally, it operates more like scanrand, unicornscan, and ZMap, using 
        asynchronous transmission. The major difference is that it’s faster than these other scanners. In addition, it’s more flexible, allowing 
        arbitrary address ranges and port ranges.\n
        NOTE: masscan uses a custom TCP/IP stack. Anything other than simple port scans will cause conflict with the local TCP/IP stack. 
        ''')
        host = input(" Enter the target IP or URL : ")
        self.menu(host)

    def installed(self):
        return (os.path.isfile("/usr/bin/masscan") or os.path.isfile("/usr/local/bin/masscan"))

    def install(self):
        os.system("sudo apt-get install git gcc make libpcap-dev")
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.Install_directory))
        os.system("cd %s && make && sudo make install" % self.Install_directory)

    def menu(self, host):
        Sclear()
        print(" MASSCAN : %s\n" % host)
        print(" 1   . Port Range ")
        print(" 2   . Selected Ports")
        print(" 3   . Exlude List Scan ")
        print(" 4   . Packet Rate Scan ")
        print(" 99  . Manual Scan")
        print(" 0   . Back ")
        choice = input(cmd)
        if choice == '1':
            start = input('Start Range: ')
            end = input('End Range: ') 
            os.system("sudo masscan %s ‐p%s-%s" % (host,start,end))
            input("\nPress Enter key to continue")
            netport()
        elif choice == '2':
            port = input('''Enter Ports(No space just ',' in between): ''')
            os.system("sudo masscan %s -p%s" % (host,port))
            input("\nPress Enter key to continue")
            netport()
        elif choice == '3':
            port = input('''Enter Ports(No space just ',' in between): ''')
            efile = input(' Exclude IP file location: ')
            os.system("masscan %s -p%s --exludefile %s" % (host,port,efile))
            input("\nPress Enter key to continue")
            netport()
        elif choice == '4':
            port = input('''Enter Ports(No space just ',' in between): ''')
            rate = input('Packet rate(Default 10000): ')
            os.system("sudo masscan %s -p%s --rate %s" % (host,port,rate))
            input("\nPress Enter key to continue")
            netport()
        elif choice == '99':
            os.system("masscan --help")
            port = input(" Enter only Flag : ")
            os.system("masscan %s %s " % (port,host))
            input("\nPress Enter key to continue")
            netport()
        elif choice == '0':
            netport()
        else:
            self.menu(host)

class nikto():
    def __init__(self):
        if not self.installed():
            self.install()
        Sclear()
        print('''
        Nikto is an Open Source (GPL) web server scanner which performs comprehensive tests against web servers for multiple items, 
        including over 6700 potentially dangerous files/programs, checks for outdated versions of over 1250 servers, and version 
        specific problems on over 270 servers. 
        ''')
        host = input(" Enter the target IP or URL : ")
        self.menu(host)

    def installed(self):
        return (os.path.isfile("/usr/bin/nikto") or os.path.isfile("/usr/local/bin/nikto"))

    def install(self):
        os.system("sudo apt-get install nikto")

    def menu(self, host):
        Sclear()
        print(" NIKTO : %s\n" % host)
        print(" 1   . Basic Scan ")
        print(" 2   . Port Scan ")
        print(" 3   . SSL Scan ")
        print(" 4   . No SSL Scan ")
        print(" 5   . Tuning Scan - Option List ")
        print(" 6   . Mutate Scan - Option List ")
        print(" 99  . Manual Scan")
        print(" 0   . Back ")
        choice = input(cmd)
        if choice == '1': 
            os.system("nikto -h %s" % host)
            input("\nPress Enter key to continue")
            webscan()
        elif choice == '2':
            port = input('''Enter Ports(No space just ',' in between): ''')
            os.system("nikto -h %s -port %s" % (host,port))
            input("\nPress Enter key to continue")
            webscan()
        elif choice == '3':
            os.system("nikto -h %s -ssl %s" % (host,port))
            input("\nPress Enter key to continue")
            webscan()
        elif choice == '4':
            os.system("nikto -h %s -nossl %s" % (host,port))
            input("\nPress Enter key to continue")
            webscan()
        elif choice == '5': 
            print('''\n1   Interesting file\n2   Misconfiguration\n3   Information Disclosure\n4   Injection (XSS/Script/HTML)\n5   Remote File Retrieval – Inside Web Root\n6   Denial of Service\n7   Remote File Retrieval – Server Wide\n8   Command Execution – Remote Shell\n9   SQL Injection\n0   File Upload\na   Authentication Bypass\nb      Software Identification\nc   Remote Source Inclusion\nx   Reverse Tuning Option ''')
            tuning = input("\nTuning Option: ")
            os.system("nikto -h %s -Tuning %s" % (host,tuning))
            input("\nPress Enter key to continue")
            webscan()
        elif choice == '6': 
            print('''\n1   Test all files in root directory\n2   Guess for password file names\n3   Enumerate user names via apache\n4   Enumerate user names via cgiwrap\n5   Attempt to brute force sub-domain names\n6   Attempt to guess directory names from a file''')
            mutate = input('\nMutate Option: ')
            os.system("nikto -h %s -mutate %s" % (host,mutate))
            input("\nPress Enter key to continue")
            webscan()
        elif choice == '99':
            os.system("nikto --help")
            port = input(" Enter only Flag : ")
            os.system("nikto %s %s " % (port,host))
            input("\nPress Enter key to continue")
            webscan()
        elif choice == '0':
            webscan()
        else:
            self.menu(host)

class sqlmap():
    def __init__(self):
        self.Install_directory = Tool_directory + "sqlmap"
        self.gitRepo = "https://github.com/sqlmapproject/sqlmap.git"
        if not self.installed():
            self.install()
        Sclear()
        print('''
        sqlmap is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws 
        and taking over of database servers. It comes with a powerful detection engine, many niche features for the ultimate penetration 
        tester and a broad range of switches lasting from database fingerprinting, over data fetching from the database, to accessing 
        the underlying file system and executing commands on the operating system via out-of-band connections.
        ''')
        host = input(" Enter the target IP or URL : ")
        self.menu(host)

    def installed(self):
        return (os.path.isdir(self.Install_directory))

    def install(self):
        os.system("git clone --depth=1 %s %s" %(self.gitRepo, self.Install_directory))

    def menu(self, host):
        Sclear()
        print(" SQLMap : %s\n" % host)
        print(" 1   . Scan ")
        print(" 2   . Database")
        print(" 3   . Tables ")
        print(" 4   . Column ")
        print(" 5   . Dumps ")
        print(" 6   . OS Shells ")
        print(" 99  . Manual Scan")
        print(" 0   . Back ")
        choice = input(cmd)
        if choice == '1': 
            os.system("python %s/sqlmap.py -u %s" % (self.Install_directory,host))
            input("\nPress Enter key to continue")
            webscan()
        elif choice == '2':
            os.system("python %s/sqlmap.py -u %s ‐‐dbs" % (self.Install_directory,host))
            input("\nPress Enter key to continue")
            webscan()
        elif choice == '3':
            dbs = input( " Database :")
            os.system("python %s/sqlmap.py -u %s -D %s --table " % (self.Install_directory,host,dbs))
            input("\nPress Enter key to continue")
            webscan()
        elif choice == '4':
            dbs = input( " Database :")
            table = input( " Table :")
            os.system("python %s/sqlmap.py -u %s ‐D %s -T %s --columns" % (self.Install_directory,host,dbs,table))
            input("\nPress Enter key to continue")
            webscan()
        elif choice == '5':
            dbs = input( " Database :")
            table = input( " Table :")
            os.system("python %s/sqlmap.py -u %s -D %s -T %s --dump" % (self.Install_directory,host,dbs,table))
            input("\nPress Enter key to continue")
            webscan()
        elif choice == '6':
            db = input(" Input Database Type (Eg. mysql): ")
            os.system("python %s/sqlmap.py --dbms=%s -u %s --os-shell" % (self.Install_directory,db,host))
            input("\nPress Enter key to continue")
            webscan()
        elif choice == '99':
            flag = input(" All flags : ")
            os.system("python %s/sqlmap.py -u %s %s" % (self.Install_directory,host,flag))
            input("\nPress Enter key to continue")
            webscan()
        elif choice == '0':
            webscan()
        else:
            self.menu(host)

class wpscan():
    def __init__(self):
        self.Install_directory = Tool_directory + "wpscan"
        self.gitRepo = "https://github.com/wpscanteam/wpscan.git"
        if not self.installed():
            self.install()
        Sclear()
        print('''
        WPScan is a black box WordPress vulnerability scanner that can be used to scan remote WordPress installations to find security issues.
        ''')
        host = input(" Enter the target IP or URL : ")
        self.menu(host)

    def installed(self):
        return (os.path.isfile("/usr/bin/wpscan") or os.path.isfile("/usr/local/bin/wpscan"))

    def install(self):
        os.system("sudo apt install curl git libcurl4-openssl-dev make zlib1g-dev gawk g++ gcc libreadline6-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 autoconf libgdbm-dev libncurses5-dev automake libtool bison pkg-config ruby ruby-bundler ruby-dev")
        os.system("sudo gem install wpscan")

    def menu(self, host):
        Sclear()
        print(" WPScan : %s\n" % host)
        print(" 1   . Enumerate Users ")
        print(" 2   . Database")
        print(" 3   . Help ")
        print(" 99  . Manual Scan")
        print(" 0   . Back ")
        choice = input(cmd)
        if choice == '1': 
            os.system("wpscan --url %s --enumerate" % host)
            input("\nPress Enter key to continue")
            webscan()
        elif choice == '2':
            username = input(" Enter Username List Location: ")
            password = input(" Enter Password List Location: ")
            os.system("wpscan --url %s --usernames %s --passwords %s" % (host,username,password))
            input("\nPress Enter key to continue")
            webscan()
        elif choice == '3':
            os.system("wpscan --help")
            input("\nPress Enter key to continue")
            webscan()
        elif choice == '99':
            os.system("wpscan --help")
            port = input(" Enter only Flag : ")
            os.system("wpscan %s %s " % (port,host))
            input("\nPress Enter key to continue")
            webscan()
        elif choice == '0':
            webscan()
        else:
            self.menu(host)

class dirb():
    def __init__(self):
        if not self.installed():
            self.install()
        Sclear()
        print('''
        DIRB is a Web Content Scanner. It looks for existing (and/or hidden) Web Objects. It basically works by launching 
        a dictionary based attack against a web server and analyzing the response.
        ''')
        host = input("HOST: ")
        self.run(host)

    def installed(self):
        return (os.path.isfile("/usr/bin/dirb") or os.path.isfile("/usr/local/bin/dirb"))

    def install(self):
        os.system("sudo apt-get install -y dirb")

    def run(self,host):
        filetype = input("Specific FileType by -X(Eg. -X .xml for XML type): ")
        wordlist = input("Enter Wordlist Location(Default- common.txt)")
        os.system("dirb http://%s %s %s" % (host,wordlist,filetype))
        input("\nPress Enter key to continue")
        webscan()
    
class skipfish():
    def __init__(self):
        self.Install_directory = Tool_directory + "skipfish"
        if not self.installed():
            self.install()
        Sclear()
        print('''
        Skipfish is an active web application security reconnaissance tool. It prepares an interactive sitemap for the targeted 
        site by carrying out a recursive crawl and dictionary-based probes. The resulting map is then annotated with the output 
        from a number of active (but hopefully non-disruptive) security checks. The final report generated by the tool is meant 
        to serve as a foundation for professional web application security assessments.
        ''')
        host = input("HOST: ")
        self.run(host)

    def installed(self):
        return (os.path.isdir(self.Install_directory))

    def install(self):
        os.system("wget http://skipfish.googlecode.com/files/skipfish-1.01b.tgz %s")
        os.system("sudo apt-get install libidn11-dev")
        os.system("tar zxvf %s/skipfish-1.01b.tgz && cd skipfish && make && cp dictionaries/default.wl skipfish.wl" % self.Install_directory)

    def run(self,host):
        output = input("OutPut Folder Name:")
        os.system("%s/./skipfish -m 5 -LY -S /usr/share/skipfish/dictionaries/complete.wl -o ./%s -u http://%s" % (output,host))
        input("\nPress Enter key to continue")
        webscan()

class inject():
    def __init__(self):
        self.Install_directory = Tool_directory + "sqliv"
        self.gitRepo = "https://github.com/the-robot/sqliv.git"
        if not self.installed():
            self.install()
        Sclear()
        #INTROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        host = input(" Enter the target IP or URL : ")
        self.menu(host)

    def installed(self):
        return (os.path.isdir(self.Install_directory))

    def install(self):
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.Install_directory))
        os.system("sudo python2 %s/setup.py -i" % self.Install_directory)

    def menu(self, host):
        Sclear() 
        print(" SQLiv : %s\n" % host)
        print('  1   -  Multiple Domain Scanning with SQLi Dork')
        print('  2   -  Target Scanning')
        print('  3   -  Reverse Domain and Scanning')
        print('  0   -  Back to Main Menu')
        choice = input(cmd)
        if choice == '1': 
            dork = input(''' Enter the Dork (Eg. "inurl:index.php?id="): ''')
            engine = input(" Enter Seach Engine(google/bing/yahoo): ")
            os.system("python %s/sqliv.py -d %s -e  %s" % (self.Install_directory,dork,engine))
            input("\nPress Enter key to continue")
            exploit()
        elif choice == '2':
            os.system("python %s/sqliv.py -t %s " % (self.Install_directory,host))
            input("\nPress Enter key to continue")
            exploit()
        elif choice == '3':
            os.system("python %s/sqliv.py -t %s -r" % (self.Install_directory,host))
            input("\nPress Enter key to continue")
            exploit()
        elif choice == '0':
            exploit()
        else:
            self.menu(host)

class broauth():
    def __init__(self):
        Sclear()
        print(" HACKBAR : It's a sidebar that assists you with Web Application Security Testing.\n")
        print('  1   -  Firefox Add-On')
        print('  0   -  Back')
        choice = input(cmd)
        if choice == '1': 
            os.system("firefox https://addons.mozilla.org/fr/firefox/addon/hackbar-free/")
            input("\nPress Enter key to continue")
            exploit()
        elif choice == '0':
            exploit()
        else:
            self.__init__()

# # class sensdata(): 
# # class xxe():
# # class broacc():
class secmisconf():
    def __init__(self):
        self.Install_directory = Tool_directory + "watobo"
        if not self.installed():
            self.install()
        Sclear()
        self.run()
#INTROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    def installed(self):
        return (os.path.isdir(self.Install_directory))

    def install(self):
        os.system("%s/./watabo.sh" % Tool_directory)
    
    def run(self):
        os.system("watobo")
        input("\nPress Enter key to continue")
        exploit()
    
class xxs():
    def __init__(self):
        if not self.installed():
            self.install()
        Sclear()
        self.run()
#INTROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    def installed(self):
        return (os.path.isfile("/usr/bin/haproxy") or os.path.isfile("/usr/local/bin/haproxy"))

    def install(self):
        os.system("apt install haproxy")

    def run(self):
        os.system("haproxy")
        input("\nPress Enter key to continue")
        exploit()
    
# class insecdes():
class kwnvuln():
    def __init__(self):
        host = input(" Enter the library/framework/software module (Use '+' instead of Spaceing) : ")
        input("\nPress Enter key to continue")
        self.menu(host)

    def menu(self, host):
        Sclear() 
        print("  Using Components with Known Vulnerabilities : %s\n" % host)
        print('  1   -  Seach from Known Vulnerabilities - CVE,NVD,Exploit-DB ')
        print('  0   -  Back to Main Menu')
        choice = input(cmd)
        if choice == '1':
            webbrowser.open('https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=%s' % host, new = 2)
            webbrowser.open('https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query=%s&search_type=all' % host, new = 3)
            webbrowser.open('https://www.exploit-db.com/search?q=%s' % host, new = 4)
            input("\nPress Enter key to continue")
            exploit()
        elif choice == '0':
            exploit()
        else:
            self.menu(host)
    
# class lognmoni():

#Report - inject -Dumping Scanned Result - python sqliv.py -d <SQLI DORK> -e <SEARCH ENGINE> -o result.json


class brutex():
    def __init__(self):
        self.Install_directory = Tool_directory + "brutex"
        self.gitRepo = "https://github.com/1N3/BruteX.git"
        if not self.installed():
            self.install()
        Sclear()
        print('''
        Automatically brute force all services running on a target:
        * Open ports
        * Usernames
        * Passwords
        ''')
        host = input("HOST: ")
        self.run()

    def installed(self):
        return (os.path.isdir(self.Install_directory))

    def install(self):
        os.system("git clone --depth=1 %s %s" %(self.gitRepo, self.Install_directory))
        if not os.path.isdir("/usr/share/brutex"):
            os.makedirs("/usr/share/brutex")
        os.system("cd %s && chmod +x install.sh && ./install.sh" % self.Install_directory)

    def run(self):
        port = input("If any specific port (Default)")
        os.system("brutex %s %s" % (host,port))
        input("\nPress Enter key to continue")
        pwdcrack()
    
class hydra():
    def __init__(self):
        if not self.installed():
            self.install()
        Sclear()
        print('''
        Hydra is a parallelized login cracker which supports numerous protocols to attack. It is very fast and flexible, 
        and new modules are easy to add. This tool makes it possible for researchers and security consultants to show 
        how easy it would be to gain unauthorized access to a system remotely.
        ''')
        host = input(" Enter the target IP or URL : ")
        self.menu(host)

    def installed(self):
        return (os.path.isfile("/usr/bin/hydra") or os.path.isfile("/usr/local/bin/hydra"))

    def install(self):
        os.system("sudo apt-get install -y hydra")

    def menu(self, host):
        Sclear()
        print(" HYDRA : %s\n" % host)
        usr = input(" Enter Username List Location: ")
        pwd = input(" Enter Password List Location: ")
        protocol = input ("Protocol (ssh/ftp/smb/mysql/telnet/smtp/postgres) : ")
        os.system("hydra -L %s -P %s %s %s -V -f " % (usr,pwd,host,protocol))
        input("\nPress Enter key to continue")
        pwdcrack()
    
class jtr():
    def __init__(self):
        if not self.installed():
            self.install()
        Sclear()
        print('''
        John the Ripper is designed to be both feature-rich and fast. It combines several cracking modes in one program and 
        is fully configurable for your particular needs (you can even define a custom cracking mode using the built-in 
        compiler supporting a subset of C).
        ''')
        input("\nPress Enter key to continue")
        self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/john") or os.path.isfile("/usr/local/bin/john"))

    def install(self):
        os.system("sudo apt-get install john")

    def run(self):
        fileloc = input("File Location : ")
        wordlist = input(" Wordlist Location: ")
        os.system("john --wordlist=%s %s" % (wordlist,fileloc))
        input("\nPress Enter key to continue")
        pwdcrack()

class hashcat():
    def __init__(self):
        if not self.installed():
            self.install()
        Sclear()
        print('''
        Hash-Identifier - Software to identify the different types of hashes used to encrypt data and especially passwords.
        Hashcat - hashcat is the world's fastest and most advanced password recovery utility, supporting five unique modes 
                  of attack for over 300 highly-optimized hashing algorithms.
        ''')
        input("Press Enter key to continue...")
        self.run()

    def installed(self):
        return ((os.path.isfile("/usr/bin/hashcat") or os.path.isfile("/usr/local/bin/hashcat")) and 
                (os.path.isfile("/usr/bin/hash-identifier") or os.path.isfile("/usr/local/bin/hash-identifier")))

    def install(self):
        os.system("sudo apt-get install -y hashcat")
        os.system("sudo apt-get install -y hash-identifier")

    def run(self):
        fileloc = input("File Location : \n")
        os.system("hash-identifier-%s" % fileloc)
        input("\nPress Enter key to continue")
        print(" HASHCAT MODE : ")
        os.system("hashcat --help")
        print(" Find the Hash Mode")
        input("\nPress Enter key to continue")
        print(" HASHCAT : ")
        wordlist = input(" Wordlist : ")
        hashtype = input(" Hashtype : ")
        os.system("hashcat -m %s %s %s" % (hashtype,fileloc,wordlist))
        input("\nPress Enter key to continue")
        pwdcrack()

class ncrack():
    def __init__(self):
        if not self.installed():
            self.install()
        print('''
        Ncrack is a high-speed network authentication cracking tool. It was built to help companies secure their networks 
        by proactively testing all their hosts and networking devices for poor passwords. Security professionals also 
        rely on Ncrack when auditing their clients.
        ''')
        input("Press Enter key to continue...")
        self.run()

    def installed(self):
        (os.path.isfile("/usr/bin/nrack") or os.path.isfile("/usr/local/bin/nrack"))

    def install(self):
        os.system("sudo apt-get install -y nrack")

    def run(self):
        ip = input(" IP Address List Location: ")
        user = input(" User List Location: ")
        password = input(" Password List Location: ")
        protocol = input('Protocal (Eg. rdp): ')
        os.system("ncrack -v -iL %s --user %s -P %s -p %s CL=1" % (ip,user,password,protocol))
        input("\nPress Enter key to continue")
        pwdcrack()

class setoolkit:
    def __init__(self):
        self.Install_directory = Tool_directory + "setoolkit"
        self.gitRepo = "https://github.com/trustedsec/social-engineer-toolkit.git"
        if not self.installed():
            self.install()
        print('''
        The Social-Engineer Toolkit is an open-source penetration testing framework designed for social engineering. 
        SET has a number of custom attack vectors that allow you to make a believable attack quickly.
        ''')
        input("Press Enter key to continue...")
        self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/setoolkit"))

    def install(self):
        os.system("apt-get --force-yes -y install git apache2 python-requests libapache2-mod-php python-pymssql build-essential python-pexpect python-pefile python-crypto python-openssl")
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.Install_directory))
        os.system("cd %s && python setup.py install" % self.Install_directory)

    def run(self):
        Sclear()
        os.system("sudo setoolkit")
        input("\nPress Enter key to continue")
        sniffsnoof()

class macchanger:
    def __init__(self):
        self.run()
    def run(self):
        print("  Macchanger: It changes MAC Address of the network interface.\n")
        print('  1   -  Create your own mac ')
        print('  2   -  Random')
        print('  0   -  Back to Main Menu')
        choice = input(cmd)
        if choice == '1':
            device = input(' Enter network device: ')
            mac = input(' Enter MAC Address(XX:XX:XX:XX:XX:XX): ')
            os.system("sudo macchanger --mac=%s %s" % (mac,device))
            input("\nPress Enter key to continue")
            sniffsnoof()
        elif choice == '2':
            device = input(' Enter network device: ')
            os.system("sudo macchanger --random %s " % device)
            input("\nPress Enter key to continue")
            sniffsnoof()
        else:
            self.menu(host)
    
class inforeport():
    def __init__(self):
        Sclear()
        host = input(" Enter the target IP or URL : ")
        ftype = input('File Type Eg. txt, xml): .')
        ftype = "." + ftype
        reportname = input("Report Name for Information Gather:")
        filename = reportname + ftype
        rep = open(filename,"w+")
        rep.write(" Information Gathering Report of Host: %s\n" % host)
        rep.close()
        print('Enter Following for theHarvester:')
        lists = input("List Results (>1): ")
        source = input("Data Source(baidu, bing, google, google-profiles, linkedin, pgp, twitter, virustotal, netcraft, yahoo) : ")
        shodan = input("If Showan Queries (type '-h') : ")
        Sclear()
        # 1
        print('Host2IP is saving...')
        ip = socket.gethostbyname(host)
        # 2
        print('NSLookup is saving...')
        nslookup = subprocess.check_output("nslookup %s" % host, shell=True)
        # 3
        print('TheHarvester is saving...')
        theharv = subprocess.check_output("theHarvester -d %s -l %s -b %s %s " % (host,lists,source,shodan), shell=True)
        # Saving File
        print('The File is saving...')
        rep = open(filename, "a")
        rep.write("Host to IP:\n\n") 
        rep.write(str(ip))
        rep.write("\n\n\nNSlookUp:\n\n")
        rep.write(str(nslookup))
        rep.write("\n\n\ntheHarverster:\n\n")
        rep.write(str(theharv))
        rep.close()
        print('The File is Saved.')
        print("Open the Saved report using this Platform in the Reporting Menu")
        input("\nPress Enter key to continue")
        report()

class scanreport():
    def __init__(self):
        Sclear()
        host = input(" Enter the target IP or URL : ")
        ftype = input('File Type Eg. txt, xml): .')
        ftype ="." + ftype
        reportname = input("Report Name for Information Gather:")
        filename = reportname + ftype
        Sclear()
        rep = open(filename,"w+")
        rep.write(" Scanning Report of Host: %s\n" % host)
        rep.close()
        print('The File is saving...')
        netmap = subprocess.check_output("sudo nmap -T4 -A -p- %s" % host, shell=True)
        rep = open(filename, "a")
        rep.write("Nmap Report:\n\n") 
        rep.write(str(netmap))
        rep.close()
        print('The File is Saved.')
        print("Open the Saved report using this Platform in the Reporting Menu")
        input("\nPress Enter key to continue")
        report()

class metasploit():
    def __init__(self):
        if not self.installed():
            self.install()
        Sclear()
        print('''
        Metasploit is a penetration testing platform that enables you to find, exploit, and validate vulnerabilities. 
        It provides the infrastructure, content, and tools to perform penetration tests and extensive security auditing 
        and thanks to the open source community and Rapid7’s own hard working content team, new modules are added on a 
        regular basis, which means that the latest exploit is available to you as soon as it’s published.
        ''')
        input("\nPress Enter key to continue")
        self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/") or os.path.isfile("/usr/local/bin/"))

    def install(self):
        os.system("sudo apt-get install ")

    def run(self):
        Sclear()
        os.system("msfconsole")
        input("\nPress Enter key to continue")
        report()

class wireshark():
    def __init__(self):
        if not self.installed():
            self.install()
        Sclear()
        print('''
        Wireshark is the world’s foremost network protocol analyzer. It lets you see what’s happening on your network 
        at a microscopic level. It is the de facto (and often de jure) standard across many industries and educational 
        institutions. Wireshark development thrives thanks to the contributions of networking experts across the globe. 

        Instructions:
        STEP 1 : OPEN WIRESHARK                                                                                                                                                                                                                    
        STEP 2 : CHOOSE NETWORK CAPTURE INTERFACE
        •       Choose network Adapter and hit start button  
        STEP 3 : CAPTURING NETWORK TRAFFIC
        •       You will find three panes: Packet list, Packet details and Packet Bytes
        STEP 4: STOP CAPTURING AND SAVE TO A .PCAP FILE
        •       Once it is stopped, simply save to .pcap file format by hitting File > Save As > fileName.pcap.
        ''')
        input("\nPress Enter key to continue")
        self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/") or os.path.isfile("/usr/local/bin/"))

    def install(self):
        os.system("sudo apt-get install ")

    def run(self):
        Sclear()
        os.system("wireshark")
        input("\nPress Enter key to continue")
        report()

class burpsuite():
    def __init__(self):
        if not self.installed():
            self.install()
        Sclear()
        print('''
        Burp Suite is an integrated platform for performing security testing of web applications. Its various tools 
        work seamlessly together to support the entire testing process, from initial mapping and analysis of an 
        application’s attack surface, through to finding and exploiting security vulnerabilities.
        
        Instructions:
        •       After opening Burp click on Start Burp it will load and Intall extensions we go to the BApp Store from the Extender menu. Install are as following: J2EEScan, Wsdler, Java Deserialization Scannerand HeartBleed
        •       Now, we are prepare for scanning. We fire up a browser (Firefox) and go to its preferences. In the Network settings (last in the General Settings), we add our HTTP Proxy, IP and Port.
        •       Click on the Intercept is on to start intercepting the requests.
        •       Then we browse the website we need to scan. Whenever all request are captured, we can just go to Target and select our domain. To perform a scan, we can select individual requests and send them for an active scan.
        •       After sending requests on Scanner, we go to the Scanner tab and choose the Options. Here we can basically tell the scanner what actually we want to scan in our target domain.
        •       After scan started see progress in scan queue 
        ''')
        input("\nPress Enter key to continue")
        self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/") or os.path.isfile("/usr/local/bin/"))

    def install(self):
        os.system("sudo apt-get install ")

    def run(self):
        Sclear()
        os.system("burpsuite")
        input("\nPress Enter key to continue")
        report()

class maltego():
    def __init__(self):
        if not self.installed():
            self.install()
        Sclear()
        print('''
        Maltego is a unique platform developed to deliver a clear threat picture to the environment that 
        an organization owns and operates. Maltego’s unique advantage is to demonstrate the complexity and 
        severity of single points of failure as well as trust relationships that exist currently within the 
        scope of your infrastructure. 
        
        Instructions:
        •       Open Maltego & Register
        •       Choose a Machine & Parameters
            1.      Company Stalker (this gathers email information)
            2.      Footprint L1 (basic information gathering)
            3.      Footprint L2 (moderate amount of information gathering)
            4.      Footprint L3 (intense and the most complete information gathering)
        •       Choose a target For example compia.org
        •       Results : Maltego will now begin to gather info on our target domain, comptia.org, and display it on screen.
        •       Finally, we can click on "Bubble View" when Maltego is done and see all of the relationships between our target and its subdomains and linked sites.

        ''')
        input("\nPress Enter key to continue")
        self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/") or os.path.isfile("/usr/local/bin/"))

    def install(self):
        os.system("sudo apt-get install ")

    def run(self):
        Sclear()
        os.system("maltego")
        input("\nPress Enter key to continue")
        report()

class metagoofil():
    def __init__(self):
        if not self.installed():
            self.install()
        Sclear()
        print('''
        Metagoofil is an information gathering tool designed for extracting metadata of public documents (pdf,doc,xls,ppt,docx,pptx,xlsx) belonging to a target company.
        ''')
        input("\nPress Enter key to continue")
        self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/") or os.path.isfile("/usr/local/bin/"))

    def install(self):
        os.system("sudo apt-get install ")

    def run(self):
        Sclear()
        host = input(' Enter the Domain: ')
        ftype = input(' File type to download ((pdf,doc,xls,ppt,odp,ods,docx,xlsx,pptx): ')
        results = input(' Enter Limit of Results (>1): ')
        download = input(' Enter the download limit: ')
        dire = input(' Enter directory to save: ')
        f = input(' Enter the File name to be saved: ')
        os.system("metagoofil -d %s -t %s -l %s -n %s -o %s -f %s" % (host,ftype,results,download,dire,f))
        input("\nPress Enter key to continue")
        report()

def Sclear():
    os.system('clear')

if __name__ == "__main__":
    pentest()
