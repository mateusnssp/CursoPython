from configs import *

from _collections import deque  #Classe para tornar filas mais eficientes

queue = deque(["Eric", "John", "Michael"])
ss(0, type(queue), 'tipo') #{i.0.0.0} : tipo
queue.append("Terry")   # Terry chega
ss(1, queue, 'Terry chega')
queue.append("Graham")  # Graham chega
ss(2, queue, 'Graham chega')
queue.popleft()         # O primeiro a chegar agora sai
ss(3, queue, 'O primeiro a chegar agora sai')
queue.popleft()         # O segundo a chegar agora parte
ss(4, queue, 'O segundo a chegar agora parte')
ss(5, queue, 'resultado')