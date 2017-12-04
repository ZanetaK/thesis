import sys
from Registry import Registry

reg = Registry.Registry(sys.argv[1])

# print all keys in the registry
def rec(key, depth=0):
     print ("\t" * depth + key.path())

     for subkey in key.subkeys():
         rec(subkey, depth + 1)
# rec(reg.root())

def amazon_drive_hkcu():
    #NTUSER.DAT soubor - najdi podklíč v Unistall
    try:
        key = reg.open("Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Amazon Drive")
        print ("Amazon Drive detekován")
    except Registry.RegistryKeyNotFoundException:
        print("Klíč Amazon Drive v Unistall nenalezen. Ukončení skriptu...")
        sys.exit(-1)
    for value in [v for v in key.values() \
              if v.value_type() == Registry.RegSZ or \
                              v.value_type() == Registry.RegExpandSZ]:
        print("%s: %s" % (value.name(), value.value()))

def dropbox_hkcu():
    # NTUSER.DAT soubor - najdi Dropbox klíče
    try:
        key = reg.open("Software\\Dropbox")
        key1 = reg.open("Software\\Dropbox\\ks")
        key2 = reg.open("Software\\Dropbox\\ks1")
        print(key, key1, key2)
    except Registry.RegistryKeyNotFoundException:
        sys.exit(1)
    for value in [v for v in key1.values() \
                  if v.value_type() == Registry.RegSZ or \
                                  v.value_type() == Registry.RegExpandSZ]:
        print("%s: %s" % (value.name(), value.value()))

def dropbox_hklm():
    # SOFTWARE soubor - najdi podklíč v Uninstall
    try:
        key = reg.open("WOW6432Node\\Dropbox")
        key1 = reg.open("WOW6432Node\\Dropbox\\Client")
        key2 = reg.open("WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Dropbox")
        key3 = reg.open("WOW6432Node\\DropboxUpdate\\Update\\ClientState\\{CC46080E-4C33-4981-859A-BBA2F780F31E}")
        print(key, key1, key2, key3)
    except Registry.RegistryKeyNotFoundException:
        print("Klíč Dropbox v Unistall nenalezen. Ukončení skriptu...")
    for value in [v for v in key2.values() \
                  if v.value_type() == Registry.RegSZ or \
                                  v.value_type() == Registry.RegExpandSZ]:
        print("%s: %s" % (value.name(), value.value()))
    for value in [v for v in key3.values() \
                  if v.value_type() == Registry.RegSZ or \
                                  v.value_type() == Registry.RegExpandSZ]:
        print("%s: %s" % (value.name(), value.value()))

def google_drive():
    # SOFTWARE soubor - najdi podklíč v Uninstall
    try:
        key = reg.open("WOW6432Node\\Google\\Drive")
        key1 = reg.open("WOW6432Node\\Google\\Update\\Clients\\{3C122445-AECE-4309-90B7-85A6AEF42AC0}")
        key2 = reg.open("WOW6432Node\\Google\\Update\\ClientState\\{3C122445-AECE-4309-90B7-85A6AEF42AC0}")
        print(key,key1,key2)
    except Registry.RegistryKeyNotFoundException:
        print("Klíče pro GoogleDrive nenalezeny. Ukončení skriptu...")
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

# check Run key in NTUSER.DAT

def google_drive_hkcu():
    # NTUSER.DAT soubor - najdi podklíč v Uninstall
    try:
        key = reg.open("Software\\Google\\Drive")
        print(key)
    except Registry.RegistryKeyNotFoundException:
        print("Klíče pro GoogleDrive nenalezeny. Ukončení skriptu...")
    for value in [v for v in key.values() \
                  if v.value_type() == Registry.RegSZ or \
                                  v.value_type() == Registry.RegExpandSZ]:
        print("%s: %s" % (value.name(), value.value()))

