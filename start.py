initPrm = input(
    "- For port forwarding, type 'proxy'. Examples include express.js and webmin.\n\n- For services located in the webroot, type 'webroot'.\n> ")

domainPrm = input("What's your domain name?\n> ")

portForForward = input("Please enter the port you wish to forward\n> ")

def proxyConf():
    if not "." in domainPrm:
        print("Not a valid domain.")
    f = open(f"{domainPrm}.conf", "w")
    f.write(
        f"<VirtualHost *:80>\nServerName {domainPrm}\nServerAlias www.{domainPrm}\nProxyPass / http://localhost:{portForForward}/\nProxyPassReverse / http://localhost:{portForForward}/\n</VirtualHost>")
    f.close
    print(f"Place the {domainPrm}.conf file in [apache install location]/sites-enabled/\n(Usually /etc/apache2/).")
    exit(0)


if initPrm == "proxy":
    proxyConf()
else:
    print("Not a valid option.")
    exit(0)