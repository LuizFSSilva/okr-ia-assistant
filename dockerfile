FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

#Cria a pasta de imagens temporáris
RUN mkdir -p /app/imagens_temporarias

# Copia o restante da aplicação
COPY . .

# Expõe a porta padrão do Flask
EXPOSE 5000

# Define variáveis de ambiente e comando para rodar o Flask
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]
