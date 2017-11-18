# start with the official Composer image and name it
FROM composer:1.5.2 AS build

ENV COMPOSER_ALLOW_SUPERUSER 1

ADD . /app
WORKDIR /app

RUN composer install


# Use apache alpine version to serve
FROM php:{{ version }}-apache-jessie

WORKDIR /var/www/html/


COPY . /var/www/html/app

RUN chown -R www-data:www-data /var/www/html/app

COPY --from=build /app/vendor  /var/www/html/app/vendor