# Python Learn day04

<p>2018年01月12日11:08:17</p>

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

### 初始化实例属性

虽然我们可以自由地给一个实例绑定各种属性，但是，现实世界中，一种类型的实例应该拥有相同名字的属性。例如，<code>Person</code>类应该在创建的时候就拥有 <code>name</code>、<code>gender</code> 和 <code>birth</code> 属性，怎么办？

在定义 Person 类时，可以为Person类添加一个特殊的<code>\__init__()</code>方法，当创建实例时，<code>\__init__()</code>方法被自动调用，我们就能在此为每个实例都统一加上以下属性：

        class Person(object):
            def __init__(self, name, gender, birth):
                self.name = name
                self.gender = gender
                self.birth = birth

<code>\__init__()</code> 方法的第一个参数必须是 <code>self</code>（也可以用别的名字，但建议使用习惯用法），后续参数则可以自由指定，和定义函数没有任何区别。

相应地，创建实例时，就必须要提供除 self 以外的参数：

        xiaoming = Person('Xiao Ming', 'Male', '1991-1-1')
        xiaohong = Person('Xiao Hong', 'Female', '1992-2-2')

有了<code>\__init__()</code>方法，每个Person实例在创建时，都会有 <code>name</code>、<code>gender</code> 和 <code>birth</code> 这3个属性，并且，被赋予不同的属性值，访问属性使用.操作符：

        print xiaoming.name
        # 输出 'Xiao Ming'
        print xiaohong.birth
        # 输出 '1992-2-2'

要特别注意的是，初学者定义<code>\__init__()</code>方法常常忘记了 <code>self</code> 参数：

        >>> class Person(object):
        ...     def __init__(name, gender, birth):
        ...         pass
        ... 
        >>> xiaoming = Person('Xiao Ming', 'Male', '1990-1-1')
        Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
        TypeError: __init__() takes exactly 3 arguments (4 given)

这会导致创建失败或运行不正常，因为第一个参数name被Python解释器传入了实例的引用，从而导致整个方法的调用参数位置全部没有对上。

        任务:
        请定义Person类的__init__方法，除了接受 name、gender 和 birth 外，还可接受任意关键字参数，并把他们都作为属性赋值给实例。

        要定义关键字参数，使用 **kw；

        除了可以直接使用self.name = 'xxx'设置一个属性外，还可以通过 setattr(self, 'name', 'xxx') 设置属性。

        参考代码:
        class Person(object):
            def __init__(self, name, gender, birth, **kw):
                self.name = name
                self.gender = gender
                self.birth = birth
                for k, v in kw.iteritems():
                    setattr(self, k, v)
        xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')
        print xiaoming.name
        print xiaoming.job

### 访问限制

我们可以给一个实例绑定很多属性，如果有些属性不希望被外部访问到怎么办？

Python对属性权限的控制是通过属性名来实现的，如果一个属性由双下划线开头(__)，该属性就无法被外部访问。看例子：

        class Person(object):
            def __init__(self, name):
                self.name = name
                self._title = 'Mr'
                self.__job = 'Student'
        p = Person('Bob')
        print p.name
        # => Bob
        print p._title
        # => Mr
        print p.__job
        # => Error
        Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
        AttributeError: 'Person' object has no attribute '__job'

可见，只有以双下划线开头的"__job"不能直接被外部访问。

但是，如果一个属性以"__xxx__"的形式定义，那它又可以被外部访问了，以"__xxx__"定义的属性在Python的类中被称为特殊属性，有很多预定义的特殊属性可以使用，通常我们不要把普通属性用"__xxx__"定义。

以单下划线开头的属性"_xxx"虽然也可以被外部访问，但是，按照习惯，他们不应该被外部访问。

### 创建类属性

类是模板，而实例则是根据类创建的对象。

绑定在一个实例上的属性不会影响其他实例，但是，类本身也是一个对象，如果在类上绑定一个属性，则所有实例都可以访问类的属性，并且，所有实例访问的类属性都是同一个！也就是说，<font color="red">实例属性每个实例各自拥有，互相独立，而类属性有且只有一份</font>。

定义类属性可以直接在 class 中定义：

        class Person(object):
            address = 'Earth'
            def __init__(self, name):
                self.name = name

因为类属性是直接绑定在类上的，所以，访问类属性不需要创建实例，就可以直接访问：

        print Person.address
        # => Earth

对一个实例调用类的属性也是可以访问的，所有实例都可以访问到它所属的类的属性：

        p1 = Person('Bob')
        p2 = Person('Alice')
        print p1.address
        # => Earth
        print p2.address
        # => Earth

由于Python是动态语言，类属性也是可以动态添加和修改的：

        Person.address = 'China'
        print p1.address
        # => 'China'
        print p2.address
        # => 'China'

因为类属性只有一份，所以，当Person类的address改变时，所有实例访问到的类属性都改变了。

