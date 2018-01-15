# Python Learn day05

<p>2018年01月15日19:18:25</p>

<div style="border-radius:10px;background:#fffddd">继承、多态、定制类</div>

---

## 继承和多态

### 什么是继承

当新类想要拥有现有类的功能结构，可以使用继承。继承的前提是新类 is a 现有类，即： 子类 is 父类

总是从某个类继承：

        class Myclass(object):
            pass
            
一定不要忘记调用<code>super().\__init__</code>

        def __init__(self,args):
            super(SubClass,self).__init__(args)
            pass
            
has 关系用组合而不是继承

### 继承一个类

如果已经定义了Person类，需要定义新的Student和Teacher类时，可以直接从Person类继承：

        class Person(object):
            def __init__(self, name, gender):
                self.name = name
                self.gender = gender

定义Student类时，只需要把额外的属性加上，例如score：

        class Student(Person):
            def __init__(self, name, gender, score):
                super(Student, self).__init__(name, gender)
                self.score = score

一定要用 <code>super(Student, self).\__init__(name, gender)</code> 去初始化父类，否则，继承自 Person 的 Student 将没有 name 和 gender。

函数<code>super(Student, self)</code>将返回当前类继承的父类，即 Person ，然后调用<code>\__init__()</code>方法，注意<font color="red">self参数已在<code>super()</code>中传入，在<code>\__init__()</code>中将隐式传递，不需要写出（也不能写）</font>。

### 判断类型

函数<code>isinstance()</code>可以判断一个变量的类型，既可以用在Python内置的数据类型如str、list、dict，也可以用在我们自定义的类，它们本质上都是数据类型。

假设有如下的 Person、Student 和 Teacher 的定义及继承关系如下：

        class Person(object):
            def __init__(self, name, gender):
                self.name = name
                self.gender = gender

        class Student(Person):
            def __init__(self, name, gender, score):
                super(Student, self).__init__(name, gender)
                self.score = score

        class Teacher(Person):
            def __init__(self, name, gender, course):
                super(Teacher, self).__init__(name, gender)
                self.course = course

        p = Person('Tim', 'Male')
        s = Student('Bob', 'Male', 88)
        t = Teacher('Alice', 'Female', 'English')

当我们拿到变量 p、s、t 时，可以使用 <code>isinstance</code> 判断类型：

        >>> isinstance(p, Person)
        True    # p是Person类型
        >>> isinstance(p, Student)
        False   # p不是Student类型
        >>> isinstance(p, Teacher)
        False   # p不是Teacher类型

这说明在继承链上，一个父类的实例不能是子类类型，因为子类比父类多了一些属性和方法。

我们再考察 s ：

        >>> isinstance(s, Person)
        True    # s是Person类型
        >>> isinstance(s, Student)
        True    # s是Student类型
        >>> isinstance(s, Teacher)
        False   # s不是Teacher类型

s 是Student类型，不是Teacher类型，这很容易理解。但是，s 也是Person类型，因为Student继承自Person，虽然它比Person多了一些属性和方法，但是，把 s 看成Person的实例也是可以的。

这说明在一条继承链上，一个实例可以看成它本身的类型，也可以看成它父类的类型。

### 多态

类具有继承关系，并且子类类型可以向上转型看做父类类型，如果我们从 Person 派生出 Student和Teacher ，并都写了一个 <code>whoAmI()</code> 方法：

        class Person(object):
            def __init__(self, name, gender):
                self.name = name
                self.gender = gender
            def whoAmI(self):
                return 'I am a Person, my name is %s' % self.name

        class Student(Person):
            def __init__(self, name, gender, score):
                super(Student, self).__init__(name, gender)
                self.score = score
            def whoAmI(self):
                return 'I am a Student, my name is %s' % self.name

        class Teacher(Person):
            def __init__(self, name, gender, course):
                super(Teacher, self).__init__(name, gender)
                self.course = course
            def whoAmI(self):
                return 'I am a Teacher, my name is %s' % self.name

