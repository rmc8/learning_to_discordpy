FROM python:3.10.1
ARG dir=/workdir
WORKDIR $dir
COPY . .
RUN pip install -U pip && \
    ls && \
    pip install --no-cache-dir -r ./requirements.txt
VOLUME $dir
CMD ["python3", "./hello_world.py"]