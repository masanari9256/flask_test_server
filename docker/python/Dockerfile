FROM python:3.11.7

WORKDIR /var/www/app

COPY app /var/www/app

RUN pip install -U pip \
    && pip install --no-cache-dir -r /var/www/app/config/requirements.txt

CMD ["python", "app.py"]
