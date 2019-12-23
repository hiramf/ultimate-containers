FROM python:3.7-slim-buster as base

# set work directory
WORKDIR /usr/src/dash

ENV TINI_VERSION v0.18.0

# Install requirements
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt \
    && chmod +x /tini

FROM base

# copy project
COPY . /usr/src/dash

EXPOSE 8050

ENTRYPOINT ["/tini", "-g", "--"]
CMD ["python", "app.py"]