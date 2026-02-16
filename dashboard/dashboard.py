import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================================
# CONFIG
# =====================================
st.set_page_config(
    page_title="E-Commerce Dashboard",
    layout="wide"
)

# =====================================
# LOAD DATA
# =====================================
@st.cache_data
def load_data():
    df = pd.read_csv("./dashboard/main_data.csv")
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    return df

df = load_data()

# =====================================
# SIDEBAR FILTER
# =====================================
st.sidebar.header("Filter Data")

min_date = df['order_purchase_timestamp'].min()
max_date = df['order_purchase_timestamp'].max()

date_range = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    [min_date, max_date]
)

mask = (
    (df['order_purchase_timestamp'] >= pd.to_datetime(date_range[0])) &
    (df['order_purchase_timestamp'] <= pd.to_datetime(date_range[1]))
)

df = df.loc[mask]

# =====================================
# TITLE
# =====================================
st.title("📊 E-Commerce Executive Dashboard")

st.markdown("""
Dashboard ini dibuat untuk menjawab dua pertanyaan bisnis utama:
1. Bagaimana tren penjualan dari waktu ke waktu?
2. Wilayah mana yang memiliki jumlah pelanggan dan transaksi tertinggi?
""")

st.markdown("---")

# =====================================
# KPI SECTION
# =====================================
col1, col2, col3 = st.columns(3)

total_orders = df['order_id'].nunique()
total_revenue = df['payment_value'].sum()
total_customers = df['customer_unique_id'].nunique()

col1.metric("Total Orders", f"{total_orders:,}")
col2.metric("Total Revenue", f"${total_revenue:,.0f}")
col3.metric("Total Customers", f"{total_customers:,}")

st.markdown("---")

# =====================================
# SECTION 1 — TREND ANALYSIS
# =====================================
st.header("📈 Tren Penjualan")

sales_trend = df.groupby(
    df['order_purchase_timestamp'].dt.to_period('M')
)['order_id'].nunique()

revenue_trend = df.groupby(
    df['order_purchase_timestamp'].dt.to_period('M')
)['payment_value'].sum()

col1, col2 = st.columns(2)

with col1:
    fig1, ax1 = plt.subplots()
    sales_trend.plot(ax=ax1)
    ax1.set_title("Jumlah Transaksi Bulanan")
    ax1.set_xlabel("Periode")
    ax1.set_ylabel("Jumlah Transaksi")
    st.pyplot(fig1)

with col2:
    fig2, ax2 = plt.subplots()
    revenue_trend.plot(ax=ax2)
    ax2.set_title("Total Revenue Bulanan")
    ax2.set_xlabel("Periode")
    ax2.set_ylabel("Revenue")
    st.pyplot(fig2)

st.markdown("""
**Insight:**  
Terlihat adanya fluktuasi penjualan dengan kecenderungan peningkatan pada periode tertentu,
yang mengindikasikan pola musiman dalam aktivitas transaksi.
""")

st.markdown("---")

# =====================================
# SECTION 2 — REGIONAL ANALYSIS
# =====================================
st.header("🌎 Analisis Wilayah")

top_state_customer = df.groupby('customer_state')['customer_unique_id'] \
                        .nunique().sort_values(ascending=False).head(10)

top_state_transaction = df.groupby('customer_state')['order_id'] \
                           .nunique().sort_values(ascending=False).head(10)

col1, col2 = st.columns(2)

with col1:
    fig3, ax3 = plt.subplots()
    top_state_customer.plot(kind='bar', ax=ax3)
    ax3.set_title("Top 10 State - Pelanggan")
    st.pyplot(fig3)

with col2:
    fig4, ax4 = plt.subplots()
    top_state_transaction.plot(kind='bar', ax=ax4)
    ax4.set_title("Top 10 State - Transaksi")
    st.pyplot(fig4)

st.markdown("""
**Insight:**  
Wilayah metropolitan mendominasi jumlah pelanggan dan transaksi.
Hal ini menunjukkan konsentrasi pasar e-commerce berada di area urban.
""")

st.markdown("---")
st.caption("Proyek Analisis Data - E-Commerce Dashboard")
