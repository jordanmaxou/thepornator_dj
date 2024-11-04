########################################################################################
FROM python:3.11-buster AS builder-base
WORKDIR /home

RUN pip install pip --upgrade

COPY ./requirements.txt .
RUN pip install -r requirements.txt

########################################################################################
FROM python:3.11-slim-buster AS production

RUN DEBIAN_FRONTEND=noninteractive\
    && apt-get update \
    && apt-get install --no-install-recommends -y gettext libmariadbclient-dev \
    && apt-get clean autoclean \
    && apt-get autoremove --yes \
    && rm -rf /var/lib/apt/lists/* /var/cache/debconf/templates.*

COPY --from=builder-base /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=builder-base /usr/local/bin/ /usr/local/bin/

COPY entrypoint.sh /usr/sbin/entrypoint.sh

WORKDIR /home
COPY . .

RUN python manage.py compilemessages

ENTRYPOINT ["/usr/sbin/entrypoint.sh"]
CMD ["app"]

########################################################################################
FROM production AS development
CMD ["noop"]
