import streamlit as st 
import cv2
import AnalyzerModule as pm
import numpy as np
import mediapipe as mp
import tempfile
import os
import time

import matplotlib.pyplot as plt
from ffmpy import FFmpeg

st.set_page_config(
    page_title="Basetball name",
    page_icon= "🏀",
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
- You have your posture reviewed!
    - analysis + score of shot on the same page''')


