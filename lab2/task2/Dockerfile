FROM python

WORKDIR "."

COPY ["container_CLI.py", "./"]
COPY ["container.py", "./"]
COPY ["main.py", "./"]
COPY ["data.txt", "./"]

ENTRYPOINT ["python", "main.py"]