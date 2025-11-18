import streamlit as st
import clips
import logging

# Setup working environment
logging.basicConfig(level=15, format='%(message)s')

env = clips.Environment()
router = clips.loggingRouter()
env.add_router(router)

#input 
name = st.text input("Enter vour name")

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
