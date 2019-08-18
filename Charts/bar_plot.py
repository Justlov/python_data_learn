#!/usr/bin/env python3
# encoding = 'utf-8'

import matplotlib.pyplot as plt
plt.style.use('ggplot')
customer = ['abc','def','ghi','jkl','mno']
customer_index = range(len(customer))
print(customer_index)
sale_amounts = [127,90,201,111,232]
flg = plt.figure()
ax1 = flg.add_subplot(1,1,1)

ax1.bar(customer_index,sale_amounts,align='center',color='darkblue')
# 设置标签位置
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xticks(customer_index,customer,rotation =0,fontsize='small')
plt.xlabel('customer Name')
plt.ylabel('sale Amount per Customer')
# plt.savefig('bar_plot.png',dpi = 400,bbox_inches='tight')
# plt.show()