import math

def AproximaPi(n):
    soma = 0
    for i in range(1,n):
        soma+=((-1)**(i-1))*(1/(2*i-1))
    return 4*soma

pi = AproximaPi(100)

print('Solucao Numerica: ',pi)
print('Solucao Exata: ',math.pi)

print('Erro real= ', (math.pi -pi))
print('Erron relativo real= ', abs((math.pi -pi)/math.pi))

