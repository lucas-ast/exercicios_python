x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
z = int(input("Digite o valor de z: "))

if x > y and x > z and y > z:
    print(f'x é maior número, y é o segundo maior número, z é o menor número')

elif x > y and x > z and z > y:
    print(f'x é o maior número, z é o segundo maior número, y é o menor número')

elif x > y and x > z and z == y:
    print(f'x é o maior número, y e z são iguais')

elif y > x and y > z and x > z:
    print(f'y é o maior número, x é o segundo maior número, z é o menor número')

elif y > x and y > z and z > x:
    print(f'y é o maior número, z é o segundo maior número, x é o menor número')

elif y > x and y > z and x == z:
    print(f'y é o maior número, x e z são iguais')

elif z > x and z > y and x > y:
    print(f'z é o maior número, x é o segundo maior número, y é o menor número')

elif z > x and z > y and y > x:
    print(f'z é o maior número, y é o segundo maior número, x é o menor número')    

elif z > x and z > y and x == y:
    print(f'z é o maior número, x e y são iguais')
else : 
    print(f'x; y; z são iguais')