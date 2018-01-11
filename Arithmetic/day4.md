# Python Learn day04

<p>2018年01月11日17:02:05</p>

<div style="border-radius:10px;background:#fffddd">模块、包、面向对象编程基础</div>

---

## 模块、包

为了便于管理和后期维护，我们通常把功能都封装在一个个的模块中，通过调用模块来进行操作，同时，为了区分同名的不同内容的模块我们一般会把不同的 <code>.py</code> 文件放入不同的包中，在 <code>.py</code> 文件中如果想要使用这些包和模块我们需要先引入对应的包才行，例如我们想要使用平方根的函数，首先需要引入对应的 math 包：

        >>> import math
        >>> math.sqrt()

为了让 <code>.py</code> 文件识别出引入的是包还是正常的文件夹，我们在所有的包中都会写上一个<code>\__init__.py</code> 文件，无论该包是否为空

### python之导入模块

要使用一个模块，我们必须首先导入该模块。Python使用 <code>import</code> 语句导入一个模块。例如，导入系统自带的模块 math：

        import math

你可以认为math就是一个指向已导入模块的变量，通过该变量，我们可以访问math模块中所定义的所有公开的函数、变量和类：

        >>> math.pow(2, 0.5) # pow是函数
        1.4142135623730951

        >>> math.pi # pi是变量
        3.141592653589793

如果我们只希望导入用到的math模块的某几个函数，而不是所有函数，可以用下面的语句：

        from math import pow, sin, log

这样，可以直接引用 pow, sin, log 这3个函数，但math的其他函数没有导入进来：

        >>> pow(2, 10)
        1024.0
        >>> sin(3.14)
        0.0015926529164868282

如果遇到名字冲突怎么办？比如math模块有一个log函数，logging模块也有一个log函数，如果同时使用，如何解决名字冲突？

如果使用import导入模块名，由于必须通过模块名引用函数名，因此不存在冲突：

        import math, logging
        print math.log(10)   # 调用的是math的log函数
        logging.log(10, 'something')   # 调用的是logging的log函数

如果使用 from...import 导入 log 函数，势必引起冲突。这时，可以给函数起个“别名”来避免冲突：

        from math import log
        from logging import log as logger   # logging的log现在变成了logger
        print log(10)   # 调用的是math的log
        logger(10, 'import from logging')   # 调用的是logging的log 
        
### python中动态导入模块

如果导入的模块不存在，Python解释器会报 ImportError 错误：

        >>> import something
        Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
        ImportError: No module named something

有的时候，两个不同的模块提供了相同的功能，比如 StringIO 和 cStringIO 都提供了StringIO这个功能。

这是因为Python是动态语言，解释执行，因此Python代码运行速度慢。

如果要提高Python代码的运行速度，最简单的方法是把某些关键函数用 C 语言重写，这样就能大大提高执行速度。

同样的功能，StringIO 是纯Python代码编写的，而 cStringIO 部分函数是 C 写的，因此 cStringIO 运行速度更快。

利用ImportError错误，我们经常在Python中动态导入模块：

        try:
            from cStringIO import StringIO
        except ImportError:
            from StringIO import StringIO

上述代码先尝试从cStringIO导入，如果失败了（比如cStringIO没有被安装），再尝试从StringIO导入。这样，如果cStringIO模块存在，则我们将获得更快的运行速度，如果cStringIO不存在，则顶多代码运行速度会变慢，但不会影响代码的正常执行。

try 的作用是捕获错误，并在捕获到指定错误时执行 except 语句。

### python之使用__future__

Python的新版本会引入新的功能，但是，实际上这些功能在上一个老版本中就已经存在了。要“试用”某一新的特性，就可以通过导入 <code>\__future__</code> 模块的某些功能来实现。

例如，Python 2.7的整数除法运算结果仍是整数：

        >>> 10 / 3
        3

但是，Python 3.x已经改进了整数的除法运算，“/”除将得到浮点数，“//”除才仍是整数：

        >>> 10 / 3
        3.3333333333333335
        >>> 10 // 3
        3

要在Python 2.7中引入3.x的除法规则，导入 <code>\__future__</code> 的<code>division</code>：

        >>> from __future__ import division
        >>> print 10 / 3
        3.3333333333333335

当新版本的一个特性与旧版本不兼容时，该特性将会在旧版本中添加到 <code>\__future__</code> 中，以便旧的代码能在旧版本中测试新特性。

### Python安装第三方模块

* easy_install

* pip(推荐，已经内置在 python2.7.9版本中)

>1.安装好你的 python 运行环境；

>2.在控制台输入命令：pip install 目标模块
例如我想要安装一个 web.py 模块就输入：pip install web.py

>3.打开 python，在下面输入：import web 即可

>访问网址 [https://www.pypi.python.org](https://www.pypi.python.org) 可以搜索想要的模块的安装名称

<img src="https://pan.baidu.com/s/1raqP6zy" alt="view" name="https://pan.baidu.com/s/1raqP6zy">


# 面向对象编程基础

通过 class 定义类，实例调用类方法；

        定义类：class Person():
        定义实例：xiaoming = new Person()

### 定义类并创建实例

在Python中，类通过 class 关键字定义。以 Person 为例，定义一个Person类如下：

        class Person(object):
            pass

按照 Python 的编程习惯，类名以大写字母开头，紧接着是(object)，表示该类是从哪个类继承下来的。类的继承将在后面的章节讲解，现在我们只需要简单地从object类继承。

有了Person类的定义，就可以创建出具体的xiaoming、xiaohong等实例。创建实例使用 类名+()，类似函数调用的形式创建：

        xiaoming = Person()
        xiaohong = Person()

### 创建实例属性

虽然可以通过Person类创建出xiaoming、xiaohong等实例，但是这些实例看上除了地址不同外，没有什么其他不同。在现实世界中，区分xiaoming、xiaohong要依靠他们各自的名字、性别、生日等属性。

如何让每个实例拥有各自不同的属性？由于Python是动态语言，对每一个实例，都可以直接给他们的属性赋值，例如，给xiaoming这个实例加上name、gender和birth属性：

        xiaoming = Person()
        xiaoming.name = 'Xiao Ming'
        xiaoming.gender = 'Male'
        xiaoming.birth = '1990-1-1'

给xiaohong加上的属性不一定要和xiaoming相同：

        xiaohong = Person()
        xiaohong.name = 'Xiao Hong'
        xiaohong.school = 'No. 1 High School'
        xiaohong.grade = 2

实例的属性可以像普通变量一样进行操作：

        xiaohong.grade = xiaohong.grade + 1

### 

### 

### 

### 

### 

### 

### 

### 
