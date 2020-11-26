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
    
    1. Information Gathering  

    2. Scaning 

    3. Exploitation 

    4. Post-Exploitation 

    5. Report 

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
            print('\nThanks.')
            sys.exit(0) 

class pet:
    def __init__(self):
        Sclear()
        now = datetime.datetime.now()
        nowstamp = now.strftime('%H:%M:%S %A, %d %B , %Y')
        print( startbanner + '\n\n    ' + nowstamp + '\n' )
        print( "    1. Information Gathering" )
        print( "    2. Scanning" )
        print( "    3. Exploitation" )
        print( "    4. Post Exploitation" ) 
        print( "    5. Password Cracking" )
        print( "    6. Sniffing & Spoofing" )
        print( "    7. Reporting" )
        print( "    0. Exit" )
        choice = input(cmd) 
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

class infogath():
     def __init__(self):
        Sclear()
        print(banner1)
        print('    1  -  Host to IP ')
        print('    2  -  NslookUp ')
        print('    3  -  Recong-ng ')
        print('    4  -  theHarvester ')
        print('    5  -  Discover ')
        print('    6  -  Shodan on Internet Browser ')
        print('    7  -  Censys on Internet Browser ')
        print('    0  -  Back to Main Menu')
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
        print('    1 - Network and Port Scanning')
        print('    2 - Web Scanning')
        print('    3 - Full Recon and Scan ')
        print('    0 - Back to Main Menu')
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
        print('    1 - Nmap')
        print('    2 - Hping3')
        print('    3 - MassScan')
        print('    0 - Back to Scanning Menu')
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
        print('    1 - Nikto')
        print('    2 - SQLMap')
        print('    3 - WPScan')
        print('    4 - Dirb')
        print('    5 - SkipFish')
        print('    0 - Back to Main Menu')
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
        print('    1  -  Full Recon and Scanning')
        print('    0  -  Back to Main Menu')
        choice = input(cmd)
        try:
            if choice == '1': 
                os.system("python 3klcon.py -t %s" % host)
                input("\nPress Enter key to continue")
                fulrecon()
            elif choice == '0':
                scann()
            else:
                self.menu(host)
        except KeyboardInterrupt:
            self.menu(host)
        

