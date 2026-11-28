# Consulta do Clima (OpenWeather)

Aplicação web feita em Python com **Streamlit** para consultar as condições meteorológicas atuais e a previsão do tempo de uma cidade usando a API pública da OpenWeather.

## Funcionalidades

- Pesquisa das condições climáticas por nome da cidade.
- Exibição da temperatura atual (em °C), descrição do clima e ícone correspondente.
- Indicadores meteorológicos: sensação térmica, umidade, velocidade do vento e pressão atmosférica.
- Gráfico de linhas com a previsão de temperatura para os próximos dias.
- Mensagens de aviso caso a cidade não seja encontrada ou ocorra erro na conexão com a API.

## Funcionamento da aplicação

1. O usuário informa o nome de uma cidade no campo de pesquisa e clica em **Consultar clima**.
2. A função `buscar_dados(url, cidade)` envia uma requisição HTTP `GET` para a API OpenWeather usando a chave armazenada em `st.secrets["OPENWEATHER_API_KEY"]`, retornando os dados em JSON com temperatura em Celsius (`units=metric`) e descrições em português (`lang=pt_br`).
3. A função `mostrar_clima_atual(dados)` exibe o ícone do clima, a descrição, a temperatura atual e os indicadores meteorológicos (sensação térmica, umidade, vento e pressão) em colunas com `st.metric`.
4. A função `mostrar_previsao(dados)` percorre a lista de previsões retornada pela API (intervalos de 3 horas) e gera um gráfico de linha interativo com `plotly.express`.
5. Caso a cidade não seja encontrada (`404`), a API retorne erro ou haja falha de conexão, a aplicação exibe um aviso na tela sem travar.

## Endpoints utilizados (API OpenWeather)

- `https://api.openweathermap.org/data/2.5/weather` - busca as condições meteorológicas atuais da cidade.
- `https://api.openweathermap.org/data/2.5/forecast` - busca a previsão do tempo para os próximos dias (intervalos de 3 horas).

## Como executar localmente

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure sua chave da API no arquivo `.streamlit/secrets.toml`:
```toml
OPENWEATHER_API_KEY = "sua_chave_aqui"
```

3. Execute o aplicativo:
```bash
streamlit run app.py
```

## Arquivos do projeto

- `app.py` - código principal da aplicação.
- `requirements.txt` - bibliotecas utilizadas (`streamlit`, `requests` e `plotly`).
- `.streamlit/secrets.toml` - arquivo local com a chave da API (não enviar para o GitHub).

## Referência

- Vídeo de estudo sobre a API: https://www.youtube.com/watch?v=brQDClSX1Do
