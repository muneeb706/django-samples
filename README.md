# Django Samples

This repository contains sample implementation of different functions in django. It contains following applications

- [Convert FHIR to Parquet](https://github.com/muneeb706/django-samples/tree/main/fhir_to_parquet)
- [Execute Lua Script on Redis](https://github.com/muneeb706/django-samples/tree/main/redis_sample)
  - run redis server locally e-g using docker `docker run -p 6379:6379 --name my-redis-server redis`
  - load event data `python manage.py loaddata events`
  - run django server `python manage.py runserver`
