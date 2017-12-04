import sys
from Registry import Registry

reg = Registry.Registry(sys.argv[1])


#Definice funkcí na prohledávání klíčů cloudových služeb

def amazon_drive_hkcu():
    #NTUSER.DAT soubor - najdi podklíč v Unistall pro Amazon Drive. Pokud existuje vypiš jeho hodnoty.
    amazon = "Amazon Drive: "
    try:
        key = reg.open("Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Amazon Drive")
        print(amazon + "Detekován")
        for value in [v for v in key.values() \
                      if v.value_type() == Registry.RegSZ or \
                                      v.value_type() == Registry.RegExpandSZ]:
            print("%s: %s" % (value.name(), value.value()))
    except Registry.RegistryKeyNotFoundException:
        print(amazon + "Nenalezen")
        pass

def dropbox_hkcu():
    # NTUSER.DAT soubor - najdi Dropbox klíče
    dropbox = "Dropobox: "
    try:
        key = reg.open("Software\\Dropbox")
        key1 = reg.open("Software\\Dropbox\\ks")
        key2 = reg.open("Software\\Dropbox\\ks1")
        print("Dropbox: " + "Detekován")
        for value in [v for v in key.values() \
                      if v.value_type() == Registry.RegSZ or \
                                      v.value_type() == Registry.RegExpandSZ]:
            print("%s: %s" % (value.name(), value.value()))
        for value in [v for v in key1.values() \
                      if v.value_type() == Registry.RegSZ or \
                                      v.value_type() == Registry.RegExpandSZ]:
            print("%s: %s" % (value.name(), value.value()))
        for value in [v for v in key2.values() \
                      if v.value_type() == Registry.RegSZ or \
                                      v.value_type() == Registry.RegExpandSZ]:
            print("%s: %s" % (value.name(), value.value()))
    except Registry.RegistryKeyNotFoundException:
        print(dropbox + "Nenalezen")
        pass

def google_drive_hkcu():
    # NTUSER.DAT soubor - najdi podklíč pro Google Drive a vypiš jeho hodnoty, pokud existuje
    google_drive = "Google Drive: "
    try:
        key = reg.open("Software\\Google\\Drive")
        print(google_drive + "Detekován")
        for value in [v for v in key.values() \
                      if v.value_type() == Registry.RegSZ or \
                                      v.value_type() == Registry.RegExpandSZ]:
            print("%s: %s" % (value.name(), value.value()))
    except Registry.RegistryKeyNotFoundException:
        print(google_drive + "Nenalezen")
        pass

def icloud_hkcu():
    # ntuser.dat soubor - najdi podklíče pro iCloud a vypiš jejich hodnoty, pokud existují
    icloud = "iCloud: "
    try:
        key = reg.open("Software\\Apple Inc.\\ASL\\filenames") #název posledního log souboru
        key1 = reg.open("SOFTWARE\\Apple Inc.\\Internet Services") #obsahuje email v hodnotě SignedIn
        print(icloud + "Detekován")
        for value in [v for v in key.values() \
                      if v.value_type() == Registry.RegSZ or \
                                      v.value_type() == Registry.RegExpandSZ]:
            print("%s: %s" % (value.name(), value.value()))
        for value in [v for v in key1.values() \
                      if v.value_type() == Registry.RegSZ or \
                                      v.value_type() == Registry.RegExpandSZ]:
            print("%s: %s" % (value.name(), value.value()))
    except Registry.RegistryKeyNotFoundException:
        print(icloud + "Nenalezen")
        pass

def onedrive_hkcu():
    # ntuser.dat soubor - najdi podklíče pro Onedrive a vypiš hodnoty pokud existují
    onedrive = "OneDrive: "
    try:
        key = reg.open("Software\\Microsoft\\OneDrive")
        key1 = reg.open("Software\\Microsoft\\OneDrive\\Accounts\\Personal")
        key2 = reg.open("Software\\Microsoft\\OneDrive\\Accounts\\Personal\\ScopeIdToMountPointPathCache")
        print(onedrive + "Detekován")
        for value in [v for v in key.values() \
                      if v.value_type() == Registry.RegSZ or \
                                      v.value_type() == Registry.RegExpandSZ or \
                                            v.value_type() == Registry.RegDWord]:
            print("%s: %s" % (value.name(), value.value()))
        for value in [v for v in key1.values() \
                      if v.value_type() == Registry.RegSZ or \
                                      v.value_type() == Registry.RegExpandSZ]:
            print("%s: %s" % (value.name(), value.value()))
        for value in [v for v in key2.values() \
                      if v.value_type() == Registry.RegSZ or \
                                      v.value_type() == Registry.RegExpandSZ]:
            print("%s: %s" % (value.name(), value.value()))
    except Registry.RegistryKeyNotFoundException:
        print(onedrive + "Nenalezeno")


#definice funkce pro hledání podklíče Run a vypsání všech hodnot

# def run_key():
#     #prohledání HKCU\Software\Microsoft\Windows\CurrentVersion\Run v NTUSER.DAT
#     #vypíše všechny hodnoty klíče
#     try:
#         key = reg.open("Software\Microsoft\Windows\CurrentVersion\Run")
#         print(key.timestamp())
#         for value in [v for v in key.values() \
#                       if v.value_type() == Registry.RegSZ or \
#                                       v.value_type() == Registry.RegExpandSZ or \
#                                       v.value_type() == Registry.RegDWord]:
#             print("%s: %s" % (value.name(), value.value()))
#     except Registry.RegistryKeyNotFoundException:
#         print("Klíč HKCU\Software\Microsoft\Windows\CurrentVersion\Run nenalezen.")
#         pass

#spuštění definovaných funkcí
amazon_drive_hkcu()
dropbox_hkcu()
google_drive_hkcu()
icloud_hkcu()
onedrive_hkcu()
exit(print("Ukončení skriptu"))
