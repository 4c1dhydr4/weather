# Weather API

_Repositorio del proyecto Weather API.._

## Contexto
El objetivo de esta proyecto es generar una API Rest sencilla para la gestión de records de clima para diferentes ciuidades.

## Instalación
Se requiere instalar las dependencias descritas en requirements.txt
Se requiere una instancia de PostgreSQL en el puerto 5432 con credenciales básicas (actualizar en settings.py) y una base de datos con nombre weather.
Se requiere una instancia de Redis en escucha en el puerto 6379
Se puede utilizar database.backup para restaurar la base de datos con datos iniciales o utilizar la base de datos desde cero aplicando las migraciones.

## Uso
* Una vez desplegado, en el home se observarán los datos del clima de las ciudades almacenadas en la base de datos.
* Se puede utilizar tanto el home principal a travez del navegador como la URL /api/v1/city/ como un endpoint de gestión de las ciudades y los registros del clima. 
* Para testear la capa channels para websockets puedes acceder a /websocket y testear un websocket básico para actualizaciones del clima en tiempo real.

## Stack

* [Django 4.1.2](https://docs.djangoproject.com/en/4.1/releases/4.1/) como framework de desarrollo web. 
* [PostgreSQL 14](https://www.postgresql.org/) como Base de Datos.
* [Django RestFramework](https://www.django-rest-framework.org/) como framework de desarrollo de la API del proyecto. 
* [Redis](https://redis.io/) como Base de Datos para manejo de Channels
* [Django Channels](https://channels.readthedocs.io/en/stable/) como async backend para Websockets.
* [JavaScript](https://www.javascript.com/) como lenguaje de scripting para la lógica e interacción lado del cliente.

Autor: [Luis Quiroz Burga](https://github.com/4c1dhydr4)