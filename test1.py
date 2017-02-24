#coding=utf-8;
#test1
#num = raw_input("now enter a number:");

#test2
#print 'doubing your number :%d' %(int(num)*2);

#test3

pystr = 'python'
print pystr[0],pystr[2:5],pystr[:2]

aDict = {"host":'earth'};
aDict['port'] = 80;
print aDict,aDict.keys();
for key,value in aDict.items():
	print key ,value;

#test4 内建函数
abs(-1)#求绝对值
coerce(12.0,12)#返回包含类型转换完毕的两个数值元素的元组
divmod(10,3) #返回地板除和取余操作的结果 元组
pow(10,3) #f返回幂次运算的结果
round(10.5) #对浮点数进行四舍五入，如果没写第二个参数，则默认返回一位小数

#python 全局变量
language = 'python';
def fool1():
	language = 'hello';
	print language; #打印hello，这是局部
def foo2():
	print language; #打印python ,这是全局
def foo3():
	global language;
	language = 'hello';
	print language ;#打印hello,全局改为hello
fool1();
foo2();
foo3();
print language;

#关键字参数和非关键字参数
def foo4(arg1,arg2,key1=1,key2=2,*arg,**keywords):
	print "arg1 parameters is ",arg1;
	print "arg2 parameters is ",arg2;
	print "key1 parameters is ",key1;
	print "key2 parameters is ",key2;#普通参数
	print "arbitrary parameters is ",arg;#非关键字参数列表
	print "keywords parameters is ",keywords;#关键字参数列表
foo4(1,2); 






