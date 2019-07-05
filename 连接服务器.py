import paramiko

cmdstr = ["ifconfig" ]
def ssh_docker(ip, user, passwd, cmd):#连接容器
    out_res=''
    ssh1 = paramiko.SSHClient()
    ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh1.connect(ip,22,user, passwd, timeout=5)
        # time.sleep(5)
    except Exception as e:
        print(e)
    for m in cmd:
        print(m)
        stdin, stdout, stderr = ssh1.exec_command(m)
        out_res=stdout.readlines()
    ssh1.close()
    print(out_res)


ssh_docker("192.168.73.148","itcast","20150101",cmdstr)