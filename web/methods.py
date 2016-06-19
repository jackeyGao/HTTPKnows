# -*- coding: utf-8 -*-
'''
File Name: web/methods.py
Author: JackeyGao
mail: gaojunqi@outlook.com
Created Time: 日  6/19 20:10:21 2016
'''
methods = {
        "GET": {
            "description": "GET请求会显示请求指定的资源。一般来说GET方法应该只用于数据的读取，而不应当用于会产生副作用的非幂等的操作中。GET会方法请求指定的页面信息，并返回响应主体，GET被认为是不安全的方法，因为GET方法会被网络蜘蛛等任意的访问。",
            "section": "https://tools.ietf.org/html/rfc7231#section-4.3.1",
            "rfc": "RFC7231",
            },
        "HEAD": {
        	"description": "HEAD方法与GET方法一样，都是向服务器发出指定资源的请求。但是，服务器在响应HEAD请求时不会回传资源的内容部分，即：响应主体。这样，我们可以不传输全部内容的情况下，就可以获取服务器的响应头信息。HEAD方法常被用于客户端查看服务器的性能。",
        	"section": "https://tools.ietf.org/html/rfc7231#section-4.3.2",
        	"rfc": "RFC7231",
        	},
        "POST": {
        	"description": "POST请求会 向指定资源提交数据，请求服务器进行处理，如：表单数据提交、文件上传等，请求数据会被包含在请求体中。POST方法是非幂等的方法，因为这个请求可能会创建新的资源或/和修改现有资源。",
        	"section": "https://tools.ietf.org/html/rfc7231#section-4.3.3",
        	"rfc": "RFC7231",
        	},
        "PUT": {
        	"description": "PUT请求会身向指定资源位置上传其最新内容，PUT方法是幂等的方法。通过该方法客户端可以将指定资源的最新数据传送给服务器取代指定的资源的内容。",
        	"section": "https://tools.ietf.org/html/rfc7231#section-4.3.4",
        	"rfc": "RFC7231",
        	},
        "DELETE": {
        	"description": "DELETE请求用于请求服务器删除所请求URI（统一资源标识符，Uniform Resource Identifier）所标识的资源。DELETE请求后指定资源会被删除，DELETE方法也是幂等的。",
        	"section": "https://tools.ietf.org/html/rfc7231#section-4.3.5",
        	"rfc": "RFC7231",
        	},
        "CONNECT": {
        	"description": "CONNECT方法是HTTP/1.1协议预留的，能够将连接改为管道方式的代理服务器。通常用于SSL加密服务器的链接与非加密的HTTP代理服务器的通信。",
        	"section": "https://tools.ietf.org/html/rfc7231#section-4.3.6",
        	"rfc": "RFC7231",
        	},
        "OPTIONS": {
        	"description": "OPTIONS请求与HEAD类似，一般也是用于客户端查看服务器的性能。 这个方法会请求服务器返回该资源所支持的所有HTTP请求方法，该方法会用'*'来代替资源名称，向服务器发送OPTIONS请求，可以测试服务器功能是否正常。JavaScript的XMLHttpRequest对象进行CORS跨域资源共享时，就是使用OPTIONS方法发送嗅探请求，以判断是否有对指定资源的访问权限。 ",
        	"section": "https://tools.ietf.org/html/rfc7231#section-4.3.7",
        	"rfc": "RFC7231",
        	},
        "TRACE": {
        	"description": "TRACE请求服务器回显其收到的请求信息，该方法主要用于HTTP请求的测试或诊断。",
        	"section": "https://tools.ietf.org/html/rfc7231#section-4.3.8",
        	"rfc": "RFC7231",
        	},
        "PATCH": {
        	"description": "PATCH方法出现的较晚，它在2010年的RFC 5789标准中被定义。PATCH请求与PUT请求类似，同样用于资源的更新。",
        	"section": "https://tools.ietf.org/html/rfc5789",
        	"rfc": "RFC5789",
            }
}
