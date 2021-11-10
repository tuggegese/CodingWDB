FROM python:latest
WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app/"
COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt
COPY . .
EXPOSE 8080
# The -u flag is important if you want to observe the logs, otherwise python buffers the output
ENTRYPOINT [ "python3", "-u", "src/api.py" ]