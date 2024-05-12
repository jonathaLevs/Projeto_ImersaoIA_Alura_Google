

import flet as ft
import google.generativeai as genai

## ------------------------------------------------------------------------------------------------
## CONFIGURAÇÕES DO GOOGLE GEMINI
## ------------------------------------------------------------------------------------------------

# Chave da API do Google Gemini. 
# É necessário ter uma chave válida para utilizar o modelo.
GOOGLE_API_KEY='DIGITE_SUA_CHAVE_AQUI'

# Configurando a API do Gemini com a chave fornecida
genai.configure(api_key=GOOGLE_API_KEY)

# Configurações do modelo Gemini
generation_config = { 
    "candidate_count": 1,  # Número de respostas a serem geradas (limitado a 1 neste caso)
    "temperature": 0.7, # Nível de criatividade (0.0 - mais preciso, 1.0 - mais criativo)
}

# Configurações de segurança do modelo Gemini
# Bloqueia conteúdo inadequado em diferentes categorias
config_security = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

# Inicializando o modelo Gemini Pro com as configurações definidas
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=config_security)

## ------------------------------------------------------------------------------------------------
## FUNÇÃO PRINCIPAL DA APLICAÇÃO
## ------------------------------------------------------------------------------------------------
def main(pagina):
    
    # Variáveis globais
    nome_carro = '' # Armazena o nome do carro digitado pelo usuário
    msg_espera = ft.Text('Aguarde... fazendo avaliação!') # Mensagem exibida enquanto a avaliação é processada

    ## ------------------------------------------------------------------------------------------------
    ## CRIAÇÃO DOS ELEMENTOS DA INTERFACE GRÁFICA
    ## ------------------------------------------------------------------------------------------------

    # Título da aplicação
    titulo_app = ft.Text(value='Avaliador de Carros para Compra', 
                         size = 35, italic=True, color='blue')
    
    # Subtítulo da aplicação
    subtitulo_app = ft.Text(value='Bem vindo ao Avaliador de carros do Gemini!', 
                         size = 20, italic=True)

    ## ------------------------------------------------------------------------------------------------
    ## DEFINIÇÃO DAS FUNÇÕES
    ## ------------------------------------------------------------------------------------------------
    
    # Função para gerar a segunda tela (tela de resultados)
    def gerar_tela02(texto_respota):
        pagina.remove(msg_espera) # Remove a mensagem de espera
        pagina.add(subtitulo_resultado_analise) # Adiciona o subtítulo da tela de resultados
        pagina.add(texto_respota) # Adiciona a resposta do Gemini formatada em Markdown
        pagina.update() # Atualiza a interface gráfica
    
    # Função para enviar a requisição para a API do Gemini
    def enviar_requisicao(nome):
        
        # Exibe a mensagem de espera
        pagina.add(msg_espera)
        pagina.update()

        # Exemplo de resposta desejada para o Gemini
        exemplo = '**Positivos:**\
    1. **Bom consumo de combustível:** Econômico, especialmente com motor 1.0.\
    2. **Design moderno e atraente:** Visual atualizado e esportivo.\
    outros pontos positivos...\
    **Negativos:**\
    1. **Acabamento interno simples:** Uso de materiais básicos e plásticos rígidos.\
    2. **Suspensão firme:** Pode comprometer o conforto em pisos irregulares.\
    outros pontos negativos....'
        
        # Comando enviado para o Gemini, incluindo o exemplo e o nome do carro
        comando =f'Faça extreitamente similar ao exemplo a seguir {exemplo}' + f'Liste em tópicos curtos e diretos, no máximo 12 tópicos, sobre o carro {nome}, pontos positivos e negativos. No final coloque o site da marca do carro como rodapé.'

        # Obtém a resposta do Gemini
        response = model.generate_content(comando)
        resposta_API_info_carro = response.text
        
        # Formata a resposta em Markdown, tornando links clicáveis
        texto_respota = ft.Markdown(resposta_API_info_carro, selectable=True,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            on_tap_link=lambda e: pagina.launch_url(e.data),)
        
        # Chama a função para gerar a tela de resultados
        gerar_tela02(texto_respota)
 
    # Função acionada ao clicar no botão "AVALIAR CARRO"
    def fazer_avaliacao(evento):
        
        # Obtém o nome do carro digitado pelo usuário
        nome_carro = campo_nome_carro.value
        
        # Remove os elementos da tela inicial
        pagina.remove(botao_avaliar)
        pagina.remove(campo_nome_carro)
        pagina.remove(subtitulo_app)
        
        # Chama a função para enviar a requisição para o Gemini
        enviar_requisicao(nome_carro)

        # Atualiza a interface gráfica
        pagina.update() 

    ## ------------------------------------------------------------------------------------------------
    ## CRIAÇÃO DOS ELEMENTOS DA TELA INICIAL
    ## ------------------------------------------------------------------------------------------------
    
    # Campo de texto para inserir o nome do carro
    campo_nome_carro = ft.TextField(label='Digite o nome do carro',width=600, on_submit=fazer_avaliacao)
    
    # Botão para iniciar a avaliação
    botao_avaliar = ft.ElevatedButton('AVALIAR CARRO', on_click=fazer_avaliacao)
    
    ## ------------------------------------------------------------------------------------------------
    ## CRIAÇÃO DOS ELEMENTOS DA TELA DE RESULTADOS
    ## ------------------------------------------------------------------------------------------------
    
    # Subtítulo da tela de resultados
    subtitulo_resultado_analise = ft.Text('Resultado da Análise', size=20, color='red')

    # Adiciona os elementos da tela inicial à interface gráfica
    pagina.add(titulo_app)
    pagina.add(subtitulo_app)
    pagina.add(campo_nome_carro)
    pagina.add(botao_avaliar)

# Inicia a aplicação com a função principal
ft.app(main)
