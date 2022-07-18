import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 修改字体  windows/linxu设置的方法
# font = {'family' : 'MicroSoft YaHei',
#         'weight' : 'bold',
#         'size'   : 'larger'}
# matplotlib.rc("font", **font)

my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

# figure 图形图标的意思，在这里值的就是我们画的图
# 通过实例化一个figure并且传递参数，能够在后台自动使用该figure实例
# 在图像模糊的时候可以传入dpi参数，让图片更加清晰 
# dpi值得是没英寸上点的个数 dot per inch
fig = plt.figure(figsize=(20, 8), dpi = 80)
x = range(2, 26, 2)
y = [5, 13, 14.5, 17, 20, 25, 26, 24, 22, 18, 15, 17]

# 绘图
plt.plot(x, y)

# _xtick_labels = [i/2 for i in range(2, 49)]
# plt.xticks(_xtick_labels)

_x = x
_xtick_labels = ["10点{}分".format(i) for i in _x]
plt.xticks(x, _xtick_labels, rotation=90, fontproperties=my_font)

plt.yticks(range(min(y), max(y)+1))

# 保存图片， 保存应该在绘图之后, 也可以保存为svg这种矢量图格式，放大不会有锯齿
# plt.savefig('./2demo.png')

plt.show()