from model.daftar_nilai import edit_data


def data_input():
    from model.daftar_nilai import tambah_data
    nama = input("NAMA   : ")
    nim = int(input("NIM    : "))
    tugas = int(input("TUGAS  : "))
    uts = int(input("UTS    : "))
    uas = int(input("UAS    : "))

    tambah_data(nama, nim, tugas, uts, uas)
    print("\n    (A)dd       (E)dit      (D)elete     (S)earch      (L)ist     (Q)uit   ")


def edit():
    edit_data(nama=input("Masukan nama untuk edit data : "))


def delet_input():
    from model.daftar_nilai import delet
    delet(nama=input("Masukan nama untuk menghapus data : "))


def carive():
    from model.daftar_nilai import cari
    cari(nama=input("Masukan nama yang di cari : "))

