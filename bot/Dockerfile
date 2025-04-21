FROM debian:12.10

RUN apt update
RUN apt install python3.11 -y
RUN apt install pip -y

RUN pip install py-cord --break-system-packages

COPY source/main.py /source/main.py

RUN ls -la /source

ENTRYPOINT ["/usr/bin/python3.11", "/source/main.py"]