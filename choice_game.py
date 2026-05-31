import streamlit as st

# إعداد الصفحة وتنسيقها
st.set_page_config(page_title="دعوة زفاف", layout="centered")

# تنسيق CSS احترافي (ستايل بينترست ملكي)
st.markdown("""
    <style>
    .stApp {background-color: #fcfcfc;}
    .invite-container {
        background-color: #ffffff;
        border: 2px solid #8B0000;
        padding: 50px;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        background-image: url('https://www.transparenttextures.com/patterns/paper-fibers.png');
    }
    .header-flower {color: #8B0000; font-size: 40px;}
    .main-text {font-family: 'Times New Roman', serif; color: #333; font-size: 22px; line-height: 1.8;}
    .names {color: #8B0000; font-weight: bold; font-size: 32px; margin: 20px 0;}
    .footer-text {margin-top: 40px; color: #555; font-style: italic;}
    </style>
""", unsafe_allow_html=True)

# حالة الزر للفتح
if 'open' not in st.session_state:
    st.session_state.open = False

if not st.session_state.open:
    st.markdown("<br><br><h1 style='text-align:center;'>💍 دعوة زفاف خاصة</h1>", unsafe_allow_html=True)
    if st.button("افتح الدعوة", use_container_width=True):
        st.session_state.open = True
        st.rerun()
else:
    # محتوى الدعوة (التصميم المطلوب)
    st.markdown("""
    <div class="invite-container">
        <div class="header-flower">🌹 وجعل بينكم مودة ورحمة 🌹</div>
        <p class="main-text">
            في العمر أيام يزينها السرور<br>
            وسرور هذا اليوم مُختلف<br><br>
            بصادق الود والمحبة نتشرف<br>
            بدعوتكم لحضور حفل زفاف
        </p>
        <div class="names">فاطمة و معمر صقلاوية</div>
        <div style="font-size: 50px; margin: 20px 0;">🌸</div>
        <p class="main-text">وذلك بمشيئة الله تعالى</p>
        <div style="display: flex; justify-content: space-around; margin-top: 30px;">
            <div>📅<br>التاريخ</div>
            <div>⏰<br>الساعة</div>
            <div>📍<br>المكان</div>
        </div>
        <p class="footer-text">بحضوركم يتم لنا الفرح والسرور</p>
    </div>
    """, unsafe_allow_html=True)
