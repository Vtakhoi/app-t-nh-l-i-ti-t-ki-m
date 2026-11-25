
import streamlit as st

# Cấu hình trang web
st.set_page_config(
    page_title="Tính lãi đơn và lãi kép",
    page_icon="💰",
    layout="centered"
)

# Tiêu đề ứng dụng
st.title("💰 TÍNH LÃI ĐƠN VÀ LÃI KÉP")
st.write("Ứng dụng tính toán số tiền khách hàng nhận được khi gửi tiết kiệm.")

st.divider()

# Nhập dữ liệu
st.subheader("1. Nhập thông tin gửi tiết kiệm")

C = st.number_input(
    "Số tiền gửi ban đầu (đồng)",
    min_value=0,
    value=100_000_000,
    step=10_000_000,
    format="%d"
)

i_percent = st.number_input(
    "Lãi suất mỗi năm (%)",
    min_value=0.0,
    value=1.0,
    step=0.1
)

n = st.number_input(
    "Thời gian gửi (năm)",
    min_value=0,
    value=3,
    step=1
)

# Chuyển lãi suất từ phần trăm sang số thập phân
i = i_percent / 100

# Nút tính toán
if st.button("TÍNH TOÁN", type="primary"):

    # Tính lãi đơn
    An = C * (1 + i * n)

    # Tính lãi kép
    Bn = C * ((1 + i) ** n)

    # Hiển thị kết quả
    st.divider()
    st.subheader("2. Kết quả tính toán")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Số tiền nhận được (Lãi đơn)",
            value=f"{An:,.0f} đồng"
        )

    with col2:
        st.metric(
            label="Số tiền nhận được (Lãi kép)",
            value=f"{Bn:,.0f} đồng"
        )

    # So sánh kết quả
    chenhlech = Bn - An

    st.divider()
    st.subheader("3. So sánh")

    st.write(
        f"Số tiền chênh lệch giữa lãi kép và lãi đơn: "
        f"**{chenhlech:,.0f} đồng**"
    )

    if Bn > An:
        st.success("Lãi kép mang lại số tiền cao hơn lãi đơn.")
    elif Bn < An:
        st.info("Lãi đơn mang lại số tiền cao hơn lãi kép.")
    else:
        st.info("Hai phương thức có số tiền nhận được bằng nhau.")

    # Công thức tính
    with st.expander("Xem công thức tính toán"):
        st.write("**Lãi đơn:**")
        st.latex(r"A_n = C(1 + i \times n)")

        st.write("**Lãi kép:**")
        st.latex(r"B_n = C(1+i)^n")
