# 最简单的
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('yourapplication', 'templates'))  # （package，path）
template = env.get_template('mytemplate.html')
print template.render(the='variables', go='here')


# 内置根据路径的加载方法
loader = FileSystemLoader('/path/to/templates')
loader = FileSystemLoader(['/path/to/templates', '/other/path'])

# 内置根据模块的加载方法
loader = PackageLoader('mypackage', 'views')

# 内置根据dict字典的加载方法
loader = DictLoader({'index.html': 'source here'})

# 根据前缀加载？
class jinja2.PrefixLoader(mapping, delimiter='/')  # 默认为'/',   'app1/index.html'
loader = PrefixLoader({
    'app1':     PackageLoader('mypackage.app1'),
    'app2':     PackageLoader('mypackage.app2')
})




# 字节码缓存
from os import path
class MyCache(BytecodeCache):
    def __init__(self, directory):
        self.directory = directory
    def load_bytecode(self, bucket):
        filename = path.join(self.directory, bucket.key)
        if path.exists(filename):
            with open(filename, 'rb') as f:
                bucket.load_bytecode(f)
    def dump_bytecode(self, bucket):
        filename = path.join(self.directory, bucket.key)
        with open(filename, 'wb') as f:
            bucket.write_bytecode(f)


# 基本定义
这里有两种分隔符: {% ... %} 和 {{ ... }} 。
前者用于执行诸如 for 循环 或赋值的语句，后者把表达式的结果打印到模板上。

{{ foo.bar }}  # 通过.访问变量的属性，或者通过下标也可以
{{ foo['bar'] }}


# 过滤器
过滤器与变量用管道符号（ | ）分割，一个过滤器的输出会被作为 后一个过滤器的输入。
{{ name|striptags|title }}  会移除 name 中的所有 HTML 标签并且改写 为标题样式的大小写格式。
个例子会 把一个列表用逗号连接起来: {{ list|join(', ') }} 

