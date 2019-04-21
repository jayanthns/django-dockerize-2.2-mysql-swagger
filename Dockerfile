# FROM python:3.6-alpine3.7 as base
FROM python:3.6-alpine3.7

# FROM base as builder

# RUN mkdir /install
# WORKDIR /install

COPY requirements.pip /requirements.pip

RUN set -ex \
    && apk add --no-cache --virtual .build-deps \
    		mariadb-dev \
            build-base \
            libffi-dev \
    && apk --update add libffi-dev gcc curl \
    && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
    && python -m venv /venv \
    && /venv/bin/pip install -U pip \
    && LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "/venv/bin/pip install --no-cache-dir -r /requirements.pip" \
    && runDeps="$( \
            scanelf --needed --nobanner --recursive /venv \
                    | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                    | sort -u \
                    | xargs -r apk info --installed \
                    | sort -u \
    )" \
    && apk add --virtual .python-rundeps $runDeps \
    && apk del .build-deps

# RUN /venv/bin/pip install -r /requirements.pip

# FROM base
# COPY --from=builder /install /usr/local

COPY . /app
WORKDIR /app

ENV DJANGO_SETTINGS_MODULE=main.settings.development

EXPOSE 8000
ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["/venv/bin/gunicorn", "--bind", ":8000", "main.wsgi:application",  "--reload"]
