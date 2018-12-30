import tkinter
from res.func import mergeLog

# 与button关联，将输入传递至合并函数中做处理
def start_merge(log_path,problem_time,search_range):
#def start_merge():#log_path,problem_time,search_range):
	log_path = log_path.get()	# 获取输入，初步交互
	problem_time = problem_time.get() # 未做条件过滤，BUG+1~
	search_range = search_range.get()
	apNum,kmsgNum = mergeLog(log_path,problem_time,search_range)
	# 将结果动态输出，完成交互
	content.set('merge done!\napp:{}\nkmsg:{}'.format(apNum,kmsgNum))

# 初始化交互页面
window = tkinter.Tk()
window.title('Log Parse')	# 标题
window.geometry('600x300')	# 框大小

# 初始化标签栏
tkinter.Label(window,text='log路径:').place(x=50,y=30)
tkinter.Label(window,text='问题时间:').place(x=50,y=80)
tkinter.Label(window,text='搜索范围:').place(x=50,y=130)

# 初始化输入栏
log_path = tkinter.StringVar() #将输入设定为动态可获取
tkinter.Entry(window,textvariable=log_path,width=65).place(x=110,y=30)
problem_time = tkinter.StringVar()
tkinter.Entry(window,textvariable=problem_time,width=65).place(x=110,y=80)
search_range = tkinter.StringVar()
tkinter.Entry(window,textvariable=search_range,width=65).place(x=110,y=130)

# 定义button，通过command与start_merge函数关联
tkinter.Button(window,text='merge',command=lambda: start_merge(log_path,problem_time,search_range)).place(x=280,y=160)

# 初始化输出标签
content = tkinter.StringVar()
tkinter.Label(window,textvariable=content).place(x=260,y=200)

# 交互界面设置完成
window.mainloop()

