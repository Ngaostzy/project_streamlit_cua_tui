##Thiết kế và mô phỏng Dashboard quản trị (Admin Dashboard)

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
st.sidebar.page_link('Bai_tap_2.py', label= 'Điều hướng')
st.sidebar.page_link('pages/bieu_do.py', label= 'Biểu đồ')
st.sidebar.page_link('pages/nguoi_dung.py', label= 'Người dùng')
st.sidebar.page_link('pages/bt_menu.py', label='Menu chọn đồ ăn')
st.header('📊Admin Dashboard')




#Thành phần cột
col1, col2, col3, col4 = st.columns(4)

with col1: 
    st.metric('Real-time Income', 'VND 12.5M', '9%')
with col2: 
    st.metric('Amount of users', 327, '10%')
with col3: 
    st.metric('Amount of orders', 142, '-1%')
with col4: 
    st.metric('Amount of visits', '1.4 M', '-3%')

col5, col6 = st.columns(2)
with col5:
    data_doanh_thu = [100_000_000, 200_000_000, 300_000_000, 150_000_000, 
                      120_000_000, 130_000_000, 400_000_000, 350_000_000]
    
    # 2. Tạo các nhãn cho trục X (giả sử 8 ngày)
    labels_ngay = [f'Ngày {i+1}' for i in range(len(data_doanh_thu))]
    
    # 3. Tạo DataFrame
    df_doanh_thu = pd.DataFrame({
        'Doanh thu (VND)': data_doanh_thu,  # Đây sẽ là nhãn trục Y
        'Ngày': labels_ngay
    })
    
    # 4. Đặt 'Ngày' làm index (nhãn trục X)
    df_doanh_thu = df_doanh_thu.set_index('Ngày')

    st.subheader('Doanh thu 7 ngày gần nhất')
    st.line_chart(df_doanh_thu) # 5. Vẽ từ DataFrame
with col6: 
    data_don_hang = [200, 100, 400, 500, 200, 300, 150, 120, 450, 220, 110]
    
    # 2. Tạo nhãn cho các trạng thái (giả sử)
    labels_trang_thai = [
        'Chờ xử lý', 'Đang xử lý', 'Đã xác nhận', 'Đang giao', 'Đã giao',
        'Hoàn tất', 'Đã hủy', 'Trả hàng', 'Thất bại', 'Đang thanh toán', 'Khác'
    ]
    
    # 3. Tạo DataFrame
    df_don_hang = pd.DataFrame({
        'Số lượng đơn': data_don_hang, # Đây sẽ là nhãn trục Y
        'Trạng thái': labels_trang_thai
    })
    
    # 4. Đặt 'Trạng thái' làm index (nhãn trục X)
    df_don_hang = df_don_hang.set_index('Trạng thái')

    st.subheader('Số lượng đơn hàng theo trạng thái')
    st.bar_chart(df_don_hang) # 5. Vẽ từ DataFrame



