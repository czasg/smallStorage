__file__ = 'note'

"""
https://www.matplotlib.org.cn/
https://www.numpy.org.cn/
https://www.pypandas.cn/

from collections import Counter  # 用于统计计数
import pandas as pd; pd.DataFrame()
"""
import matplotlib.pyplot as plt
import numpy as np
# fig = plt.figure()  # an empty figure with no axes 创建一个空画布，没有任何轴
# fig.suptitle('No axes on this figure')  # Add a title so we know which it is 为我们的画布添加一个标题
# fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes 创建一个子画布吗
# plt.plot  # 简单的就是输入x，y，然后定义一个label的名字。如何只提供一组数据，则默认为y数据，并从0开始自动补全x
# plt.axis([0, 6, 0, 20])  # 设置x、y轴的坐标范围，这里就是0-6和0-20。 [xmin, xmax, ymin, ymax]
# plt.plot 提供第三个参数来改变样式，默认格式字符串为“b-”，为蓝色实线。'ro'为红点
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
"""一个图的一部分：
title：标题
Figure：画布
Axes：数据空间的图像区域，包含两个Axis对象，负责数据限制（数据限制也可以通过 set_xlim() 和 set_ylim() 来设置Axes方法）每个Axes都有一个标题（通过 set_title() 设置）一个x标签（通过 set_xlabel() 设置）和一个通过 set_ylabel() 设置的y标签。
Axis：设置图形限制并生成刻度线
Artist：艺术家。渲染图形时，所有艺术家都被绘制到画布（canvas）上。




character	description
'.'	point marker
','	pixel marker
'o'	circle marker
'v'	triangle_down marker
'^'	triangle_up marker
'<'	triangle_left marker
'>'	triangle_right marker
'1'	tri_down marker
'2'	tri_up marker
'3'	tri_left marker
'4'	tri_right marker
's'	square marker
'p'	pentagon marker
'*'	star marker
'h'	hexagon1 marker
'H'	hexagon2 marker
'+'	plus marker
'x'	x marker
'D'	diamond marker
'd'	thin_diamond marker
'|'	vline marker
'_'	hline marker

character	description
'-'	solid line style
'--'	dashed line style
'-.'	dash-dot line style
':'	dotted line style

character	color
'b'	blue
'g'	green
'r'	red
'c'	cyan
'm'	magenta
'y'	yellow
'k'	black
'w'	white


"""