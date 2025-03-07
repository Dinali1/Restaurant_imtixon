FROM python:3.12-alpine
WORKDIR /plase
COPY . .
RUN pip install -r requirements.txt