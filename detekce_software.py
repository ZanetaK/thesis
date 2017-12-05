import sys
from Registry import Registry

reg = Registry.Registry(sys.argv[1])

def dropbox_hklm():
    # SOFTWARE soubor - najdi podklíče pro Dropbox
    dropbox = "Dropobox: "
    try:
        key = reg.open("WOW6432Node\\Dropbox")
        key1 = reg.open("WOW6432Node\\Dropbox\\Client")
        key2 = reg.open("WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Dropbox")
        key3 = reg.open("WOW6432Node\\DropboxUpdate\\Update\\ClientState\\{CC46080E-4C33-4981-859A-BBA2F780F31E}")
        print()
        print(dropbox + "Detekován")
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
        for value in [v for v in key3.values() \
                      if v.value_type() == Registry.RegSZ or \
                                      v.value_type() == Registry.RegExpandSZ]:
            print("%s: %s" % (value.name(), value.value()))
    except Registry.RegistryKeyNotFoundException:
        print()
        print(dropbox + "Nenalezen")
        pass

def google_drive_hklm():
    # SOFTWARE soubor - najdi podklíče pro Google Drive
    google_drive = "Google Drive: "
    try:
        key = reg.open("WOW6432Node\\Google\\Drive")
        key1 = reg.open("WOW6432Node\\Google\\Update\\Clients\\{3C122445-AECE-4309-90B7-85A6AEF42AC0}")
        key2 = reg.open("WOW6432Node\\Google\\Update\\ClientState\\{3C122445-AECE-4309-90B7-85A6AEF42AC0}")
        print()
        print(google_drive + "Detekován")
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
        print()
        print(google_drive + "Nenalezen")
        pass

def icloud_hklm():
    # software soubor - najdi podklíče iCloudu
    iCloud = "iCloud: "
    try:
        key = reg.open("Microsoft\\Windows\\CurrentVersion\\Uninstall\\{7464D896-C63C-412E-8ED3-3261C9F14E21}")
        print()
        print(iCloud + "Detekován")
        for value in [v for v in key.values() \
                      if v.value_type() == Registry.RegSZ or \
                                      v.value_type() == Registry.RegExpandSZ]:
            print("%s: %s" % (value.name(), value.value()))
    except Registry.RegistryKeyNotFoundException:
        print()
        print(iCloud + "Nenalezen")
        pass

def owncloud_hklm():
    # software soubor - najdi podklíče pro owncloud
    owncloud = "OwnCloud: "
    try:
        key = reg.open("WOW6432Node\\ownCloud")
        key1 = reg.open("WOW6432Node\\ownCloud\\ownCloud")
        key2 = reg.open("WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\ownCloud")
        print()
        print(owncloud + "Detekován")
        for value in [v for v in key.values() \
                        if v.value_type() == Registry.RegSZ or \
                                        v.value_type() == Registry.RegExpandSZ or \
                                        v.value_type() == Registry.RegDWord]:
                print("%s: %s" % (value.name(), value.value()))
        for value in [v for v in key1.values() \
                        if v.value_type() == Registry.RegSZ or \
                                        v.value_type() == Registry.RegExpandSZ or \
                                        v.value_type() == Registry.RegDWord]:
                print("%s: %s" % (value.name(), value.value()))
        for value in [v for v in key2.values() \
                        if v.value_type() == Registry.RegSZ or \
                                        v.value_type() == Registry.RegExpandSZ or \
                                        v.value_type() == Registry.RegDWord]:
                print("%s: %s" % (value.name(), value.value()))
    except Registry.RegistryKeyNotFoundException:
        print()
        print(owncloud + "Nenalezen")


#spuštění funkcí
dropbox_hklm()
google_drive_hklm()
icloud_hklm()
owncloud_hklm()
print()
exit(print("-------------Ukončení skriptu-------------"))