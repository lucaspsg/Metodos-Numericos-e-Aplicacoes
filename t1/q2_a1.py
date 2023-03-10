# o problema de solução inicial vai ser y'(t) = y - e^t.sin(t) com y(t0) = 0
# para esse problema, a solução é y(t) = e^t.cos(t)
# usaremos o método de Euler para resolvê-lo
# a solução será avaliada  o intervalo de 0 a 3
# Yk+1 = Yk + Hn.r(t, y(t)) = Yk + Hn.y' = Yk + Hn.(Yk - e^Tk.sin(Tk))
import numpy as np
import math
import matplotlib.pyplot as plt
from decimal import Decimal

# função de discretização
def discretization_function(Tk, Yk):
    return Yk - math.exp(Tk) * math.sin(Tk)

# função que calcuka Yk+1
def calculate_Ykp1(Yk, Tk, Hn):
    return Yk + Hn * discretization_function(Tk, Yk)

# função que formata os números para a tabela de convergẽncia
def formatNumber(n):
    if n == "-":
        return "----------"
    return str("{:.5E}".format(Decimal(n)))

# define o intervalo de partição
function_range_0 = 0
function_range_f = 3

n = 16 # número de partições
iter_n = n # variável auxiliar de iteração para testar diferentes Ns
r = 2 # fator multiplicativo de n a cada iteração

y0 = 1 # y(0)

Tk = 0 # t = 0
Tks = np.array([Tk])
Yk = y0 # yk = y(0)
Yks = np.array([Yk])

error = 0 # erro na iteração
errors = np.array([]) # array qye guarda os erros

p = '-' # o valor inicial de p é inválido, pois são necessário 2 erros para 
        # computá-lo

index = 0 # vaŕiavel auxiliar para acessar o erros no array

print("Tabela de Convergência Numérica")

while iter_n <= 16384: # define o número de partições do intervalo em cada iteração

    Hn = (function_range_f - function_range_0) / iter_n # dt

    while Tk < function_range_f: # enquanto t estiver contido no intervalo
        Yk = calculate_Ykp1(Yk, Tk, Hn) # calcula Yk+1
        Yks = np.append(Yks, Yk)
        Tk = Tk + Hn # t = t + dt
        Tks = np.append(Tks, Tk)

    # calcula o erro e adiciona no array
    error = abs(Yk - math.exp(Tk) * math.cos(Tk))
    errors = np.append(errors, error)

    # calcula o p
    if iter_n > n:
        p = math.log(errors[index - 1]/error, r)

    # printa a tabela de convergência
    print(str(iter_n) + " & " + formatNumber(Hn) + " & " + formatNumber(error) + " & " +  formatNumber(p) + " \\\\" + "\n")

    if index < 3:
        linestyle = ''
        if index == 0:
            linestyle = 'solid'
        elif index == 1:
            linestyle = 'dashed'
        else:
            linestyle = 'dotted'
        
        plt.xlabel('t')
        plt.ylabel('y')
        plt.title('Aproximações de y(t) = e^t.cos(t)')

        plt.plot(Tks, Yks, linestyle=linestyle, color='k', label = 'n = ' + str(iter_n))

    # atualiza e reseta os valores para a nova iteração
    iter_n *= r
    Tk = 0
    Tks = 0
    Yk = y0
    Yks = [y0]
    index += 1


plt.legend(loc='best')
plt.show()




