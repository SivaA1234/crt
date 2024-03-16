Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=7
>>> type(a)
<class 'int'>
>>> b=7.14
>>> type(b)
<class 'float'>
>>> c='string'
>>> type(c)
<class 'str'>
>>> d=a+bi
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d=a+bi
NameError: name 'bi' is not defined. Did you mean: 'b'?
>>> d='a+bi'
>>> type(d)
<class 'str'>
>>> e=true
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    e=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> e='true'
>>> type(e)
<class 'str'>
>>> e=True
>>> type(e)
<class 'bool'>
>>> d="a+bi"
>>> type(d)
<class 'str'>
>>> d=(a+bi)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d=(a+bi)
NameError: name 'bi' is not defined. Did you mean: 'b'?
>>> d=(a+ib)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d=(a+ib)
NameError: name 'ib' is not defined. Did you mean: 'b'?