在一个函数中，如果我们接收一个变量 x，则无论该 x 是 Person、Student还是 Teacher，都可以正确打印出结果：

        def who_am_i(x):
            print x.whoAmI()

        p = Person('Tim', 'Male')
        s = Student('Bob', 'Male', 88)
        t = Teacher('Alice', 'Female', 'English')

        who_am_i(p)
        who_am_i(s)
        who_am_i(t)

运行结果：

        I am a Person, my name is Tim
        I am a Student, my name is Bob
        I am a Teacher, my name is Alice

这种行为称为多态。也就是说，方法调用将作用在 x 的实际类型上。s 是Student类型，它实际上拥有自己的 <code>whoAmI()</code>方法以及从 Person继承的 whoAmI方法，但调用 <code>s.whoAmI()</code>总是先查找它自身的定义，如果没有定义，则顺着继承链向上查找，直到在某个父类中找到为止。

由于Python是动态语言，所以，传递给函数 <code>who_am_i(x)</code>的参数 x 不一定是 Person 或 Person 的子类型。任何数据类型的实例都可以，只要它有一个<code>whoAmI()</code>的方法即可：

        class Book(object):
            def whoAmI(self):
                return 'I am a book'

这是动态语言和静态语言（例如Java）最大的差别之一。动态语言调用实例方法，不检查类型，只要方法存在，参数正确，就可以调用。

### 多重继承

除了从一个父类继承外，Python允许从多个父类继承，称为多重继承。

多重继承的继承链就不是一棵树了，它像这样：

        class A(object):
            def __init__(self, a):
                print 'init A...'
                self.a = a
        
        class B(A):
            def __init__(self, a):
                super(B, self).__init__(a)
                print 'init B...'
        
        class C(A):
            def __init__(self, a):
                super(C, self).__init__(a)
                print 'init C...'
        
        class D(B, C):
            def __init__(self, a):
                super(D, self).__init__(a)
                print 'init D...'
看下图:

<img src="http://img.mukewang.com/54daf037000142d207580552.jpg">

像这样，D 同时继承自 B 和 C，也就是 D 拥有了 A、B、C 的全部功能。多重继承通过 super()调用<code>\__init__()</code>方法时，A 虽然被继承了两次，但<code>\__init__()</code>只调用一次：

        >>> d = D('d')
        init A...
        init C...
        init B...
        init D...

多重继承的目的是从两种继承树中分别选择并继承出子类，以便组合功能使用。

举个例子，Python的网络服务器有TCPServer、UDPServer、UnixStreamServer、UnixDatagramServer，而服务器运行模式有 多进程ForkingMixin 和 多线程ThreadingMixin两种。

要创建多进程模式的 TCPServer：

        class MyTCPServer(TCPServer, ForkingMixin)
            pass

要创建多线程模式的 UDPServer：

        class MyUDPServer(UDPServer, ThreadingMixin):
            pass

如果没有多重继承，要实现上述所有可能的组合需要 4x2=8 个子类。

### 获取对象信息

拿到一个变量，除了用 <code>isinstance()</code> 判断它是否是某种类型的实例外，还有没有别的方法获取到更多的信息呢？

例如，已有定义：

        class Person(object):
            def __init__(self, name, gender):
                self.name = name
                self.gender = gender
        
        class Student(Person):
            def __init__(self, name, gender, score):
                super(Student, self).__init__(name, gender)
                self.score = score
            def whoAmI(self):
                return 'I am a Student, my name is %s' % self.name
首先可以用 type() 函数获取变量的类型，它返回一个 Type 对象：

        >>> type(123)
        <type 'int'>
        >>> s = Student('Bob', 'Male', 88)
        >>> type(s)
        <class '__main__.Student'>

其次，可以用 dir() 函数获取变量的所有属性：

            >>> dir(123)   # 整数也有很多属性...
            ['__abs__', '__add__', '__and__', '__class__', '__cmp__', ...]
            
            >>> dir(s)
            ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'gender', 'name', 'score', 'whoAmI']

