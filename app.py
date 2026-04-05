import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Parfumerie Hadek", layout="wide")
st.markdown("<h1 style='text-align: center; color: #E67E22;'>✨ Parfumerie Hadek ✨</h1>", unsafe_allow_html=True)

try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(worksheet="Products")
    
    st.sidebar.title("القائمة")
    menu = st.sidebar.radio("اختار:", ["🛒 البيع", "📦 السطوك"])

    if menu == "🛒 البيع":
        barcode = st.text_input("سكان كودبار المنتج:")
        if barcode:
            item = df[df['Barcode'].astype(str) == str(barcode)]
            if not item.empty:
                st.success(f"المنتج: {item['Name'].values[0]}")
                st.info(f"الثمن: {item['Price'].values[0]} DH")
                if st.button("تأكيد البيع"):
                    st.balloons()
            else:
                st.error("المنتج غير موجود!")
    elif menu == "📦 السطوك":
        st.dataframe(df[['Name', 'Barcode', 'Price', 'Quantity']])
except:
    st.warning("في انتظار ربط الساروت JSON...")
