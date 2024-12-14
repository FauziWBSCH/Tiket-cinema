list = []

def menu():
    print('\n')
    print('===== Sistem Penjualan Tiket Bioskop =====')
    print('''
1. Tampilkan Daftar Film
2. Beli Tiket
3. Total pendapatan (khusus admin, Jika ingin masuk harus menggunakan username dan password)
4. Keluar
          ''')


def daftar_film():
    print('='*40)
    print('FILM CINEMA BIOSKOP UNTUK HARI INI')
    print('='*40)
    print('''
1. AGAK LAEN                    Rp55.000
2. VENOM                        Rp60.000
3. KKN DI DESA PENARI           Rp50.000
          ''')
    input_user = input('apakah anda ingin keluar dari menu daftar film? (y/n): ')
    if input_user == 'y':
        quit
    elif input_user == 'n':
        daftar_film()
        
def film():
    print('\n')
    print('='*40)
    print('FILM CINEMA BIOSKOP UNTUK HARI INI')
    print('='*40)
    print('''
1. AGAK LAEN                    Rp55.000
2. VENOM                        Rp60.000
3. KKN DI DESA PENARI           Rp50.000
          ''')
        
def buy_ticket():
    film()
    agak_laen = 55000
    venom = 60000
    kkn = 50000
    satu = 'Agak Laen'
    dua = 'Venom'
    tiga = 'KKN Di Desa Penari'
    input_tiket = input('Film yang mana yang anda ingin tonton? (1,2,3): ')
    input_jumlah = int(input('Berapa banyak tiket yang ingin anda beli: '))
   
    if input_tiket == '1':
        total = agak_laen * input_jumlah
        list.append(total)
        print(f'\nAnda memilih film bioskop berjudul {satu}\nHarga: {agak_laen}\nJumlah Tiket: {input_jumlah} tiket\nTotal Keseluruhan: {total}\n')
    elif input_tiket == '2':
        total = venom * input_jumlah
        list.append(total)
        print(f'\nAnda memilih film bioskop berjudul {dua}\nHarga: {venom}\nJumlah Tiket: {input_jumlah} tiket\nTotal Keseluruhan: {total}\n')
    elif input_tiket == '3':
        total = kkn * input_jumlah
        list.append(total)
        print(f'\nAnda memilih film bioskop berjudul {tiga}\nHarga: {kkn}\nJumlah Tiket: {input_jumlah} tiket\nTotal Keseluruhan: {total}\n')
    else:
        print('Pilihan Error!\n')
    input_user = input('apakah anda ingin keluar dari menu pembelian tiket? (y/n): ')
    if input_user == 'y':
        quit
    elif input_user == 'n':
        buy_ticket()

def login():
    input_usn = input('\nMasukkan Username\t: ')
    input_pw = input('Masukkan Password\t: ')
    usn = 'admin'
    pw = '12345'
    if input_usn == usn and input_pw == pw:
        pendapatan()
    else:
        print('Maaf password salah, silahkan coba lagi!')
    input_user = input('\napakah anda ingin keluar dari menu total pendapatan? (y/n): ')
    if input_user == 'y':
        quit
    elif input_user == 'n':
        login()
              
def pendapatan():
    for i, total in enumerate(list, 1):
        print(f'{i}. {total}')
    jumlah = sum(list)
    print(f'jumlah keuntungan: {jumlah}')

    
    
    


while True:
    menu()
    input_user = input('Masukkan pilihan anda: ')
    
    if input_user == '1':
        daftar_film()
        
    if input_user == '2':
        buy_ticket()
        
    if input_user == '3':
        login()
        
    if input_user == '4':
        break