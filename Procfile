release: cd ./meaao && python ./manage.py migrate --noinput
web: cd ./meaao && waitress-serve --port=$PORT meaao.wsgi:application
web-local: cd meaao && python ./manage.py collectstatic --noinput && waitress-serve --port=8000 meaao.wsgi:application