class exploit():
    def __init__(self):
        Sclear()
        print(banner3)
        print('    OWASP TOP 10 ')
        print('    1  -  Injection')
        print('    2  -  Broken Authentication')
        print('    3  -  Sensitive Data Exposure')
        print('    4  -  XML Enternal Entities XXE')
        print('    5  -  Broken Access Control')
        print('    6  -  Security Misconfiguration')
        print('    7  -  Cross-Site Scripting XSS')
        print('    8  -  Insecure Deserialization')
        print('    9  -  Using Components with Known Vulnerabilities')
        print('    10  - Insufficient Logging & Monitoring')
        print('    99  - Searchsploit')
        print('    0  -  Back to Main Menu')
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
        print('    1  -  BruteX')
        print('    2  -  Hydra')
        print('    3  -  JohnThRipper')
        print('    4  -  Hashcat')
        print('    5  -  Ncrack')
        print('    0  -  Back to Main Menu')
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
        print('    1  -  Setoolkit')
        print('    2  -  Macchanger')
        print('    0  -  Back to Main Menu')
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
        print( "    1. Information Gathering Report" )
        print( "    2. Scanning Report" )
        print( "    3. Metasploit")
        print( "    4. Wireshark")
        print( "    5. Burp Suite")
        print( "    6. Maltego")
        print( "    7. Metagoofil")
        print( "    99. Read Report" )
        print( "    0. Back" )
        choice = input(cmd) 
        if choice == '1':
            inforeport()
        elif choice == '2':
            scanreport()
        elif choice == '3':
            Sclear()
            print('''
            Metasploit is a penetration testing platform that enables you to find, exploit, and validate vulnerabilities. 
            It provides the infrastructure, content, and tools to perform penetration tests and extensive security auditing 
            and thanks to the open source community and Rapid7’s own hard working content team, new modules are added on a 
            regular basis, which means that the latest exploit is available to you as soon as it’s published.
            ''')
            input("\nPress Enter key to continue")
            os.system("msfconsole")
            input("\nPress Enter key to continue")
            report() 
        elif choice == '4':
            Sclear()
            print('''
            Wireshark is the world’s foremost network protocol analyzer. It lets you see what’s happening on your network 
            at a microscopic level. It is the de facto (and often de jure) standard across many industries and educational 
            institutions. Wireshark development thrives thanks to the contributions of networking experts across the globe. 
            ''')
            input("\nPress Enter key to continue")
            os.system("wireshark")
            input("\nPress Enter key to continue")
            report()
        elif choice == '5':
            Sclear()
            print('''
            Burp Suite is an integrated platform for performing security testing of web applications. Its various tools 
            work seamlessly together to support the entire testing process, from initial mapping and analysis of an 
            application’s attack surface, through to finding and exploiting security vulnerabilities.
            ''')
            input("\nPress Enter key to continue")
            os.system("burpsuite")
            input("\nPress Enter key to continue")
            report()
        elif choice == '6':
            Sclear()
            print('''
            Maltego is a unique platform developed to deliver a clear threat picture to the environment that 
            an organization owns and operates. Maltego’s unique advantage is to demonstrate the complexity and 
            severity of single points of failure as well as trust relationships that exist currently within the 
            scope of your infrastructure. 
            ''')
            input("\nPress Enter key to continue")
            os.system("maltego")
            input("\nPress Enter key to continue")
            report()
        elif choice == '7':
            Sclear()
            print('''
            Metagoofil is an information gathering tool designed for extracting metadata of public documents (pdf,doc,xls,ppt,docx,pptx,xlsx) belonging to a target company.
            ''')
            host = input(' Enter the Domain: ')
            ftype = input(' File type to download ((pdf,doc,xls,ppt,odp,ods,docx,xlsx,pptx): ')
            results = input(' Enter Limit of Results (>1): ')
            download = input(' Enter the download limit: ')
            dire = input(' Enter directory to save: ')
            f = input(' Enter the File name to be saved: ')
            os.system("metagoofil -d %s -t %s -l %s -n %s -o %s -f %s" % (host,ftype,results,download,dire,f))
            input("\nPress Enter key to continue")
            report()
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
        self.Install_directory = Tool_directory + "recon-ng"
        self.gitRepo = "https://github.com/lanmaster53/recon-ng.git"
        if not self.installed():
            self.install()      
        Sclear()
        print('''Recon-Ng - Recon-ng is a full-featured Web Reconnaissance framework written in Python. Complete with independent modules, database interaction, \nbuilt in convenience functions, interactive help, and command completion, Recon-ng provides a powerful environment in which \nopen source web-based reconnaissance can be conducted quickly and thoroughly.''')
        input("\n\nPress Enter key to continue")
        self.run()

    def installed(self):
        return (os.path.isdir(self.Install_directory))

    def install(self):
        os.system("git clone --depth=1 %s %s" %(self.gitRepo, self.Install_directory))
        os.system("cd %s && pip install -r REQUIREMENTS" % self.Install_directory)

    def run(self):   
        os.system("bash %s/recon-ng" % self.Install_directory)
        input("\n\nPress Enter key to continue")
        infogath()

class theharv():
    def __init__(self):
        self.Install_directory = Tool_directory + "theHarveaster"
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
        return ((os.path.isfile("/usr/bin/theHarvester") or os.path.isfile("/usr/local/bin/theHarvester")) or os.path.isdir(self.Install_directory))

    def install(self):
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.Install_directory))

    def run(self,host):
        lists = input("List Results (>1): ")
        source = input("Data Source(baidu, bing, google, google-profiles, linkedin, pgp, twitter, virustotal, netcraft, yahoo) : ")
        shodan = input("If Shodan Queries (type '-h') : ")
        os.system("python3 %s/theHarvester.py -d %s -l %s -b %s %s" % (self.Install_directory,host,lists,source,shodan) or "theHarvester -d %s -l %s -b %s %s" % (host,lists,source,shodan))
        input("\n\nPress Enter key to continue")
        infogath()

class discover(): 
    def __init__(self):
        self.Install_directory = toolDir + "discover"
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
        os.system("%s./update.sh" % self.Install_directory)
        
    def run(self):
        os.system("bash %s/discover.sh" % self.Install_directory)
        input("\n\nPress Enter key to continue")
        infogath()

class nmap():
    def __init__(self):
        self.Install_directory = toolDir + "nmap"
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
        print(" 1 . Simple Scan ")
        print(" 2 . Port Scan ")
        print(" 3 . Operating System Scan ")
        print(" 4 . All port Scan ")
        print(" 5 . Manual Scan")
        print(" 0 . Back on Network and Port Scanning ")
        choice = input(cmd)
        try:
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
            elif choice == '5':
                os.system("nmap --help")
                port = input(" Enter only Flag : ")
                os.system("nmap %s %s " % (port,host))
                input("\nPress Enter key to continue")
                netport()
            elif choice == '0':
                netport()
            else:
                self.menu(host)
        except KeyboardInterrupt:
            self.menu(host)

