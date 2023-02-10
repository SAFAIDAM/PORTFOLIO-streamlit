

# importing streamlit
import requests
import streamlit as st
from streamlit_lottie import st_lottie
# load assets


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl(
    "https://assets3.lottiefiles.com/packages/lf20_glp2wakj.json")


# title of the page web

st.set_page_config(page_title='MY PORTFOLIO', page_icon=':tada', layout='wide')
st.title('HELLO, MY NAME IS :wave:')
st.title('Safa Idam hamed:')
st.title('A Front-end developer from Morocco:woman:')
st.write('HI,sranger!:smile:,i am safa i am passionate about digital products that help people experience everyday life, :computer:not endure it.')
st.write(':point_down:')
st.write('[find my github here](https://github.com/SAFAIDAM):link:')
st.write('---')

# my description
st.title('WHAT I DO:bulb:')
st.write('##')
st.write(
    """ 
  From understanding your requirements, designing a
  blueprint and delivering the final product, I do 
  everything that falls in between these lines. """)
st.header('WEB DEVELOPMENT')
st.write("If you are lookig for developer who'll take over the research and ")
st.write(
    "development of your website, I am a well-established professional to help you with this"
)
st.header('UI/UX DESIGN')
st.write("An effective UI/UX is what captures attention and spreads a clear message.")
st.write("I make sure the design is innovative and neat with all of this.")

st.write('---')


# defining skills
st.title("SKILLS")
st.header('html 90%')
st.header('css 90%')
st.header('js 10%')
st.header('python 20%')
st.header('illustrator 95%')
st.header('photoshop 80%')

st.write('---')

# contact form

st.write('contact me here :wave:')
st.write('idamhamedsafa@gmail.com')
