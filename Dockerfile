FROM python:latest

RUN apt-get update
RUN apt-get install -y openjdk-17-jdk

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"
