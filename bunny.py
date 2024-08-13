import requests
from PIL import Image
import streamlit as st
import streamlit_lottie as st_lottie

st.set_page_config(page_title="Mills Yamoah Portfolio" , layout= "wide")


img2 = Image.open("/Users/millsyamoah/anaconda3/bin/download-2.png")
img_contact_form = Image.open("/Users/millsyamoah/anaconda3/bin/myenv/download.png")

def first(text):
    return text.capitalize() if text else ""


nameofp =st.text_input(label="Whats Your Name?")
snap = first(nameofp)
newnop = "Thank You " + snap + "!"

with st.container():
    st.subheader("Hi, I am Mills:")
    st.title("A Texas Tech Computer Science Honors Student")
    st.write("I have a strong desire to become a software engineer and a deep passion for writing, especially in Python and C++. These languages marked the beginning of my adventure into the world of programming, where I fell in love with the challenge of delving into intricate issues and creating scalable, effective solutions. Combining C++'s strength and performance with Python's ease of use and adaptability has given me a solid foundation in both high-level and low-level programming.")
    st.write("My Projects")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("About Me")
        st.write("##")
        st.write(
            """
            My Background
            - Excel in coding with the programming languages of Python and C++
            - Completed data structures and computational thinking courses.
            - Have knowledgeable about data analysis and coding utilizing Jupyter Lab and Visual Studio Code (VS Code).
            - Took part in the NASA L'SPACE program, where they learned a lot about space-related tasks and acquired significant experience.
            - I'm in the honors program right now.

            """
        )

    with right_column:
        st.image(img2)
                  
            

with st.container():
    st.write("---")
    st.header("My Project")
    st.write("##")
    image_column , text_column = st.columns((1,3))
    with image_column:
        st.image(img_contact_form)


    with text_column:
        st.subheader(" Rate My Proffesor")
        st.write(
            """

            In this project , I coded in Python on the platform Jupyter Lab.
            I extracted the grade distrubution from the Texas Tech website,
            and used the Pandas Library to interept the information and graph
            which teachers have the best grades. With this information it gives 
            you the best teacher for the subject.
            """
        ) 
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    ctf = """
    <form action="https://formsubmit.co/myamoah@ttu.edu" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder = Mills Yamoah required>
        <input type="email" name="email" placeholder = myamoah@ttu.edu required>
        <button type="submit">Send</button>
    </form>
    """

    left_column,right_column =st.columns(2)
    with left_column:
        st.markdown(ctf,unsafe_allow_html=True)
    with right_column:
      st.empty()    



with st.container():
    st.write("---")
    st.subheader(newnop)