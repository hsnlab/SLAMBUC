FROM python:3.14-alpine
LABEL maintainer="czentye@tmit.bme.hu"
WORKDIR /usr/src/slambuc
ENV PYTHONUNBUFFERED=1 PIP_ROOT_USER_ACTION=ignore
RUN apk add glpk
ENV SLAMBUC_PULP_SOLVER=glpk
COPY ./ ./
RUN pip3 install --no-cache-dir -e .
ENTRYPOINT ["slambuc"]