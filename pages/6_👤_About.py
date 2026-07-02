import streamlit as st
from PIL import Image
import os

# -----------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------

st.set_page_config(
    page_title="About Me",
    page_icon="👨‍💻",
    layout="wide"
)

# -----------------------------------------------------
# CUSTOM CSS
# -----------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

.stApp{
    background:linear-gradient(135deg,#0B1120,#111827,#0F172A);
}

/* Hero */

.hero{
    text-align:center;
    padding-top:30px;
    padding-bottom:40px;
}

.hero h3{
    color:#94A3B8;
    font-weight:400;
    letter-spacing:2px;
}

.hero h1{

    font-size:68px;

    font-weight:800;

    margin-top:10px;

    margin-bottom:10px;

    background:linear-gradient(
    90deg,
    #38BDF8,
    #3B82F6,
    #8B5CF6,
    #38BDF8);

    background-size:300%;

    -webkit-background-clip:text;

    -webkit-text-fill-color:transparent;

    animation:gradient 8s linear infinite;

}

@keyframes gradient{

0%{background-position:0%;}

50%{background-position:100%;}

100%{background-position:0%;}

}

.hero p{

font-size:24px;

color:#CBD5E1;

}

/* Floating image */

.float{

animation:float 5s ease-in-out infinite;

}

@keyframes float{

0%{
transform:translateY(0px);
}

50%{
transform:translateY(-15px);
}

100%{
transform:translateY(0px);
}

}

/* Cards */

.card{

background:rgba(255,255,255,.05);

backdrop-filter:blur(18px);

border:1px solid rgba(255,255,255,.08);

border-radius:25px;

padding:30px;

box-shadow:0 15px 35px rgba(0,0,0,.35);

transition:.35s;

}

.card:hover{

transform:translateY(-8px);

box-shadow:0 0 25px rgba(59,130,246,.6);

}

/* Skills */

.skill{

display:inline-block;

padding:10px 18px;

margin:6px;

background:#2563EB;

color:white;

border-radius:30px;

font-weight:600;

transition:.3s;

}

.skill:hover{

background:#38BDF8;

transform:scale(1.08);

}

/* Section Title */

.section{

font-size:34px;

font-weight:700;

margin-top:20px;

margin-bottom:25px;

color:white;

}

/* ===============================
   SKILL CARDS
================================ */

.skill-card{

background:#1C2333;

padding:25px;

border-radius:18px;

border:1px solid rgba(255,255,255,.08);

height:310px;

display:flex;

flex-direction:column;

box-shadow:0 8px 20px rgba(0,0,0,.25);

transition:all .3s ease;

}

.skill-card:hover{

transform:translateY(-6px);

border:1px solid #38BDF8;

box-shadow:0 10px 25px rgba(56,189,248,.30);

}

.skill-card h3{

font-size:30px;

color:#38BDF8;

margin-bottom:10px;

}

.skill-card hr{

border:none;

height:1px;

background:rgba(255,255,255,.08);

margin:10px 0 15px 0;

}

.skill-card ul{

list-style:none;

padding:0;

margin:0;

}

.skill-card li{

font-size:18px;

padding:8px 0;

color:#E5E7EB;

}
/* ==========================================
   PROJECT CARDS
========================================== */

.project-card{

background:rgba(255,255,255,.05);

backdrop-filter:blur(18px);

border:1px solid rgba(255,255,255,.08);

border-radius:20px;

padding:22px;

height:280px;

display:flex;

flex-direction:column;

justify-content:space-between;

transition:.35s;

box-shadow:0 10px 25px rgba(0,0,0,.25);

margin-bottom:25px;

}

.project-card:hover{

transform:translateY(-8px);

border:1px solid #38BDF8;

box-shadow:0 0 25px rgba(56,189,248,.35);

}

.project-title{

font-size:26px;

font-weight:700;

color:#38BDF8;

margin-bottom:12px;

}

.project-desc{

color:#D1D5DB;

line-height:1.7;

margin-bottom:20px;

}

.tech-stack{

margin-top:auto;

}

.tech{

display:inline-block;

background:#2563EB;

color:white;

padding:6px 14px;

border-radius:25px;

margin:4px;

font-size:13px;

font-weight:600;

}

.project-card:hover{

transform:translateY(-8px);

border:1px solid #38BDF8;

box-shadow:0 0 22px rgba(56,189,248,.40);

}

.project-title{

font-size:24px;

font-weight:700;

color:#38BDF8;

margin-bottom:12px;

}

.tech{

display:inline-block;

padding:6px 12px;

margin:4px;

background:#2563EB;

color:white;

border-radius:25px;

font-size:13px;

font-weight:600;

}

.profile-image{
    margin-top:35px;
    
}          



</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# HERO
# -----------------------------------------------------

st.markdown("""
<div class="hero">

<h3>👋 HELLO, I'M</h3>

<h1>Amos Vivek Gaikwad</h1>

<p>
Full Stack Developer • Data Analyst • AI & Machine Learning Enthusiast
</p>

</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# PROFILE SECTION
# -----------------------------------------------------

left, right = st.columns([1,2])

with left:

    if os.path.exists("assets/profile.png"):

        image = Image.open("assets/profile.png")

        st.markdown('<div class="profile-image float">', unsafe_allow_html=True)
        
        st.image(image, width=320)

        st.markdown("</div>", unsafe_allow_html=True)

    else:

        st.warning("Place profile.png inside assets folder")

with right:
    
    
    

    # st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("## About Me")

    st.write("""

I am **Amos Vivek Gaikwad**, a Computer Science Engineering student at **MIT ADT University, Pune**, passionate about **Full Stack Development, Data Analytics, Artificial Intelligence, and Machine Learning**.

I enjoy building scalable web applications, designing interactive dashboards, analyzing data to uncover valuable insights, and developing machine learning solutions that solve real-world business problems.

My experience spans both **software development** and **data-driven applications**, allowing me to combine strong programming skills with analytical thinking to create impactful solutions.

I am passionate about developing innovative software solutions and leveraging data analytics to solve real-world business challenges.

Currently, I am seeking opportunities where I can contribute my technical skills, collaborate with experienced professionals, and continue growing as a Full Stack Developer and Data Analyst.
""")

    st.success("🟢 Open to Data Analytics & Machine Learning Opportunities")

    st.markdown("</div>", unsafe_allow_html=True)

st.write("")
st.write("")



# -----------------------------------------------------
# SKILLS PREVIEW
# -----------------------------------------------------
# =====================================================
# CORE SKILLS
# =====================================================

st.markdown("## Core Skills")
st.write("")

col1, col2 = st.columns(2, gap="large")

# -----------------------------------------------------
# LEFT COLUMN
# -----------------------------------------------------

with col1:

    with st.container(border=True):

        st.markdown("### Programming")

        st.markdown("""
- Python
- Java
- JavaScript
- SQL
- C++
        """)

    st.write("")

    with st.container(border=True):

        st.markdown("### Data Analytics")

        st.markdown("""
- Power BI
- Pandas
- NumPy
- Plotly
- Excel
- Business Intelligence
        """)

# -----------------------------------------------------
# RIGHT COLUMN
# -----------------------------------------------------

with col2:

    with st.container(border=True):

        st.markdown("### Full Stack Development")

        st.markdown("""
- HTML
- CSS
- React
- Streamlit
- REST APIs
        """)

    st.write("")

    with st.container(border=True):

        st.markdown("### AI & Machine Learning")

        st.markdown("""
- Scikit-Learn
- TensorFlow
- Machine Learning
- Predictive Analytics
- Data Visualization
- Model Development
        """)

st.write("")
st.divider()

# =====================================================
# FEATURED PROJECTS
# =====================================================

st.markdown("##  Projects")

st.write("")

col1, col2 = st.columns(2)

# -----------------------------------------------------

with col1:

    st.markdown("""

<div class="project-card">

<div>

<div class="project-title">
Retail Analytics Platform
</div>

<div class="project-desc">
End-to-end retail analytics platform featuring interactive dashboards,
AI-powered sales forecasting and business intelligence insights.
</div>

</div>

<div class="tech-stack">

<span class="tech">Python</span>
<span class="tech">Streamlit</span>
<span class="tech">Power BI</span>
<span class="tech">Prophet</span>
<span class="tech">Plotly</span>

</div>

</div>

</div>

""", unsafe_allow_html=True)

    st.markdown("""

<div class="project-card">

<div>

<div class="project-title">
Gesture Presentation System
</div>

<div class="project-desc">
Computer vision application that allows users to control 
PowerPoint presentations using real-time hand gestures.
</div>

</div>

<div class="tech-stack">

<span class="tech">Python</span>
<span class="tech">OpenCV</span>
<span class="tech">MediaPipe</span>
<span class="tech">PyAutoGUI</span>
<span class="tech">PyMuPDF</span>

</div>

</div>

</div>

""", unsafe_allow_html=True)

# -----------------------------------------------------

with col2:

    st.markdown("""

<div class="project-card">

<div>

<div class="project-title">
Potato Disease Detection
</div>

<div class="project-desc">
Deep Learning application that detects potato leaf diseases 
using CNN models and image classification.
</div>

</div>

<div class="tech-stack">

<span class="tech">Python</span>
<span class="tech">TensorFlow</span>
<span class="tech">Keras</span>
<span class="tech">OpenCV</span>
<span class="tech">Matplotlib</span>

</div>

</div>

</div>

""", unsafe_allow_html=True)

    st.markdown("""

<div class="project-card">

<div>

<div class="project-title">
InstaPrint
</div>

<div class="project-desc">
Online document printing platform connecting students with nearby 
print shops for seamless digital printing services.
</div>

</div>

<div class="tech-stack">

<span class="tech">React</span>
<span class="tech">Node.js</span>
<span class="tech">Express.js</span>
<span class="tech">MongoDB</span>
<span class="tech">Firebase</span>

</div>

</div>

</div>

""", unsafe_allow_html=True)
    
# =====================================================
# EDUCATION
# =====================================================

st.divider()

st.markdown("##  Education")

st.write("")

st.markdown("""

###  MIT ADT University, Pune

**Bachelor of Technology (B.Tech)**

Computer Science & Engineering

 2023 – 2027

 CGPA: **7.8 / 10**

""")

st.write("")

st.markdown("""

### Diploma in Computer Science

Data Science Specialization

Completed

""")

st.divider()

st.markdown("##  Certifications")

c1, c2 = st.columns(2)

with c1:

    st.success("✔ Data Analytics Internship - Unlox")

    st.success("✔ Data Analytics Job Simulation - Deloitte")

    st.success("✔ LinkedIn - Artificial Intelligence Foundations: Machine Learning")


with c2:

    st.success("✔ ServiceNow CSA")

    st.success("✔ Python Programming")
    
    st.success("✔ Python for Data Science - Reliance Foundation Skilling Academy")



st.divider()

st.markdown("##  Let's Connect")

st.write("")

c1, c2, c3 = st.columns(3)

with c1:

    st.link_button(
        "💼 LinkedIn",
        "https://www.linkedin.com/in/amos-gaikwad-6a79b82b0"
    )

with c2:

    st.link_button(
        "🐙 GitHub",
        "https://github.com/amosgaikwad"
    )

with c3:

    st.link_button(
        "📧 Email",
        "mailto:amosgaik16@gmail.com"
    )

st.write("")
st.write("")

st.markdown("---")

st.markdown(
    """
<div style="text-align:center;color:gray;">

Made using Python & Streamlit

<br><br>

© 2026 Amos Vivek Gaikwad

</div>
""",
unsafe_allow_html=True
)