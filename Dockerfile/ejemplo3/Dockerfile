FROM httpd:2.4-alpine
LABEL maintainer="lorente.alalv24@triana.salesianos.edu"
LABEL version="3.0"
RUN apk add git
WORKDIR /web
RUN git clone https://github.com/alvaroloal/alvaroloal.github.io /usr/local/apache2/htdocs/web
RUN mv ./* /usr/local/apache2/htdocs/








