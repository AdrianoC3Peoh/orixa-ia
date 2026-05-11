#!/bin/bash
cd "$(dirname "$0")"
echo "Iniciando Orixá IA..."

# Verifica dependências
python3 -c "import fastapi" 2>/dev/null || pip3 install -r requirements.txt -q

# Cria .env se não existir
if [ ! -f .env ]; then
  cp .env.example .env
  echo "Arquivo .env criado. Edite com sua ANTHROPIC_API_KEY para ativar o chat com IA."
fi

export $(grep -v '^#' .env | xargs) 2>/dev/null || true

python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
