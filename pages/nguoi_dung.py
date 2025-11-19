import streamlit as st
import json

##Thiết kế và mô phỏng Dashboard quản trị (Admin Dashboard)
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
st.header('📊Nhập thông tin cá nhân')


if 'lst_nguoi_dung' not in st.session_state:
    st.session_state.lst_nguoi_dung = []
options_so_thich = ['Đọc sách', 'Chơi game', 'Đá bóng', 'Cầu lông', 'Bóng rổ']
nguoi_dung = {}

if 'lst_tuoi' not in st.session_state:
    st.session_state.lst_tuoi = []
    

with st.form('Nhập thông tin cá nhân'):
    nguoi_dung['ho_ten'] = st.text_input('Họ và tên: ')
    nguoi_dung['tuoi'] = st.text_input('Tuổi: ')
    nguoi_dung['gender'] = st.radio(
        'Giới tính: ', 
        ['Nam', 'Nữ', 'Khác']
        )
    nguoi_dung['so_thich'] = st.multiselect('Sở thích',
                   options_so_thich,
                   default=['Đọc sách', 'Chơi game']
                   )
    

    submit = st.form_submit_button('Hoàn tất')

if submit: 
    st.session_state.lst_nguoi_dung.append(nguoi_dung)
    if nguoi_dung['tuoi'] != '':
        st.session_state.lst_tuoi.append(int(nguoi_dung['tuoi']))
    st.markdown(f"""
Thông tin bạn vừa nhập là: <br>
Họ và tên: {nguoi_dung['ho_ten']} <br>
Tuổi: {nguoi_dung['tuoi']} <br>
Giới tính: {nguoi_dung['gender']} <br>
Sở thích: {" , ".join(nguoi_dung['so_thich'])}
                """, True)



with open ('data_nguoi_dung.json', 'w', encoding='utf-8') as json_file:
    json.dump(st.session_state.lst_nguoi_dung, json_file, ensure_ascii = False)




st.line_chart(st.session_state.lst_tuoi)





