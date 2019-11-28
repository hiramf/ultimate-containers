FROM python:3.7-slim-buster AS base

# set work directory
WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/
RUN pip install -r /usr/src/app/requirements.txt

FROM base

# copy project
COPY . /usr/src/app/

# Add Tini
ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

EXPOSE 8050

ENTRYPOINT ["/tini", "-g", "--"]
CMD ["python", "app.py"]