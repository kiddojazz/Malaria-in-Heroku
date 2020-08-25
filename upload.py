import streamlit as st 
from PIL import Image
from classify import predict

def converter(value):
    if value == 0:
        return "infected"
    else:
        return "uninfected"

st.title("Upload + MALARIA IMAGE")
st.text("NAME : OMONIYI TEMIDAYO ANDREW")
st.text("TEAM : TEAM WAKANDA")
st.text("EMAIL: omoniyiandrewai@gmail.com, kiddojazz@gmail.com")
st.text("NO:    +2348166220117")
html_temp="""
<div style="background-color:gray;padding:15px;">
<h2>RGB IMAGE OF BLOOD SAMPLE</h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose an image...", type=("jpeg","jpg","png"))
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    converter = predict(uploaded_file)
    st.write('I THINK:', converter)




