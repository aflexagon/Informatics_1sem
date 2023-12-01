import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(111)

I_measured = [62.32, 92.78, 127.64, 166.13, 170.39, 198.93, 225.22, 256.58, 299.64, 306.65,
             236.82, 230.17, 220.16, 212.33, 205.28, 197.43, 187.28, 174.92, 164.68, 155.14,
       146.81, 140.92, 133.53, 125.86, 115.56, 111.72, 103.62, 91.87, 85.83, 82.72]

V_measured = [ 130, 195, 265, 345, 355, 415, 470, 535, 625, 640,
       730, 710, 680, 655, 635, 610, 580, 540, 510, 480,
       735, 705, 670, 630, 580, 560, 520, 460, 430, 415]

n = 10

delta_v = 4.5069 #погрешность стрелочного вольтметра

for i in range (0,3):
    I1 = I_measured[n*i:n*(i+1)]
    V1 = V_measured[n*i:n*(i+1)]
    print(I1)
    print(V1)
    I = np.array(I1)
    V = np.array(V1)

    numerator = I*V
    denominator = I**2
    k = np.sum(numerator)/np.sum(denominator)

    print(f'Сопротивление <R{i}> среднее или угловой коэффициент k{i} = {np.round(k,6)}')

    s_k = np.sqrt((1/(n-1))*(np.sum(V**2)/np.sum(I**2)-k**2))
    
    print(f'Погрешность углового коэффициента s_k{i} = {np.round(s_k,6)}')
    
    delta_i = 0.002*max(I1)+2*0.01 #погрешность цифрового амперметра

    delta_rsys = k*np.sqrt((delta_v/max(V1))**2+(delta_i/max(I1))**2) 
    
    print(f'Систематическа погрешность delta_r_sys{i} = {np.round(delta_rsys,6)}')

    s_rpoln = np.sqrt(s_k**2+delta_rsys**2)

    print(f'Полная погрешность s_rpoln{i} <= {np.round(s_rpoln,6)}')
 
    if i == 0: 
        plt.axline((0,0),(1,k),label=f'l{i}',color = 'b')
    elif i == 1: 
        plt.axline((0,0),(1,k),label=f'l{i}',color = 'g')
    else:
        plt.axline((0,0),(1,k),label=f'l{i}',color = 'r')
    
    ax1.errorbar(I1, V1, yerr = delta_v, xerr = delta_i, color = 'k', linestyle = 'None')
    ax1.scatter(I1, V1, marker='x')
  
plt.xlim(0, 350)
plt.ylim(0, 800)

ax1.grid() 
plt.xlabel('I,мА')
plt.ylabel('V, мВ')

plt.title('Результаты измерений напряжений V в зависимости от тока I', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.legend()

plt.savefig('first_lab.png', dpi=300)
plt.show()
