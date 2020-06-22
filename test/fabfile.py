from fabric import  Connection

host_ip = '172.168.10.225'
user_name = 'root'
password = '1234qwer!@#'
cmd = 'date' # 服务器时间命令

con = Connection(host_ip, user_name, connect_kwargs={'password': password})
print(con)
result = con.run(cmd, hide=True)
# print(result.stdout)
print(result.connection.host)
con.put('mantisbt-2.24.1.zip','/root/mantisBT')