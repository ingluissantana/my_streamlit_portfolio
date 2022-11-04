import requests
import streamlit as st
from streamlit_lottie import st_lottie
from bokeh.models.widgets import Div


st.set_page_config(
    page_title="Luis Santana Portfolio Page",
    page_icon=":boy:",
    layout="wide",
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


#  To get rid of the Streamlit branding stuff
local_css("css/styles.css")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#  Anchor
st.title("#")  # This anchor is needed for the page to start at the top when it is called.

# --- INTRO ---
with st.container():
    col1, col2 = st.columns((2, 1))
    with col1:
        st.title("Welcome to my Portfolio Page!")
        st.subheader("Hi, I am Luis :)")
        st.subheader(
            """
            I'm a Munich-based *Service Engineer* with a passion for *Data Analysis* and *Machine Learning*.
            """
        )
        st.write("""""")
        st.subheader(
            """
            This page is actually made with Python :snake: and the associated Streamlit library. The purpose of this library is mainly data science and in this case, it showcase how even with no knowledge of Web Development you can make a nice looking portfolio page with pure Python code.
            """
        )
    with col2:
        st_lottie(
            load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_npd3g4ks.json"),
            height=500,
        )

# --- ABOUT ---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st_lottie(
            load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_iqbweiiz.json"),
            height=500,
        )
    with col2:
        st.header("About")
        st.write(
            """
            I have been learning Python since almost one year and at the moment, I am able to create some portfolio projects.
            
            Short facts & milestones:
            - Self-Learning Python using free resources (as MOOCs) and books.
            - Electronic Engineer.
            - 8+ years of professional experience in various companies as a Field Service Engineer.
            - Enthusiasm for data science, machine learning, beachvolleyball and making music.
            If you are interested in building something together, have questions/suggestions about my code or just wanna connect, feel free to get in touch with me! 
            """
        )


# --- TECH STACK / SKILLS ---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Tech Stack / Skills")
        st.write(
            """
            Languages
            - Python
            Frameworks
            - Pandas, Streamlit, Scikit-learn
            Databases
            - MySQL (learning)
            Hosting & Cloud
            - Streamlit Cloud
            Miscellaneous
            - Github, Tableau
             """
        )

    with col2:
        st_lottie(
            load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_esw9ibjj.json"),
            height=500,
        )

# --- PORTFOLIO ---
with st.container():
    st.write("---")
    st.header("Portfolio")
    st.write("##")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://img.freepik.com/free-photo/close-up-man-writing-code-laptop_158595-5169.jpg?w=2000&t=st=1664902081~exp=1664902681~hmac=eb52218837e2e3dc35453544a82a190ec616c1ce87b9c012b489e28a4dfde7aa")
        st.subheader("Munich bike sharing analysis")
        st.write("Basic analysis of the 2021 data from the Munich bike sharing model (data: www.mvg.de). This project was meant to learn to clean data and to visualize data using Tableau.")
        if st.button('Enter Visualization', key="ews_enter"):
            js = "window.open('https://public.tableau.com/views/Munichbikesharing/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.write('Web Application opens in new browser tab')
            st.bokeh_chart(div)
        if st.button('Github', key="ews_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/ingluissantana/Munich_bike_rental')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    with col2:
        st.image("https://img.freepik.com/free-photo/close-up-man-writing-code-laptop_158595-5169.jpg?w=2000&t=st=1664902081~exp=1664902681~hmac=eb52218837e2e3dc35453544a82a190ec616c1ce87b9c012b489e28a4dfde7aa")
        st.subheader("Music Scales and Harmonic Fields")
        st.write("This projects came from a real need as a guitarrist. The software let the user select a Key and it returns all the scales and the harmonic fields related to it.")
        if st.button('Enter App', key="gee_enter"):
            js = "window.open('https://bit.ly/3e6ZsbO')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.write('Web Application opens in new browser tab')
            st.bokeh_chart(div)
        if st.button('Github', key="gee_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/ingluissantana/Scales')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    with col3:
        st.image("https://img.freepik.com/free-photo/close-up-man-writing-code-laptop_158595-5169.jpg?w=2000&t=st=1664902081~exp=1664902681~hmac=eb52218837e2e3dc35453544a82a190ec616c1ce87b9c012b489e28a4dfde7aa")
        st.subheader("German analysis")
        st.write("This is a NLP project that analyzes German text.")
        if st.button('Enter App', key="egn_enter"):
            js = "window.open('https://bit.ly/3FOTmIq')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.write('Web Application opens in new browser tab')
            st.bokeh_chart(div)
        if st.button('Github', key="egn_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/ingluissantana/Learning_german')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

# --- CONTACT ---
with st.container():
    st.write("---")
    st.markdown("<h2 style='text-align: center;'>Contact</h2>", unsafe_allow_html=True)
    st.write("##")

    col1, col2, col3 = st.columns(3)
    with col2:
        contact_form = """
            <form action="https://formsubmit.co/ingluissantana@gmail.com" method="POST">
                <input type="hidden" name="_captcha" value="true">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message" required></textarea>
                <button type="submit">Send</button>
            </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

with st.container():
    for i in range(8):
        st.write("##")
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.write(
            """
            
            """
        )
    with col2:
        st.markdown("<p style='text-align: right;'>Made in 2022 with ❤, 🐍 and Streamlit</p>", unsafe_allow_html=True)
    st.write("---")