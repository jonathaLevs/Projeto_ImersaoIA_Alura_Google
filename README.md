# Projeto ImersaoIA da Alura e Google

# avaliador_carro.py - Avaliando carros com o poder do Google Gemini!

Este código em Python, utilizando a biblioteca `flet` para interface gráfica e a API `google.generativeai` para acessar o modelo de linguagem Gemini, cria uma aplicação web interativa para avaliar carros.

## Objetivo:

O objetivo principal do código é fornecer uma ferramenta simples e intuitiva para os usuários obterem uma rápida avaliação sobre um determinado modelo de carro. A aplicação consulta o modelo Gemini, que utiliza seus vastos conhecimentos para gerar uma lista de pontos positivos e negativos do carro, além de fornecer um link para o site oficial da marca.

## Funcionalidades:

1. **Interface amigável:** O aplicativo apresenta uma interface simples com um campo de texto para inserir o nome do carro e um botão "AVALIAR CARRO".
2. **Integração com o Gemini:**  O código utiliza a API `google.generativeai` para se conectar ao modelo Gemini Pro. A chave da API (GOOGLE_API_KEY) deve ser fornecida pelo usuário.
3. **Formatação da resposta:** A resposta do Gemini é formatada usando a biblioteca `flet` em Markdown para melhor visualização, incluindo links clicáveis para o site da marca.
4. **Exibição dos resultados:**  A aplicação exibe os resultados da avaliação em uma nova tela, substituindo os elementos da tela inicial.

## Tecnologias utilizadas:

* **Flet:** Uma estrutura Python moderna para construir interfaces de usuário web interativas. ([https://flet.dev/](https://flet.dev/))
* **Google Gemini:** Um modelo de linguagem avançado com amplo conhecimento e capacidades de geração de texto. ([https://developers.generativeai.google](https://developers.generativeai.google))
* **Python:** Linguagem de programação versátil e poderosa usada para desenvolver a lógica da aplicação.

## Como funciona:

1. **Inicialização:** O código inicializa a API do Gemini, define as configurações do modelo (temperatura e número de candidatos) e configurações de segurança.
2. **Interface do usuário:** A função `main` cria a interface do usuário com os elementos necessários: título, subtítulo, campo de texto para inserir o nome do carro e o botão "AVALIAR CARRO".
3. **Ação do botão:**  Ao clicar no botão "AVALIAR CARRO", a função `fazer_avaliacao` é acionada.
4. **Processamento da requisição:** A função `enviar_requisicao` é chamada, enviando o nome do carro para o Gemini. A resposta do modelo é então formatada em Markdown e exibida na tela.

## Observações:

* É crucial substituir `'DIGITE_SUA_CHAVE_AQUI'` pela sua chave da API do Google Gemini.
* As configurações do modelo, como temperatura e configurações de segurança, podem ser ajustadas de acordo com as necessidades do usuário.
