import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
import json
from PIL import Image

st.set_page_config(layout="wide")

def load_lottiefile(filepath: str): 
    with open(filepath, "r") as f: 
        return json.load(f) 
    
lottie_file = "about.json"
lottie_file2 = "contact.json"  
lottie_about = load_lottiefile(lottie_file)
lottie_contact = load_lottiefile(lottie_file2)
monte_carlo = Image.open("C:/Users/llluc/Documents/streamlit/monte_carlo.png")
regressao_multivariada = Image.open("C:/Users/llluc/Documents/streamlit/monte_carlo.png")
queimadas = Image.open("C:/Users/llluc/Documents/streamlit/monte_carlo.png")

st.write("##")
st.markdown("<h3 style='text-align: center;'>Olá, visitante! 👋</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Meu nome é Lucas</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Analista de Dados</h3>", unsafe_allow_html=True)
st.markdown(""" 
    <div style='text-align: center;'> 
        <a href='https://github.com/lll-lucas' target='_blank' style='text-decoration: none;'>
            <img src='https://img.icons8.com/ios-filled/50/808080/github.png' alt='GitHub' style='margin: 0 10px;'/> 
        </a> 
        <a href='www.linkedin.com/in/lucas-barboza-de-araújo-' target='_blank' style='text-decoration: none;'>
            <img src='https://img.icons8.com/ios-filled/50/808080/linkedin.png' alt='LinkedIn' style='margin: 0 10px;'/> 
        </a> 
        <a href='https://medium.com/@lllucas.barboza' target='_blank' style='text-decoration: none;'>
             <img src='https://img.icons8.com/ios-filled/50/808080/medium.png' alt='Medium' style='margin: 0 10px;'/> 
        </a> 
    </div> 
    """, unsafe_allow_html=True)
st.write('---')

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About', 'Projects', 'Contact'],
        icons = ['person', 'code-slash', 'chat-left-text-fill'],
        orientation = 'horizontal'
    )
if selected == 'About':

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.title("Saiba mais sobre mim")
            st.markdown(""" <div style='text-align: justify; font-size: 1.2em;'> Sou um Analista de Dados com uma formação acadêmica em Estatística, o que me proporcionou uma base sólida de 
                     conhecimento para a análise e interpretação de dados. Possuo domínio das principais ferramentas e metodologias para
                     a extração de insights valiosos, fundamentais para orientação na tomada de decisões estrategicas. </div>""", unsafe_allow_html=True)
            st.markdown(""" <div style='text-align: justify; font-size: 1.2em;'> Entre as principais tecnologias que domino estão: </div>""", unsafe_allow_html=True)
            st.write("") 
            col3, col4, col5, col6, col7, col8 = st.columns(6) 
            with col3: st.image("python.png", width=48) 
            with col4: st.image("r.png", width=48) 
            with col5: st.image("mysql.png", width=48) 
            with col6: st.image("postgresql.png", width=48) 
            with col7: st.image("power_bi.png", width=48) 
            with col8: st.image("excel.png", width=48) 
            st.write("") 
            st.markdown(""" <div style='text-align: justify; font-size: 1.2em;'> Ficou interessado? Acesse a sessão de projetos para ver alguns dos meus principais trabalhos. Lá, você 
                        encontrará estudos de caso detalhados, análises aprofundadas e soluções inovadoras que desenvolvi ao longo da minha trajetória. Não perca a oportunidade de conhecer
                        mais sobre minhas habilidades e experiências! </div>""", unsafe_allow_html=True)
        with col2: 
            st_lottie(lottie_about)

if selected == "Projects":
    with st.container():
        st.header("Meus Projetos")
        st.write("##")

        col3,col4 = st.columns((1,2))
        with col3:
            st.image(monte_carlo)
        with col4:
            st.subheader("Projeto X")
            st.markdown(""" <div style='text-align: justify;'> breve resumo sobre o projeto </div>""", unsafe_allow_html=True)
            st.markdown("[Saiba mais](https://github.com/lll-lucas/Estudo-de-impacto-de-tratamentos-no-peso-de-plantas)")
        st.write("---")

        col5, col6 = st.columns((1, 2)) 
        with col5:
            st.image(regressao_multivariada)  
        with col6:
            st.subheader("Projeto Y") 
            st.markdown(""" <div style='text-align: justify;'> Breve resumo sobre o segundo projeto. </div> """, unsafe_allow_html=True)
            st.markdown("[Saiba mais](https://github.com/lll-lucas/Outro-Projeto)") 
        st.write("---")

        
        col7, col8 = st.columns((1, 2)) 
        with col7:
            st.image(queimadas)  
        with col8:
            st.subheader("Projeto Z") 
            st.markdown(""" <div style='text-align: justify;'> Breve resumo sobre o segundo projeto. </div> """, unsafe_allow_html=True)
            st.markdown("[Saiba mais](https://github.com/lll-lucas/Outro-Projeto)") 
        st.write("---")

if selected == "Contact":
    st.header("Get in touch!")
    st.write('##')

    contact_form = """ 
    <form action="https://formsubmit.co/aa2d317fc38704aa46e7b3463446c7b1" method="POST" style="display: flex; flex-direction: column; gap: 10px;"> 
    <input type="text" name="name" placeholder="Seu nome" required style="padding: 10px; border: 1px solid #ccc; border-radius: 5px;"> 
    <input type="email" name="email" placeholder="Seu email" required style="padding: 10px; border: 1px solid #ccc; border-radius: 5px;"> 
    <textarea name="message" placeholder="Sua mensagem" required style="padding: 10px; border: 1px solid #ccc; border-radius: 5px;"></textarea> 
    <button type="submit" style="padding: 10px; border: none; border-radius: 5px; background-color: #4CAF50; color: white; cursor: pointer;">Enviar</button> 
    </form> """

    left_col, right_col = st.columns((2,1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html= True)
    with right_col:
        st_lottie(lottie_contact, height=320)