try:
    a= input('Masukkan nama file:')
    file = open(a, 'a')
    file.write(input('Data yang mau ditambahkan:'))
    tambah=input('Mau lagi? (y/n):')
    while tambah=='y':
        file.write(input('Data yang mau ditambahkan:'))
        tambah=input('Mau lagi? (y/n):')
        if tambah=='n':
            file.close()
        else:
            print('input hanya y/n')
            tambah=input('Mau lagi? (y/n):')

except FileNotFoundError:
    print('File tidak ditemukan')
except ValueError:
    print('Input tidak valid')
except PermissionError:
    print('Tidak diizinkan membuka direktori tersebut')
