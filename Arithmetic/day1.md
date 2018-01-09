# Python Learn day1

<p>2018年01月09日19:20:27</p>

>简介：Python入门、变量和数据类型、List、Tuple、set、if、while、for、Dict

---

## Python 入门

* 1.安装 python
    在官网下载 python 点击安装即可，我使用的是 [python3.6](https://www.python.org/downloads/)

* 2.运行 python
    直接在 python 解释器上写代码回车直接运行，因为我们下载的 python 版本中都已经集成自带了 CPython 解释器。
    在 python 命令行面板中使用命令运行，例如我要运行一个 test.py 的文件则需要在命令行中输入：python test.py 然后回车即可
    
* <div style='color:red'>3.注意：
    Python 是一门动态编程的语言，没有具体的变量类型。Pyhton 对于格式缩进有着严格的要求，尽量不要使用 Tab 进行缩进而采用4个空格进行缩进从而判断代码块。

    
## 变量和数据类型

* 1.因为 python 是一种动态的编程语言，因此对于数据类型并没有像 java 一样必须要相同的数据类型才能进行操作。Python 的基本数据类型是：整数型、浮点型、字符串型。
例如：

JAVA:

    <code>int a = 10;
    String b = 'abc';
    int c = a + b;//此时报错，因为类型不同，强转</code>
    
Python：

    <code>a = 10;
    b = "abc";
    c = a + b;//输出：10abc，并不会报错</code>

* 2.单行注释在代码块的头部加上#号；

* 3.单行输入文本内容采用两个单引号''；

* 4.多行文本内容采用一对3个单引号'''....'''；

* 5.使用反斜杠\表示该个字符采用转义，例如\n 表示换行\"表示"；

* 6.在文本的前面加上 r 表示为该行文本的所有内容都采用了转义；

* 7.因为历史遗留的问题，python 使用的是 ASCII 的编码格式，为了让程序识别为 Unicode 编码格式我们需要在文本内容的前面加上一个小 u 进行给程序进行识别提示。

* 8.当我们想要让整个程序都采用 UTF-8的编码格式的时候我们只需要在头部加上 <code># -*- coding: utf-8 -*- </code>这样一句注释即可，注意当我们加上这句话后我们就不需要在文本内容的前面加 r 或者 u 来进行编码识别了。

* 9.python 中的精度问题可以使用浮点来解决，例如我们要计算<code>2.5+10/2</code>的结果是多少的时候，运行结果是4二不是5，因为我们10/2只能取到整数位，为了取到值是2.5，修改为<code>2.5+10.0/2</code>即可。

* 10.python 支持 boolean 值的运行，虽然 boolean 值只有 true 和 false 两种，可是使用 and 、 or 、 not 来进行计算结果子，返回的结果一样是 true 和 false。

## 集合类型 List、Tuple、set、Dict

1.List 集合 [ value1,  value2, value3,......]

* List 集合是一种有序的集合，可以随时对里面的元素进行增加和删除。

* List 集合的模型是：<code>L = ['i','am','list']</code>，使用中括号表示。

* 可以通过下标访问 List 集合中的元素，例如 L[0]，list 集合的下标时从0开始的，当我们想要从最后一个访问的话直接输入 L[-1]即代表该集合的最后一个元素，依次倒序的下标时-2、-3、-4等。

* 增加 list 中的元素有两种方法：

    >1.append()新增元素到集合的末尾：<code>L.append('python')</code>

    >2.insert(index, value)方法中有两个参数，第一个参数表示想要新增数据在 list 中的位置，第二个参数表示新增的元素的数据内容，例如：<code>L.insert(1,'me')</code>即表示在下标为1的位置新增一个内容为'me'的元素

* 删除 list 集合中的元素使用 pop()方法，例如：<code>L.pop(2)</code> 表示删除下标为2的元素

* 替换元素直接把对应下标位置的元素内容赋值为新内容即可，例如：<code>L[2] = 'new'</code>

2.Tuple 元组 ( value1,  value2, value3,......)

* Tuple 是一种有序的列表，和 List 类似，中文翻译为”元组“,但是相比较 List 集合，Tuple 元组一旦赋值完毕就不再能修改里面的任何元素了。但是我们有其他方法可以修改元祖的内容，下面会讲到。

* tuple 使用小括号进行创建，例如：<code>T = ('1','2')</code>，需要注意的是，当我们的 tuple 列表中只有一个元素的时候系统并不会识别为元组类型，因此当我们的元组内只有一个数据的时候我们需要在后面加上一个逗号，例如：<code>t = (1,)</code>即可

* 如何改变一个元祖中的数据呢，如果按照标准结构写的 tuple 列表是不能该表的，但是 list 集合是可以改变的，所以我们可以把 tuple 元组中的数据变成 list 类型的即可，写如：<code>lt = (['me','am'],['jj',1])</code>这样我们就可以赋值的方式取出需要修改的数据的对应集合然后再进行下一步操作。例如我们想要修改 'jj' 这个数据为 'mm' 可以进行如下操作：

    <code>l = lt[1]
    l.insert(0,'mm')</code>
    
    这样就可以实现修改元组中的数据了
    
<center><img src="http://img.mukewang.com/540538d400010f4603500260.jpg"></center>

3.Set ( [list] )

* dict的作用是建立一组 key 和一组 value的映射关系，dict的key是不能重复的。有的时候，我们只想要 dict 的 key，不关心 key 对应的value，目的就是保证这个集合的元素不会重复，这时，set就派上用场了。set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。

* set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。

创建 set 的方式是调用 set() 并传入一个 list，list的元素将作为set的元素：

<code>\>>> s = set(['A', 'B', 'C'])</code>

可以查看 set 的内容：

<code>\>>> print s
set(['A', 'C', 'B'])</code>

请注意，上述打印的形式类似 list， 但它不是 list，仔细看还可以发现，打印的顺序和原始 list 的顺序有可能是不同的，因为set内部存储的元素是无序的。

因为set不能包含重复的元素，所以，当我们传入包含重复元素的 list 会怎么样呢？

<code>\>>> s = set(['A', 'B', 'C', 'C'])

\>>> print s

set(['A', 'C', 'B'])

\>>> len(s)

3</code>

结果显示，set会自动去掉重复的元素，原来的list有4个元素，但set只有3个元素。

* 由于set存储的是无序集合，所以我们没法通过索引来访问。访问 set中的某个元素实际上就是判断一个元素是否在set中。

例如，存储了班里同学名字的set：

<code>>>> s = set(['Adam', 'Lisa', 'Bart', 'Paul'])</code>

我们可以用 in 操作符判断：Bart是该班的同学吗？

<code>\>>> 'Bart' in s

True</code>

Bill是该班的同学吗？

<code>\>>> 'Bill' in s

False</code>

bart是该班的同学吗？

<code>\>>> 'bart' in s

False</code>

看来大小写很重要，'Bart' 和 'bart'被认为是两个不同的元素。

* set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。最后，set存储的元素也是没有顺序的。set的这些特点，可以应用在哪些地方呢？
    <pre>星期一到星期日可以用字符串'MON', 'TUE', ... 'SUN'表示。假设我们让用户输入星期一至星期日的某天，如何判断用户的输入是否是一个有效的星期呢？可以用 if 语句判断，但这样做非常繁琐：
<code>x = '???' # 用户输入的字符串

if x!= 'MON' and x!= 'TUE' and x!= 'WED' ... and x!= 'SUN':

     print 'input error'
    
else:

    print 'input ok'</code>注意：if语句中的...表示没有列出的其它星期名称，测试时，请输入完整。如果事先创建好一个set，包含'MON' ~ 'SUN'：

<code>weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])</code>