def icloud_hklm():
    # software soubor - najdi podklíče
    try:
        key = reg.open("Microsoft\\Windows\\CurrentVersion\\Uninstall\\{7464D896-C63C-412E-8ED3-3261C9F14E21}")
        print(key)
    except Registry.RegistryKeyNotFoundException:
        print("Klíče pro iCloud nenalezeny. Ukončení skriptu...")
    for value in [v for v in key.values() \
                  if v.value_type() == Registry.RegSZ or \
                                  v.value_type() == Registry.RegExpandSZ]:
        print("%s: %s" % (value.name(), value.value()))

def icloud_hkcu():
    # ntuser.dat soubor - najdi podklíče
    try:
        key = reg.open("Software\\Apple Inc.\\ASL\\filenames") #název posledního log souboru
        key1 = reg.open("SOFTWARE\\Apple Inc.\\Internet Services") #obsahuje email v hodnotě SignedIn
        print(key, key1)
    except Registry.RegistryKeyNotFoundException:
        print("Klíče pro iCloud nenalezeny. Ukončení skriptu...")
    for value in [v for v in key.values() \
                  if v.value_type() == Registry.RegSZ or \
                                  v.value_type() == Registry.RegExpandSZ]:
        print("%s: %s" % (value.name(), value.value()))
    for value in [v for v in key1.values() \
                  if v.value_type() == Registry.RegSZ or \
                                  v.value_type() == Registry.RegExpandSZ]:
        print("%s: %s" % (value.name(), value.value()))

def onedrive():
    # ntuser.dat soubor - najdi podklíče
    try:
        key = reg.open("Software\\Microsoft\\OneDrive")
        key1 = reg.open("Software\\Microsoft\\OneDrive\\Accounts\\Personal")
        key2 = reg.open("Software\\Microsoft\\OneDrive\\Accounts\\Personal\\ScopeIdToMountPointPathCache")
        print(key, key1, key2)
    except Registry.RegistryKeyNotFoundException:
        print("Klíče pro OneDrive nenalezeny. Ukončení skriptu...")
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

def owncloud():
    # software soubor - najdi podklíče
    try:
        key = reg.open("WOW6432Node\\ownCloud")
        key1 = reg.open("WOW6432Node\\ownCloud\\ownCloud")
        key2 = reg.open("WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\ownCloud")
        print(key, key1, key2)
    except Registry.RegistryKeyNotFoundException:
        print("Klíče pro OwnCloud nenalezeny. Ukončení skriptu...")
    for value in [v for v in key1.values() \
                    if v.value_type() == Registry.RegSZ or \
                                    v.value_type() == Registry.RegExpandSZ or \
                                    v.value_type() == Registry.RegDWord]:
            print("%s: %s" % (value.name(), value.value()))

def run_key():
    #prohledání HKCU\Software\Microsoft\Windows\CurrentVersion\Run v NTUSER.DAT
    try:
        key = reg.open("Software\Microsoft\Windows\CurrentVersion\Run")
        print(key.timestamp())
    except Registry.RegistryKeyNotFoundException:
        print("Klíč Run neobsahuje žádné hodnoty spojené s cloudovými uložišti. Ukončení skriptu...")
        sys.exit(-1)
    for value in [v for v in key.values() \
                  if v.value_type() == Registry.RegSZ or \
                                  v.value_type() == Registry.RegExpandSZ or \
                                  v.value_type() == Registry.RegDWord]:
        print("%s: %s" % (value.name(), value.value()))

dropbox_hkcu()

# def dropbox_hkcu():
#     # NTUSER.DAT soubor - najdi Dropbox klíče
#     dropbox = "Dropobox: "
#     try:
#         try:
#             key = reg.open("Software\\Dropbox")
#             print(key)
#         except Registry.RegistryKeyNotFoundException:
#             pass
#         try:
#             key1 = reg.open("Software\\Dropbox\\ks")
#             print(key1)
#         except Registry.RegistryKeyNotFoundException:
#             pass
#         try:
#             key2 = reg.open("Software\\Dropbox\\ks1")
#             print(key2)
#         except Registry.RegistryKeyNotFoundException:
#             pass
#     except Registry.RegistryKeyNotFoundException:
#         print(dropbox + "Nenalezen")
#         pass
