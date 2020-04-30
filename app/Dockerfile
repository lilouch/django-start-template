# ./sentive_saas/Dockerfile
FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV APP_ROOT /app
ENV CONFIG_ROOT /config

RUN mkdir ${CONFIG_ROOT}
RUN mkdir ${APP_ROOT}

COPY requirements.txt ${CONFIG_ROOT}/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ${CONFIG_ROOT}/requirements.txt

WORKDIR ${APP_ROOT}
#Expose the container to other service internally but not outside docker
EXPOSE 8000

# copy project
ADD . ${APP_ROOT}
#CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "sentive_saas.wsgi:application"]
CMD python manage.py makemigrations;python manage.py migrate;gunicorn sentive_saas.wsgi -b 0.0.0.0:8000