# Python Learn day03

<p>2018年01月10日15:10:50</p>

<div style="border-radius:10px;background:#fffddd">函数式编程</div>

---

# 函数式编程

* <font color="red">特点：

    1.不是纯函数式编程，允许有变量；
    
    2.支持高阶函数，函数也可以作为变量传入；
    
    3.支持闭包，有了闭包就能返回函数；
    
    4.有限度的支持匿名函数；</font>

## 高阶函数

    1.变量可以指向函数
    2.函数的参数可以接收变量
    3.一个函数可以接收另一个函数作为参数
    能接收函数作为参数的函数就是高阶函数
    
示例：

        >>>def and(x,y,f):
            return f(x)+f(y)        
        >>>and(-5,9,abs)
        14

其中我们把 <code>abs()</code> 求绝对值的函数传入了 <code>and()</code> 函数中，这样就实现了变量指向函数的行为
    
    def add(x, y, f):
        return f(x) + f(y)

如果传入abs作为参数f的值：

    add(-5, 9, abs)

根据函数的定义，函数执行的代码实际上是：

    abs(-5) + abs(9)

由于参数 x, y 和 f 都可以任意传入，如果 f 传入其他函数，就可以得到不同的返回值。

## Map() 函数

<code>map()</code>是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。

例如，对于<code>list [1, 2, 3, 4, 5, 6, 7, 8, 9]</code>

如果希望把list的每个元素都作平方，就可以用map()函数：

<center><img src="http://img.mukewang.com/54c8a7e40001327303410245.png"></center>

因此，我们只需要传入函数<code>f(x)=x*x</code>，就可以利用map()函数完成这个计算：

        def f(x):
            return x*x
        print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

输出结果：

    [1, 4, 9, 10, 25, 36, 49, 64, 81]

<font color="red">注意：<code>map()</code>函数不改变原有的 list，而是返回一个新的 list。</font>

利用<code>map()</code>函数，可以把一个 list 转换为另一个 list，只需要传入转换函数。

由于list包含的元素可以是任何类型，因此，<code>map()</code> 不仅仅可以处理只包含数值的 list，事实上它可以处理包含任意类型的 list，只要传入的函数f可以处理这种数据类型。

    任务:
    假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，请利用map()函数，把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list：

        输入：['adam', 'LISA', 'barT']
        输出：['Adam', 'Lisa', 'Bart']
        
        def format_name(s):
            return s[0].upper()+s[1:].lower()
        print map(format_name, ['adam', 'LISA', 'barT'])
    
        运行成功
        ['Adam', 'Lisa', 'Bart']

## Reduce() 函数

<code>reduce()</code>函数也是 Python 内置的一个高阶函数。<code>reduce()</code>函数接收的参数和 <code>map()</code>类似，一个函数 f，一个list，但行为和 <code>map()</code>不同，<code>reduce()</code>传入的函数 f 必须接收两个参数，<code>reduce()</code>对list的每个元素反复调用函数f，并返回最终结果值。

例如，编写一个f函数，接收x和y，返回x和y的和：

        def f(x, y):
            return x + y

调用 <code>reduce(f, [1, 3, 5, 7, 9])</code>时，reduce函数将做如下计算：

        先计算头两个元素：f(1, 3)，结果为4；
        再把结果和第3个元素计算：f(4, 5)，结果为9；
        再把结果和第4个元素计算：f(9, 7)，结果为16；
        再把结果和第5个元素计算：f(16, 9)，结果为25；
        由于没有更多的元素了，计算结束，返回结果25。
        上述计算实际上是对 list 的所有元素求和。虽然Python内置了求和函数sum()，但是，利用reduce()求和也很简单。

<code>reduce()</code>还可以接收第3个可选参数，作为计算的初始值。如果把初始值设为100，计算：

        reduce(f, [1, 3, 5, 7, 9], 100)

结果将变为125，因为第一轮计算是：

计算初始值和第一个元素：f(100, 1)，结果为101。
