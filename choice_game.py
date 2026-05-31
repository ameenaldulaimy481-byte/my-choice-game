import streamlit as st
from datetime import datetime, timedelta

# إعداد الصفحة
st.set_page_config(page_title="دعوة زفاف", page_icon="💍")

# إخفاء قائمة Streamlit الافتراضية
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# حساب التاريخ (بعد أسبوع من اليوم)
wedding_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

# استخدام session_state لإدارة ظهور الدعوة
if 'show_invite' not in st.session_state:
    st.session_state.show_invite = False

# الواجهة
if not st.session_state.show_invite:
    # تنسيق الزر الدائري
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write("")
        st.write("")
        if st.button("اضغط هنا لفتح الدعوة", use_container_width=True):
            st.session_state.show_invite = True
            st.rerun()
else:
    # محتوى الدعوة
    st.markdown("<h1 style='text-align: center; color: #8B7355;'>دعوة زفاف</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>يتشرف زينب وعبدالله بدعوتكم لحفل زفافهم السعيد</h3>", unsafe_allow_html=True)
    st.write(f"**التاريخ:** {wedding_date}")
    st.write("**الموقع:** بغداد - العامرية")
    st.markdown("<h2 style='text-align: center; color: #8B7355;'>تنورونا وتشرفونا!</h2>", unsafe_allow_html=True)
    
    st.error("ملاحظة: نعتذر عن استقبال فاطمة في الحفل")
