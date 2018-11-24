import requests

proxy_host='http-dyn.abuyun.com'#动态版HTTP隧道服务器地址
proxy_port='9020'#端口号

#这是你购买之后代理商提供给你的验证信息
proxy_user='HA4J68562OTMV1AD'#通行证书
proxy_pass='7C459C6A5616F197'#通行密钥

proxy_meta='http://%(user)s:%(pass)s@%(host)s:%(port)s'%{
    'host':proxy_host,
    'port':proxy_port,
    'user':proxy_user,
    'pass':proxy_pass,
}
proxies={
    'http':proxy_meta,
    'https':proxy_meta,
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                 ' Chrome/70.0.3538.102 Safari/537.36'
}

url='http://httpbin.org/get'#这连接可返回请求的信息

r=requests.get(url,headers=headers,proxies=proxies)
print(proxies)
print(r.url)
print(r.status_code)
print(r.text)#返回信息里的origin就是代理的ip的地址，反复运行代码后发现ip会改变

#无须切换IP，每一个请求从IP池中挑选一个随机IP，有并发请求限制，默认每秒只允许 5 个请求。如果需要更多请求数，需要额外购买
#阿布云在云端维护一个全局 IP池 供 HTTP隧道 使用，池中的 IP 会不间断更新，以保证 IP池 中有足够多的 IP ，但是
#IP池中有一些IP可能会在当天重复出现多次。