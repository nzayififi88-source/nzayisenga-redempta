import numpy as np
import pickle
import streamlit as st

with open('Save.pkl','rb') as file:
    Model=pickle.load(file)
st.title("Student performance analysis")
st.write("Fill the student behaviours below:")
st_hours=st.number_input("STtdying hours")
st_attend=st.number_input("Attendance")
st_part=st.number_input("Participation")

if st.button("Grade"):
    input_=np.array([[st_hours,st_attend,st_part]])
    Pred=Model.predict(input_)
    st.success(Pred[0])