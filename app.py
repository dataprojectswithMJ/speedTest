import streamlit as st
import pyspeedtest
import random

st.set_page_config(page_title='WASD Gaming',
                   page_icon=':video_game:')

st.image('TEST.jpg')
st.markdown("<h1 style='text-align: center; color: white;'>The platform that will make gaming accessible to "
            "everyone</h1>", unsafe_allow_html=True)

# st.subheader('The platform that will make gaming accessible to everyone')

st.markdown('-----')


# @st.cache
def speed():
    return int(round(pyspeedtest.SpeedTest(host='www.google.com').ping(), 2))


# @st.cache
def npc_speed():
    return random.randint(10, 71)


player_speed = speed()
npc = npc_speed()

st.write('Before you can begin your gaming experience, we want to test your network speed in order for us to '
         'match you to the best gameplay.')

st.write("")
st.write('Maximum acceptable latency: 100ms')

testBtn = st.button('RUN SPEED TEST')

if testBtn:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Your network strength')
        st.metric('Latency', f'{player_speed}ms')

    with col2:
        st.subheader('AI network strength')
        st.metric('Latency', f'{npc}ms')

    if player_speed >= 100:
        st.error('Your connection cannot hold')

    elif player_speed <= npc:
        st.success('Your connection is top tier')

    else:
        st.warning('Your connection is sufficient. We will level it out for you during gameplay')
