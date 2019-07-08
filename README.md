# ApiForPython
基于Python3语言接口自动化测试

# 介绍
## 环境准备
- Pyhton3
- requests
- unittest
- ddt
- xlrd
- BeautifulReport

## 实现功能
- requests封装请求
- Excel管理测试数据, xlrd读取Excel文件
- unittest + ddt数据驱动模式执行
- BeautifulReport生成可视化html报告

## 项目结构
ApiForPython

    |-- config 配置文件
    
    |-- excel_file 存放excel文件
    
    |-- report 存放报告文件
    
    |---- logs 存放日志文件
    
    |-- test_case 存放测试用例
    
    |-- utils 存放封装代码
    
    |---- checkPointUtils.py 通过jsonpath提取校验的值
    
    |---- excelUtils.py 读写excel文件
    
    |---- logger.py 日志输出
    
    |---- read_ini.py 读取配置文件
    
    |---- requestsUtils.py 封装请求
    
    |-- run_main.py 执行文件
    
## http协议简介
### 什么是http
- 1.HTTP协议是Hyper Text Transfer Protocol（超文本传输协议）的缩写,是用于从万维网（WWW:World Wide Web ）服务器传输超文本到本地浏览器的传送协议。
- 2.HTTP（HyperText Transfer Protocol）协议是基于TCP的应用层协议，它不关心数据传输的细节，主要是用来规定客户端和服务端的数据传输格式，最初是用来向客户端传输HTML页面的内容。默认端口是80
- 3.http（超文本传输协议）是一个基于请求与响应模式的、无状态的、应用层的协议
### 请求报文
HTTP请求报文主要由请求行、请求头部、空一行、请求正文4部分组成
![请求报文](http://m.qpic.cn/psb?/V12A7VgS03zLND/xzi9XB0b9p248xC3Lo3i*jGy1btUz*qZ4.SSjqDRbCg!/b/dLgAAAAAAAAA&bo=JASGAQAAAAADB4U!&rf=viewer_4 "请求报文")


#### 请求行
请求行有三个主要参数：请求方法、url、协议版本

请求方法包含：
- get 请求指定的页面信息，并返回实体主体。 
- post 向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。
- HEAD 类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头 
- OPTIONS 返回服务器针对特定资源所支持的HTTP请求方法，也可以利用向web服务器发送‘*’的请求来测试服务器的功能性
- PUT 向指定资源位置上传其最新内容
- DELETE 请求服务器删除Request-URL所标识的资源
- TRACE 回显服务器收到的请求，主要用于测试或诊断
- CONNECT HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器

**注意：**
- 方法名称是区分大小写的。
- 最常见的的就是通常说的get和post方法。

#### url详解
一个完整的url地址，基本格式如下：

https://host:port/path?xxx=aaa&ooo=bbb

- --http/https：这个是协议类型
- --host:服务器的IP地址或者域名
- --port:HTTP服务器的默认端口是80，这种情况下端口号可以省略
    如果使用了别的端口，必须指明，例如：192.168.3.111:8080，这里的8080就是端口
- --path:访问资源的路径,如图中3所示/s (图中3是把path和请求参数放一起了)
- --？:url里面的？这个符号是个分割线，用来区分问号前面的是path，问号后面的是参数
- --url-params:问号后面的是请求参数，格式：xxx=aaa，如图4区域就是请求参数
- --&：多个参数用&符号连接

#### 协议版本
根据HTTP标准，HTTP请求可以使用多种请求方法。
- HTTP1.0定义了三种请求方法： GET, POST 和 HEAD方法。
- HTTP1.1新增了五种请求方法：OPTIONS, PUT, DELETE, TRACE 和 CONNECT 方


### 响应报文
HTTP响应报文主要由状态行、消息报头、空一行、响应正文4部分组成
![响应报文](http://m.qpic.cn/psb?/V12A7VgS03zLND/*Sk.YWiZZ6Vw.fzoJ1E2AfLLKPRSUoIM6pa5X2mj7mg!/b/dD4BAAAAAAAA&bo=ygNgAQAAAAADF5o!&rf=viewer_4 "响应报文")


### 完整的http内容
一个完整的http协议其实就两块内容，一个是发的请求，一个服务端给的响应


## requests
[官网地址](http://cn.python-requests.org/zh_CN/latest/)

## 测试报告
[BeautifulReport Python Github地址](https://github.com/TesterlifeRaymond/BeautifulReport/)

![测试报告](http://m.qpic.cn/psb?/V12A7VgS03zLND/jzc2tvqeK*7qICu0AeT0a0vnER3sjfaUOAq49snW5s4!/b/dFMBAAAAAAAA&bo=Swg4BAAAAAADJ30!&rf=viewer_4 "测试报告")
![测试报告](http://m.qpic.cn/psb?/V12A7VgS03zLND/wIlhvhvNYvQEp2cbFEXV**xZkPFIvkErOzud5sPJw1w!/b/dFQBAAAAAAAA&bo=TAg4BAAAAAADRxo!&rf=viewer_4 "测试报告")



