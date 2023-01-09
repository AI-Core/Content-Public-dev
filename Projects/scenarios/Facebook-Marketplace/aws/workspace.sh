#!/bin/bash

sudo apt install -y unzip

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" &&
unzip awscliv2.zip &&
sudo ./aws/install

VOLUME="$(aws ec2 describe-instances | \
grep "VolumeId" -m 1 | \
head -1 | \
grep -E "vol-[0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z]" -o -m 1)" \
&& aws ec2 modify-volume --size 50 --volume-id $VOLUME

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

sudo chmod 666 /var/run/docker.sock

sudo apt install docker-compose -y

cd /home/ubuntu
sudo mkdir /home/ubuntu/images

aws s3 cp s3://aicore-projects-datasets-prod/MetaMarketplaceMLEng/images/ /home/ubuntu/images --recursive

sudo mkdir /home/ubuntu/app

sudo mkdir /home/ubuntu/api

sudo growpart /dev/xvda 1

sudo resize2fs /dev/xvda1 

aws s3 cp s3://aicore-projects-prod/MetaMarketplaceMLEng/assets /home/ubuntu/api --recursive

echo 'export BUCKET_NAME="$(aws s3 ls | grep "datalake" | cut -c 21-82)"' >> /home/ubuntu/.bashrc



