# Python Learn day05

<p></p>

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



