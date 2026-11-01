import numpy as np
import matplotlib.pyplot as plt

tInicial = 0.0
uInicial = 0
passo = 0.05

uDerivada = lambda t, u: 50 - (10 * u)
uExata = lambda t: 5 * (1 - np.exp(-10 * t)) 

tIndice = tInicial
uIndice = uInicial
maiorErro = 0.0

tValores = [tIndice]
uValores = [uIndice]

print(f"{'i':<3} | {'t':<4} | {'u (RK4)':<10} | {'u (Exato)':<10} | {'Erro'}")
print("-" * 52)

for i in range(21):
    valorExato = uExata(tIndice)
    erroAtual = abs(uIndice - valorExato)
    
    if erroAtual > maiorErro:
        maiorErro = erroAtual
        
    print(f"{i:<3} | {tIndice:<4.1f} | {uIndice:<10.6f} | {valorExato:<10.6f} | {erroAtual:.6f}")
    
    k1 = uDerivada(tIndice, uIndice)
    k2 = uDerivada(tIndice + passo/2, uIndice + k1 * passo/2)
    k3 = uDerivada(tIndice + passo/2, uIndice + k2 * passo/2)
    k4 = uDerivada(tIndice + passo, uIndice + k3 * passo)
        
    uIndice = uIndice + (passo / 6) * (k1 + 2*k2 + 2*k3 + k4)
    tIndice += passo
        
    tValores.append(tIndice)
    uValores.append(uIndice)

#print(f"\nO maior erro cometido foi: {maiorErro:.6f}")

'''
#item b
plt.plot(tValores, uValores, 'go-', label='Runge-Kutta (Estimativa)')

tLinha = np.linspace(0, 1, 100)
uLinha = uExata(tLinha)
plt.plot(tLinha, uLinha, 'b-', label='Solução Analítica (Exata)')

plt.xlabel('t')
plt.ylabel('u(t)')
plt.legend()
plt.grid(True)
plt.show()'''