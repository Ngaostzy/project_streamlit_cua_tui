import streamlit as st

#Ẩn hiển thị auto sidebar không cần thiết
hide_sidebar_nav = """
<style>
[data-testid="stSidebarNavItems"] {
    display: none !important;
}
</style>
"""

st.markdown(hide_sidebar_nav, unsafe_allow_html=True)


st.sidebar.header('Menu')
st.sidebar.page_link('app.py', label= 'Điều hướng')
st.sidebar.page_link('pages/bieu_do.py', label= 'Biểu đồ')
st.sidebar.page_link('pages/nguoi_dung.py', label= 'Người dùng')
st.sidebar.page_link('pages/bt_menu.py', label='Menu chọn đồ ăn')

st.header('🍗Menu KFC Mini🏚️')
menu={}
col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        with st.form('Menu chọn đồ ăn'):
            st.subheader('🏩Chọn món ăn: ')
            menu['chicken'] = st.number_input('Gà rán', min_value=0, max_value=10, step=1)
            menu['hamburger'] = st.number_input('Hamburger', min_value=0, max_value=10, step=1)
            menu['potatoes'] = st.number_input('Khoai tây chiên', min_value=0, max_value=10, step=1)
            menu['pepsi'] = st.number_input('Pepsi', min_value=0, max_value=10, step=1)
            menu['ice cream'] = st.number_input('Kem', min_value=0, max_value=10, step=1)
            submit = st.form_submit_button('Hoàn tất order')


gia = {
    'chicken': 40000,
    'hamburger': 50000,
    'potatoes': 15000,
    'pepsi': 10000,
    'ice cream': 10000
}

tong_cong = sum(menu[item] * gia[item] for item in menu)    

with col2: 
    with st.container(border=True):
        st.subheader('💴Hóa đơn của bạn')
        st.table(data=menu)
        st.write(f"💰Tổng cộng: {tong_cong:,.0f}")
        thanh_toan = st.button('Thanh toán')
        if thanh_toan:
            st.success('Đã thanh toán thành công, cảm ơn quý khách ❤️')


