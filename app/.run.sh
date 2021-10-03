#!/bin/bash
# ".run" is an utility script that is called by main appctl
# to run certain actions inside Misago's docker container.

# Text styles
RED='\033[0;31m'
NORMAL=$(tput sgr0)

# Utility functions used by action commands
error() {
    echo -e "${RED}Error:${NORMAL} $1"
    echo
    exit 1
}


wait_for_db() {
    export PGPASSWORD=$SQL_PASSWORD
    RETRIES=10
    until psql -h $SQL_HOST -U $SQL_USER -d $SQL_DATABASE -c "select 1" > /dev/null 2>&1 || [ $RETRIES -eq 0 ]; do
        ((RETRIES--))
        sleep 2
    done
}

# Handle invalid argument
invalid_argument() {
    echo -e "Invalid argument: ${RED}$1${NORMAL}"
    echo
    exit 1
}

# Initialize default database
initialize_default_database() {
    wait_for_db
    echo "Migrating database"
    python manage.py migrate
    echo "Loading default avatar gallery"
    python manage.py loadavatargallery
    echo "Creating first superuser account"
    python manage.py createsuperuser
}

# Run psql connected to database
run_psql() {
    wait_for_db
    psql --username $SQL_USER --host $SQL_HOST $SQL_DATABASE
}

# Backup database
backup_db() {
    wait_for_db
    pg_dump -U $SQL_USER -h $SQL_HOST $SQL_DATABASE -Oxc > "/app/backups/$1/database.sql"
}

# Command dispatcher
if [[ $1 ]]; then
    if [[ $1 = "initialize_default_database" ]]; then
        initialize_default_database
    elif [[ $1 = "wait_for_db" ]]; then
        wait_for_db
    elif [[ $1 = "psql" ]]; then
        run_psql
    elif [[ $1 = "backup_db" ]]; then
        backup_db $2
    else
        invalid_argument $1
    fi
fi