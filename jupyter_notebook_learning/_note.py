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
# plt.subplot(131)  # plt.subplot(1, 3, 1) 一个意思，y轴上一个父类，x轴上三个子类，选择当前第1个图 bar柱状图scatter散点图plot默认折线图  figure定义花布
# plt.figure(1)  # 用来创建第1个figure，可以创建多个
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')  # 在指定位置显示文本
# plt.annotate  # 添加相关的注释。第一个参数是文本，第二个是箭头的坐标。后序可以添加文本从而指向箭头 ylim 设置y轴的间隔
# Data for plotting

# 热力图，太漂亮了把。bilinear - 这个是比较漂亮的热力图。数字越大的，颜色越亮，给人一种热热的感觉咯
# 可以设置origin='upper' origin='lower'来控制值越大颜色的深浅
# A = np.random.rand(5, 5)
# print(A)
# fig, axs = plt.subplots(1, 3, figsize=(10, 3))
# for ax, interp in zip(axs, ['nearest', 'bilinear', 'bicubic']):
#     ax.imshow(A, interpolation=interp)
#     ax.set_title(interp.capitalize())
#     ax.grid(True)
# plt.show()

# ax.hist(x, num_bins, density=1) 画直方图，返回y轴的值，x轴的值
# ax.scatter  # 四个参数分别为x轴坐标，y轴坐标。然后就是每个点的大小，再然后就是每个点的颜色

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