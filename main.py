from view.view_nilai import cari_input,cetak_data
from view.input_nilai import data_input,edit,delet_input
print("                 PROGRAM INPUT DATA MAHASISWA ")
print("(A)dd      (E)dit     (D)elete    (S)earch     (L)ist    (Q)uit  ")
while True:

    c = input("\nPilih Opsi: ")

    if c.lower() == 'q':
            break

    elif c.lower() == 'l':
        cetak_data()

    elif c.lower() == 'a':
        data_input()

    elif c.lower() == 'e':
        edit()

    elif c.lower() == 's':
        cari_input()

    elif c.lower() == 'd':
        delet_input()

    else:
        print("Pilih opsi yang tersedia")



