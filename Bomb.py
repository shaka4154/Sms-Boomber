from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
import threading

# Şifre kontrolü
def temizle():
    system("cls||clear")

temizle()
print(Fore.LIGHTBLUE_EX + "Divan'a giriş için şifre gerekli." + Style.RESET_ALL)
sifre = input(Fore.LIGHTYELLOW_EX + "Şifreyi giriniz: " + Fore.LIGHTGREEN_EX)
if sifre != "Emirhan":
    temizle()
    print(Fore.LIGHTRED_EX + "Yanlış şifre Kalfa, bacini sikim")
    sleep(3)
    exit()
temizle()
print(Fore.LIGHTGREEN_EX + "Hoşgeldiniz Burak Bey!" + Style.RESET_ALL)
sleep(2)

# Servisleri topla
servisler_sms = []
for attribute in dir(SendSms):
    if callable(getattr(SendSms, attribute)) and not attribute.startswith('__'):
        servisler_sms.append(attribute)

# Ana döngü
while True:
    temizle()
    print(f"""{Fore.LIGHTYELLOW_EX}
    𝐀𝐩𝐨𝐲𝐮𝐬𝐢𝐤𝐞𝐧
                {Style.RESET_ALL}{Fore.LIGHTBLUE_EX}Genç Kalfa - Haberci Hanesi{Style.RESET_ALL}

{Fore.LIGHTCYAN_EX}Ulaşılabilen Servis Sayısı: {len(servisler_sms)} {Style.RESET_ALL}
""")

    try:
        secim = input(
            Fore.LIGHTMAGENTA_EX +
            " [1] Mesaj Gönder (Normal Hız)\n"
            " [2] Mesaj Gönder (Tek Farlı Supra:D)\n"
            " [3] Siktirip Gidicem\n\n"
            + Fore.LIGHTYELLOW_EX + " Emir buyur Kalfa: ")
        if secim == "":
            continue
        secim = int(secim)
    except ValueError:
        temizle()
        print(Fore.LIGHTRED_EX + "Bibokuda yap aq")
        sleep(3)
        continue

    if secim == 1 or secim == 2:
        turbo_mu = secim == 2
        temizle()
        print(Fore.LIGHTYELLOW_EX + "Hangi ahaliye haber uçurulacak? (+90 yazma): " + Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        try:
            if len(tel_no) != 10 or not tel_no.isdigit():
                raise ValueError
            if tel_no == "5433457671":
                raise Exception("Yer mi lan Anadolu çocuğu")
        except ValueError:
            temizle()
            print(Fore.LIGHTRED_EX + "O bacini yerle bir ederim bu numara turk değil")
            sleep(3)
            continue
        except Exception as e:
            temizle()
            print(Fore.LIGHTRED_EX + str(e))
            sleep(3)
            continue

        temizle()
        print(Fore.LIGHTYELLOW_EX + "mail gircen mi lan: " + Fore.LIGHTGREEN_EX, end="")
        mail = input()
        if mail and ("@" not in mail or ".com" not in mail):
            temizle()
            print(Fore.LIGHTRED_EX + "Yanlis.")
            sleep(3)
            continue

        sms = SendSms(tel_no, mail)
        
        if turbo_mu:
            dur = threading.Event()

            def turbo_mesaj():
                while not dur.is_set():
                    thread_listesi = []
                    for servis in servisler_sms:
                        t = threading.Thread(target=getattr(sms, servis), daemon=True)
                        thread_listesi.append(t)
                        t.start()
                    for t in thread_listesi:
                        t.join()

            try:
                turbo_mesaj()
            except KeyboardInterrupt:
                dur.set()
                temizle()
                print("\nKalfa'nın sabrı tükendi. Divan'a dönülüyor...")
                sleep(2)
        else:
            temizle()
            try:
                print(Fore.LIGHTYELLOW_EX + "Kaç haber uçurulacak (sonsuzsa boş bırak): " + Fore.LIGHTGREEN_EX, end="")
                adet = input()
                adet = int(adet) if adet else None
            except ValueError:
                temizle()
                print(Fore.LIGHTRED_EX + "Rakam gir Kalfa...")
                sleep(3)
                continue

            temizle()
            try:
                print(Fore.LIGHTYELLOW_EX + "Kaç saniye: " + Fore.LIGHTGREEN_EX, end="")
                aralik = int(input())
            except ValueError:
                temizle()
                print(Fore.LIGHTRED_EX + "Kalfa, sayıları karıştırdın galiba.")
                sleep(3)
                continue

            if adet is None:
                while True:
                    for servis in servisler_sms:
                        getattr(sms, servis)()
                        sleep(aralik)
            else:
                while sms.adet < adet:
                    for servis in servisler_sms:
                        if sms.adet >= adet:
                            break
                        getattr(sms, servis)()
                        sleep(aralik)
            print(Fore.LIGHTCYAN_EX + "\nDivan'a dönmek için bir tuşa bas Kalfa...")
            input()

    elif secim == 3:
        temizle()
        print(Fore.LIGHTRED_EX + "Divan dağılıyor... Güle güle Kalfa!")
        break
