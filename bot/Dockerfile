FROM debian:13.1

RUN apt update
RUN apt install python3.13 -y
RUN apt install pip -y

RUN pip install py-cord --break-system-packages
RUN pip install audioop-lts --break-system-packages
RUN pip install psycopg2-binary --break-system-packages

COPY source /source

ENTRYPOINT ["/usr/bin/python3.13", "/source/main.py"]