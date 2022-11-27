from tabulate import tabulate

#Buat program sederhana yang akan menampilkan daftar nilai mahasiswa, dengan ketentuan sebagai berikut

# Program dibuat dengan menggunakan Dictionary
dictMahasiswa = {
    'No'    : [],
    'Nim'   : [],
    'Nama'  : [],
    'Tugas' : [],
    'Uts'   : [],
    'Uas'   : [],
    'Nilai Akhir' : [],
}
no = 0

# Tampilkan menu pilihan: (Tambah Data, Ubah Data, Hapus Data, Tampilkan Data, Cari Data)
def tambahData(no):

    nim    = int(input("Masukan Nim          : "))
    nama   = input("Masukan Nama             : ")
    tugas  = int(input("Masukan Nilai Tugas  : ")) 
    uts    = int(input("Masukan Nilai UTS    : "))
    uas    = int(input("Masukan Nilai UAS    : "))
    nilai_akhir = (tugas * 30 / 100 ) + (uts * 35 / 100 ) + (uas * 35 / 100)

    dictMahasiswa['No'].append(no)
    dictMahasiswa['Nim'].append(nim)
    dictMahasiswa['Nama'].append(nama)
    dictMahasiswa['Uts'].append(uts)
    dictMahasiswa['Tugas'].append(tugas)
    dictMahasiswa['Uas'].append(uas)
    dictMahasiswa['Nilai Akhir'].append(nilai_akhir)


def editData(nim):

    if nim in dictMahasiswa['Nim']:

        nimIndex = dictMahasiswa['Nim'].index(nim)
        print("Pilih data yang akan dirubah")

# Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%)
        while True:
            editApa = int(input(" (1) Nim, \n (2) Nama, \n (3) Nilai Tugas, \n (4) Nilai Uts, \n (5) Nilai Uas, \n (0) Simpan perubahan & Keluar \n :"))
            if editApa == 1:
                newNim = int(input("Masukan Nim : "))
                dictMahasiswa['NIM'][nimIndex] = newNim
            elif editApa==2:
                newNama=input("Masukan Nama : ")
                dictMahasiswa['Nama'][nimIndex] = newNama
            elif editApa==3:
                newTugas = int(input("Masukan Nilai Tugas : "))
                nilai_akhir=(newTugas * 30 / 100) +(dictMahasiswa['Uts'][nimIndex] * 35 / 100 ) 
                + (dictMahasiswa['Uas'][nimIndex] * 35/100 )
                dictMahasiswa['Tugas'][nimIndex]= newTugas
                dictMahasiswa ['Nilai Akhir'][nimIndex] = nilai_akhir
            elif editApa==4:
                newUts = int(input("Masukan Nilai Uts : "))
                nilai_akhir= (dictMahasiswa['Tugas'][nimIndex] * 30 / 100) + (newUts * 35/100) + (
                dictMahasiswa['Uas'][nimIndex] * 35 / 100)
                dictMahasiswa['Uts'][nimIndex] = newUts
                dictMahasiswa['Nilai Akhir'][nimIndex] = nilai_akhir
            elif editApa==5:
                newUas = int(input("Masukan Nilai Uas : "))
                nilai_akhir= (dictMahasiswa['Tugas'][nimIndex] * 30 / 100) + (dictMahasiswa['Uts'][nimIndex] * 35/100) + (
                newUas * 35 / 100)
                dictMahasiswa['Uas'][nimIndex] = newUas
                dictMahasiswa['Nilai Akhir'][nimIndex] = nilai_akhir
            elif editApa == 0:
                break
        else:
            print("Data tidak ditemukan")

def deleteData(nim):
    if nim in dictMahasiswa['Nim']:
        nimIndex = dictMahasiswa['Nim'].index(nim)

        del dictMahasiswa['No'][nimIndex]
        del dictMahasiswa['Nim'][nimIndex]
        del dictMahasiswa['Nama'][nimIndex]
        del dictMahasiswa['Tugas'][nimIndex]
        del dictMahasiswa['Uts'][nimIndex]
        del dictMahasiswa['Uas'][nimIndex]
        del dictMahasiswa['Nilai Akhir'][nimIndex]
        print("Data berhasil dihapus")
    else:
        print ("Data tidak ditemukan")

def cariData(nim):
    if nim in dictMahasiswa['Nim']:
        nimIndex = dictMahasiswa['Nim'].index(nim)

        hasilCari = {
            'No' : dictMahasiswa['No'][nimIndex],
            'Nim' : dictMahasiswa['Nim'][nimIndex],
            'Nama' : dictMahasiswa['Nama'][nimIndex],
            'Tugas' : dictMahasiswa['Tugas'][nimIndex],
            'Uts' : dictMahasiswa['Uts'][nimIndex],
            'Uas' : dictMahasiswa['Uas'][nimIndex],
            'Nilai Akhir' : dictMahasiswa['Nilai Akhir'][nimIndex],}

        print(hasilCari)
    else:
            print("Data tidak ditemukan")

# Tampilkan menu pilihan: (Tambah Data, Ubah Data, Hapus Data, Tampilkan Data, Cari Data)
while True :
    tanya = input( "(C) Menambah data, \n (R) Melihat semua data, \n (U) Update data, \n (D) Menghapus data, \n (F) Mencari data, \n (Q) Keluar Program : ")

    if tanya == "C":   
        while True:
            no += 1

            tambahData(no)
            tambahDataLagi = input("Tambah data lagi ? (y/n) :")
            if tambahDataLagi == 'n':
                break
    elif tanya == "R":
        print(tabulate(dictMahasiswa, headers= ['NO','NIM','NAMA','TUGAS','UTS','UAS','NILAI AKHIR'], tablefmt="fancy_grid"))
    elif tanya == "U":
        print(tabulate(dictMahasiswa, headers= ['NO','NIM','NAMA','TUGAS','UTS','UAS','NILAI AKHIR'], tablefmt="fancy_grid"))
        nim = int(input('Masukan nim untuk edit data :' ))
        editData(nim)
    elif tanya == "D":
        print(tabulate(dictMahasiswa, headers= ['NO','NIM','NAMA','TUGAS','UTS','UAS','NILAI AKHIR'], tablefmt="fancy_grid"))
        nim = int(input('Masukan nim yang mau dihapus :' ))
        deleteData(nim)
    elif tanya == "F":
        nim = int(input('Masukan Nim untuk mencari data: '))
        cariData(nim)
    elif tanya == "Q":
        break