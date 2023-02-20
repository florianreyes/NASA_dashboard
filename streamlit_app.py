import streamlit as st
import pandas as pd
from nasa import make_neows_dataframe, get_hazardous_proportion,URL_NEOWS, get_data

data_asteroids = make_neows_dataframe(get_data(URL_NEOWS))

with open('style.css') as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


st.title("🌎 NASA informative dashboard")
st.markdown('''---''')

#Row A
st.markdown(''' ## Near Earth Object Metrics''')
col1, col2, col3 = st.columns(3)
col1.metric("Hazardous Asteroid Proportion", str(round(get_hazardous_proportion(data_asteroids)*100,2)) + "%")
col2.metric("Average Velocity", str(round(data_asteroids['Velocity'].mean())) + " km")
col3.metric("Average Diameter", str(round(data_asteroids['Diameter'].mean(),2)) + " km")
st.markdown('''---''')

#Row B

c1,c2 = st.columns(2)
data_diameter = data_asteroids.groupby(data_asteroids['Date'])['Diameter'].mean()
data_velocity = data_asteroids.groupby(data_asteroids['Date'])['Velocity'].mean()

with c1: 
    st.markdown(''' ### Average Diameter (km)''')
    st.line_chart(data_diameter)

with c2: 
    st.markdown(''' ### Average Velocity (km/h)''')
    st.line_chart(data_velocity)