### python中类属性和实例属性名字冲突

修改类属性会导致所有实例访问到的类属性全部都受影响，但是，如果在实例变量上修改类属性会发生什么问题呢？

            class Person(object):
                address = 'Earth'
                def __init__(self, name):
                    self.name = name

            p1 = Person('Bob')
            p2 = Person('Alice')

            print 'Person.address = ' + Person.address

            p1.address = 'China'
            print 'p1.address = ' + p1.address

            print 'Person.address = ' + Person.address
            print 'p2.address = ' + p2.address

结果如下：

            Person.address = Earth
            p1.address = China
            Person.address = Earth
            p2.address = Earth

我们发现，在设置了 p1.address = 'China' 后，p1访问 address 确实变成了 'China'，但是，Person.address和p2.address仍然是'Earch'，怎么回事？

原因是 p1.address = 'China'并没有改变 Person 的 address，而是给 p1这个实例绑定了实例属性address ，对p1来说，它有一个实例属性address（值是'China'），而它所属的类Person也有一个类属性address，所以:

            访问 p1.address 时，优先查找实例属性，返回'China'。

            访问 p2.address 时，p2没有实例属性address，但是有类属性address，因此返回'Earth'。

可见，<font color="red">当实例属性和类属性重名时，实例属性优先级高</font>，它将屏蔽掉对类属性的访问。

当我们把 p1 的 address 实例属性删除后，访问 p1.address 就又返回类属性的值 'Earth'了：

            del p1.address
            print p1.address
            # => Earth

可见，<font color="red">千万不要在实例上修改类属性，它实际上并没有修改类属性，而是给实例绑定了一个实例属性</font>。

### python中定义实例方法

一个实例的私有属性就是以__开头的属性，无法被外部访问，那这些属性定义有什么用？

虽然私有属性无法从外部访问，但是，从类的内部是可以访问的。除了可以定义实例的属性外，还可以定义实例的方法。

实例的方法就是在类中定义的函数，它的第一个参数永远是 self，指向调用该方法的实例本身，其他参数和一个普通函数是完全一样的：

        class Person(object):
            def __init__(self, name):
                self.__name = name
            def get_name(self):
                return self.__name

<code>get_name(self)</code> 就是一个实例方法，它的第一个参数是self。<code>\__init__(self, name)</code>其实也可看做是一个特殊的实例方法。

调用实例方法必须在实例上调用：

        p1 = Person('Bob')
        print p1.get_name()  # self不需要显式传入
        # => Bob

在实例方法内部，可以访问所有实例属性，这样，如果外部需要访问私有属性，可以通过方法调用获得，这种数据封装的形式除了能保护内部数据一致性外，还可以简化外部调用的难度。

### python中方法也是属性

我们在 class 中定义的实例方法其实也是属性，它实际上是一个函数对象：

        class Person(object):
            def __init__(self, name, score):
                self.name = name
                self.score = score
            def get_grade(self):
                return 'A'

        p1 = Person('Bob', 90)
        print p1.get_grade
        # => <bound method Person.get_grade of <__main__.Person object at 0x109e58510>>
        print p1.get_grade()
        # => A

也就是说，<code>p1.get_grade</code> 返回的是一个函数对象，但这个函数是一个绑定到实例的函数，<code>p1.get_grade()</code> 才是方法调用。

因为方法也是一个属性，所以，它也可以动态地添加到实例上，只是需要用 <code>types.MethodType()</code> 把一个函数变为一个方法：

        import types
        def fn_get_grade(self):
            if self.score >= 80:
                return 'A'
            if self.score >= 60:
                return 'B'
            return 'C'

        class Person(object):
            def __init__(self, name, score):
                self.name = name
                self.score = score

        p1 = Person('Bob', 90)
        p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
        print p1.get_grade()
        # => A
        p2 = Person('Alice', 65)
        print p2.get_grade()
        # ERROR: AttributeError: 'Person' object has no attribute 'get_grade'
        # 因为p2实例并没有绑定get_grade

给一个实例动态添加方法并不常见，直接在class中定义要更直观。

### python中定义类方法

和属性类似，方法也分实例方法和类方法。

在class中定义的全部是实例方法，实例方法第一个参数 self 是实例本身。

要在class中定义类方法，需要这么写：

        class Person(object):
            count = 0
            @classmethod
            def how_many(cls):
                return cls.count
            def __init__(self, name):
                self.name = name
                Person.count = Person.count + 1

        print Person.how_many()
        p1 = Person('Bob')
        print Person.how_many()

通过标记一个 <code>@classmethod</code>，该方法将绑定到 Person 类上，而非类的实例。类方法的第一个参数将传入类本身，通常将参数名命名为 cls，上面的 cls.count 实际上相当于 Person.count。

因为是在类上调用，而非实例上调用，因此类方法无法获得任何实例变量，只能获得类的引用。