对于实例变量，<code>dir()</code>返回所有实例属性，包括`__class__`这类有特殊意义的属性。注意到方法`whoAmI`也是 s 的一个属性。

如何去掉`__xxx__`这类的特殊属性，只保留我们自己定义的属性？回顾一下filter()函数的用法。

dir()返回的属性是字符串列表，如果已知一个属性名称，要获取或者设置对象的属性，就需要用 getattr() 和 setattr( )函数了：

        >>> getattr(s, 'name')  # 获取name属性
        'Bob'
        
        >>> setattr(s, 'name', 'Adam')  # 设置新的name属性
        
        >>> s.name
        'Adam'
        
        >>> getattr(s, 'age')  # 获取age属性，但是属性不存在，报错：
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        AttributeError: 'Student' object has no attribute 'age'
        
        >>> getattr(s, 'age', 20)  # 获取age属性，如果属性不存在，就返回默认值20：
        20


## 定制类

### 什么是特殊方法

用于 print 的<code>\__str__</code>

用于 len 的<code>\__len__</code>

用于 cmp 的<code>\__cmp__</code>

特点：

1.特殊方法定义在 class 中

2.不需要直接调用

3.Python 的某些函数或操作符会调用对应的特殊方法

<img src="https://img4.mukewang.com/5a5c76910001e63112800720.jpg">

正确实现特殊方法：

1.只需要编写需要的特殊方法

2.有关联性的特殊方法都必须实现

例如当我们实现<code>\__getattr__</code>函数的时候就必须同时实现<code>\__setattr__</code>和<code>\__delattr__</code>

###  __str__和__repr__

如果要把一个类的实例变成 str，就需要实现特殊方法<code>\__str__()</code>：

        class Person(object):
            def __init__(self, name, gender):
                self.name = name
                self.gender = gender
            def __str__(self):
                return '(Person: %s, %s)' % (self.name, self.gender)
                
现在，在交互式命令行下用 print 试试：

        >>> p = Person('Bob', 'male')
        >>> print p
        (Person: Bob, male)
        
但是，如果直接敲变量 p：

        >>> p
        <main.Person object at 0x10c941890>
        
似乎<code>\__str__()</code> 不会被调用。

因为 Python 定义了<code>\__str__()</code>和<code>\__repr__()</code>两种方法，<code>\__str__()</code>用于显示给用户，而<code>\__repr__()</code>用于显示给开发人员。

有一个偷懒的定义<code>\__repr__</code>的方法：

        class Person(object):
            def __init__(self, name, gender):
                self.name = name
                self.gender = gender
            def __str__(self):
                return '(Person: %s, %s)' % (self.name, self.gender)
            __repr__ = __str__

### python中 \__cmp__

对 int、str 等内置数据类型排序时，Python的 <code>sorted()</code> 按照默认的比较函数 cmp 排序，但是，如果对一组 Student 类的实例排序时，就必须提供我们自己的特殊方法 <code>\__cmp__()</code>：

        class Student(object):
            def __init__(self, name, score):
                self.name = name
                self.score = score
            def __str__(self):
                return '(%s: %s)' % (self.name, self.score)
            __repr__ = __str__
        
            def __cmp__(self, s):
                if self.name < s.name:
                    return -1
                elif self.name > s.name:
                    return 1
                else:
                    return 0
                    
上述 Student 类实现了<code>\__cmp__()</code>方法，<code>\__cmp__</code>用实例自身self和传入的实例 s 进行比较，如果 self 应该排在前面，就返回 -1，如果 s 应该排在前面，就返回1，如果两者相当，返回 0。

Student类实现了按name进行排序：

        >>> L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 77)]
        >>> print sorted(L)
        [(Alice: 77), (Bob: 88), (Tim: 99)]
注意: 如果list不仅仅包含 Student 类，则 <code>\__cmp__</code> 可能会报错：

        L = [Student('Tim', 99), Student('Bob', 88), 100, 'Hello']
        print sorted(L)

