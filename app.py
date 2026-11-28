import streamlit as st
import requests
import plotly.express as px

#VENDO ESSE VIDEO PARA APRENDER SOBRE ESSA API E APLICAR AQUI https://www.youtube.com/watch?v=brQDClSX1Do

URL_CLIMA = "https://api.openweathermap.org/data/2.5/weather"
URL_PREVISAO = "https://api.openweathermap.org/data/2.5/forecast"


# uso a mesma funcao pro clima atual e pra previsao pra nao repetir codigo
def buscar_dados(url, cidade):
    params = {
        "q": f"{cidade},BR",
        "appid": st.secrets["OPENWEATHER_API_KEY"],
        "units": "metric",
        "lang": "pt_br"
    }

    try:
        resp = requests.get(url, params=params)
        if resp.status_code == 200:
            return resp.json()
        elif resp.status_code == 404:
            st.warning("Cidade não encontrada.")
        else:
            st.error("Não foi possível buscar os dados do clima.")
    except requests.exceptions.RequestException:
        st.error("Erro de conexão com a API.")

    return None


def mostrar_clima_atual(dados):
    st.subheader(f"Clima em {dados['name']}")

    # pega o icone e a descricao dentro da lista "weather" que vem no json
    icone = dados["weather"][0]["icon"]
    descricao = dados["weather"][0]["description"].capitalize()
    st.image(f"https://openweathermap.org/img/wn/{icone}@2x.png", width=80)
    st.write(f"**{descricao}** - {dados['main']['temp']:.1f} °C")

    # st.columns(4) divide a tela em 4 colunas lado a lado (c1 ate c4). Se quiser mais ou menos colunas, só mudar o numero
    c1, c2, c3, c4 = st.columns(4)
    # st.metric mostra um bloquinho com titulo e valor em cada coluna
    c1.metric("Sensação térmica", f"{dados['main']['feels_like']:.1f} °C")
    c2.metric("Umidade", f"{dados['main']['humidity']}%")
    c3.metric("Vento", f"{dados['wind']['speed']} m/s")
    c4.metric("Pressão", f"{dados['main']['pressure']} hPa")


def mostrar_previsao(dados):
    st.subheader("Previsão para os próximos dias")

    # a API manda dados de 3 em 3 horas, aqui separo data/hora e temperatura pro grafico
    datas = []
    temps = []
    for item in dados["list"]:
        datas.append(item["dt_txt"])
        temps.append(item["main"]["temp"])

    fig = px.line(
        x=datas,
        y=temps,
        markers=True,
        labels={"x": "Data e hora", "y": "Temperatura (°C)"}
    )
    st.plotly_chart(fig, use_container_width=True)


# parte visual do site
st.set_page_config(page_title="Consulta do Clima", layout="centered")

# mudando a fonte que usamos, o fundo e centralizando tudo ( FIZ NA ATIVIDADE 1 E REAPROVEITEI AQUI)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=National+Park&display=swap');

.stApp {
    background-color: #111827;
    font-family: 'National Park', sans-serif;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.title("Consulta do Clima")

cidade = st.text_input("Digite o nome da cidade", placeholder="Ex: Itabira")

if st.button("Consultar clima"):
    if not cidade.strip():
        st.warning("Digite uma cidade antes de pesquisar.")
    else:
        clima = buscar_dados(URL_CLIMA, cidade.strip())
        if clima:
            mostrar_clima_atual(clima)
            previsao = buscar_dados(URL_PREVISAO, cidade.strip())
            if previsao:
                st.divider()
                mostrar_previsao(previsao)
