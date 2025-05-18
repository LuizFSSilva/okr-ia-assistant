from flask import Flask,render_template, request, Response
import google.generativeai as genai
from dotenv import load_dotenv
import os
from time import sleep
from helper import carrega, salva
from selecionar_persona import personas, selecionar_persona
from gerenciar_historico import remover_mensagens_mais_antigas
import uuid
from gerenciar_imagem import gerar_imagem_gemini

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GOOGLE_API_KEY")
MODELO_ESCOLHIDO = "gemini-2.0-flash"   
genai.configure(api_key=CHAVE_API_GOOGLE)

app = Flask(__name__)
app.secret_key = 'alura'

contexto = carrega("dados/modeloOKR.txt")

caminho_imagem_enviada = None
UPLOAD_FOLDER = "imagens_temporarias"

def criar_chatbot():
    personalidade = "neutro"

    prompt_do_sistema = f"""
    # PERSONA

    Você é um especialista de processos ágeis de desenvolvimento de software, de produtos digitais e do método de gestão de resultados OKRs.
    Você é um assistente que ajuda a escrever OKRs de forma que demonstrem real resultado das implentações realizadas pelos projetos de TI.
    Você avalia OKRs escritos caso seja requisitado.
    Você não deve responder perguntas que não sejam dados de OKRs ou Metodologias Ágeis!
    O usuário já é apresentado as quatro opções: 1. analisar os OKRs separando o Objetivo e os Resultados Chaves 2. criar novos OKRs 3. tirar dúvidas sobre OKRs e Metodolodias ágeis 4. Conversa livre sobre Metologias Ágeis ou OKRs. Verificar de qual assunto o usuário está falando se seguir os casos 1, 2, 3 ou 4.
    Caso 1: Solicitar o Objetivo e os Key Results para análise. Após, analise e dê uma nota de 0 a 10 de acordo com a aderência a metodologia dos OKRs e o 'contexto'.
    Caso 2: Realizar 5 perguntas ao usuário: Pergunta 1: Qual é o objetivo principal que queremos alcançar neste período? Pergunta 2: Como podemos medir o sucesso desse objetivo de forma objetiva e mensurável? Pergunta 3: Esse objetivo está alinhado com a estratégia geral da empresa ou do time? Pergunta 4: Quais são os desafios ou obstáculos que podem impedir o alcance desse objetivo? Pergunta 5: Como essa OKR vai motivar e engajar a equipe para alcançá-la? A partir das 5 perguntas, crie três sugestões de objetivos e cinco key results.
    Caso 3: utilize os dados do 'contexto' para retirar as dúvidas.
    Caso 4: interaja de acordo com o usuário.
    
    Você deve utilizar apenas dados que estejam dentro do 'contexto'

    # CONTEXTO
    {contexto}

    # PERSONALIDADE
    {personalidade}

    # Histórico
    Acesse sempre o históricio de mensagens, e recupere informações ditas anteriormente.
    """

    configuracao_modelo = {
        "temperature" : 0.1,
        "max_output_tokens" : 8192
    }

    llm = genai.GenerativeModel(
        model_name=MODELO_ESCOLHIDO,
        system_instruction=prompt_do_sistema,
        generation_config=configuracao_modelo
    )

    chatbot = llm.start_chat(history=[])

    return chatbot

chatbot = criar_chatbot()

def bot(prompt):
    maximo_tentativas = 1
    repeticao = 0
    global caminho_imagem_enviada

    while True:
        try:
            personalidade = personas[selecionar_persona(prompt)]
            mensagem_usuario = f"""
            Considere esta personalidade para responder a mensagem:
            {personalidade}

            Responda a seguinte mensagem, sempre lembrando do históricio:
            {prompt}
            """

            if caminho_imagem_enviada:
                mensagem_usuario += "\n Utilize as caracteristicas da imagem em sua resposta"
                #arquivo_imagem = gerar_imagem_gemini(caminho_imagem_enviada)
                #resposta = chatbot.send_message([arquivo_imagem, mensagem_usuario])
                arquivo_imagem = gerar_imagem_gemini(caminho_imagem_enviada)
                resposta = chatbot.send_message([arquivo_imagem, mensagem_usuario])
                os.remove(caminho_imagem_enviada)
                caminho_imagem_enviada = None
            else:
                resposta = chatbot.send_message(mensagem_usuario)

            if len(chatbot.history) > 10:
                chatbot.history = remover_mensagens_mais_antigas(chatbot.history)

            return resposta.text
        except Exception as erro:
            repeticao += 1
            if repeticao >= maximo_tentativas:
                return "Erro no Gemini: %s" % erro
            
            if caminho_imagem_enviada:
                os.remove(caminho_imagem_enviada)
                caminho_imagem_enviada = None

            sleep(50)

@app.route("/upload_imagem", methods=["POST"])
def upload_imagem():
    global caminho_imagem_enviada

    if "imagem" in request.files:
        imagem_enviada = request.files["imagem"]
        nome_arquivo = str(uuid.uuid4()) + os.path.splitext(imagem_enviada.filename)[1]
        caminho_arquivo = os.path.join(UPLOAD_FOLDER, nome_arquivo)
        imagem_enviada.save(caminho_arquivo)
        caminho_imagem_enviada = caminho_arquivo
        return "Imagem enviada com sucesso", 200
    return "Nenhum arquivo enviado", 400

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["msg"]
    resposta = bot(prompt)
    return resposta

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
