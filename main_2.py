import subprocess

subprocess.call('sudo ifconfig enp4s0 down', shell=True)
subprocess.call('sudo ifconfig enp4s0 hw ether 00:11:22:33:44:55', shell=True)
subprocess.call('sudo ifconfig enp4s0 up', shell=True)
