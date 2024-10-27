#!/bin/bash

APP_DATABASE_PORT=${APP_DATABASE_PORT:=5432}

case ${1} in

noop)
  exec tail -f /dev/null
  ;;

shell)
  /bin/bash
  ;;

init)
  python -m manage migrate
  ;;

runserver)
  python -m manage runserver 0.0.0.0:80
  ;;

app)
  python -m daphne -b 0.0.0.0 -p 80 "project.asgi:application"
  ;;

*)
  echo "$@"
  exec "$@"
  ;;

esac