再判断输入是否有效，只需要判断该字符串是否在set中：

<code>x = '???' # 用户输入的字符串
if x in weekdays:
    print 'input ok'
else:
    print 'input error'</code>

这样一来，代码就简单多了。</pre>


* 由于 set 也是一个集合，所以，遍历 set 和遍历 list 类似，都可以通过 for 循环实现。

    <pre>直接使用 for 循环可以遍历 set 的元素：

<code>\>>> s = set(['Adam', 'Lisa', 'Bart'])

\>>> for name in s:

...     print name

... 

Lisa

Adam

Bart</code>

注意: 观察 for 循环在遍历set时，元素的顺序和list的顺序很可能是不同的，而且不同的机器上运行的结果也可能不同。</pre>

* 由于set存储的是一组不重复的无序元素，因此，更新set主要做两件事：一是把新的元素添加到set中，二是把已有元素从set中删除。
    <pre>添加元素时，用set的add()方法：

<code>\>>> s = set([1, 2, 3])<br>
\>>> s.add(4)<br>
\>>> print s<br>
set([1, 2, 3, 4])</code><br>
如果添加的元素已经存在于set中，add()不会报错，但是不会加进去了：<br>
<code>\>>> s = set([1, 2, 3])<br>
\>>> s.add(3)<br>
\>>> print s<br>
set([1, 2, 3])</code><br>
删除set中的元素时，用set的remove()方法：<br>
<code>\>>> s = set([1, 2, 3, 4])<br>
\>>> s.remove(4)<br>
\>>> print s<br>
set([1, 2, 3])</code><br>
如果删除的元素不存在set中，remove()会报错：<br>
<code>\>>> s = set([1, 2, 3])<br>
\>>> s.remove(4)<br>
Traceback (most recent call last):<br>
  File "<stdin>", line 1, in <module><br>
