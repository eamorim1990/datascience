def ehPrimo(n):
    if n == 1:
        return True
    else:
        teste = True
        for i in range(2,n):
            if n % i == 0:
                teste = False
                
        return teste

if ehPrimo(int(input("Digite um número: "))):
    print("É Primo!")
else:
    print("Não é Primo!")