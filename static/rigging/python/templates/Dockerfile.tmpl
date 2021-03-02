# first stage
FROM python:3.8 AS builder
COPY requirements.txt .

# install dependencies to the local user directory (eg. /root/.local)
RUN pip install --user -r requirements.txt

# second unnamed stage
FROM python:3.8-slim
WORKDIR /code

# copy only the dependencies installation from the 1st stage image
COPY --from=builder /root/.local/bin /root/.local
COPY ./src .

# update PATH environment variable
ENV PATH=/root/.local:$PATH

CMD [ "python", "./server.py" ]