class hping3():
    def __init__(self):
        self.Install_directory = toolDir + "hping3"
        self.gitRepo = "https://github.com/HiddenShot/Hping3.git"
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
        return (os.path.isdir(self.Install_directory))

    def install(self):
        os.system("git clone --depth=1 %s %s" %(self.gitRepo, self.Install_directory))

    def menu(self, host):
        print(" HPING3 : %s\n" % host)
        print(" 1 . Scan Mode")
        print(" 2 . TraceRoute Mode ")
        print(" 3 . Verbose Scan ")
        print(" 4 . SYN FLood ")
        print(" 0 . Back on Network and Port Scanning ")
        choice = input(cmd)
        try:
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
            elif choice == '0':
                netport()
            else:
                self.menu(host)
        except KeyboardInterrupt:
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
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.Install_directory))
        os.system("cd %s && ./configure && make && make install" % self.Install_directory)
    
    def menu(self, host):
        Sclear()
        print(" MASSCAN : %s\n" % host)
        print(" 1 . Port Range ")
        print(" 2 . Selected Ports")
        print(" 3 . Exlude List Scan ")
        print(" 4 . Packet Rate Scan ")
        print(" 0 . Back ")
        choice = input(cmd)
        try:
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
            if choice == '4':
                port = input('''Enter Ports(No space just ',' in between): ''')
                rate = input('Packet rate(Default 10000): ')
                os.system("sudo masscan %s -p%s --rate %s" % (host,port,rate))
                input("\nPress Enter key to continue")
                netport()
            elif choice == '0':
                netport()
            else:
                self.menu(host)
        except KeyboardInterrupt:
            self.menu(host)

class nikto():
    def __init__(self):
        self.Install_directory = toolDir + "nikto"
        self.gitRepo = "https://github.com/sullo/nikto.git"
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
        return (os.path.isdir(self.Install_directory))

    def install(self):
        os.system("git clone --depth=1 %s %s" %(self.gitRepo, self.Install_directory))

    def menu(self, host):
        Sclear()
        print(" NIKTO : %s\n" % host)
        print(" 1 . Basic Scan ")
        print(" 2 . Port Scan ")
        print(" 3 . SSL Scan ")
        print(" 4 . No SSL Scan ")
        print(" 5 . Tuning Scan ")
        print(" 6 . Mutate Scan ")
        print(" 0 . Back ")
        choice = input(cmd)
        try:
            if choice == '1': 
                os.system("nikto -h %s" % host)
                input("\nPress Enter key to continue")
                webscan()
            elif choice == '2':
                port = input('''Enter Ports(No space just ',' in between): ''')
                os.system("nikto -h %s -port %s" % (host,port))
                input("\nPress Enter key to continue")
                webscan()
            if choice == '3':
                os.system("nikto -h %s -ssl %s" % (host,port))
                input("\nPress Enter key to continue")
                webscan()
            if choice == '4':
                os.system("nikto -h %s -nossl %s" % (host,port))
                input("\nPress Enter key to continue")
                webscan()
            if choice == '5': 
                print('''\n1   Interesting file\n2   Misconfiguration\n3   Information Disclosure\n4   Injection (XSS/Script/HTML)\n5   Remote File Retrieval – Inside Web Root\n6   Denial of Service\n7   Remote File Retrieval – Server Wide\n8   Command Execution – Remote Shell\n9   SQL Injection\n0   File Upload\na   Authentication Bypass\nb      Software Identification\nc   Remote Source Inclusion\nx   Reverse Tuning Option ''')
                tuning = input("\nTuning Option: ")
                os.system("nikto -h %s -Tuning %s" % (host,tuning))
                input("\nPress Enter key to continue")
                webscan()
            if choice == '6': 
                print('''\n1   Test all files in root directory\n2   Guess for password file names\n3   Enumerate user names via apache\n4   Enumerate user names via cgiwrap\n5   Attempt to brute force sub-domain names\n6   Attempt to guess directory names from a file''')
                mutate = input('\nMutate Option: ')
                os.system("nikto -h %s -mutate %s" % (host,mutate))
                input("\nPress Enter key to continue")
                webscan()
            elif choice == '0':
                webscan()
            else:
                self.menu(host)
        except KeyboardInterrupt:
            self.menu(host)

