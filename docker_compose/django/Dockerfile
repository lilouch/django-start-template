# ./sentive_saas/Dockerfile
FROM python:3.8-slim

ENV APP_ROOT /app
ENV CONFIG_ROOT /config

RUN mkdir ${CONFIG_ROOT}
COPY requirements.txt ${CONFIG_ROOT}/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ${CONFIG_ROOT}/requirements.txt

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}

#Expose the container to other service internally but not outside docker
EXPOSE 8000

# copy project
ADD . ${APP_ROOT}
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "sentive_saas.wsgi:application"]
