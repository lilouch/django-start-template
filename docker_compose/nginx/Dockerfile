FROM nginx:1.17
RUN rm /etc/nginx/conf.d/default.conf
COPY local.conf /etc/nginx/conf.d
RUN mkdir /etc/nginx/conf.d/certs
COPY docker.crt /etc/nginx/conf.d/certs
COPY docker.key /etc/nginx/conf.d/certs
COPY timeout.conf /etc/nginx/conf.d
EXPOSE 80
