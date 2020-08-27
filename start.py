import os


initPrm = input("- For port forwarding, type 'proxy'. Examples include express.js and webmin.\n\n- For services located in the webroot, type 'webroot'.\n> ")

APACHE_LOG_DIR = "{APACHE_LOG_DIR}"

def proxyConf():
    if not "." in domainPrm:
        print("Not a valid domain.")
    f = open(f"{domainPrm}.conf", "w")
    f.write(f"<VirtualHost *:80>\nServerName {domainPrm}\nServerAlias www.{domainPrm}\nProxyPass / http://localhost:{portForForward}/\nProxyPassReverse / http://localhost:{portForForward}/\n</VirtualHost>")
    f.close
    os.system(f'cp {domainPrm}.conf {apcPa}/sites-enabled/{domainPrm}.conf')
    exit(0)

def regConf():
    if not "." in domainPrm:
        print("Not a valid domain.")
    f = open(f"{domainPrm}.conf", "w")
    portForForward = None
    f.write(f"<VirtualHost *:80>\nServerName {domainPrm}\nServerAlias www.{domainPrm}\nDocumentRoot {webLoc}\nErrorLog ${APACHE_LOG_DIR}/error.log\nCustomLog ${APACHE_LOG_DIR}/access.log combined\n</VirtualHost>")
    f.close
    os.system(f'cp {domainPrm}.conf {apcPa}/sites-enabled/{domainPrm}.conf')
    exit(0)

if initPrm == "proxy":
    domainPrm = input("What's your domain name?\n> ")
    portForForward = input("Please enter the port you wish to forward\n> ")
    apcPa = input("Where is your Apache installation located? e.g. '/etc/apache2/'\n> ")
    proxyConf()
elif initPrm == "webroot":
    domainPrm = input("What's your domain name?\n> ")
    webLoc = input("What is the absolute path of the files for your website?\n> ")
    apcPa = input("Where is your Apache installation located? e.g. '/etc/apache2/'\n> ")
    regConf()
else:
    print("Not a valid option.")
    exit(0)