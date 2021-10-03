#!/bin/bash

WAGTAIL_SERVICE=web
WAGTAIL_USER=wagtail
DB_SERVICE=db

# set environment specific variables
source ./.env.upgrade

docker-compose -f ${DOCKER_COMPOSE_FILE} up -d

# create backup
backup_dir="upgrade-$(date +%Y%m%d%H%M%S)"
mkdir "./backups/$backup_dir"
# backup database
echo "Backing up database..."

docker-compose -f ${DOCKER_COMPOSE_FILE} exec ${WAGTAIL_SERVICE} ./.run.sh backup_db $backup_dir

# backup media
echo "Backing up media..."
cp -r ${MEDIA_PATH} "./backups/$backup_dir/media"
cd ./backups/
# archive backup dir
backup_archive="upgrade-$(date +%Y%m%d%H%M%S).tar.gz"
GZIP=-9
tar -zcf $backup_archive "$backup_dir"
# delete backup dir as its no longer required
rm -rf $backup_dir
cd ..
echo "New backup has been created at backups/$backup_archive"
echo

docker-compose -f ${DOCKER_COMPOSE_FILE} down
docker-compose -f ${DOCKER_COMPOSE_FILE} build
docker-compose -f ${DOCKER_COMPOSE_FILE} up -d
docker-compose -f ${DOCKER_COMPOSE_FILE} exec -u ${WAGTAIL_USER} ${WAGTAIL_SERVICE} python manage.py migrate
docker-compose -f ${DOCKER_COMPOSE_FILE} exec -u ${WAGTAIL_USER} ${WAGTAIL_SERVICE} python manage.py collectstatic --noinput --clear
docker-compose -f ${DOCKER_COMPOSE_FILE} exec -u ${WAGTAIL_USER} ${WAGTAIL_SERVICE} python manage.py compress --force
docker system prune --force

# docker-compose -f ${DOCKER_COMPOSE_FILE} down