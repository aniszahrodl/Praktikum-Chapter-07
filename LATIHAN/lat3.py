print('----------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('----------------------------')

def bil():
    try:
        print('Masukkan bilangan bulat:', end='')
        global p
        p= int(input())
        List.append(p)
    except ValueError:
        print('Bukan bilangan bulat')

List=[]
bil()
lagi=input('Lagi (y/n)? :')
while lagi=='y':
    bil()
    lagi=input('Lagi (y/n)? :')
    if lagi=='n':
        sum=0
        for i in range(len(List)):
            sum+=List[i]
        rata=sum/len(List)
        print('Rata-rata:',rata)
