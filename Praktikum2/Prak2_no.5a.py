# blok try-except
try:
    #membuka dan mau membaca file d:/data.txt
    file=open("c:/data.txt", "r")

    #baca baris pertama dari file
    # simpan ke dalam variabel bil1 sbg integrer
    bil1= int(file.readline())

    #baca baris pertama dari file
    # simpan ke dalam variabel bil2 sbg integrer
    bil2= int(file.readline())

    #hitung dan tampilkan hasil bagi
    hasil = bil1/bil2
    print(bil1, 'dibagi', bil2, 'sama dengan', hasil)
except FileNotFoundError:
    print('File tidak ditemukan')
except ZeroDivisionError:
    print('Tidak boleh pembagian dengan nol')
