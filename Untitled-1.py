while True :
    print("h")
    x = int (input("zadejte proměnou x: "))
    y = int (input("zadejte proměnou y: "))
    print("sčítaní +,odčítání -,dělení /,násobení *,mocnění **,odmocnění //")
    znamenko = str(input("jaký chcete operator? "))
    if znamenko == "+":
     print("sčítání")
    x = x + y
     print(x)
    elif znamenko == "-":
     print("odčítání")
    x = x - y
    print(x)
    elif znamenko == "/":
    print("dělení")
    if y == 0:
    print("nejde dělit nulou")
    else:
    x = x / y
    print(x)
    elif znamenko == "*":
    print("násobení")
    if y == 0:
    print("násobení nulou je vždy nula")
    else:
    x = x * y
    print(x)
    elif znamenko == "**":
    print("mocnění")
    if y < 0:
    print("nesmí být menší než nula")
    else:
    x = x ** y
    print(x)
    elif znamenko == "//":
    print("odmocnění")
    if y < 0:
    print("nesmí být menší než nula")
    else:
    x = x**(1/y)
    print(x)
    else:
    print("vybrali jste špatné znaménko")