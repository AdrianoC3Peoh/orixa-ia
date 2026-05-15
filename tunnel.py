from pyngrok import ngrok, conf
import time

TOKEN = "3DgCKDqMFV9ckUbfEf5WSeuPMop_5YmWrVyxozVdV9FQK89U7"
ngrok.set_auth_token(TOKEN)

# Encerra túneis anteriores antes de criar um novo
for t in ngrok.get_tunnels():
    ngrok.disconnect(t.public_url)

tunnel = ngrok.connect(8000)
url = tunnel.public_url

print("\n" + "="*52)
print(f"  URL PÚBLICA: {url}")
print("="*52)
print("  Compartilhe esse link para testes mobile.")
print("  Pressione Ctrl+C para encerrar.\n")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    ngrok.kill()
    print("Túnel encerrado.")
