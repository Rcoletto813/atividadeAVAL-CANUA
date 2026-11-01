import matplotlib.pyplot as plt
import numpy as np

tInicial = 0.0
uInicial = 0
passo = 0.05
maiorErro = 0.0

tFinal = 1

uDerivada = lambda t, u: 50 - (10 * u)
uExata = lambda t: 5 * (1 - np.exp(-10 * t)) 

tIndice = tInicial
uIndice = uInicial

#cord
tValores = [tIndice] 
uValores = [uIndice]

print(f"{'i':<4} | {'ti':<5} | {'uAproximado':<12} | {'tExato':11} | {'k'}")
print("-" * 30)
for i in range( int ((tFinal / passo) + 1) ):
    k = uDerivada(tIndice, uIndice)
    valorExato = uExata(tIndice)

    erroAtual = abs(uIndice - valorExato)

    if (erroAtual > maiorErro):
        maior_erro = erroAtual

    print(f"{i:<4} | {tIndice:<5.1f} | {uIndice:<12.4f} | {valorExato:<11.4f} | {k:.4f}")
    
    uIndice = uIndice + k * passo
    tIndice += passo

    tValores.append(tIndice)
    uValores.append(uIndice)
    
print(f"O maior erro cometido foi: {maior_erro:.4f}")

'''#item b
plt.plot(tValores, uValores, 'ro-', label='Método de Euler (Estimado)')

t_linha = np.linspace(0, 1, 100) 
u_linha = uExata(t_linha)
plt.plot(t_linha, u_linha, 'b-', label='Solução Analítica (Exata)')

plt.xlabel('t')
plt.ylabel('u(t)')
plt.legend()
plt.grid(True)

plt.show()'''