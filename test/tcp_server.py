import socket,json,time
import logging
logging.basicConfig(filename='translator.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)

# 创建socket
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 本地信息
address = ('127.0.0.1', 7788)

# 绑定
tcp_server_socket.bind(address)


# 设置监听
# 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
# 128:表示最大等待连接数
tcp_server_socket.listen(128)

# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
# client_socket用来为这个客户端服务
# tcp_server_socket就可以省下来专门等待其他新客户端的链接
while 1:
    client_socket, clientAddr = tcp_server_socket.accept()

    # 接收对方发送过来的数据
    recv_data = client_socket.recv(4096)  # 接收1024个字节
    j_recv_data = json.loads(recv_data)
    print('接收到的数据为:',j_recv_data)  # {'data': '[ 100 sys tfp ]', 'Dyno': 1587431294.8837473, 'engine': 1587431294.8837473}
    # time_a = time.localtime(time.time())
    # TIME = time.strftime("%Y-%m-%d %H:%M:%S", time_a)
    # print("TIME:", TIME)
    a = j_recv_data.split(" ")
    print(a[1:-1])
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
        log = a[1:-1][1] + ';' + a[1:-1][2]
        logging.info(log)

    if 100 <= int(a[1:-1][0]) and int(a[1:-1][0]) < 200:
        status_a['puma'] = 'Monitor'
        status_a['engine'] = '停机'
        status_a['client'] = '连接'
    if int(a[1:-1][0]) == 200:
        status_a['puma'] = 'Manual'
        Dyno = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        status_a['Dyno'] = '启动'
        status_a['engine'] = '停机'
        log = a[1:-1][1] + ';' + a[1:-1][2] + ";" + Dyno
        logging.info(log)
        status_a['client'] = '连接'
    if int(a[1:-1][0]) >= 200 and int(a[1:-1][0]) < 500:
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
        for idx, SPEED in enumerate(a[1:-1]):
            print(idx, SPEED)
            if int(SPEED) > 500:
                status_a['engine'] = '启动'
                status_a['engine_time'] = '启动'
                status_a['oil_'] = '启动'
                logging.info('发动机启动')
                status_a['client'] = '连接'
                logging.info('自动累计时间记录')
            if int(SPEED) < 200:
                logging.info('发动机停机')
                status_a['engine_time'] = '停止'
                status_a['oil_'] = '停止'
                logging.info('发动机停止时间' + ';' + '积分油耗')
                status_a['client'] = '连接'
    if int(a[1:-1][0]) == 500:
        logging.info('自动试验循环启动')
        status_a['puma'] = 'Automatic Testrun is Running'
    if int(a[1:-1][0]) == 520:
        logging.info('自动试验循环结束')
        status_a['puma'] = 'Automatic Testrun Finished'

    if int(a[1:-1][0]) < 200:
        status_a['puma'] = 'Monitor'
        status_a['Dyno'] = '停止'
        status_a['engine'] = '停机'
        logging.info('测功机停止运行')
        logging.info('累计时间')

        # 发送一些数据到客户端
        client_socket.send("接收成功!".encode('gbk'))

        # 关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
    # client_socket.close()