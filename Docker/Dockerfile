FROM centos

RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
      && yum --enablerepo=extras install -y epel-release \
      && yum install -y python3-pip \
      && yum install -y yum-utils \
      && pip3 install flask

COPY . .

#EXPOSE 8081

#WORKDIR /src

RUN chmod u+x hello_world.py

ENTRYPOINT ["python3"]
CMD ["hello_world.py"]
