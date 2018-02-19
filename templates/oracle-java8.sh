#!/usr/bin/env bash

wget -N \
"https://s3.amazonaws.com/datapassport-lib/jdk-8u144-linux-x64.rpm"

sudo rpm -Uvh jdk-8u144-linux-x64.rpm

sudo alternatives --install /usr/bin/java java /usr/java/jdk1.8.0/jre/bin/java 20000
sudo alternatives --install /usr/bin/jar jar /usr/java/jdk1.8.0/bin/jar 20000
sudo alternatives --install /usr/bin/javac javac /usr/java/jdk1.8.0/bin/javac 20000
sudo alternatives --install /usr/bin/javaws javaws /usr/java/jdk1.8.0/jre/bin/javaws 20000
