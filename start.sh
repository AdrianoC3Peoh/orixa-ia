#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Parando processos anteriores..."
pkill -f "python3 main.py" 2>/dev/null
pkill -f ngrok 2>/dev/null
lsof -ti :8000 | xargs kill -9 2>/dev/null
sleep 2

echo "Iniciando servidor..."
cd "$DIR"
nohup python3 main.py > "$DIR/server.log" 2>&1 &

echo "Aguardando servidor..."
for i in {1..15}; do
  sleep 1
  STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/ 2>/dev/null)
  [ "$STATUS" = "200" ] && echo "Servidor OK" && break
done

echo "Iniciando ngrok..."
nohup python3 -c "
from pyngrok import ngrok
import time
ngrok.set_auth_token('3DgCKDqMFV9ckUbfEf5WSeuPMop_5YmWrVyxozVdV9FQK89U7')
[ngrok.disconnect(t.public_url) for t in ngrok.get_tunnels()]
tunnel = ngrok.connect(8000)
open('$DIR/tunnel.log','w').write(tunnel.public_url)
[time.sleep(60) or True for _ in iter(int,1)]
" > /dev/null 2>&1 &

sleep 5
URL=$(cat "$DIR/tunnel.log" 2>/dev/null)
echo ""
echo "======================================="
echo " Orixa IA rodando!"
echo " Local:   http://localhost:8000"
echo " Publico: $URL"
echo "======================================="
