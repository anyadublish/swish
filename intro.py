import streamlit as st 
import cv2
import AnalyzerModule as pm
import numpy as np
import mediapipe as mp
import tempfile
import os
import time
import base64

import matplotlib.pyplot as plt
from ffmpy import FFmpeg

st.set_page_config(
    page_title="Basetball name",
    page_icon= "🏀",
)

st.markdown(
        '''<style>
        body{
            background-image: url(https://www.google.com/imgres?imgurl=https%3A%2F%2Ft3.ftcdn.net%2Fjpg%2F05%2F70%2F06%2F64%2F360_F_570066449_SS8sx5K4ZsYXCcXvR014q2prysMs1kf2.jpg&tbnid=coVR4L5VbrryiM&vet=12ahUKEwiWh5uHv9GBAxXycmwGHcGeC_gQMygKegUIARCCAQ..i&imgrefurl=https%3A%2F%2Fstock.adobe.com%2Fsearch%3Fk%3Dbasketball%2Bwallpaper&docid=yZGhP2qPk-WQxM&w=540&h=360&q=basketball&client=safari&ved=2ahUKEwiWh5uHv9GBAxXycmwGHcGeC_gQMygKegUIARCCAQ);
            background-attachment: fixed;
            background size: cover
        }
        </style>
        ''',
        unsafe_allow_html=True
    )
st.title("SWISH!")
st.subheader("...for the perfect shot")
st.sidebar.success("Select a page above:")

joints = [pm.SHOULDER_RIGHT,pm.HIP_RIGHT,pm.KNEE_RIGHT,pm.ANKLE_RIGHT,pm.ELBOW_RIGHT]
limbs = [pm.ARM_LOWER_RIGHT,pm.ARM_UPPER_RIGHT,pm.UPPER_BODY_RIGHT,pm.LEG_UPPER_RIGHT,pm.LEG_LOWER_RIGHT, pm.FOOT_RIGHT]

st.markdown('''
What to do: 
- Click the sport you would like to review from the sidepanel
- Wait for the process to run 
- You have your posture reviewed
    - analysis + score of shot!''')

def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack('bb1.jpg')
