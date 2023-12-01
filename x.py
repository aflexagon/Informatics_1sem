import matplotlib.pyplot as plt
import openpyxl

fig = plt.figure(figsize = (10,9))
ax1 = fig.add_subplot(121)
ax2 = ax1.twinx()

A = []
A1 = []
B = []
C = []
k = 0
book = openpyxl.open("Лаб_1_1_4.xlsx")

sheet = book.active

for row in sheet.iter_rows(min_row=2, max_row=21, min_col=2, max_col=11):
    for cell in row:
        A.append(int(cell.value))


for i in range(min(A),max(A)+1):
    B.append(i)

for y in range(min(A), max(A)+1):
    for x in range(0,len(A)):
        if y == A[x]:
            k += 1
    C.append(k)
    k = 0

for i in range(0, len(A)):
    if i % 2 == 0:
        A1.append(A[i] + A[i+1])

s = sum(C)

for i in range(0,len(C)):
    C[i] = C[i]/s #посчитана доля случаев

ax1.bar(B, C, width=1, color="skyblue", edgecolor="white", linewidth=0)

plt.xlabel('n', fontsize=10, color='blue')
plt.ylabel('w', fontsize=10, color='blue')

ax2.hist(A1, bins=max(A1)-min(A1), color='darkgreen', density=True)
#plt.hist(A, bins=28, density=True)
#plt.xlim(0,50)
ax1.set_title('Гистограмма для 20 с',fontdict={'fontname': 'sans-serif', 'fontsize': 20})
ax2.set_title('Гистограмма для 40 с',fontdict={'fontname': 'sans-serif', 'fontsize': 20})

#ax1.legend()
#ax2.legend()
ax1.set_xlabel('n, число импульсов', color='blue',fontdict=None, labelpad=None, loc=None)
ax1.set_ylabel('w, доля случаев', color='blue',fontdict=None, labelpad=None, loc=None)

ax2.set_xlabel('n, число импульсов', color='blue',fontdict=None, labelpad=None, loc=None)
ax2.set_ylabel('w, доля случаев', color='blue',fontdict=None, labelpad=None, loc=None)

plt.savefig('114_test')
plt.show()