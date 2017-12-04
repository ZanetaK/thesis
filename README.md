"# thesis" 
Pro detekci cloudových klientů jsou zde vytvořeny dva skripty, které se spouštění z příkazového řádku.
Skript detekce_software.py prohledává klíče registru v HKLM\SOFTWARE hive - SOFTWARE soubor.
Skript detekce_ntuser.py prohledává klíče registru v HKCU - NTUSER.DAT soubor

Použití skriptů:
  Je zapotřebí mít k dispozici vyexportované "mrtvé" registry, které chcete zkoumat.
  Skripty se spouštění z příkazové řádky:
 >> <cestaKeSkriptu>\<nazevSkriptu> <cestaKSouboruRegistru>\SouborRegistru

 příklad:
 c:\Users\Žaneta\PycharmProjects\Thesis>detekce_software.py C:\Users\Žaneta\Downloads\RegistryAll\SOFTWARE
 
 Výpis je pak vypsán do konzole.

  
