#Deniz KALI

values = list(range(5))

for i in range(5):
    x = input("{}. Value: ".format(i + 1))

    try:
        values[i] = int(x)
    except ValueError:
        try:
            values[i] = float(x)
        except ValueError:
            values[i]= x

for i in range(5):
    print(f'{i+1}. value: {values[i]} Type: {type(values[i])}')
