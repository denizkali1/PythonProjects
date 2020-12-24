#Deniz KALI

liste = list(range(4))
informations=["First name:","Last name:","Age:","Birth of date(year):"]


for i in range(4):
    liste[i]=input(informations[i])
for i in range(4):
    print(informations[i]+liste[i])


if int(liste[2])<18:
        print("You can't go out because it's too dangerous.")
elif int(liste[2])>=18:
        print("You can go out the street.")
