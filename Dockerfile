ARG         base=python:3.12.1-alpine

###

FROM        ${base}

ARG         version=

ENV         PYYAML_FORCE_LIBYAML=1
ENV         PYYAML_FORCE_CYTHON=1

ENTRYPOINT  ["jinja2"]

RUN         apk add --no-cache --virtual .build-deps \
                build-base \
                yaml-dev && \
            pip install \
                jinja2==${version} \
                jinja2-cli[yaml,toml,xml]==0.8.2 && \
            apk del .build-deps
