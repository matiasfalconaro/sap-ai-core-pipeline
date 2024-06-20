# Specify which base layers (default dependencies) to use
# You may find more base layers at https://hub.docker.com/
FROM python:3.7

# Creates directory within your Docker image
RUN mkdir -p /app/src/

# Copies file from your Local system TO path in Docker image
COPY main.py /app/src/
COPY requirements.txt /app/src/

# Installs dependencies within you Docker image
RUN pip3 install -r /app/src/requirements.txt

# Enable permission to execute anything inside the folder app
RUN chgrp -R 65534 /app && \
    chmod -R 777 /app

# not specify the command to run the script main.py in the Dockerfile.
# This command will be written into the AI workflow and is covered later in this tutorial.
# ENTRYPOINT ["sh", "-c"]
# CMD ["python /app/src/main.py"]
