import numpy as np


N = 7
MTCCA = 489
MTTBR = 2

#N = 9
#MTCCA = 75
#MTTBR = 7

alpha = 1 / MTCCA
beta = 1 / MTTBR

AA = 1 - N * alpha
AB = N * alpha
BA = beta
BC = (N - 1) * alpha
BB = 1 - beta - BC
CC = 1.0

answer = [[AA, AB, 0.0], [BA, BB, BC], [0.0, 0.0, CC]]
print("Описание структуры марковской цепи:")
print(answer)

# исходная матрица вероятностных переходов P
P = np.array(answer)
# получаем матрицу надежности Q
P = np.delete(P, 2, axis=0)
P = np.delete(P, 2, axis=1)
# матрица M
P = np.identity(2) - P
# матрица N
P = np.linalg.inv(P)
# суммируем элементы первой строки матрицы N
MTTPL = np.sum(P[0])
print("Среднее время до потери пакета MTTPL при данных параметрах сети:")
print(MTTPL)

# IA = uptime / uptime + downtime
IA = MTTPL / (MTTPL + MTTBR)
print("Коэффициент доступности информации:")
print(IA)




