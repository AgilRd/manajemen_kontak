# Program Manajemen Kontak

def melihat_kontak():
    # Melihat semua kontak

    # Jika kontak bernilai True (List kontak ada isinya)
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'{num}. {item["nama"]}, {item["Hp"]}, {item["email"]}')
    else:
        print('Kontak masih kosong')
        return  1

def menambah_kontak():
    # Menambahkan kontak
    nama = input('Masukan nama kontak yang baru = ')
    hp = input('Masukan nomer hp yang baru = ')
    email = input('Masukan email yang baru = ')

    kontak_baru = {'nama': nama, 'Hp': hp, 'email': email}
    kontak.append(kontak_baru)

    print('Kontak baru telah ditambahkan')

def menghapus_kontak():
    # Menghapus kontak

    # jika kontak kosong (dalam fungsi lihat kontak), maka akan return atau keluar
    if melihat_kontak() == 1:
        return
    else:
        indeks_hapus = int(input('masukan nomer yang ingin dihapus = '))
        del kontak[indeks_hapus - 1]  # kenapa dikurangi 1, karena indeks enumerate dimulai dari 0
        print('Kontak sudah dihapus')


kontak = []

while True:
    print('\nMenu Kontak')
    print('1. Melihat Keseluruhan Kontak')
    print('2. Menambahkan Kontak Baru')
    print('3. Menghapus Kontak')
    print('4. Keluar dari Kontak')

    pilihan = input('Masukan pilihan menu (1-4) = ')

    if pilihan == '1':
       melihat_kontak()

    elif pilihan == '2':
        menambah_kontak()

    elif pilihan == '3':
        menghapus_kontak()

    elif pilihan == '4':
        # Keluar dari kontak
        break

    else:
        print('Anda memasukan pilihan yang salah')

print("Terimakasih!")