KeyError: 4</code><br>
所以用add()可以直接添加，而remove()前需要判断。</pre>

4.Dict { key1 : value1,  key2 : value2,.....}

* 我们已经知道了 list 和 tuple 都是表，如果我们想要同时表示一个对应的数据怎么表达了，在 Java 中有 Map 类型来表示，Dict 和 Map 是很类似的，表示为<code>d = { key : value}</code>。形成了一对键值对，一个 dict 里面可以同时存在多个键值对，同大括号来表示 dict 类型。

* dict 类型的特点：

>1.查找速度很快，无论是10条数据还是10万条数据都是一样的速度；

>2.dict 中存储的键值对 key-value 是没有顺序的；

>3.dict 中作为 key的元素必须不可变，Python的基本类型如字符串、整数、浮点数都是不可变的，都可以作为 key。但是list是可变的，就不能作为 key。

* dict 类型可以简单的使用访问 key 值<code>d[key]</code>来获取返回值<code>d = {'Adam': 95,'Lisa': 85,'Bart': 59}  d['Adam']</code>，这个和 list 获取对象值很类似但是需要注意的是 list 必须使用索引返回对应的元素，而 dict 使用 key。

* 通过 key 来访问 dict 中的元素，当存在的时候会直接返回值，若 key 值不存在则会报 keyError 的错误，为了避免这种错误我们一般在外部先使用 if 做判断，<code>if key in d</code>表示判断 key 时候存在于 dict 类型的 d 中。

* dict是可变的，也就是说，我们可以随时往dict中添加新的 key-value。比如已有<code>dict：d = {'Adam': 95,'Lisa': 85,'Bart': 59}</code>，要把新同学'Paul'的成绩72加进去，用赋值语句：

<code>>>> d['Paul'] = 72</code>

再看看dict的内容：

<code>>>> print d
{'Lisa': 85, 'Paul': 72, 'Adam': 95, 'Bart': 59}</code>

如果 key 已经存在，则赋值会用新的 value 替换掉原来的 value：

<code>>>> d['Bart'] = 60
\>>> print d{'Lisa': 85, 'Paul': 72, 'Adam': 95, 'Bart': 60}</code>

* 由于dict也是一个集合，所以，遍历dict和遍历list类似，都可以通过 for 循环实现。直接使用for循环可以遍历 dict 的 key：

<code>>>> d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
\>>> for key in d:
\>>>     print key
Lisa
Adam
Bart</code>

由于通过 key 可以获取对应的value，因此，在循环体内，可以获取到value的值。


## 循环判断 if、while、for

1.if

* 判断元素时候存在：<code>if a in b</code>

* 判断元素是否等于：

<code>if a is b
if a == b</code>

两者的区别在于第一个是判断值相等，第二个判断所有信息是否相等。
 
* 三种判断语法：

1.<code>if 条件语句</code>

2.<code>if 条件1 else </code>

3.<code>if 条件1 elif 条件2 elif 条件3 else  </code>这里的 elif 就等于 else if


2.while

* <code>while 条件</code>

例如：<code>
sum = 0
x = 1
while x<=100:
    if x%2!=0
        sum = sum+x
print sum</code>

* 跳出循环 break

* 跳出该步循环执行下一步 continue

3.for

* Python的 for 循环就可以依次把list或tuple的每个元素迭代出来：

<code>L = ['Adam', 'Lisa', 'Bart']
for name in L:
    print name</code>
    
注意:  name 这个变量是在for循环中定义的，意思是，依次取出list中的每一个元素，并把元素赋值给name，然后执行for循环体（就是缩进的代码块）。这样一来，遍历一个list或tuple就非常容易了。
