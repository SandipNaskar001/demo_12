import streamlit as st

name= st.text_input("Enter Your name ")
fname=st.text_input(" Enter your Father name")
ad=st.text_area("Enter Your address")
classdata= st.selectbox("Enter Your class :",(1,2,3,4,5))
button = st.button("Done")
if button :
    st.markdown (f""" 
                 Name--> {name}
                 Father Name--> {fname}
                 address--> {ad}
                 class--> {classdata}""")