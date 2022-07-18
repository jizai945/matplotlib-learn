# matplotlib-learn
learn matplotlib





## 为什么要学matplotlib

1. 能将数据进行可视化，更直观的呈现
2. 使数据更加**客观**、更具**说服力**



## 什么是matplotlib

最流行的python底层绘图库，主要做**数据可视化图表**，名字取材于MATLIB，模仿MATLAB构建



## matplotlib基本要点

axix轴，指的是x或者y这种坐标轴

如果把每一些点连接成一条线，组成了一个折线图

```python
from matplotlib import pyplot as plt # 导入 pyplot

x = range(2, 24, 2) # 数组在x轴的位置，是一个可迭代对象
y = [5, 13, 14.5, 17, 20, 25, 26, 24, 22, 18, 15] # 数据在y轴的位置， 是一个可迭代对象
# ---> x轴和y轴的数据一起组成了所有要绘制出的坐标
# ---> 分别是(2,15) (4,13) (6, 14.5) (8, 17) .....

plt.plot(x, y) # 传入x y 通过plot绘制出折线图
plt.show() # 在执行程序的时候展示图形

```

上面这种方式， x y的刻度自动帮你设置



除了上面，还可以做更多的什么?

+ 设置图片大小
+ 保存到本地
+ 描述信息，比如x轴和y轴表示什么，这个图表示什么
+ 调整x或者y的刻度的间距
+ 线条的样式(比如颜色，透明等)
+ 标记出特殊的点
+ 给图片添加一个水印



## 设置图片大小

2_demo.py

```python
import matplotlib.pyplot as plt

# figure 图形图标的意思，在这里值的就是我们画的图
# 通过实例化一个figure并且传递参数，能够在后台自动使用该figure实例
# 在图像模糊的时候可以传入dpi参数，让图片更加清晰 
# dpi值得是没英寸上点的个数 dot per inch
fig = plt.figure(figsize=(20, 8), dpi = 80)
x = range(2, 26, 2)
y = [5, 13, 14.5, 17, 20, 25, 26, 24, 22, 18, 15, 17]

# 绘图
plt.plot(x, y)

# 保存图片， 保存应该在绘图之后, 也可以保存为svg这种矢量图格式，放大不会有锯齿
plt.savefig('./2demo.png')

plt.show()
```



## 绘制xy轴的刻度

比如： `plt.xticks(range(2, 30, 3))`

还可以传递一个最大值，最小值 `plt.yticks(range(min(y), max(y)+1))`

绘制120分钟内的信息，可以这样生成一个随机数： `a = [random.randint(20, 35) for i in range(120)]`

比如在2_demo.py中



如何调整成自定义的刻度信息?

下面所示刻度上可以显示成自定义的字符串

raotation,显示时旋转的度数

```python
_x = x
_xtick_labels = ["10点{}分".format(i) for i in _x]
plt.xticks(x, _xtick_labels, rotation=90)
```



## 设置中文显示

为什么无法显示中文字符?

matplotlib默认不支持中文字符，因为默认的英文字体无法显示函数



查看linux/mac下面支持的字体:

`fc-list` 查看支持的字体

`fc-list:lang=zh`   查看支持的中文(冒号前面有空格)



那么问题来了: 如何修改matplotlib的默认字体?

+ 通过matplotlib.rc可以修改, 具体方法参见源码 (windows/linux)

+ 通过matplotlib下的font_manager可以解决 (windows/linux/mac)

  比如：

  ```python
  my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")
  plt.xticks(x, _xtick_labels, rotation=90, fontproperties=my_font)
  ```

  
