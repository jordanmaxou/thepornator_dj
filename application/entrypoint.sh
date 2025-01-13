#!/bin/bash

APP_DATABASE_PORT=${APP_DATABASE_PORT:=5432}
SUPPORTED_LANGUAGES=("fr")

make_messages() {
  for lang in ${SUPPORTED_LANGUAGES[@]}; do
    echo $lang
    python -m manage makemessages --no-obsolete -l $lang --no-wrap --extension=html,txt,py,tpl,email
  done
}

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

makemessages)
  make_messages
  ;;

lint)
  ruff check --fix
  ruff format
  ;;

tests)
  python -m manage migrate
  make_messages
  python manage.py test -t . && python manage.py check --fail-level WARNING && ./check_i18n.sh
  ;;

*)
  echo "$@"
  exec "$@"
  ;;

esac
