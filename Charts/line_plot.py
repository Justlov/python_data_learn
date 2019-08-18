#!usr/bin/env python3
# encoding = 'utf-8'

from numpy.random import randn
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plot_data1  = randn(50).cumsum()
plot_data2  = randn(50).cumsum()
plot_data3  = randn(50).cumsum()
plot_data4  = randn(50).cumsum()
print(plot_data1)
print(plot_data2)
print(plot_data3)
print(plot_data4)
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(plot_data1,marker = "o",color = u'blue',linestyle = '-',label = 'Blue Solid')
ax1.plot(plot_data2,marker = "+",color = u'red',linestyle = '-',label = 'red Solid')
ax1.plot(plot_data3,marker = "*",color = 'green',linestyle = '-',label = 'green Solid')
ax1.plot(plot_data4,marker = "s",color = 'orange',linestyle = '-',label = 'orange Solid')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title('Line PLots: Maker,Color, and Linestyles')
plt.xlabel('Draw')
plt.ylabel('Randdom Number')
plt.legend(loc = 'best')
plt.savefig('line_plot.png',dpi = 400,bbox_inches='tight')
