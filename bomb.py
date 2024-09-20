from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
from concurrent.futures import ThreadPoolExecutor, wait

# SMS servislerinin yöntemlerini al
servisler_sms = [attr for attr in dir(SendSms) if callable(getattr(SendSms, attr)) and not attr.startswith('__')]

while True:
    system("cls||clear")
    print(f"{Fore.LIGHTGREEN_EX} Genç Kalfa SMS: {len(servisler_sms)}           by @GencKalfa\n")
    
    try:
        menu = int(input(f"{Fore.LIGHTGREEN_EX}1- SMS Gönder (Normal)\n2- SMS Gönder Turbo (Hızlı ve çok(önerilmez))\n3- Çıkış\n{Fore.LIGHTGREEN_EX}Seçimin: "))
    except ValueError:
        system("cls||clear")
        print(f"{Fore.LIGHTRED_EX}Geçersiz giriş. Lütfen tekrar deneyin.{Style.RESET_ALL}")
        sleep(3)
        continue
    
    if menu == 1:
        system("cls||clear")
        tel_no = input(f"{Fore.LIGHTGREEN_EX}Telefon numarasını başında '+90' olmadan yazınız (Birden fazla numara varsa her satıra bir numara): {Fore.LIGHTGREEN_EX}")
        tel_liste = []
        if not tel_no:
            dizin = input(f"{Fore.LIGHTGREEN_EX}Telefon numaralarının bulunduğu dosyanın dizinini giriniz: {Fore.LIGHTGREEN_EX}")
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    tel_liste = [line.strip() for line in f if len(line.strip()) == 10]
            except FileNotFoundError:
                system("cls||clear")
                print(f"{Fore.LIGHTRED_EX}Dosya bulunamadı. Lütfen geçerli bir dizin giriniz.{Style.RESET_ALL}")
                sleep(3)
                continue
        else:
            try:
                if len(tel_no) == 10 and tel_no.isdigit():
                    tel_liste.append(tel_no)
                else:
                    raise ValueError
            except ValueError:
                system("cls||clear")
                print(f"{Fore.LIGHTRED_EX}Hatalı telefon numarası. Lütfen 10 haneli bir numara giriniz.{Style.RESET_ALL}")
                sleep(3)
                continue
        
        system("cls||clear")
        mail = input(f"{Fore.LIGHTGREEN_EX}Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): {Fore.LIGHTGREEN_EX}")
        if mail and ("@" not in mail or ".com" not in mail):
            system("cls||clear")
            print(f"{Fore.LIGHTRED_EX}Geçersiz mail adresi. Lütfen doğru formatta bir mail adresi giriniz.{Style.RESET_ALL}")
            sleep(3)
            continue
        
        system("cls||clear")
        try:
            kere = input(f"{Fore.LIGHTGREEN_EX}Kaç SMS göndermek istersiniz (sonsuz ise 'enter' tuşuna basınız): {Fore.LIGHTGREEN_EX}")
            kere = None if not kere else int(kere)
        except ValueError:
            system("cls||clear")
            print(f"{Fore.LIGHTRED_EX}Geçersiz sayı. Lütfen bir sayı giriniz.{Style.RESET_ALL}")
            sleep(3)
            continue
        
        system("cls||clear")
        try:
            aralik = int(input(f"{Fore.LIGHTGREEN_EX}Gönderim aralığı (saniye): {Fore.LIGHTGREEN_EX}"))
        except ValueError:
            system("cls||clear")
            print(f"{Fore.LIGHTRED_EX}Geçersiz giriş. Lütfen bir sayı giriniz.{Style.RESET_ALL}")
            sleep(3)
            continue
        
        system("cls||clear")
        if kere is None:
            sms = SendSms(tel_no, mail)
            while True:
                for method in servisler_sms:
                    exec(f"sms.{method}()")
                    sleep(aralik)
        else:
            for numara in tel_liste:
                sms = SendSms(numara, mail)
                while sms.adet < kere:
                    for method in servisler_sms:
                        if sms.adet >= kere:
                            break
                        exec(f"sms.{method}()")
                        sleep(aralik)
        
        print(f"{Fore.LIGHTRED_EX}\nMenüye dönmek için 'enter' tuşuna basınız..{Style.RESET_ALL}")
        input()
    
    elif menu == 2:
        system("cls||clear")
        tel_no = input(f"{Fore.LIGHTGREEN_EX}Telefon numarasını başında '+90' olmadan yazınız: {Fore.LIGHTGREEN_EX}")
        if not (len(tel_no) == 10 and tel_no.isdigit()):
            system("cls||clear")
            print(f"{Fore.LIGHTRED_EX}Geçersiz telefon numarası. Lütfen 10 haneli bir numara giriniz.{Style.RESET_ALL}")
            sleep(3)
            continue
        
        system("cls||clear")
        mail = input(f"{Fore.LIGHTGREEN_EX}Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): {Fore.LIGHTGREEN_EX}")
        if mail and ("@" not in mail or ".com" not in mail):
            system("cls||clear")
            print(f"{Fore.LIGHTRED_EX}Geçersiz mail adresi. Lütfen doğru formatta bir mail adresi giriniz.{Style.RESET_ALL}")
            sleep(3)
            continue
        
        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        try:
            while True:
                with ThreadPoolExecutor() as executor:
                    futures = [executor.submit(getattr(send_sms, method)) for method in servisler_sms]
                    wait(futures)
        except KeyboardInterrupt:
            system("cls||clear")
            print("\nCtrl+C tuşuna basıldı. Menüye dönülüyor..")
            sleep(2)
    elif menu == 3:
        system("cls||clear")
        print(f"{Fore.LIGHTRED_EX}Çıkış yapılıyor...{Style.RESET_ALL}")
        break
    else:
        system("cls||clear")
        print(f"{Fore.LIGHTRED_EX}Geçersiz seçenek. Lütfen tekrar deneyiniz.{Style.RESET_ALL}")
        sleep(3)
