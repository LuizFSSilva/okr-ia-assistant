# OKR-AI Assistant 🧠🎯

**Inteligência Artificial para apoio na criação, análise e melhoria de OKRs estratégicos e táticos, com foco em projetos de desenvolvimento de software.**

---

## 🧩 Visão Geral

Este projeto é um assistente virtual baseado em IA que auxilia times e lideranças da Bradesco Seguros a criarem, analisarem e validarem OKRs (Objectives and Key Results), com foco em resultados reais entregues pelos projetos de TI. A aplicação é composta por:

- Backend em **Python (Flask)** com integração à **Google Generative AI**.
- Frontend com **HTML, CSS e JavaScript**.
- Prompt estruturado com foco em **boas práticas de gestão por resultados e metodologias ágeis**.

---

## 🔧 Funcionalidades

O assistente oferece 4 opções principais para o usuário:

1. **Analisar OKRs**: separa Objetivo e Resultados-Chave, avalia e atribui uma nota de 0 a 10 com base na metodologia e contexto fornecido.
2. **Criar novos OKRs**: conduz o usuário por 5 perguntas para gerar sugestões de Objetivos e Resultados-Chave.
3. **Tirar dúvidas sobre OKRs ou metodologias ágeis**: responde com base no modelo operacional (contexto).
4. **Conversa livre sobre OKRs ou metodologias ágeis**: interações abertas dentro do escopo do tema.

---

## ⚙️ Tecnologias Utilizadas

### Backend
- `Flask==3.0.3` – Servidor web para API
- `google-generativeai==0.8.3` – Integração com modelo de linguagem da Google
- `numpy==2.1.2` – Manipulação de dados
- `python-dotenv==1.0.1` – Variáveis de ambiente
- `requests==2.32.3` – Chamadas HTTP

### Frontend
- HTML, CSS, JavaScript (em `static/`)

---

## 🚀 Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone git@github.com:LuizFSSilva/python_gemini.git
   cd python_gemini
2. Crie e ative um ambiente virtual:
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
3. Instale as dependências:
    pip install -r requirements.txt
4. Crie um arquivo .env com sua chave da API:
    GOOGLE_API_KEY=sua-chave-aqui
5. Rode o servidor:
    flask run
6. Acesse a aplicação:
    http://localhost:5000

---

📁 Estrutura do Projeto

okr-project-bs/
├── dados                   # Dados consultados pela IA de modelo operacional
├── imagens_temporarias     # Imagens upadas pelo usuário
├── scriptsPY/              # Scripts auxiliares da aplicação
├── static/                 # HTML, CSS e JS
├── templates/              # (se usar templates Flask)
├── .env                    # Configurações (não versionado)
├── .gitignore              # Arquivos para serem ignorados no git
├── app.py                  # Lógica principal
├── docker-compose.yml      # Arquivo de configuração
├── dockerfile              # Imagem docker
├── gerenciar_historico.py  # Remove mensagens antigas para memória da IA, ficam registradas 2 anteriores
├── gerenciar_imagem.py     # Gerencia imagens que o usuário fez upload
├── requirements.txt        # Dependências
└── selecionar_persona.py   # Identifica e muda personalidade da IA de acordo com o perfil do usuário

---

🔒 Observações

• A IA responde somente sobre OKRs e metodologias ágeis, com base no contexto do negócio.
• O prompt do sistema segue um roteiro rígido, guiando o usuário com perguntas estratégicas.
• A aplicação é orientada ao modelo operacional de gestão de resultados da empresa.

---

✉️ Contato
Luiz F. S. Silva
📧 cefet.luiz@gmail.com



