#coding:utf-8

import subprocess
import re
from time import sleep

def exe_adb_cmd(cmd):
	'''执行adb命令，返回执行结果list'''
	p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	return p.stdout.readlines()	

def get_uid():
	'''获取设备的uid，方便获取流量'''
	cmd="adb shell ps | findstr com.fcuh.consumer"
	stdout = exe_adb_cmd(cmd)
	if stdout[0].split()[0]:
		m = re.match(r'^u0_a(\d+)$',stdout[0].split()[0])
		if m:
			return int(m.group(1))+10000;
	else:
		print "APP uid not exist!"
		#retval = p.wait()

def get_throughput(cmd):
	'''获取流量'''
	return float(exe_adb_cmd(cmd)[0].replace('\r\r\n',''))

def run(m_time,interval):
	'''
	@param m_time 执行时间
	@param interval 执行间隔
	比如run(1,5)，表示执行1分钟，每5秒执行一次
	'''
	uid = str(get_uid())
	cmd_in = "adb shell cat /proc/uid_stat/" + uid + "/tcp_rcv"
	cmd_out = "adb shell cat /proc/uid_stat/" + uid +"/tcp_snd"
	#print cmd_in,cmd_out
	old_in_bytes = get_throughput(cmd_in)
	old_out_bytes = get_throughput(cmd_out)
	print "时间(s),入流量(Mb),出流量(Mb)"
	s_time = m_time * 60
	i = 0
	while i < s_time :
		sleep(interval)
		in_bytes = (get_throughput(cmd_in) - old_in_bytes)/1024/1024
		out_bytes = (get_throughput(cmd_out) - old_out_bytes)/1024/1024
		print "%d,%.3f,%.3f" %(i+interval,in_bytes,out_bytes)
		i +=interval

if __name__ == '__main__':
	#et_uid()
	#print exe_adb_cmd('adb shell cat /proc/uid_stat/10042/tcp_rcv')
	#print get_uid()
	run(1,5)
