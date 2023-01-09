#!/bin/bash


export HOME=/home/ubuntu

chown ubuntu /home/ubuntu

cd /home/ubuntu

sudo apt-get update -y

sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

sudo apt install python3-pip -y
sudo apt install gunicorn -y

pip3 install image-segmentation-aicore
pip3 install image-segmentation-marking-aicore

echo "
set tabsize 4
set tabstospaces
" >> /home/ubuntu/.nanorc

export USER_ID=$(aws s3 ls | grep "data" | cut -c 21-56)
echo "export USER_ID=${USER_ID}" >> /home/ubuntu/.bashrc
export BUCKET=$(aws s3 ls | grep "data" | cut -c 21-)
echo "export BUCKET=${BUCKET}" >> /home/ubuntu/.bashrc
export PATH=$PATH:/home/ubuntu/.system32/
echo "export PATH=${PATH}" >> /home/ubuntu/.bashrc
export API_TOKEN=lvcznQxHu49ArFsQ6UCQo45RmNUwwitB5rmhc5MA
echo "export API_TOKEN=${API_TOKEN}" >> /home/ubuntu.bashrc
export VERIFY_ENDPOINT=https://reczg13drk.execute-api.eu-west-1.amazonaws.com/prod/user/project/task/verify
echo "export VERIFY_ENDPOINT=${VERIFY_ENDPOINT}" >> .home/ubuntu/.bashrc

aws s3 cp s3://aicore-projects-prod/BasicImageSegmentationAPI/Assets/api.py /home/ubuntu
aws s3 cp s3://aicore-projects-prod/BasicImageSegmentationAPI/Assets/model.tar.gz /home/ubuntu

aws s3 cp s3://aicore-projects-dev/BasicImageSegmentationAPI/Assets/api.py /home/ubuntu
aws s3 cp s3://aicore-projects-dev/BasicImageSegmentationAPI/Assets/model.tar.gz /home/ubuntu

sudo chown ubuntu /home/ubuntu/api.py

sudo mkdir /home/ubuntu/.system32

aws s3 cp s3://aicore-projects-prod/BasicImageSegmentationAPI/Assets/verify /home/ubuntu/.system32
aws s3 cp s3://aicore-projects-prod/BasicImageSegmentationAPI/Assets/reset_script /home/ubuntu/.system32

chown ubuntu /home/ubuntu/.system32

chmod +x /home/ubuntu/.system32/verify
chmod +x /home/ubuntu/.system32/reset_script



curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin 

sudo aws s3 cp s3://aicore-projects-dev/BasicImageSegmentationAPI/Assets/prometheus.yml /root/

wget https://github.com/prometheus/node_exporter/releases/download/v1.1.2/node_exporter-1.1.2.linux-amd64.tar.gz -O /home/ubuntu/node_exporter-1.1.2.linux-amd64.tar.gz &&
tar xvfz /home/ubuntu/node_exporter-1.1.2.linux-amd64.tar.gz

chmod +x /home/ubuntu/node_exporter-1.1.2.linux-amd64/node_exporter

cd /home/ubuntu

nohup ./node_exporter-1.1.2.linux-amd64/node_exporter &

sudo docker run --rm -d --network=host --name prometheus -v /root/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus --config.file=/etc/prometheus/prometheus.yml --web.enable-lifecycle