import streamlit as st
import random

# App page settings
st.set_page_config(page_title="Would You Rather", page_icon="🤔", layout="centered")

# Custom styles for mobile look and big buttons
st.markdown("""
    <style>
    .main { text-align: center; direction: rtl; }
    div.stButton > button:first-child {
        width: 100%;
        height: 70px;
        font-size: 20px !important;
        font-weight: bold;
        border-radius: 15px;
        color: white;
        margin-bottom: 10px;
    }
    /* Colors for buttons */
    .blue-btn div.stButton > button:first-child { background-color: #1A73E8; }
    .red-btn div.stButton > button:first-child { background-color: #D93025; }
    </style>
""", unsafe_allow_html=True)

st.title("🤔 لو خيروك؟ 🤔")
st.write("---")

# Group questions
questions = [
    ("تطرد فاطمة من الكروب 🚷", "لو تطرد فاطمة من الكروب 🤫"),
    ("فاطمة تتزوج سيف الهنداوي 💍", "لو تتزوج معمر صكلاوية 🤵"),
    ("زينب تحب عبدالله ❤️", "لو عبدالله يحب زينب 🏹"),
    ("زهراء ناصبه علينه 🕵️‍♀️", "لو زهراء ناصبه علينه 🤡"),
    ("أبو علاوي يحب النساء؟ 🧔", "لو أبو علي يحب النسوان ؟ 🕶️"),
    ("محمد يريد يتزوج ؟ 🤵‍♂️", "لو يريد يتزوج 💍")
]

# Session state to keep track of the current question
if 'current_q' not in st.session_state:
    st.session_state.current_q = random.choice(questions)

# Display the options
q1, q2 = st.session_state.current_q

col1 = st.container()
with col1:
    st.markdown('<div class="blue-btn">', unsafe_allow_html=True)
    if st.button(q1, key="btn1"):
        st.session_state.current_q = random.choice(questions)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("### **أو**")

col2 = st.container()
with col2:
    st.markdown('<div class="red-btn">', unsafe_allow_html=True)
    if st.button(q2, key="btn2"):
        st.session_state.current_q = random.choice(questions)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.caption("Made by Ameen Al-Halbousi")