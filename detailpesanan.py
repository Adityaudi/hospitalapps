import data
from termcolor import colored
from utility import ColoredPrint
color = ColoredPrint()

def detailpesanan():
    # Wording Text
    txtKamar = colored("Kamar Rawat inap yang dipesan: ", 'yellow')
    TxtBiodata = colored("Biodata pasien: ", 'yellow')
    Txtpembayaraan =  colored("Detail Pembayaraan: ", 'yellow')
    # Data Pasien
    txtName = data.BiodataPasien[0]
    txtGender = data.BiodataPasien[1]
    txtTTL = data.BiodataPasien[2]
    txtHP = data.BiodataPasien[3]
    txtWorks = data.BiodataPasien[4]
    txtAge = data.BiodataPasien[5]
    txtSick = data.BiodataPasien[6]
    # Rawat Inap
    txthargainap = data.rawatinap[0]
    txtKamarinap = data.rawatinap[1]
    # TOtal
    hargainap = int(txthargainap)
    potongan = hargainap * 10 /100 
    Pakaibpjs = data.Pakaibpjs[0]
    if Pakaibpjs == True:
        NoBPJS = data.NoKartu[0]
        BPJS = data.NoKartu[1]
        payMethod = data.NoKartu[2]
        TOTAL = txthargainap - potongan
    else:
        NoBPJS = colored('-', 'yellow')
        BPJS = colored('-', 'yellow')
        payMethod = data.NoKartu[0]
        TOTAL = data.rawatinap[0]
    Status = colored('Pending', 'yellow')
    color.info("=-"*30)
    print("                  SANGKURIANG HOSPITAL")
    print ('=-'*30)
    print('\n\n')
    print(
f"""
    \U0001F9FE      DETAIL PEMESANAN KAMAR RAWAT INAP       \U0001F9FE
    {txtKamar}
        ----- {txtKamarinap} --- \n
    {TxtBiodata}
        \U0001F466 Nama Lengkap             : {txtName}
        \U0001F466 Jenis Kelamin            : {txtGender}
        \U0001F3E0 Tempat, Tanggal Lahir    : {txtTTL}
        \U0001F4DE Telepon/NoHP             : {txtHP}
        \U0001F9F3 Pekerjaan                : {txtWorks}
        \U0001F466 Umur Sekarang            : {txtAge}
        \U0001FA7A Keluhaan                 : {txtSick} \n
    {Txtpembayaraan}
        \U0001F3E6 Metode Pembayaraan       : {payMethod}
        \U0001F4B3 Biaya Rawat Inap         : Rp. {txthargainap},-
        \U0001F4B3 BPJS/KIP                 : {BPJS} 
        \U0001F4B3 NO Kartu                 : {NoBPJS} \n
                    ---------------------------------------------------------------------------
                    Total Pembayaraan       : Rp. {TOTAL},-
                    Status                  : {Status}.

"""
            )
    color.success("Pesanan kamu telah terbuat! Silahkan lakukan konfirmasi ke bagian administarasi!")
    input('Klik Enter untuk melanjutkan..')