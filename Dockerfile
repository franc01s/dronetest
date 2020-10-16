FROM python:3.7-alpine

LABEL maintainer="François Egger <francois.egger@swatchgroup.com>"

# copy over our requirements.txt file
COPY requirements.txt /tmp/


# upgrade pip and install required python packages
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

# copy over our app code
COPY ./  /app/

WORKDIR /app

CMD ["gunicorn", "-w 1", "-b 0.0.0.0:5000" , "--forwarded-allow-ips='*'","run:app"]
#CMD ["tail", "-f", "/dev/null"]
