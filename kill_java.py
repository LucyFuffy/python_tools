import xml.etree.ElementTree as ET
import os
from xml.etree.ElementTree import Element

def kill_port(port):
    """根据端口号杀死对应的进程"""
    # 根据端口号查询pid
    find_port = 'netstat -aon | findstr %s' % port
    # 执行cmd命令 返回对象
    result = os.popen(find_port)
    # 读取返回结果
    text = result.read()
    print(f'端口:{port}占用情况：')
    print(text)
    # 提取pid
    text = [i.split(' ') for i in text.split('\n') if i]
    pids = []
    for i in text:
        pid = [u for u in i if u]
        if str(port) in pid[1]:
            pids.append(pid[-1])
    pids = list(set(pids))#set可以消除重复端口
    print(f'{pids}')
    # 杀死占用端口的pid
    for pid in pids:
        find_kill = 'taskkill -f -pid  %s ' % pid
        print(f'{find_kill}')
        result = os.popen(find_kill)
        print(result.read())

tree = ET.parse("conf\server.xml")
root = tree.getroot()
port = "" #端口
for child in root:
    if('Service'==(child.tag)):#先找到最外层的tag中为Service
    	for i in child:
    		  if('Connector'==(i.tag)):#Connector的子tag
    		  		port = i.attrib['port'] #找出所有Connector的port,并杀死

if "" != port: #端口如果不为空，则
	kill_port(port)
