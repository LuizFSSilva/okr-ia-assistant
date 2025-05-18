import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=CHAVE_API_GOOGLE)
MODELO_ESCOLHIDO = "gemini-2.0-flash"

prompt_sistema = "Agir como um especialista em OKRs. Responda somente assuntos sobre OKRs e metodolodias ágeis. Sujira três opções ao usuário, analisar os OKRs requisitados separando o Objetivo e os Resultados Chaves, criar novos OKRs ou tirar dúvidas sobre OKRs e Metodolodias ágeis. No caso de análise, traga um valor percentual de aderência a uma OKR ideal. Proponha melhorias para o Objetivo e Resultados Chaves listados."

configuracao_modelo = {
    "temperature" : 1.0, # de 0-2 maior criatividade possível
    "top_p" : 0.9,  #de 0-1 critério de palavras que são similares ou não para compor a resposta
    "top_k" : 64,  #quantidade de palavras que o modelo irá observar dentro do vocabulário, escolhe de acordo com o top_p
    "max_output_tokens" : 8192 #quantidade máxima de tokens que poderá ser utilziado na resposta
    #"response_mime_type" : "text/plain" #formato do texto de saída  
}

llm = genai.GenerativeModel(
    MODELO_ESCOLHIDO,
    system_instruction=prompt_sistema,
    generation_config=configuracao_modelo
)

pergunta = "Objetivo: construir uma ferramenta facilite a construção de OKRs. Key Result 1: implementar um consumo de um modelo de IA generativa para a ferramenta de construção de OKRS. Key Result 2: Aumentar o número de usuários da ferramenta de 0 para 10 pessoas em 1 mês."
resposta = llm.generate_content(pergunta)
print(f"A resposta gerada para a pergunta é: {resposta.text}")