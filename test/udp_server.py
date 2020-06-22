import time
import socket
import logging

SENDERIP = '127.0.0.1'
MYPORT = 1234
MYGROUP = '224.1.1.1'

logging.basicConfig(filename='server.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)


def receiver():
    # 创建udp 链接
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    # 允许多个套接字使用相同的端口号
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定到我们知道将接收多播数据的端口
    sock.bind((SENDERIP, MYPORT))
    # 告诉内核我们是一个多播套接字
    # sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
    # 告诉内核我们要将自己添加到多播组中＃该多播组的地址是第三个参数
    status = sock.setsockopt(socket.IPPROTO_IP,
                             socket.IP_ADD_MEMBERSHIP,
                             socket.inet_aton(MYGROUP) + socket.inet_aton(SENDERIP))

    sock.setblocking(False)
    #     # ts = time.time()
    while 1:
        try:
            data, addr = sock.recvfrom(1024)
            print("Receive data!")
            print('DATA', data)
            print("FROM: ", addr)
            time_a = time.localtime(time.time())
            print("TIME:", time.strftime("%Y-%m-%d %H:%M:%S", time_a))
            print("" + "{}".format(data.decode()))
            status = data.decode()  # [ 100 sys tfp ]
            a = status.split(" ")
            print(a[1:-1])  # ['[', '100', 'sys', 'tfp', ']']
            status_a = {}
            if int(a[1:-1][0]) < 100:
                status_a['puma'] = 'Not Started'
                status_a['engine'] = '停机'
                status_a['client'] = '断开'
            # print(puma)
            if int(a[1:-1][0]) == 100:
                status_a['puma'] = 'Monitor'
                status_a['engine'] = '停机'
                status_a['client'] = '连接'
                log = a[1:-1][1]+';'+a[1:-1][2]
                logging.info(log)

            if 100 <= int(a[1:-1][0]) and int(a[1:-1][0]) < 200:
                status_a['puma'] = 'Monitor'
                status_a['engine'] = '停机'
                status_a['client'] = '连接'
            if int(a[1:-1][0]) ==200:
                status_a['puma'] ='Manual'
                Dyno = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                status_a['Dyno'] ='启动'
                status_a['engine'] ='停机'
                log = a[1:-1][1]+ ';'+a[1:-1][2]+";"+Dyno
                logging.info(log)
                status_a['client'] = '连接'
            if int(a[1:-1][0])>=200 and int(a[1:-1][0])<500:
                dyno_on = time.time()
                status_a['puma'] = 'Manual'
                status_a['Dyno'] = dyno_on
                status_a['engine'] = '停机'
                status_a['client'] = '连接'
                logging.info('测功机上电')
                '''
                发动机时间/dyno 运行时间  （需要确认）
                将累计时间积分油耗按指定的间隔写入日志文件
                
                '''
                for idx,SPEED in enumerate(a[1:-1]):
                    print(idx,SPEED)
                    if int(SPEED) > 500:
                        status_a['engine'] = '启动'
                        status_a['engine_time'] = '启动'
                        status_a['oil_'] = '启动'
                        logging.info('发动机启动')
                        status_a['client'] = '连接'
                        logging.info('自动累计时间记录')
                    if int(SPEED) <200:
                        logging.info('发动机停机')
                        status_a['engine_time'] = '停止'
                        status_a['oil_'] = '停止'
                        logging.info('发动机停止时间'+';'+'积分油耗')
                        status_a['client'] = '连接'
            if int(a[1:-1][0]) == 500:
                logging.info('自动试验循环启动')
                status_a['puma'] = 'Automatic Testrun is Running'
            if int(a[1:-1][0]) == 520:
                logging.info('自动试验循环结束')
                status_a['puma'] = 'Automatic Testrun Finished'

            if int(a[1:-1][0])<200:
                status_a['puma'] = 'Monitor'
                status_a['Dyno'] = '停止'
                status_a['engine'] = '停机'
                logging.info('测功机停止运行')
                logging.info('累计时间')

























        except socket.error as e:
            pass


if __name__ == "__main__":
    receiver()
