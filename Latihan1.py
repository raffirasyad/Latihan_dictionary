# Buat Dictionary daftar kontak Nama sebagai key, dan nomor sebagai value
dict = {'Nama': ['Ari', 'Dina'],'Nomor Telepon':[6981267888,6987677776] }

# Tampilkan kontaknya Ari
print("Menampilkan Nomor Telepon Ari")
print(dict['Nomor Telepon'][0])
print('')

#Tambah kontak baru dengan nama Riko, nomor 087654544
print("Menambahkan data baru ")
dict['Nama'].append('Riko')
dict['Nomor Telepon'].append('087654544')
print(dict)

#Ubah kontak Dina dengan nomor baru 088999776
if 'Dina' in dict['Nama']:
    DinaIndex = dict['Nama'].index('Dina')
    dict['Nomor Telepon'][DinaIndex] = '088999776'
else:
    print("Merubah Nomor Telepon Dina")
    print(dict['Nomor Telepon'][1])
print("Merubah Nomer Telepon Dina")
print(dict)

#Tampilkan Semua Nama
print("Tampilkan Semua Nama ")
print(dict['Nama'])

# Tampilkan semua Nomor
print("Tampilkan Semua Nomor")
print(dict['Nomor Telepon'])

# Tampilkan daftar Nama dan nomornya
print("Tampilkan Daftar Nama Dan Nomor Telepon")
print(dict)


