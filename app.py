import time
import streamlit as st
import pyspeedtest
import random

st.set_page_config(page_title='WASD Gaming',
                   page_icon=':video_game:')

st.image('TEST.jpg')
st.markdown("<h1 style='text-align: center; color: white;'>The platform that will make gaming accessible to "
            "everyone</h1>", unsafe_allow_html=True)

host = 'c.speedtest.net'

st.markdown('-----')


def speed():
    return int(round(pyspeedtest.SpeedTest(host=host).ping(), 2))


def npc_speed():
    return random.randint(30)


player_speed = speed()
npc = npc_speed()
speedDifference = player_speed - npc

placeholder = st.empty()
placeholder2 = st.empty()
placeholder3 = st.empty()

with placeholder.container():
    st.write('Before you can begin your gaming experience, we want to test your network speed in order for us to '
             'match you to the best gameplay.')

    st.write('If your internet speed is slower than your opponents, we will automatically calibrate it after this '
             'speed test.')

    st.markdown('#### Maximum acceptable latency *200ms*')

    testBtn = st.button('Begin speed test')

    if testBtn:

        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Your network strength')
            if player_speed < npc:
                st.metric('Latency', f'{player_speed}ms',
                          delta=f'{npc - player_speed}ms faster than opponent')  # , delta_color="inverse")
            else:
                st.metric('Latency', f'{player_speed}ms',
                          delta=f'-{player_speed - npc}ms slower than opponent')  # , delta_color="inverse")

        with col2:
            st.subheader('AI network strength')
            if npc < player_speed:
                st.metric('Latency', f'{npc}ms', delta=f'{player_speed - npc}ms faster than you')
            else:
                st.metric('Latency', f'{npc}ms', delta=f'-{npc - player_speed}ms slower than you')

        if player_speed >= 200:
            time.sleep(1)
            st.error('Your connection cannot hold')


        elif player_speed <= npc:
            time.sleep(1)
            st.success('Your connection is top tier')
            time.sleep(0.5)
            st.success('You are good to go')


        else:
            time.sleep(1)
            st.warning('Your network needs calibration.')
            time.sleep(1)

            st.info(f'Sending and receiving 1MB data packet for optimization task...')
            for x in range(speedDifference, 0, -2):
                placeholder2.markdown(f'### Latency rate: **{x}ms**')
                time.sleep(x/ 10)
                new_ping = x
            time.sleep(2)

            with placeholder2.container():
                my_bar = st.progress(0)
                for percent_complete in range(100):
                    time.sleep(0.05)
                    my_bar.progress(percent_complete + 1)
                time.sleep(1)
            placeholder2.empty()

            st.success('Calibration complete and successful')

            time.sleep(1)

            st.metric('New Gameplay latency', f'{npc}ms', delta=f'{player_speed - npc}ms faster')
