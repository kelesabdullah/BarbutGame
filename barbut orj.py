from random import randint as r
bakiye1,bakiye2=500,500

while bakiye1>100 and bakiye2>100:

    bahis1=int(input("1.Oyuncu; Lütfen bahis tutarınızı giriniz: "))
    bahis2=int(input("2.Oyuncu; Lütfen bahis tutarınızı giriniz: "))
    zar1=r(1,6)
    zar2=r(1,6)
    havuz=bahis2+bahis1
    kayıp1 = 3
    kayıp2 = 3
    if zar1<zar2:
        print("2.Oyuncunun zarı {}, 1.Oyuncunun zarı {}'dan büyük. Turu 2.Oyuncu kazandı...".format(zar2,zar1))
        bakiye2+=havuz
        bakiye1-=bahis1
        kayıp1-=1
        print("1.Oyuncunun Bakiyesi {}, 2.Oyuncunun bakiyesi {}. Oyun devam ediyor...".format(bakiye1,bakiye2))
    elif zar1>zar2:
        print("1.Oyuncunun zarı {}, 2.Oyuncunun zarı {}'dan büyük. Turu 1.Oyuncu kazandı...".format(zar1,zar2))
        bakiye1+=havuz
        bakiye2-=bahis2
        kayıp2-=1
        print("1.Oyuncunun Bakiyesi {}, 2.Oyuncunun bakiyesi {}. Oyun devam ediyor...".format(bakiye1, bakiye2))

    else:
        print("Zarlar eşit. Kazanan yok.")

if bakiye1<100 or bakiye2<100:
    print("Oyun sonra erdi")

else:
    pass
