# Module Required
import emoji
import os
from utility import ColoredPrint
color = ColoredPrint()
from simple_term_menu import TerminalMenu

# Module Aplikasi
from rooms import inap_president, inap_VIP_A, inap_VIP_B, inap_VIP_C, inap_VIP_Lily, inap_VVIP_A, inap_VVIP_B, inap_KELAS_A, inap_KELAS_B, inap_KELAS_C
from biodata import biodata
from payment import payment
import data

def rooms():
    color.info("=-"*30)
    print("                  SANGKURIANG HOSPITAL")
    print ('=-'*30)
    Rooms = ["[1] President Suite", "[2] Kamar Inap VVIP A", "[3] Kamar Inap VVIP B", "[4] Kamar Inap VIP Lily", 
        "[5] Kamar Inap VIP A", "[6] Kamar Inap VIP B", "[7] Kamar Inap VIP C", 
        "[8] Kamar Inap Kelas A", "[9] Kamar Inap Kelas B", "[~] Kamar Inap Kelas C"]
    Confirm = ["[?] Kembali", "[?] Pesan Sekarang"]
    Next = ["[!] Lanjutkan >"]
    MethodPayment = ["[+] BCA (Bank Central Asia)", "[+] Mandiri", 
                    "[+] BRI (Bank Central Indonesia)", "[+] Bank Jakarta", 
                    "[+] Bank Banten", "[+] BNI (Bank Nasional Indonesia)"]
    roomschoice = TerminalMenu(Rooms, title="Tipe Kamar Rawat Inap:", 
                                        menu_cursor_style=("fg_yellow", "bold"),
                                        shortcut_key_highlight_style=("fg_yellow", "bold"))
    rooms_choice_index = roomschoice.show()
    if rooms_choice_index == 0:
        inap_president(3800000  , 30, 'link photo')
        confirmchoice = TerminalMenu(Confirm, menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold", "bold"))
        confirm_choice_index = confirmchoice.show()
        if confirm_choice_index == 1:
            os.system("clear")
            biodata()
            data.rawatinap.append('Rawat Inap President Suite')
            input('Klik Enter untuk melanjutkan..')
            os.system("clear")
            payment()
            os.system("clear")  
        elif confirm_choice_index == 0:
            os.system("clear")
    elif rooms_choice_index == 1:
        inap_VVIP_A(1500000, 20, 'link photo')
        confirmchoice = TerminalMenu(Confirm, menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold", "bold"))
        confirm_choice_index = confirmchoice.show()
        if confirm_choice_index == 1:
            os.system("clear")
            biodata()
            data.rawatinap.append('Rawat Inap VVIP A')
            input('Klik Enter untuk melanjutkan..')
            os.system("clear")
            payment()
            os.system("clear")  
        elif confirm_choice_index == 0:
            os.system("clear")
    elif rooms_choice_index == 2:
        inap_VVIP_B(1100000, 10, 'link photo')
        confirmchoice = TerminalMenu(Confirm, menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold", "bold"))
        confirm_choice_index = confirmchoice.show()
        if confirm_choice_index == 1:
            os.system("clear")
            biodata()
            data.rawatinap.append('Rawat Inap VVIP B')
            input('Klik Enter untuk melanjutkan..')
            os.system("clear")
            payment()
            os.system("clear")  
        elif confirm_choice_index == 0:
            os.system("clear")
    elif rooms_choice_index == 3:
        inap_VIP_Lily(1000000, 20, 'link photo')
        confirmchoice = TerminalMenu(Confirm, menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold", "bold"))
        confirm_choice_index = confirmchoice.show()
        if confirm_choice_index == 1:
            os.system("clear")
            biodata()
            data.rawatinap.append('Rawat Inap VVIP Lily')
            input('Klik Enter untuk melanjutkan..')
            os.system("clear")
            payment()
            os.system("clear")  
        elif confirm_choice_index == 0:
            os.system("clear")
    elif rooms_choice_index == 4:
        inap_VIP_A(1000000, 15, 'link photo')
        confirmchoice = TerminalMenu(Confirm, menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold", "bold"))
        confirm_choice_index = confirmchoice.show()
        if confirm_choice_index == 1:
            os.system("clear")
            biodata()
            data.rawatinap.append('Rawat Inap VIP A')
            input('Klik Enter untuk melanjutkan..')
            os.system("clear")
            payment()
            os.system("clear")  
        elif confirm_choice_index == 0:
            os.system("clear")
    elif rooms_choice_index == 5:
        inap_VIP_B(750000, 12, 'link photo')
        confirmchoice = TerminalMenu(Confirm, menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold", "bold"))
        confirm_choice_index = confirmchoice.show()
        if confirm_choice_index == 1:
            os.system("clear")
            biodata()
            data.rawatinap.append('Rawat Inap VIP B')
            input('Klik Enter untuk melanjutkan..')
            os.system("clear")
            payment()
            os.system("clear")  
        elif confirm_choice_index == 0:
            os.system("clear")
    elif rooms_choice_index == 6:
        inap_KELAS_C(600000, 25, 'link photo')
        confirmchoice = TerminalMenu(Confirm, menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold", "bold"))
        confirm_choice_index = confirmchoice.show()
        if confirm_choice_index == 1:
            os.system("clear")
            biodata()
            data.rawatinap.append('Rawat Inap VIP C')
            input('Klik Enter untuk melanjutkan..')
            os.system("clear")
            payment()
            os.system("clear")  
        elif confirm_choice_index == 0:
            os.system("clear")
    elif rooms_choice_index == 7:
        inap_KELAS_A(250000, 15, 'link photo')
        confirmchoice = TerminalMenu(Confirm, menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold", "bold"))
        confirm_choice_index = confirmchoice.show()
        if confirm_choice_index == 1:
            os.system("clear")
            biodata()
            data.rawatinap.append('Rawat Inap KELAS C - Room Carmelia')
            input('Klik Enter untuk melanjutkan..')
            os.system("clear")
            payment()
            os.system("clear")  
        elif confirm_choice_index == 0:
            os.system("clear")
    elif rooms_choice_index == 8:
        inap_KELAS_B(130000, 11, 'link photo')
        confirmchoice = TerminalMenu(Confirm, menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold", "bold"))
        confirm_choice_index = confirmchoice.show()
        if confirm_choice_index == 1:
            os.system("clear")
            biodata()
            data.rawatinap.append('Rawat Inap KELAS B - Rooms Bougenfille')
            input('Klik Enter untuk melanjutkan..')
            os.system("clear")
            payment()
            os.system("clear")  
        elif confirm_choice_index == 0:
            os.system("clear")
    elif rooms_choice_index == 9:
        inap_KELAS_C(75000, 5, 'link photo')
        confirmchoice = TerminalMenu(Confirm, menu_cursor_style=("fg_yellow", "bold"), shortcut_key_highlight_style=("fg_yellow", "bold", "bold"))
        confirm_choice_index = confirmchoice.show()
        if confirm_choice_index == 1:
            os.system("clear")
            biodata()
            data.rawatinap.append('Rawat Inap KELAS C - Rooms Gardenia')
            input('Klik Enter untuk melanjutkan..')
            os.system("clear")
            payment()
            os.system("clear")  
        elif confirm_choice_index == 0:
            os.system("clear")

if __name__ == "__main__":
        print ("Selamat datang di Rumah Sakit Sejahtera\U0001F44B")
        while True:
            rooms()