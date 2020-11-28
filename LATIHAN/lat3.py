print('----------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('----------------------------')


def rata():
    p=0
    i=0
    for i in range(p):
        p+=i
        i+=1
        rataRata= p/i
    print('rata-rata=',rataRata)

try:
    
    while True:
        y=0
        n=0
        print('Masukkan bilangan bulat:', end='')
        p= int(input())
        print('Lagi (y/n)? :',end='')
        lagi= (input())
        if lagi==y:
            print('Masukkan bilangan bulat:', end='')
            p= int(input())
            print('Lagi (y/n)? :',end='')
            lagi= (input())
            if lagi==n:
                rata()
except ValueError:
    print('input tidak valid')

