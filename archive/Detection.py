# importovani knihovny pro registry
from winreg import *
from termcolor import colored

ColTextNazev = colored('Název: ', 'red')
ColTextData = colored('Data: ', 'blue')

# pripojeni registru HKCR, HKCU, HKLM, HKU
RegHKCR = ConnectRegistry(None, HKEY_CLASSES_ROOT)
RegHKCU = ConnectRegistry(None, HKEY_CURRENT_USER)
RegHKLM = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
RegHKU = ConnectRegistry(None, HKEY_USERS)

RawKeyHKCU = OpenKey(RegHKCU, "Software\SyncEngines\Providers")
RawKeyHKLM = OpenKey(RegHKLM, "SOFTWARE\WOW6432Node\Apple Inc.\Apple Mobile Device Support\Shared")
print(RawKeyHKCU)


def enum_value():
    try:
        i = 0
        while 1:
            name, value, type = EnumValue(RawKeyHKCU, i)
            print(name, value, i)
            i += 1
    except WindowsError:
        print()


def enum_keys(name):
    try:
        i = 0
        while 1:
            name = EnumKey(RawKeyHKCU, i)
            return
            i += 1
    except WindowsError:
        print()


def onedrive():
    try:
        key=OpenKey(RegHKCU, "SOFTWARE\WOW6432Node\Apple Inc.\Apple Mobile Device Support\Shared")
        print("Found the key")
    except WindowsError:
        print("Couldn't find Run key. Exiting...")

onedrive()
