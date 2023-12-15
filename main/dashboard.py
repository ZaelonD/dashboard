import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings

# Игнорируем предупреждения
warnings.filterwarnings("ignore")

# Настраиваем параметры страницы
st.set_page_config(
    page_title="Dashboard",
    page_icon=":bar_chart:",
    layout="wide")

# Настраиваем заголовок
st.title(":bar_chart: Superstore dashboard", anchor=False)
