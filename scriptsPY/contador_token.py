import google.generativeai as genai

MODELO_FLASH = "gemini-2.0-flash"
MODELO_PRO = "gemini-1.5-pro"

CUSTO_ENTRADA_FLASH = 0.075
CUSTO_SAIDA_FLASH = 0.30

CUSTO_ENTRADA_PRO = 3.5
CUSTO_SAIDA_PRO = 10.50

model_flash = genai.get_model(f"models/{MODELO_FLASH}")
limites_modelo_flash = {
    "tokens_entrada": model_flash.input_token_limit,
    "tokens_saida": model_flash.output_token_limit
}

print(f"Limites do modelo flash são: {limites_modelo_flash}")

llm_flash = genai.GenerativeModel(
    f"models/{MODELO_FLASH}"
)

quantidade_tokens = llm_flash.count_tokens("O que é uma calça de shopping?")
print(f"A quantidade de tokens é: {quantidade_tokens}")

resposta = llm_flash.generate_content("O que é uma calça de shopping?")
tokens_prompt = resposta.usage_metadata.prompt_token_count
tokens_resposta = resposta.usage_metadata.candidates_token_count

custo_total = (tokens_prompt * CUSTO_ENTRADA_FLASH) / 1000000 + (tokens_resposta * CUSTO_SAIDA_FLASH) / 1000000
print(f"Custo Total U$ Flash: ", custo_total)

custo_total = (tokens_prompt * CUSTO_ENTRADA_PRO) / 1000000 + (tokens_resposta * CUSTO_SAIDA_PRO) / 100.000
print(f"Custo Total U$ Pro: ", custo_total)
