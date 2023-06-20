import matplotlib.pyplot as plt
from matplotlib import ticker

y = []


def function():
    y.append(1)  # y_0
    y_k_2 = 0
    y_k_1 = 1
    for i in range(20):
        y_k = -0.5 * y_k_1 - y_k_2
        y.append(y_k)
        y_k_2 = y_k_1
        y_k_1 = y_k


function()
x = [i for i in range(21)]
fig = plt.figure()
axe1 = fig.subplots()
axe1.xaxis.set_major_locator(ticker.MultipleLocator(1))
axe1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
axe1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
axe1.set_xlabel('k')
axe1.set_ylabel('y[k]')

axe1.stem(x[1:20], y[1:20])
for x, y in zip(x, y):
    plt.text(x, y + 0.3, '%.3f' % y, ha='center', va='bottom', fontsize=10.5)
axe1.grid()
axe1.legend()
plt.xlim(0, 20)
plt.show()
