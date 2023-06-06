FROM python

WORKDIR "."

COPY ["containerCLI.py", "./"]
COPY ["container.py", "./"]
COPY ["main.py", "./"]
COPY ["data.txt", "./"]

ENTRYPOINT ["python", "main.py"]