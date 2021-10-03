# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.8.1-slim-buster

# Add user that will be used in the container.
RUN groupadd --gid 1000 wagtail && useradd --uid 1000 -g wagtail wagtail

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

ENV PYTHONDONTWRITEBYTECODE 1

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    netcat \
    postgresql-client-11 \
 && rm -rf /var/lib/apt/lists/*

# upgrade pip
RUN pip install --upgrade pip

# Install the project requirements.
COPY requirements.txt /
RUN pip install -r /requirements.txt

# Use /app folder as a directory where the source code is stored.
ENV APP_HOME=/app
RUN mkdir ${APP_HOME}
RUN mkdir ${APP_HOME}/static && mkdir ${APP_HOME}/media && mkdir ${APP_HOME}/backups
WORKDIR ${APP_HOME}

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' ${APP_HOME}/entrypoint.sh
RUN chmod +x ${APP_HOME}/entrypoint.sh

# copy .run.sh
COPY ./.run.sh .
RUN chown wagtail:wagtail ${APP_HOME}/.run.sh && chmod +x ${APP_HOME}/.run.sh

# Set WORKDIR directory and sub dirs to be owned by the "wagtail" user.
RUN chown -R wagtail:wagtail ${APP_HOME}

# Copy the source code of the project into the container.
COPY --chown=wagtail:wagtail . .

# Use user "wagtail" to run the build commands below and the server itself.
USER wagtail

# This line can not take a variable
# When changing the APP_HOME, adjust this line as well
ENTRYPOINT ["/app/entrypoint.sh"]
