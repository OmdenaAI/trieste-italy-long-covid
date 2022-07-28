
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd


st.write("Long Covid in Italy")

#df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
#st.write(df)

topics_coherence_handle = open(r'..\task-7-descriptive_data_analysis\final LDA attempt\02_Create pretrained LDA Model on Q1 Data\lda_visualization_6_topics_Q1_data.html', 'r')
topics_coherence = topics_coherence_handle.read()
components.html(topics_coherence, width=500, height=500, scrolling=True)

