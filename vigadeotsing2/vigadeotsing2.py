
print("*** m�ngud ts�klid ***")
print()
while 1:
    try:
        a = (abs(int(input("Sisesta t�isarv => "))))
        break
    except ValueError:
         print("See pole t�isarv.")
         break #lisas break
if a==0:
    print("Nulliga pole m�tet midagi teha.")
else:
    print("M��rake, kui palju on paaris- ja mitu paaritut numbrit")
    print()
    c=b=a #eemaldasin =
    paaris =0 #eemaldasin =
    paaritu = 0 #eemaldasin =
    while b > 0:
        if b % 2 == 0:  #lisatud =
            paaris += 1 #vahetas kohad + ja 
        else:
            paaritu += 1 #vahetas kohad + ja
        b = b // 10
print("Numbrite arv:",paaris)
print("Paaritu arv:",paaritu)
print()
print("*P��rame* sisestatud arvu �mber")
print()
b=0
while a > 0:    #asendasin m�ned muutujad mugavuse
    l = a % 10
    a = a // 10
    b = b * 10       #jagasin arvu t�hikutega ja �hendas teises j�rjekorras
    b = b + l
print("*Muudetud* arv", b)
print()
print("Syracuse h�poteesi testimine")
print()
if c % 2 == 0:     #lisatud ==
    print("s on paarisarv. Jagage 2 -ga.")
else:
    print("s on paaritu arv. Korrutage 3 -ga, lisage 1 ja jagage 2 -ga.")
while c > 1:    #lisatud >
    if c%2:
        c = 3*c+1  #eemaldasin sulud
    c //= 2
    print(c, end=" ")
print()
print("H�potees on �ige")