### python中 \__len__

如果一个类表现得像一个list，要获取有多少个元素，就得用 <code>len()</code> 函数。

要让 <code>len()</code> 函数工作正常，类必须提供一个特殊方法<code>\__len__()</code>，它返回元素的个数。

例如，我们写一个 Students 类，把名字传进去：

        class Students(object):
            def __init__(self, *args):
                self.names = args
            def __len__(self):
                return len(self.names)
                
只要正确实现了<code>\__len__()</code>方法，就可以用<code>len()</code>函数返回Students实例的“长度”：

        >>> ss = Students('Bob', 'Alice', 'Tim')
        >>> print len(ss)
        3
        
        任务：
        斐波那契数列是由 0, 1, 1, 2, 3, 5, 8...构成。
        请编写一个Fib类，Fib(10)表示数列的前10个元素，print Fib(10) 可以打印出数列的前 10 个元素，len(Fib(10))可以正确返回数列的个数10。
        需要根据num计算出斐波那契数列的前N个元素。
    
        参考代码:
        
        class Fib(object):
            def __init__(self, num):
                a, b, L = 0, 1, []
                for n in range(num):
                    L.append(a)
                    a, b = b, a + b
                self.numbers = L
        
            def __str__(self):
                return str(self.numbers)
        
            __repr__ = __str__
        
            def __len__(self):
                return len(self.numbers)
        
        f = Fib(10)
        print f
        print len(f)
        
### python中数学运算

Python 提供的基本数据类型 int、float 可以做整数和浮点的四则运算以及乘方等运算。

但是，四则运算不局限于int和float，还可以是有理数、矩阵等。

要表示有理数，可以用一个Rational类来表示：

        class Rational(object):
            def __init__(self, p, q):
                self.p = p
                self.q = q
                
p、q 都是整数，表示有理数 p/q。

如果要让Rational进行+运算，需要正确实现<code>\__add__</code>：

        class Rational(object):
            def __init__(self, p, q):
                self.p = p
                self.q = q
            def __add__(self, r):
                return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
            def __str__(self):
                return '%s/%s' % (self.p, self.q)
            __repr__ = __str__
现在可以试试有理数加法：

        >>> r1 = Rational(1, 3)
        >>> r2 = Rational(1, 2)
        >>> print r1 + r2
        5/6

        任务:
        Rational类虽然可以做加法，但无法做减法、乘方和除法，请继续完善Rational类，实现四则运算。
        
        提示：
        减法运算：__sub__
        乘法运算：__mul__
        除法运算：__div__

        如果运算结果是 6/8，在显示的时候需要归约到最简形式3/4。
        
        参考代码:
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        class Rational(object):
            def __init__(self, p, q):
                self.p = p
                self.q = q
            def __add__(self, r):
                return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
            def __sub__(self, r):
                return Rational(self.p * r.q - self.q * r.p, self.q * r.q)
            def __mul__(self, r):
                return Rational(self.p * r.p, self.q * r.q)
            def __div__(self, r):
                return Rational(self.p * r.q, self.q * r.p)
            def __str__(self):
                g = gcd(self.p, self.q)
                return '%s/%s' % (self.p / g, self.q / g)
            __repr__ = __str__
        
        r1 = Rational(1, 2)
        r2 = Rational(1, 4)
        print r1 + r2
        print r1 - r2
        print r1 * r2
        print r1 / r2
        
### python中类型转换

Rational类实现了有理数运算，但是，如果要把结果转为 int 或 float 怎么办？

考察整数和浮点数的转换：

        >>> int(12.34)
        12
        >>> float(12)
        12.0
        
如果要把 Rational 转为 int，应该使用：

        r = Rational(12, 5)
        n = int(r)
        
要让<code>int()</code>函数正常工作，只需要实现特殊方法<code>\__int__()</code>:

        class Rational(object):
            def __init__(self, p, q):
                self.p = p
                self.q = q
            def __int__(self):
                return self.p // self.q

