import streamlit as st
from agent import get_answer

st.set_page_config(page_title="Wiki Geopixel", layout="wide")
st.title("Wiki Geopixel")

st.markdown("""
    <style>
        .fixed-bottom {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: white;
            padding: 1rem;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
            z-index: 100;
        }
        
        .main .block-container {
            padding-bottom: 150px;
        }
        
        .message {
            padding: 0.5rem 1rem;
            margin: 0.5rem 0;
            border-radius: 0.5rem;
            max-width: 80%;
        }
        
        .user-message {
            background-color: gray;
            margin-left: auto;
            margin-right: 0;
            width: fit-content;
        }
        
        .bot-message {
            background-color: steelblue;
            margin-left: 0;
            margin-right: auto;
        }
    </style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.container():
        if message["role"] == "user":
            st.markdown(f'<div class="message user-message">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="message bot-message">{message["content"]}</div>', unsafe_allow_html=True)
            if "sources" in message:
                with st.expander("Fontes utilizadas"):
                    for doc in message["sources"]:
                        st.markdown(f"**Arquivo:** `{doc.metadata.get('source', 'desconhecido')}`")
                        st.write(doc.page_content[:400] + "...")

with st.container():
    st.markdown('<div class="fixed-bottom">', unsafe_allow_html=True)
    pergunta = st.text_input("Digite sua pergunta:", placeholder="Ex: Como funciona o editor de estilos?")
    enviar = st.button("Perguntar")
    st.markdown('</div>', unsafe_allow_html=True)

if enviar and pergunta.strip():
    st.session_state.messages.append({"role": "user", "content": pergunta})
    
    with st.spinner("Buscando..."):
        resposta = get_answer(pergunta)
        
        st.session_state.messages.append({
            "role": "bot",
            "content": resposta["result"],
            "sources": resposta["source_documents"]
        })
        
        st.rerun()
        
elif enviar:
    st.warning("Digite uma pergunta antes de enviar.")