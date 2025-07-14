x = int(input("Digite o valor de x: "))

if x <= 12:
    print("infância")
elif x >= 13 and x <= 19:
    print("adolescência")
elif x >= 20 and x <= 59:
    print("adulto")
    if 45 < x and x <= 59:
        print("de meia idade")
elif x >= 60:
    print("idoso")
else :
    print("idade não válida")