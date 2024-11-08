import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
import json
from PIL import Image
import os

st.set_page_config(layout="wide")

def load_lottiefile(filepath: str): 
    try: 
        with open(filepath, "r") as f: 
            return json.load(f) 
    except FileNotFoundError: 
        st.error(f"Arquivo não encontrado: {filepath}") 
        return None 
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}") 
        return None
    
current_dir = os.path.dirname(os.path.abspath(__file__)) 
lottie_file = os.path.join(current_dir, "about.json") 
lottie_file2 = os.path.join(current_dir, "contact.json")

lottie_about = load_lottiefile(lottie_file)
lottie_contact = load_lottiefile(lottie_file2)

if lottie_about is None or lottie_contact is None: 
    st.stop()

# Verifique se os arquivos de imagem estão no diretório correto 
image_files = ["python.png", "r.png", "mysql.png", "mariadb.png", "power_bi.png", "excel.png"] 
for image_file in image_files:
    image_path = os.path.join(current_dir, image_file) 
    if not os.path.exists(image_path): 
        st.error(f"Arquivo de imagem não encontrado: {image_path}")
    
monte_carlo = Image.open("streamlit/monte_carlo.png")
regressao_multivariada = Image.open("streamlit/monte_carlo.png")
queimadas = Image.open("streamlit/monte_carlo.png")

# Textos de boas-vindas
st.write("##")
st.markdown("<h3 style='text-align: center;'>Olá, visitante! 👋</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Meu nome é Lucas</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Analista de Dados</h3>", unsafe_allow_html=True)
st.markdown(""" 
    <div style='text-align: center;'> 
        <a href='https://github.com/lll-lucas' target='_blank' style='text-decoration: none;'>
            <img src='https://img.icons8.com/ios-filled/50/808080/github.png' alt='GitHub' style='margin: 0 10px;'/> 
        </a> 
        <a href='https://www.linkedin.com/in/lucas-barboza-de-araujo' target='_blank' style='text-decoration: none;'>
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
        options = ['Sobre mim', 'Projetos', 'Contato'],
        icons = ['person', 'code-slash', 'chat-left-text-fill'],
        orientation = 'horizontal'
    )
if selected == 'Sobre mim':

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.title("Saiba mais sobre mim")
            st.markdown(""" <div style='text-align: justify; font-size: 1.2em;'> Sou um Analista de Dados com uma formação acadêmica em Estatística, o que me proporcionou uma base sólida de 
                     conhecimento para a análise e interpretação de dados. Possuo domínio das principais ferramentas e metodologias para
                     a extração de insights valiosos, fundamentais para orientação na tomada de decisões estratégicas. </div>""", unsafe_allow_html=True)
            st.markdown(""" <div style='text-align: justify; font-size: 1.2em;'> Entre as principais tecnologias que domino estão: </div>""", unsafe_allow_html=True)
            st.write("") 
            col3, col4, col5, col6, col7, col8, col9 = st.columns(7) 
            with col3: 
                st.image(os.path.join(current_dir, "python.png"), width=48)                
            with col4: 
                st.image(os.path.join(current_dir, "r.png"), width=48)
            with col5: 
                st.image(os.path.join(current_dir, "mysql.png"), width=48)
            with col6: 
                st.image(os.path.join(current_dir, "mariadb.png"), width=48)
            with col7: 
                st.image(os.path.join(current_dir, "sqlite.png"), width=48)
            with col8: 
                st.image(os.path.join(current_dir, "power_bi.png"), width=48)
            with col9: 
                st.image(os.path.join(current_dir, "excel.png"), width=48)
            st.write("") 
            st.markdown(""" <div style='text-align: justify; font-size: 1.2em;'> Acesse a sessão de projetos para ver alguns dos meus principais trabalhos. Lá, você 
                        encontrará estudos de caso detalhados, análises aprofundadas e soluções inovadoras que desenvolvi ao longo da minha trajetória. Não perca a oportunidade de conhecer
                        mais sobre minhas habilidades e experiências! </div>""", unsafe_allow_html=True)
        with col2: 
            st_lottie(lottie_about)

if selected == "Projetos":
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
            st.subheader("Análise Estatística do Impacto de Fertilizantes")
            st.markdown("""
    <div style='display: flex; gap: 10px;'>
        <span style='font-size: 14px; color: #FFFFFF; background-color: #007BFF; padding: 5px; border-radius: 5px;'>Python</span>
        <span style='font-size: 14px; color: #FFFFFF; background-color: #28A745; padding: 5px; border-radius: 5px;'>R</span>
    </div>
    """, unsafe_allow_html=True)
            st.write("")
            st.markdown(""" <div style='text-align: justify;'> Este é um projeto de análise estatística que visa verificar o impacto de diferentes fertilizantes em uma produção agrícola.
                    Para isto utilizei técnicas como a ANOVA e o Teste de Dunnett para comparação das médias dos tratamentos. </div> """, unsafe_allow_html=True)
            st.markdown("[Saiba mais](https://github.com/lll-lucas/Outro-Projeto)") 
        st.write("---")

if selected == "Contato":
    st.header("Entre em contato por aqui!")
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
