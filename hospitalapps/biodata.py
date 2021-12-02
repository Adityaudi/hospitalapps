import emoji
from utility import ColoredPrint
color = ColoredPrint()
import data

def biodata():
    
    color.info("=-"*30)
    print("                  SANGKURIANG HOSPITAL")
    print ('=-'*30)
    print("Input Biodata Pasien: \n\n")
    NamaP = input('\U0001F466 Nama Lengkap             : ')
    data.BiodataPasien.append(NamaP)
    jenisKelaminP = input('\U0001F466 Jenis Kelamin            : ')
    data.BiodataPasien.append(jenisKelaminP)
    TtlP = input('\U0001F3E0 Tempat, Tanggal Lahir    : ')
    data.BiodataPasien.append(TtlP)
    TeleponP = input('\U0001F4DE Telepon/NoHP             : ')
    data.BiodataPasien.append(TeleponP)
    PekerjaanP = input('\U0001F9F3 Pekerjaan                : ')
    data.BiodataPasien.append(PekerjaanP)
    UmurP = input('\U0001F466 Umur Sekarang            : ')
    data.BiodataPasien.append(UmurP)
    KeluhanP = input('\U0001FA7A Keluhaan                 : ')
    data.BiodataPasien.append(KeluhanP)
    print('\n\n')

    color.success("Biodata kamu berhasil di simpan!")

