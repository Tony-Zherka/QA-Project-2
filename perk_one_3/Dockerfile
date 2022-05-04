FROM python:latest
RUN apt update
RUN apt install python3-pip -y
WORKDIR /perk_one_3
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3","app.py"]