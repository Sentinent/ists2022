#!/usr/bin/env bash

BACKUP_DIR=~/minecraft

dirs=(
    /etc
    /var/www
    /usr/share/nginx
)

mkdir -p $BACKUP_DIR

for dir in ${dirs[@]}; do
    echo "Backing up: $dir"
    cp -r $dir $BACKUP_DIR
done

chattr +i -R $BACKUP_DIR