class sqlmap():
    def __init__(self):
        self.Install_directory = toolDir + "sqlmap"
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
        print(" 1 . Scan ")
        print(" 2 . Database")
        print(" 3 . Tables ")
        print(" 4 . Column ")
        print(" 5 . Dumps ")
        print(" 6 . OS Shells ")
        print(" 7 . Manual Scan")
        print(" 0 . Back ")
        choice = input(cmd)
        try:
            if choice == '1': 
                os.system("sqlmap -u %s" % host)
                input("\nPress Enter key to continue")
                webscan()
            elif choice == '2':
                os.system("sqlmap -u %s ‐‐dbs" % host)
                input("\nPress Enter key to continue")
                webscan()
            elif choice == '3':
                dbs = input( " Database :")
                os.system("sqlmap -u %s -D %s --table " % (host,dbs))
                input("\nPress Enter key to continue")
                webscan()
            elif choice == '4':
                dbs = input( " Database :")
                table = input( " Table :")
                os.system("sqlmap -u %s ‐D %s -T %s --columns" % (host,dbs,table))
                input("\nPress Enter key to continue")
                webscan()
            elif choice == '5':
                dbs = input( " Database :")
                table = input( " Table :")
                os.system("sqlmap -u %s -D %s -T %s --dump" % (host,dbs,table))
                input("\nPress Enter key to continue")
                webscan()
            elif choice == '6':
                db = input(" Input Database Type (Eg. mysql): ")
                os.system("sqlmap --dbms=%s -u %s --os-shell" % (db,host))
                input("\nPress Enter key to continue")
                webscan()
            elif choice == '7':
                flag = input(" All flags : ")
                os.system("sqlmap -u %s %s" % (host,flag))
                input("\nPress Enter key to continue")
                webscan()
            elif choice == '0':
                webscan()
            else:
                self.menu(host)
        except KeyboardInterrupt:
            self.menu(host)

class wpscan():
    def __init__(self):
        self.Install_directory = toolDir + "wpscan"
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
        return (os.path.isdir(self.Install_directory))

    def install(self):
        os.system("git clone --depth=1 %s %s" %(self.gitRepo, self.Install_directory))

    def menu(self, host):
        Sclear()
        print(" WPScan : %s\n" % host)
        print(" 1 . Enumerate Users ")
        print(" 2 . Database")
        print(" 3 . Help ")
        print(" 0 . Back ")
        choice = input(cmd)
        try:
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
            elif choice == '0':
                webscan()
            else:
                self.menu(host)
        except KeyboardInterrupt:
            self.menu(host)

class dirb():
    def __init__(self):
        self.Install_directory = toolDir + "dirb"
        self.gitRepo = "https://github.com/v0re/dirb.git"

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
        return (os.path.isdir(self.Install_directory))

    def install(self):
        os.system("git clone --depth=1 %s %s" %(self.gitRepo, self.Install_directory))

    def run(self,host):
        filetype = input("Specific FileType by -X(Eg. -X .xml for XML type): ")
        wordlist = input("Enter Wordlist Location(Default- common.txt)")
        os.system("dirb http://%s %s %s" % (host,wordlist,filetype))
        input("\nPress Enter key to continue")
        webscan()
    
class skipfish():
    def __init__(self):
        self.Install_directory = toolDir + "skipfish"
        self.gitRepo = "https://github.com/spinkham/skipfish.git"

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
        os.system("git clone --depth=1 %s %s" %(self.gitRepo, self.Install_directory))

    def run(self,host):
        output = input("OutPut Folder Name:")
        os.system("skipfish -m 5 -LY -S /usr/share/skipfish/dictionaries/complete.wl -o ./%s -u http://%s" % (output,host))
        input("\nPress Enter key to continue")
        webscan()

class inject():
    def __init__(self):
        self.Install_directory = toolDir + "sqliv"
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
        os.system("git clone --depth=1 %s %s" %(self.gitRepo, self.Install_directory))

    def menu(self, host):
        Sclear() 
        print(" SQLiv : %s\n" % host)
        print('  1  -  Multiple Domain Scanning with SQLi Dork')
        print('  2  -  Target Scanning')
        print('  3  -  Reverse Domain and Scanning')
        print('  0  -  Back to Main Menu')
        choice = input(cmd)
        try:
            if choice == '1': 
                dork = input(''' Enter the Dork (Eg. "inurl:index.php?id="): ''')
                engine = input(" Enter Seach Engine(google/bing/yahoo): ")
                os.system("python sqliv.py -d %s -e  %s" % (dork,engine))
                input("\nPress Enter key to continue")
                exploit()
            elif choice == '2':
                os.system("python sqliv.py -t %s " % host)
                input("\nPress Enter key to continue")
                exploit()
            elif choice == '3':
                os.system("python sqliv.py -t %s -r" % host)
                input("\nPress Enter key to continue")
                exploit()
            elif choice == '0':
                exploit()
            else:
                self.menu(host)
        except KeyboardInterrupt:
            self.menu(host)

