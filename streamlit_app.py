import streamlit as st
import pandas as pd
from nasa import make_neows_dataframe, get_hazardous_proportion

with open('style.css') as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

data_asteroids = make_neows_dataframe()

st.title("NASA informative dashboard")
st.markdown('''---''')

#Row A
st.markdown(''' ## Near Earth Object Metrics''')
col1, col2, col3 = st.columns(3)
col1.metric("Hazardous Asteroid Proportion", str(round(get_hazardous_proportion(data_asteroids)*100,2)) + "%")
col2.metric("Average Velocity", str(round(pd.to_numeric(data_asteroids['Velocity']).mean(),2)) + " km")
col3.metric("Average Diameter", str(round(pd.to_numeric(data_asteroids['Diameter']).mean(),2)) + " km")
st.markdown('''---''')
