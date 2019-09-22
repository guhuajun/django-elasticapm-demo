FROM python:3-alpine

WORKDIR /app/

COPY requirements.txt .

RUN pip install -r requirements.txt \
        --index-url http://mirrors.aliyun.com/pypi/simple/ \
        --trusted-host mirrors.aliyun.com

COPY /project/ .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]