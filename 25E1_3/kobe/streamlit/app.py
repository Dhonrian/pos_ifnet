import streamlit as st
import requests
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO


def get_prediction(row):
    """
    Função para fazer a previsão do arremesso
    """
    response = requests.post(
        "http://localhost:5001/invocations",
        json={'inputs': row},
        headers={"Content-Type": "application/json"}
    )
    
    prediction = response.json()
    shot_made = bool(prediction.get("predictions", [0])[0])
    
    return shot_made

if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=['lat', 'lon', 'shot_made'])

with st.container():
    col1, col2 = st.columns(2)
    
    lat = col1.slider("Lat", 33.5, 34.5, 34.043, step=0.001, format="%.3f")
    lon = col1.slider("Lon", -119.0, -118.0, -118.267, step=0.001, format="%.3f")
    shot_distance = col1.slider("Distância", 0, 50, 10, key='dist')
    
    minutes_remaining = col2.slider("Minutos Restantes", 0, 11, 5, key='min')
    period = col2.slider("Tempo", 1, 7, 1, key='period')
    playoffs = col2.selectbox("Playoffs", [0, 1], format_func=lambda x: "Não" if x == 0 else "Sim", key='playoffs')


    if st.button("Prever Arremesso", use_container_width=True):
        data = {
            "lat" : lat,
            "lon" : lon,
            "minutes_remaining" : minutes_remaining,
            "period" : period,
            "playoffs" : playoffs,
            "shot_distance" : shot_distance
        }

        row = [
            list(data.values())
        ]
        
        try:
            shot_made = get_prediction(row)
             
            new_shot = pd.DataFrame([[lat, lon, shot_made]], 
                                   columns=['lat', 'lon', 'shot_made'])
            st.session_state.history = pd.concat([st.session_state.history, new_shot])
            
            if shot_made:
                st.success("Arremesso Acertou!")
            else:
                st.error("Arremesso Errou!")
        except Exception as e:
            st.error(f"Erro na previsão: {str(e)}")

if not st.session_state.history.empty:
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-119.0, -118.0)
    ax.set_ylim(33.0, 35.0)
    
    for _, row in st.session_state.history.iterrows():
        color = 'green' if row['shot_made'] else 'red'
        ax.scatter(row['lon'], row['lat'], color=color, alpha=0.6)
    
    ax.set_title("Histórico de Arremessos")
    ax.set_xlabel("Lon")
    ax.set_ylabel("Lat")
    
    buf = BytesIO()
    fig.savefig(buf, format="png")
    st.image(buf)
    buf.close()