# 注释
 {# ... #} 
{# note: disabled template because we no longer use this
    {% for user in users %}
        ...
    {% endfor %}
#}


# 加入了-，则会去掉空白
{% for item in seq -%}
    {{ item }}
{%- endfor %}   # 标签和减号之间不能有空白。



# 行语句, 使用#代替{}
<ul>
# for item in seq
    <li>{{ item }}</li>
# endfor
</ul>

<ul>
{% for item in seq %}
    <li>{{ item }}</li>
{% endfor %}
</ul>


# 基本模板 所有的 block 标签 告诉模板引擎 子模板可以覆盖模板中的这些部分
{% block %}    # {% block sidebar %} 后面是注释
# 子模板  {% extend %} 标签是这里的关键。它告诉模板引擎这个模板“继承”另一个模板
# 如 {% extends "layout/default.html" %}
{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
    {{ super() }}
    <style type="text/css">
        .important { color: #336699; }
    </style>
{% endblock %}
{% block content %}
    <h1>Index</h1>
    <p class="important">
      Welcome on my awesome homepage.
    </p>
{% endblock %}


# Super 块   可以调用 super 来渲染父级块的内容。这会返回父级块的结果:
{% block sidebar %}
    <h3>Table Of Contents</h3>
    ...
    {{ super() }}
{% endblock %}


# 在一个 for 循环块中你可以访问这些特殊的变量:
loop.index	当前循环迭代的次数（从 1 开始）
loop.index0	当前循环迭代的次数（从 0 开始）
loop.revindex	到循环结束需要迭代的次数（从 1 开始）
loop.revindex0	到循环结束需要迭代的次数（从 0 开始）
loop.first	如果是第一次迭代，为 True 。
loop.last	如果是最后一次迭代，为 True 。
loop.length	序列中的项目数。
loop.cycle	在一串序列间期取值的辅助函数。见下面的解释。



要递归地 使用循环，你只需要在循环定义中加上 recursive 修饰，并在你想使用递归的地 方，对可迭代量调用 loop 变量。
<ul class="sitemap">
{%- for item in sitemap recursive %}
    <li><a href="{{ item.href|e }}">{{ item.title }}</a>
    {%- if item.children -%}
        <ul class="submenu">{{ loop(item.children) }}</ul>
    {%- endif %}</li>
{%- endfor %}
</ul>



# 宏
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{
        value|e }}" size="{{ size }}">
{%- endmacro %}
在命名空间中，宏之后可以像函数一样调用:
<p>{{ input('username') }}</p>
<p>{{ input('password', type='password') }}</p>

如果宏在不同的模板中定义，你需要首先使用 import 。
在宏内部，你可以访问三个特殊的变量:

# 调用
在某些情况下，需要把一个宏传递到另一个宏。为此，可以使用特殊的 call 块    让宏利用调用功能:
{% macro render_dialog(title, class='dialog') -%}
    <div class="{{ class }}">
        <h2>{{ title }}</h2>
        <div class="contents">
            {{ caller() }}
        </div>
    </div>
{%- endmacro %}
总而言之，调用块的工作方 式几乎与宏相同，只是调用块没有名称。
{% call render_dialog('Hello World') %}
    This is a simple dialog rendered by using a macro and
    a call block.
{% endcall %}



# 赋值
赋值使用 set 标签，并且可以为多个变量赋值:
{% set navigation = [('index.html', 'Index'), ('about.html', 'About')] %}
{% set key, value = call_something() %}


# 包含
include 语句用于包含一个模板，并在当前命名空间中返回那个文件的内容渲 染结果:
{% include 'header.html' %}
    Body
{% include 'footer.html' %}

样 如果模板不存在，Jinja 会忽略这条语句。与 with 或 without context 语句联合使用时，它必须被放在上下文可见性语句 之前 。
{% include "sidebar.html" ignore missing %}
{% include "sidebar.html" ignore missing with context %}
{% include "sidebar.html" ignore missing without context %}
你也可以提供一个模板列表，它会在包含前被检查是否存在。
{% include ['page_detailed.html', 'page.html'] %}
{% include ['special_sidebar.html', 'sidebar.html'] ignore missing %}


# 导入
{% macro input(name, value='', type='text') -%}
    <input type="{{ type }}" value="{{ value|e }}" name="{{ name }}">
{%- endmacro %}

{%- macro textarea(name, value='', rows=10, cols=40) -%}
    <textarea name="{{ name }}" rows="{{ rows }}" cols="{{ cols
        }}">{{ value|e }}</textarea>
{%- endmacro %}
------------------最简单灵活的方式是把整个模块导入为一个变量。这样你可以访问属性:
{% import 'forms.html' as forms %}
<dl>
    <dt>Username</dt>
    <dd>{{ forms.input('username') }}</dd>
    <dt>Password</dt>
    <dd>{{ forms.input('password', type='password') }}</dd>
</dl>
<p>{{ forms.textarea('comment') }}</p>
------------------此外你也可以从模板中导入名称到当前的命名空间:
{% from 'forms.html' import input as input_field, textarea %}
<dl>
    <dt>Username</dt>
    <dd>{{ input_field('username') }}</dd>
    <dt>Password</dt>
    <dd>{{ input_field('password', type='password') }}</dd>
</dl>
<p>{{ textarea('comment') }}</p>


# 导入上下文行为  render_box.html 可以 访问 box 
{% for box in boxes %}
    {% include "render_box.html" %}
{% endfor %}

# 列表用于存储和迭代序列化的数据。例如 你可以容易地在 for 循环中用列表和元组创建一个链接的列表:
<ul>
{% for href, caption in [('index.html', 'Index'), ('about.html', 'About'),
                         ('downloads.html', 'Downloads')] %}
    <li><a href="{{ href }}">{{ caption }}</a></li>
{% endfor %}
</ul>



