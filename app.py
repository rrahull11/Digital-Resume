from pathlib import Path

import streamlit as st
from PIL import Image


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"res.pdf"
profile_pic = current_dir/"assets"/"dp.png"

# general settings

Page_title = "Resume | Rahul Vishwakarma"
Page_icon = ":wave:"
name = "Rahul Vishwakarma"
description = "A lifelong learner aiming to excel my skills in devlopment"
email = "rahulvishwakarma7a@gmail.com"
SOCIAL_MEDIA = {"Youtube" : "https://www.youtube.com/channel/UCgNJVmXVMi6P6-LMe3xWVgw",
                "Linked In" : "https://www.linkedin.com/in/rrahull11/",
                "Github" : "https://github.com/rrahull11"
                }

PROJECTS = "Face Recognition Model"

st.set_page_config(page_title=Page_title,page_icon=Page_icon)

# LOAD CSS,PDF & PROFILE PIC---

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)


# HERO SECTION

col1,col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=230)

with col2:
    st.title(name)
    st.write(description)
    st.download_button(
        label="📄 Download Resume",
        data = PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",   
    )
    st.write("Email",email)

    # SOCIAL LINKS

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index,(platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# Experience
        
st.subheader("Experience & Qualification")
st.write(""" 
- 🟢 Excellent team-player and displaying strong sense of initiative on tasks
- 🟢 Strong hands on DSA, solved more than 100000 questions on Leetcode
- 🟢 Apart from tech-skills I Worked as a Video Editor with India's biggest tech-creator TECH BURNER 
 """)
st.write("---")
st.write("#")
st.subheader("Hard Skills")
st.write(""" 
- 👨‍💻 Programming : CPP, Python, Java
- 📂 Databases   : MYSQL
- ✍️ UI/UX       : Figma
 """)