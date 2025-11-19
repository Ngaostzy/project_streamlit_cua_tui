import streamlit as st
import pandas as pd 


#Ẩn hiển thị auto sidebar không cần thiết
hide_sidebar_nav = """
<style>
[data-testid="stSidebarNavItems"] {
    display: none !important;
}
</style>
"""

st.markdown(hide_sidebar_nav, unsafe_allow_html=True)

#Sidebar chính edit đẹp
st.sidebar.header('Menu')
st.sidebar.page_link('app.py', label= 'Điều hướng')
st.sidebar.page_link('pages/bieu_do.py', label= 'Biểu đồ')
st.sidebar.page_link('pages/nguoi_dung.py', label= 'Người dùng')
st.sidebar.page_link('pages/bt_menu.py', label='Menu chọn đồ ăn')
st.header('📊Admin Dashboard')




data_doanh_thu = pd.DataFrame({
    'Tháng' : ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12'],
    'Doanh Thu' : [12, 15, 18, 22, 28, 35, 40, 38, 36, 42, 48, 55]
})
st.header('Biểu đồ hiển thị doanh thu')
st.area_chart(data_doanh_thu, x= "Tháng", y='Doanh Thu')