结果如下：

        >>> print int(Rational(7, 2))
        3
        >>> print int(Rational(1, 3))
        0
        
同理，要让<code>float()</code>函数正常工作，只需要实现特殊方法<code>\__float__()</code>。

### python中 @property

考察 Student 类：

        class Student(object):
            def __init__(self, name, score):
                self.name = name
                self.score = score
                
当我们想要修改一个 Student 的 scroe 属性时，可以这么写：

        s = Student('Bob', 59)
        s.score = 60
        
但是也可以这么写：

        s.score = 1000
        
显然，直接给属性赋值无法检查分数的有效性。

如果利用两个方法：

        class Student(object):
            def __init__(self, name, score):
                self.name = name
                self.__score = score
            def get_score(self):
                return self.__score
            def set_score(self, score):
                if score < 0 or score > 100:
                    raise ValueError('invalid score')
                self.__score = score
                
这样一来，s.set_score(1000) 就会报错。

这种使用 get/set 方法来封装对一个属性的访问在许多面向对象编程的语言中都很常见。

但是写 s.get_score() 和 s.set_score() 没有直接写 s.score 来得直接。

有没有两全其美的方法？----有。

因为Python支持高阶函数，在函数式编程中我们介绍了装饰器函数，可以用装饰器函数把 get/set 方法“装饰”成属性调用：

        class Student(object):
            def __init__(self, name, score):
                self.name = name
                self.__score = score
            @property
            def score(self):
                return self.__score
            @score.setter
            def score(self, score):
                if score < 0 or score > 100:
                    raise ValueError('invalid score')
                self.__score = score
                
<font color="red">注意: 第一个score(self)是get方法，用@property装饰，第二个score(self, score)是set方法，用@score.setter装饰，@score.setter是前一个@property装饰后的副产品。</font>

现在，就可以像使用属性一样设置score了：

        >>> s = Student('Bob', 59)
        >>> s.score = 60
        >>> print s.score
        60
        >>> s.score = 1000
        Traceback (most recent call last):
          ...
        ValueError: invalid score
        
说明对 score 赋值实际调用的是 set方法。

### python中 \__slots__

由于Python是动态语言，任何实例在运行期都可以动态地添加属性。

如果要限制添加的属性，例如，Student类只允许添加 name、gender和score 这3个属性，就可以利用Python的一个特殊的<code>\__slots__</code>来实现。

顾名思义，<code>\__slots__</code>是指一个类允许的属性列表：

        class Student(object):
            __slots__ = ('name', 'gender', 'score')
            def __init__(self, name, gender, score):
                self.name = name
                self.gender = gender
                self.score = score

现在，对实例进行操作：

        >>> s = Student('Bob', 'male', 59)
        >>> s.name = 'Tim' # OK
        >>> s.score = 99 # OK
        >>> s.grade = 'A'
        Traceback (most recent call last):
          ...
        AttributeError: 'Student' object has no attribute 'grade'

<code>\__slots__</code>的目的是限制当前类所能拥有的属性，如果不需要添加任意动态的属性，使用<code>\__slots__</code>也能节省内存。

### python中 \__call__
在Python中，函数其实是一个对象：

        >>> f = abs
        >>> f.__name__
        'abs'
        >>> f(-123)
        123
        
由于 f 可以被调用，所以，f 被称为可调用对象。

所有的函数都是可调用对象。

一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法<code>\__call__()</code>。

我们把 Person 类变成一个可调用对象：

        class Person(object):
            def __init__(self, name, gender):
                self.name = name
                self.gender = gender
        
            def __call__(self, friend):
                print 'My name is %s...' % self.name
                print 'My friend is %s...' % friend
                
现在可以对 Person 实例直接调用：

        >>> p = Person('Bob', 'male')
        >>> p('Tim')
        My name is Bob...
        My friend is Tim...
        
单看 p('Tim') 你无法确定 p 是一个函数还是一个类实例，所以，在Python中，函数也是对象，对象和函数的区别并不显著。
