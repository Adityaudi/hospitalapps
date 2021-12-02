from utility import ColoredPrint
color = ColoredPrint()
from simple_term_menu import TerminalMenu
from termcolor import colored
import os
import emoji
import data
from paymethod import BANK_BCA, BANK_MANDIRI, BANK_BRI, BANK_JAKARTA, BANK_BANTEN, BANK_BNI
from detailpesanan import detailpesanan

global NoBPJS
MethodPayment = ["[+] BCA (Bank Central Asia)", "[+] Mandiri", 
                "[+] BRI (Bank Rakyat Indonesia)", "[+] Bank Jakarta", 
                "[+] Bank Banten", "[+] BNI (Bank Nasional Indonesia)"]
Lainnya = ["[?] Yes", "[?] No"]

def payment():
    color.info("=-"*50)
    print("                                     SANGKURIANG HOSPITAL")
    print ('=-'*50)
    print('\n\n')
    MethodPaymentchoice = TerminalMenu(MethodPayment, title="Pilih Metode Pembayaraan Anda:", menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold"))
    MethodPayment_choice_index =  MethodPaymentchoice.show()
    LainnyaPaymentchoice = TerminalMenu(Lainnya, title="Apakah anda mempunyai BPJS/KIS? ", menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold"))
    LainnyaPayment_choice_index =  LainnyaPaymentchoice.show()

#
# ------------------- BANK BCA -------------------------

    if MethodPayment_choice_index == 0:
        if LainnyaPayment_choice_index == 0: 
            NoBPJS = input('Masukan NO BPJS/KIS Anda: ')
            data.NoKartu.append(NoBPJS)
            data.NoKartu.append('Ada - pot: 10%')
            data.NoKartu.append('BANK BCA - Transfer')
            data.Pakaibpjs.append(True)
            print('\n\n')
            color.success("Pesanan kamu sudah di simpan!")
            input('Klik Enter untuk melanjutkan pembayaraan..')
            os.system("clear")
            color.info("=-"*50)
            BANK_BCA()
            ClosePaymentchoice = TerminalMenu(Lainnya, title="Print Bukti Pembayaraan? ", menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold"))
            ClosePayment_choice_index =  ClosePaymentchoice.show()
            if ClosePayment_choice_index == 0:
                detailpesanan()
                os.system('clear')
            else:
                print('\n\n\n\n\n')
                color.success("Pesanan kamu telah terbuat! Silahkan lakukan konfirmasi ke bagian administarasi!")
                input('Klik Enter untuk melanjutkan..')
                os.system("clear")
        elif LainnyaPayment_choice_index == 1:
            data.NoKartu.append('BANK BCA - Transfer')
            data.Pakaibpjs.append(False)
            print('\n\n')
            color.success("Pesanan kamu sudah di simpan!")
            input('Klik Enter untuk melanjutkan pembayaraan..')
            os.system("clear")
            color.info("=-"*50)
            BANK_BCA()
            ClosePaymentchoice = TerminalMenu(Lainnya, title="Print Bukti Pembayaraan? ", menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold"))
            ClosePayment_choice_index =  ClosePaymentchoice.show()
            if ClosePayment_choice_index == 0:
                detailpesanan()
                os.system('clear')
            elif ClosePayment_choice_index == 1:
                print('\n\n\n\n\n')
                color.success("Pesanan kamu telah terbuat! Silahkan lakukan konfirmasi ke bagian administarasi!")
                input('Klik Enter untuk melanjutkan..')
                os.system("clear")
        
#
#    ------------------ BANK MANDIRI -------------------------

    elif MethodPayment_choice_index == 1:
        if LainnyaPayment_choice_index == 0: 
            NoBPJS = input('Masukan NO BPJS/KIS Anda: ')
            data.NoKartu.append(NoBPJS)
            data.NoKartu.append('Ada - pot: 10%')
            data.NoKartu.append('BANK MANDIRI - Transfer')
            data.Pakaibpjs.append(True)
            print('\n\n')
            color.success("Pesanan kamu sudah di simpan!")
            input('Klik Enter untuk melanjutkan pembayaraan..')
            os.system("clear")
            color.info("=-"*50)
            BANK_MANDIRI()
            ClosePaymentchoice = TerminalMenu(Lainnya, title="Print Bukti Pembayaraan? ", menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold"))
            ClosePayment_choice_index =  ClosePaymentchoice.show()
            if ClosePayment_choice_index == 0:
                detailpesanan()
                os.system('clear')
            else:
                print('\n\n\n\n\n')
                color.success("Pesanan kamu telah terbuat! Silahkan lakukan konfirmasi ke bagian administarasi!")
                input('Klik Enter untuk melanjutkan..')
                os.system("clear")
        elif LainnyaPayment_choice_index == 1:
            data.NoKartu.append('BANK MANDIRI - Transfer')
            data.Pakaibpjs.append(False)
            print('\n\n')
            color.success("Pesanan kamu sudah di simpan!")
            input('Klik Enter untuk melanjutkan pembayaraan..')
            os.system("clear")
            color.info("=-"*50)
            BANK_MANDIRI()
            ClosePaymentchoice = TerminalMenu(Lainnya, title="Print Bukti Pembayaraan? ", menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold"))
            ClosePayment_choice_index =  ClosePaymentchoice.show()
            if ClosePayment_choice_index == 0:
                detailpesanan()
                os.system('clear')
            elif ClosePayment_choice_index == 1:
                print('\n\n\n\n\n')
                color.success("Pesanan kamu telah terbuat! Silahkan lakukan konfirmasi ke bagian administarasi!")
                input('Klik Enter untuk melanjutkan..')
                os.system("clear")

#     ------------------ BANK BRI -------------------------
    elif MethodPayment_choice_index == 2:
        if LainnyaPayment_choice_index == 0: 
            NoBPJS = input('Masukan NO BPJS/KIS Anda: ')
            data.NoKartu.append(NoBPJS)
            data.NoKartu.append('Ada - pot: 10%')
            data.NoKartu.append('BANK BRI - Transfer')
            data.Pakaibpjs.append(True)
            print('\n\n')
            color.success("Pesanan kamu sudah di simpan!")
            input('Klik Enter untuk melanjutkan pembayaraan..')
            os.system("clear")
            color.info("=-"*50)
            BANK_BRI()
            ClosePaymentchoice = TerminalMenu(Lainnya, title="Print Bukti Pembayaraan? ", menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold"))
            ClosePayment_choice_index =  ClosePaymentchoice.show()
            if ClosePayment_choice_index == 0:
                detailpesanan()
                os.system('clear')
            else:
                print('\n\n\n\n\n')
                color.success("Pesanan kamu telah terbuat! Silahkan lakukan konfirmasi ke bagian administarasi!")
                input('Klik Enter untuk melanjutkan..')
                os.system("clear")
        elif LainnyaPayment_choice_index == 1:
            data.NoKartu.append('BANK BRI - Transfer')
            data.Pakaibpjs.append(False)
            print('\n\n')
            color.success("Pesanan kamu sudah di simpan!")
            input('Klik Enter untuk melanjutkan pembayaraan..')
            os.system("clear")
            color.info("=-"*50)
            BANK_BRI()
            ClosePaymentchoice = TerminalMenu(Lainnya, title="Print Bukti Pembayaraan? ", menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold"))
            ClosePayment_choice_index =  ClosePaymentchoice.show()
            if ClosePayment_choice_index == 0:
                detailpesanan()
                os.system('clear')
            elif ClosePayment_choice_index == 1:
                print('\n\n\n\n\n')
                color.success("Pesanan kamu telah terbuat! Silahkan lakukan konfirmasi ke bagian administarasi!")
                input('Klik Enter untuk melanjutkan..')
                os.system("clear")

 #    ------------------ BANK JAKARTA -------------------------
    elif MethodPayment_choice_index == 3:
        if LainnyaPayment_choice_index == 0: 
            NoBPJS = input('Masukan NO BPJS/KIS Anda: ')
            data.NoKartu.append(NoBPJS)
            data.NoKartu.append('Ada - pot: 10%')
            data.NoKartu.append('BANK JAKARTA - Transfer')
            data.Pakaibpjs.append(True)
            print('\n\n')
            color.success("Pesanan kamu sudah di simpan!")
            input('Klik Enter untuk melanjutkan pembayaraan..')
            os.system("clear")
            color.info("=-"*50)
            BANK_JAKARTA()
            ClosePaymentchoice = TerminalMenu(Lainnya, title="Print Bukti Pembayaraan? ", menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold"))
            ClosePayment_choice_index =  ClosePaymentchoice.show()
            if ClosePayment_choice_index == 0:
                detailpesanan()
                os.system('clear')
            else:
                print('\n\n\n\n\n')
                color.success("Pesanan kamu telah terbuat! Silahkan lakukan konfirmasi ke bagian administarasi!")
                input('Klik Enter untuk melanjutkan..')
                os.system("clear")
        elif LainnyaPayment_choice_index == 1:
            data.NoKartu.append('BANK JAKARTA - Transfer')
            data.Pakaibpjs.append(False)
            print('\n\n')
            color.success("Pesanan kamu sudah di simpan!")
            input('Klik Enter untuk melanjutkan pembayaraan..')
            os.system("clear")
            color.info("=-"*50)
            BANK_JAKARTA()
            ClosePaymentchoice = TerminalMenu(Lainnya, title="Print Bukti Pembayaraan? ", menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold"))
            ClosePayment_choice_index =  ClosePaymentchoice.show()
            if ClosePayment_choice_index == 0:
                detailpesanan()
                os.system('clear')
            elif ClosePayment_choice_index == 1:
                print('\n\n\n\n\n')
                color.success("Pesanan kamu telah terbuat! Silahkan lakukan konfirmasi ke bagian administarasi!")
                input('Klik Enter untuk melanjutkan..')
                os.system("clear")

#    ------------------ BANK BANTEN -------------------------
    elif MethodPayment_choice_index == 4:
        if LainnyaPayment_choice_index == 0: 
            NoBPJS = input('Masukan NO BPJS/KIS Anda: ')
            data.NoKartu.append(NoBPJS)
            data.NoKartu.append('Ada - pot: 10%')
            data.NoKartu.append('BANK BANTEN - Transfer')
            data.Pakaibpjs.append(True)
            print('\n\n')
            color.success("Pesanan kamu sudah di simpan!")
            input('Klik Enter untuk melanjutkan pembayaraan..')
            os.system("clear")
            color.info("=-"*50)
            BANK_BANTEN()
            ClosePaymentchoice = TerminalMenu(Lainnya, title="Print Bukti Pembayaraan? ", menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold"))
            ClosePayment_choice_index =  ClosePaymentchoice.show()
            if ClosePayment_choice_index == 0:
                detailpesanan()
                os.system('clear')
            else:
                print('\n\n\n\n\n')
                color.success("Pesanan kamu telah terbuat! Silahkan lakukan konfirmasi ke bagian administarasi!")
                input('Klik Enter untuk melanjutkan..')
                os.system("clear")
        elif LainnyaPayment_choice_index == 1:
            data.NoKartu.append('BANK BANTEN - Transfer')
            data.Pakaibpjs.append(False)
            print('\n\n')
            color.success("Pesanan kamu sudah di simpan!")
            input('Klik Enter untuk melanjutkan pembayaraan..')
            os.system("clear")
            color.info("=-"*50)
            BANK_BANTEN()
            ClosePaymentchoice = TerminalMenu(Lainnya, title="Print Bukti Pembayaraan? ", menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold"))
            ClosePayment_choice_index =  ClosePaymentchoice.show()
            if ClosePayment_choice_index == 0:
                detailpesanan()
                os.system('clear')
            elif ClosePayment_choice_index == 1:
                print('\n\n\n\n\n')
                color.success("Pesanan kamu telah terbuat! Silahkan lakukan konfirmasi ke bagian administarasi!")
                input('Klik Enter untuk melanjutkan..')
                os.system("clear")

#     ------------------ BANK BNI -------------------------
    elif MethodPayment_choice_index == 5:    
        if LainnyaPayment_choice_index == 0: 
            NoBPJS = input('Masukan NO BPJS/KIS Anda: ')
            data.NoKartu.append(NoBPJS)
            data.NoKartu.append('Ada - pot: 10%')
            data.NoKartu.append('BANK BNI - Transfer')
            data.Pakaibpjs.append(True)
            print('\n\n')
            color.success("Pesanan kamu sudah di simpan!")
            input('Klik Enter untuk melanjutkan pembayaraan..')
            os.system("clear")
            color.info("=-"*50)
            BANK_BNI()
            ClosePaymentchoice = TerminalMenu(Lainnya, title="Print Bukti Pembayaraan? ", menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold"))
            ClosePayment_choice_index =  ClosePaymentchoice.show()
            if ClosePayment_choice_index == 0:
                detailpesanan()
                os.system('clear')
            else:
                print('\n\n\n\n\n')
                color.success("Pesanan kamu telah terbuat! Silahkan lakukan konfirmasi ke bagian administarasi!")
                input('Klik Enter untuk melanjutkan..')
                os.system("clear")
        elif LainnyaPayment_choice_index == 1:
            data.NoKartu.append('BANK BNI - Transfer')
            data.Pakaibpjs.append(False)
            print('\n\n')
            color.success("Pesanan kamu sudah di simpan!")
            input('Klik Enter untuk melanjutkan pembayaraan..')
            os.system("clear")
            color.info("=-"*50)
            BANK_BNI()
            ClosePaymentchoice = TerminalMenu(Lainnya, title="Print Bukti Pembayaraan? ", menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold"))
            ClosePayment_choice_index =  ClosePaymentchoice.show()
            if ClosePayment_choice_index == 0:
                detailpesanan()
                os.system('clear')
            elif ClosePayment_choice_index == 1:
                print('\n\n\n\n\n')
                color.success("Pesanan kamu telah terbuat! Silahkan lakukan konfirmasi ke bagian administarasi!")
                input('Klik Enter untuk melanjutkan..')
                os.system("clear")