import urllib.request,time

def get_price(code):
        url = "http://hq.sinajs.cn/?list=%s" % code
        req = urllib.request.Request(url)
#如果不需要设置代理，下面的set_proxy就不用调用了。由于公司网络要代理才能连接外网，所以这里有set_proxy…
        #req.set_proxy("proxy.XXX.com:911", "http")
        content = urllib.request.urlopen(req).read()
        str = content.decode('gbk')
        data = str.split('"')[1].split(',')
        name = "%-6s" % data[0]
        price_current = "%-6s" % float(data[3])
        open_price = "%-6s" % float(data[1])
        close_price = "%-6s"% float(data[2])
        change_percent = ( float(data[3]) - float(data[2]) )*100 / float(data[2])
        change_percent = "%-6s" % round (change_percent, 2)
        #print("股票名称:{0} 最新价:{1} 涨跌幅：{2} 今日开盘价:{3} 昨日收盘价:{4}".format(name, price_current,change_percent,open_price, close_price) )
        return name,price_current,change_percent,open_price,close_price
    
def get_all_price(code_list):
    for code in code_list:
        get_price(code)





n=0
#code_list = ['sh600030','sh601001','sh601006']
#get_all_price(code_list)

ntime = float(input("Input refresh interval in seconds: \n"))
#ntime = 3

while n==0:
        code = input("Input stock code: (eg. sh601006) \n")
        try:
                print("\n","股票名称：",get_price(code)[0],"\n")
                print("时间\t","当前价格","涨跌幅")
                n=1
                
        except IndexError:
                print("Stock code doesn't exist")


while True:
        stock = get_price(code)
        local_t = time.strftime('%X',time.localtime())
        print(local_t, stock[1],stock[2])
        time.sleep(ntime)



