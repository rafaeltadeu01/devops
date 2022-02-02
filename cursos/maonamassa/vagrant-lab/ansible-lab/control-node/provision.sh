#!/bin/bash
sudo yum -y install epel-release
echo "Inicio da instalação do ansible"
sudo yum -y install ansible
car <<EOT >> /etc/hosts
192.168.1.2 control-node
192.168.1.3 app01
192.168.1.4 db-1
EOT