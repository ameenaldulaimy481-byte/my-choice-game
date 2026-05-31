import streamlit as st
from datetime import datetime, timedelta

# تنسيق الصفحة
st.set_page_config(page_title="دعوة زفاف زينب وعبدالله", page_icon="💍")

# ألوان وتنسيقات عصرية (CSS)
st.markdown("""
    <style>
    .main {background-color: #FDFBF7;}
    .invite-card {
        background-color: #FFFFFF;
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        text-align: center;
        border: 2px solid #D4AF37;
    }
    .title {color: #8B7355; font-size: 40px; font-weight: bold; font-family: 'Arial';}
    .text {color: #555; font-size: 18px; line-height: 1.6;}
    </style>
""", unsafe_allow_html=True)

# حساب التاريخ
wedding_date = (datetime.now() + timedelta(days=7)).strftime("%d / %m / 2026")

# الحالة
if 'open' not in st.session_state:
    st.session_state.open = False

# واجهة البداية (عصرية)
if not st.session_state.open:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💍 افتح ظرف الدعوة", use_container_width=True):
            st.session_state.open = True
            st.rerun()
else:
    # واجهة الدعوة (ستايل بينترست)
    st.markdown("""
    <div class="invite-card">
        <h1 class="title">دعوة زفاف</h1>
        <p class="text">بكل مودة وحب، ندعوكم لمشاركتنا فرحتنا</p>
        <h2 style="color: #D4AF37;">زينب ❤️ عبدالله</h2>
        <hr>
        <p class="text"><b>التاريخ:</b> """ + wedding_date + """</p>
        <p class="text"><b>المكان:</b> بغداد - العامرية - قاعة الزمرد</p>
        <br>
        <h3 style="color: #8B7355;">تنورونا وتشرفونا</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.warning("⚠️ ملاحظة: نعتذر عن استقبال فاطمة في الحفل")
