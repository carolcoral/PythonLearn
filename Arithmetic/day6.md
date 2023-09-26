# Python Learn day06

> 本章节讲解内容：

1. 文件概念

2. 文件打开方式

3. 文件读写操作

4. 文件指针

5. 文件对象属性

## 文件概念

文件：Python 中文件是对象

linux 文件：一切设备都可以看成文件。例如：磁盘文件、管道、wa 那个罗 Sockect、外设等

文件属性：用户，读、写、执行权限等

## 文件打开和读写方式

* 文件打开方法：<code>open(name[,mode[buf]])</code>

```python
        name:文件名
        mode:打开方式（只读、只写等）
        buf:缓冲 buffering的大小
```

* 文件读取方式：

```python
        read([size]):读取文件，默认读取全部，设置了 size 则读取 size 个字节
        readline([size]):读取一行
        readlines([size]):读取全部，以一行一行组成列表的形式返回
 ```       


默认读取的 size 缓存大小是8192个字节左右

也就是说但我们使用 <code>readlines([size])</code>的时候，每一次读取8192个字节，若文件的内容和8192的缓存大小接近则全部读取，若不到8192个字节则只读取文件的全部内容。

可以使用 iter 迭代器实现读取文件全部内容。推荐使用该方式访问。

```python
        # 首先打开一个文件
        f = open('python.txt','w+')
        # 然后转换成 iter 类型
        iter_f = iter(f)
        # 最后使用迭代器进行读取
        for iters in iter
            iter iter_f
        for iters in iter_f
```

* 文件写入方式：

```python
        write(str):将字符串写入文件
        writelines(sequence_of_string):写多行到文件
```

python 有写缓存的机制，因此，但我们写入内容后如果不调用 close()方法，文件是没有写入内容的。

* Python 写磁盘时机：

1. 主动调用 close()或 flush()方法，写缓存到磁盘；
2. 写入数据量大于或者等于写缓存，写缓存同步到磁盘；

## 文件关闭

* Python 中为什么需要关闭文件：

1. 将写缓存同步到磁盘；
2. linux 系统中每个进程打开文件的个数是有限制的；
3. 如果打开文件数到了系统限制，再打开文件就会失败；

* linux 系统中查看系统限制：

```shell
        >ps 查看进程
        >cat /proc/UID(进程 ID)/limite
```

## 文件指针

* Python 文件指针操作：

```python
        seek(offset[,whence]):移动文件指针；
            offset:偏移量，可以为负数
            whence:偏移相对位置
```

* Python 指针定位方式：

```python
        os.SEEK_SET:相对文件起始位置  0
        os.SEEK_CUR:相对文件当前位置  1
        os.SEEK_END:相对文件结尾位置  2
```

* <font color="red">当我们使用 seek 的时候长度超过了文本的长度就 会报错。</font>

* Python 文件属性：

1. file.fileno():文件描述符
2. file.mode:文件打开权限
3. file.encoding:文件编码格式
4. file.closed:文件是否关闭
        
* Python 标准文件：

1. sys.stdin:文件标准输入
2. sys.stdout:文件标准输出
3. sys.stderr:文件标准错误
