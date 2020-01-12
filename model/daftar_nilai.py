daftar = {}


def tambah_data(nama,nim,tugas,uts,uas):
    akhir = round((float(tugas) * 0.3) + (float(uts) * 0.35) + (float(uas) * 0.35), 2)
    daftar[nama] = nama,nim,tugas,uts,uas,akhir


def edit_data(nama):
    if nama in daftar.keys():
        del daftar[nama]
        print("\nMasukan data baru")
        from view.input_nilai import data_input
        data_input()
    else:
        print("Data '{}' tidak ditemukan ".format(nama))

def cari(nama):
    if nama in daftar.keys():
        print("|      NAMA       |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR |")
        print("| {0:15} | {1:16} | {2:5} | {3:5} | {4:5} | {5:5} |".format(nama, daftar[nama][1], daftar[nama][2],daftar[nama][3],daftar[nama][4], daftar[nama][5]))
    else:
        print("| Data '{}' tidak ditemukan |".format(nama))


def delet(nama):
    if nama in daftar.keys():
        del daftar[nama]
        return True
    else:
        print("| Data '{}' tidak ditemukan |".format(nama))

        return False