class broauth():
    def __init__(self):
        Sclear()
        print(" HACKBAR : It's a sidebar that assists you with Web Application Security Testing.\n")
        print('  1  -  Firefox Add-On')
        print('  0  -  Back')
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
        self.Install_directory = toolDir + "watobo"
        self.gitRepo = "https://github.com/siberas/watobo.git"
        if not self.installed():
            self.install()
        Sclear()
        self.run()
# apt-get install watobo
#INTROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    def installed(self):
        return (os.path.isdir(self.Install_directory))

    def install(self):
        os.system("git clone --depth=1 %s %s"(self.gitRepo, self.Install_directory))
    
    def run(self):
        os.system("watobo")
        input("\nPress Enter key to continue")
        exploit()
    
class xxs():
    def __init__(self):
        self.Install_directory = toolDir + "zaproxy"
        self.gitRepo = "https://github.com/ParrotSec/zaproxy.git"

        if not self.installed():
            self.install()
        Sclear()
        self.run()
#INTROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    def installed(self):
        return (os.path.isdir(self.Install_directory))

    def install(self):
        os.system("git clone --depth=1 %s %s" %(self.gitRepo, self.Install_directory))

    def run(self):
        os.system("zaproxy")
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
        print('  1  -  Seach from Known Vulnerabilities - CVE,NVD,Exploit-DB ')
        print('  0  -  Back to Main Menu')
        choice = input(cmd)
        try:
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
        except KeyboardInterrupt:
            self.menu(host)

# class lognmoni():

#Report - inject -Dumping Scanned Result - python sqliv.py -d <SQLI DORK> -e <SEARCH ENGINE> -o result.json


class brutex():
    def __init__(self):
        self.Install_directory = toolDir + "brutex"
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
        self.Install_directory = toolDir + "thc-hydra"
        self.gitRepo = "https://github.com/vanhauser-thc/thc-hydra.git"

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
        return (os.path.isdir(self.Install_directory))

    def install(self):
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.Install_directory))

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
        self.Install_directory = toolDir + "john_the_ripper"
        self.gitRepo = "https://github.com/openwall/john.git"

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
        return (os.path.isdir(self.Install_directory))

    def install(self):
        os.system("git clone --depth=1 %s %s" %(self.gitRepo, self.Install_directory))

    def run(self):
        fileloc = input("File Location : ")
        wordlist = input(" Wordlist Location: ")
        os.system("john --wordlist=%s %s" % (wordlist,fileloc))
        input("\nPress Enter key to continue")
        pwdcrack()

class hashcat():
    def __init__(self):
        self.Install_directory1 = toolDir + "hashcat"
        self.gitRepo1 = "https://github.com/hashcat/hashcat.git"
        self.Install_directory2 = toolDir + "hash-identifier"
        self.gitRepo2 = "https://github.com/blackploit/hash-identifier.git"
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

    def hcinstalled(self):
        return (os.path.isdir(self.Install_directory1) and (os.path.isdir(self.Install_directory2)))

    def hcinstall(self):
        os.system("git clone --depth=1 %s %s" %(self.gitRepo1, self.Install_directory1))
        os.system("git clone --depth=1 %s %s" % (self.gitRepo2, self.Install_directory2))

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
        print('''
        Ncrack is a high-speed network authentication cracking tool. It was built to help companies secure their networks 
        by proactively testing all their hosts and networking devices for poor passwords. Security professionals also 
        rely on Ncrack when auditing their clients.
        ''')
        input("Press Enter key to continue...")
        self.run()
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
        print('''
        The Social-Engineer Toolkit is an open-source penetration testing framework designed for social engineering. 
        SET has a number of custom attack vectors that allow you to make a believable attack quickly.
        ''')
        input("Press Enter key to continue...")
        self.run()
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
        print('  1  -  Create your own mac ')
        print('  2  -  Random')
        print('  0  -  Back to Main Menu')
        choice = input(cmd)
        try:
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
        except KeyboardInterrupt:
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

def Sclear():
    os.system('clear')

if __name__ == "__main__":
    pentest()
