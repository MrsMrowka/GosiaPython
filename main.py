print("Hello Gosia")
# TODO Lazy

print("Wybierz działanie; 1. dodawanie 2. odejmowanie 3. mnożenie 4. dzielenie 5. potęgowanie 6. pierwiastkowanie")

if int(input()) == 1:
    print("podaj pierwszą liczbę:")
    a = int(input())
    print("podaj drugą liczbę:")  # dodawanie działa, potem są błędy
    b = int(input())
    c = a + b
    print(c)

elif int(input()) == 2:
    print("podaj pierwszą liczbę:")
    a = int(input())
    print("podaj drugą liczbę:")
    b = int(input())
    c = a - b
    print(c)

elif int(input()) == 3:
    print("podaj pierwszą liczbę:")
    a = int(input())
    print("podaj drugą liczbę:")
    b = int(input())
    c = a * b
    print(c)

elif int(input()) == 4:
    print("podaj pierwszą liczbę:")
    a = int(input())
    print("podaj drugą liczbę:")
    b = int(input())
    c = a / b
    print(c)
