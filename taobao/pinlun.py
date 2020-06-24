import requests

import json

from bs4 import BeautifulSoup as bs

import csv

import re

PAGE_URL = []

# 获取url
def Get_url(num):
    urlfrist= 'https://rate.tmall.com/list_detail_rate.htm?itemId=552918017887&spuId=856416229&sellerId=2455250363&order=3&currentPage='
    urllast = '&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvMvvXvcQvUvCkvvvvvjiPn2LwsjDCRscyzjYHPmPOzjlbP2cwlj1Un2cy0jtWRphvCvvvvvmCvpvWzPshceNNznswnSt4dphvmpvvnvUmv9mkgT6CvvyvCCGm%2FNyv950rvpvEvvoavSclvHdjdphvmpvhhvU9UvC81T6CvvyvvnKm40%2BvBdvtvpvhvvvvvvwCvvNwzHi4zqKMRphvCvvvvvmjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvvPvpvhvv2MMQyCvhQWPrvvCA7HyJcnR3H%2BCNL9sWAOHFXXiXVvQE01Ux8x9RLIRfU6pwet987JVcBCsb2XSfpAOH2%2BFOcn%2B3C1pJFEDaVTRogRD7zhaXTAuphvmvvv9bk5NERXkphvC99vvOCgofyCvm9vvvvvphvvvvvv98Hvpv9EvvmmvhCvmhWvvUUvphvUI9vv99CvpvkkvphvC9vhvvCvpvwCvvNwzHi4zMEVdphvmpvvcIvR292lJ86CvvyvvhpvKfyvYaJrvpvEvv2wv7C9vvTWdphvmpvvJ9bGMvC8E86CvvyvvRZmW2vvi9w%3D&needFold=0&_ksTS=1588732934471_1266&callback=jsonp1267"'
    for i in range(0,num):
        PAGE_URL.append(urlfrist+str(i+1)+urllast)
# 获取评论数据
def GetInfo(num):
    # 定义接收列表字段 用户名、评论时间、颜色分类 评论
    name = []
    auctionSku = []
    ratecontent = []
    ratedate = []
    for i in range(num):
        proxies = {
            "http": "http://117.131.235.198:8060"  # 代理ip
        }
            # 设置请求头
        headers = {
            'cookie':'cna=+WAMF857+GkCAd3ox8envKr4; lid=%E6%B7%AC%E7%82%BCzhou; enc=h8YKjDp6qPSlRgWJ6G0qvB4R87yumfmbS7woCwGiO6UMastu62dv%2B2%2F2ky4p6ckUqmWrIjgtWmwKUNZLT0YPBA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; cq=ccp%3D1; sgcookie=EFVUwSF4tq%2F4GCI2TCB6j; uc1=cookie14=UoTUMtdbGPA8mQ%3D%3D; uc3=id2=Uone9dndeRw%2FZw%3D%3D&lg2=UIHiLt3xD8xYTw%3D%3D&nk2=1y%2Bf1dk1D7Y%3D&vt3=F8dBxdGO2FQgDstR6Rk%3D; t=74222df419ee45e31b2b5c5fd62faf98; tracknick=%5Cu6DEC%5Cu70BCzhou; uc4=id4=0%40UOE0D1wKLvo%2B%2F%2FmsQwfrzpzLHF%2Fl&nk4=0%401eCbXFX%2F4GtUrO%2FyzAQ0549hLw%3D%3D; lgc=%5Cu6DEC%5Cu70BCzhou; _tb_token_=fd55f53ee78e3; cookie2=1f4ae0f56762931f91fcc3f05597a06b; pnm_cku822=098%23E1hvSQvUvbpvUvCkvvvvvjiPn2L9sjrPR2Fh0jD2PmPOAjDUPscU6jtbPFqZgjrU2QhvCvvvMM%2FivpvUphvh1NX70DeEvpvVpyUUCCAOKphv8hCvvvvvvhCvphvZvvvvp9CvpCpvvvCmyyCvHvvvvhbuphvZvvvvpKIEvpCWpnDYv8R4axWDN%2BClHdUfb369%2FX7re161EcqwaXgXaZCev0zvd3ODN5vrYPeAdcwufvDrz8TJEctl8EkxdB9aWox%2FQj7JPAx%2FaAuQDphCvvXvppvvvvvtvpvhphvvv8wCvvBvpvpZ; _m_h5_tk=c80008edccac5aa93fcebddc841935a5_1588839445835; _m_h5_tk_enc=b5cd1a92272f4a04095f21a1d0519bfb; l=eBODqXLqQpBdf-6DBOfZFurza77TTIRfguPzaNbMiT5POk1woU0fWZbmnyTeCnGVH689R3yAaP02BlTepyd4XOTlR_BkdlPq3dC..; isg=BLm5XWoFwxunmp-uzk5waJNcyCWTxq14umyJLdvubuBNYtj0IxcrSB2w4GaUWkWw',
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'referer':'https://detail.tmall.com/item.htm?spm=a230r.1.14.1.55a84b1721XG00&id=552918017887&ns=1&abbucket=17',
            "accept": "*/*",
            'accept-encoding':'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8'
        }
        # 解析js 内容
        content = requests.get(PAGE_URL[i],headers = headers,proxies = proxies).text
        dk = re.findall('"displayUserNick":"(.*?)"',content)
        name.extend(dk)
        print('dk',dk)
        auctionSku.extend(re.findall('"auctionSku":"(.*?)"',content))
        ratecontent.extend(re.findall('"rateContent":"(.*?)"',content))
        ratedate.extend(re.findall('"rateDate":"(.*?)"',content))
        # 通过内容提取的内容输出
    for i in list(range(0,len(name))):
        text = ','.join((name[i],ratedate[i],auctionSku[i],ratecontent[i]))+'\n'

        with open(r'./content.txt','a+',encoding='UTF-8') as file:
            file.write(text+' ')
            print(i+1,'写入成功')

# 主函数
if __name__ == '__main__':
    Page_Num = 20
    Get_url(Page_Num)
    GetInfo(20)







