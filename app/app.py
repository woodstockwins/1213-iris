import streamlit as st
import plotly.express as px
import numpy as np
import pickle
import time
from predict import predict_flower

# streamlit run "/Users/genebob/Dropbox/test/app.py"
# network url should allow you to run from any browser

st.title('Iris Species Predictor')
# start by clickling 'always rerun'
# st.header("Let's predict Iris species")
st.subheader('Cool app, huh?')

@st.cache()
def read_data():
    return px.data.iris()

df_iris = read_data()

# hist_sl = px.histogram(df_iris, x='sepal_length')
# hist_sl

show_df = st.checkbox("Do you want to see the data?")

if show_df:
    df_iris

sl = st.number_input("Sepal Length {cm}", 0, 100)
sw = st.number_input("Sepal Width {cm}", 0, 100)
pl = st.number_input("Petal Length {cm}", 0, 100)
pw = st.number_input("Petal Width {cm}", 0, 100)


# pw

# st.write(sl)
# sl

user_input = np.array([sl, sw, pl, pw])
user_input

# with context block to open a file and load it with pickle
with open("saved-iris-model.pkl", 'rb') as f:
    classifier = pickle.load(f)

with st.spinner("Predicting your iris species..."):
    time.sleep(2)
    prediction = predict_flower(classifier, user_input)
    prediction

st.header(f"The model predicts: {prediction[0]}!")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col2:
    if prediction[0] == 'setosa':
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    else:
        st.header("A owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")
        st.balloons()

with col3:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")


#
# st.sidebar.button("Click here for balloons!")
# st.balloons()

