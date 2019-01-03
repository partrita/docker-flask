FROM debian:stretch-slim

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
    python3-pip python3-dev uwsgi-plugin-python \
    nginx supervisor

COPY nginx/flask.conf /etc/nginx/sites-available/
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY app /var/www/app

COPY app/Pipfile .
COPY app/Pipfile.lock .
# copy over our requirements.txt file
COPY app/requirements.txt /tmp/

RUN mkdir -p /var/log/nginx/app /var/log/uwsgi/app /var/log/supervisor \
    && rm /etc/nginx/sites-enabled/default \
    && ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf \
    && echo "daemon off;" >> /etc/nginx/nginx.conf \
    # upgrade pip and install required python packages
    # && pip install -U pip \
    && pip3 install -r /tmp/requirements.txt \
    # Due to pipenv bug
    # &&  pip install pipenv \
    # &&  pipenv install --system \
    && chown -R www-data:www-data /var/www/app \
    && chown -R www-data:www-data /var/log


CMD ["/usr/bin/supervisord"]
