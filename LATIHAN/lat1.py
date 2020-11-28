try:
    a= input('Masukkan nama file:')
    file = open(a, 'r')
    print('Isi file', a, 'adalah:')
    print(file.read())
except FileNotFoundError:
    print('File tidak ditemukan')
