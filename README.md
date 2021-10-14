# trufan
Trufan project

README Notes:

Pre-requisites:
1) Have a working ansible master node installed on a AWS Ubuntu machine
2) edit the /etc/ansible/hosts of the ansible master node as following

|-----------|------------|-------------|----------------------------|
[localhost]
local
[final_server]
172.31.10.37 ansible_ssh_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa
ansible_python_interpreter=/usr/bin/python3
|-----------|------------|-------------|----------------------------|

3) From the master ansible node, run below ansible command and this creates the target AWS instances
Run sudo ansible-playbook /home/ubuntu/playbooks/create-ec2.yml -vvv

3 b) Created ssh-keygen to generate Public, private key and saved the ~/.ssh/id_rsa.pub key on to the target Ubuntu instance under /home/ubuntu/.ssh/authorized_keys
This helps the ansible master to directly talk/connect to target machine.

4) The following command needs to be executed to run the ansible playbook
ansible-playbook  ~/install_minikube.yml  -vvv
ansible-playbook  ~/install_docker.yml  -vvv
ansible-playbook  ~/install_container.yml  -vvv

install_minikube installs minikube and realted binaries, along with kubectl
install_docker installs docker and related binaries
Finally install_container will create the hello world image, creates a container, and exposes the minikube url to the internet

4) minikube service my-service, gives the exposed url
|-----------|------------|-------------|----------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL             |
|-----------|------------|-------------|----------------------------|
| default   | my-service |        5000 | http://<external_ip>:5000    |
|-----------|------------|-------------|----------------------------|

I have seen problems with the minikube in the later stages, the above end point keeps failing at times
The alternative is to expose the minikube url as a patch:
kubectl patch service my-service -p '{"spec": {"type": "LoadBalancer", "externalIPs":["<external_ip>"]}}'
