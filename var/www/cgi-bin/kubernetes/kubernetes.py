#!/usr/bin/python3
import cgi
import subprocess
import time


print("content-type: text/html")
print()


f = cgi.FieldStorage()
key = f.getvalue("key")
cmd1 = f.getvalue("x")
cmd2 = f.getvalue("y")

# print(key, cmd1, cmd2)


if key=="Pod/Deployment":
	run = "kubectl get pods --kubeconfig /root/Kubernetes/admin.conf"

elif key=="Services":
	run = "kubectl get svc --kubeconfig /root/Kubernetes/admin.conf"

elif key=="launchpod":
	run = "kubectl run {} --image={} --kubeconfig /root/Kubernetes/admin.conf".format(cmd1,cmd2)

elif key=="podDeployment":
	run = "kubectl create deployment {} --image={} --kubeconfig /root/Kubernetes/admin.conf".format(cmd1,cmd2)

elif key=="scaleReplica":
	run = "kubectl scale deployment {} --replicas={} --kubeconfig /root/Kubernetes/admin.conf".format(cmd1,cmd2)

elif key=="portNumber":
	temp = subprocess.getoutput("sudo kubectl expose deployment {} --port={} --type=NodePort --kubeconfig /root/Kubernetes/admin.conf".format(cmd1, cmd2))

	time.sleep(1)
	run = "kubectl get svc --kubeconfig /root/Kubernetes/admin.conf"

elif key=="freeResource":
	run = "kubectl delete service {} --kubeconfig /root/Kubernetes/admin.conf".format(cmd1)

elif key=="delEnv":
	if cmd1=="Pod":
		run = "kubectl delete pod {} --kubeconfig /root/Kubernetes/admin.conf".format(cmd2)
	else:
		run = "kubectl delete deployments {} --kubeconfig /root/Kubernetes/admin.conf".format(cmd2)

else:
	run = "sudo echo Something wrong"
	
o = subprocess.getoutput("sudo " + run)
print(o)

