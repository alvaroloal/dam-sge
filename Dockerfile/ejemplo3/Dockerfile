FROM httpd:2.4-alpine
LABEL maintainer="lorente.alalv24"
RUN apk add git
RUN git clone https://github.com/alvaroloal/alvaroloal.github.io /usr/local/apache2/htdocs/web
WORKDIR ./web
RUN mv ./* /usr/local/apache2/htdocs/


