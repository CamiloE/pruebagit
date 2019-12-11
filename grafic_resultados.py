# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 22:07:44 2019

@author: Camilo Farelo
"""

import numpy as np
import matplotlib.pyplot as plt
num_hor=np.array([0,1,2,3,4])
results=np.array([63,65,62,61,55])
plt.plot(num_hor,results)
plt.grid()
plt.title('Valor de beta vs Solucion',size=14)
plt.xlabel('Valor de beta',size=14)
plt.ylabel('Solución',size=14)
plt.savefig('variacion beta.png')
plt.show()