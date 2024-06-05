import streamlit as st
import mysql.connector
from pathlib import Path
import base64
import matplotlib.pyplot as plt
import pandas as pd
import os

user = st.secrets["db_username"]
password = st.secrets["db_password"]
host = st.secrets["mysql"]["host"]
port = st.secrets["mysql"]["port"]
database = st.secrets["mysql"]["database"]

conn = mysql.connector.connect(
        host=host,
        port=int(port),
        user=user,
        password=password,
        db=database
    )

st.write("DB username:", user)
st.write("DB password:", password)

# Initial page config
st.set_page_config(
    page_title='Adventurework Dashboard',
    layout="wide",
    initial_sidebar_state="expanded",
)

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)

def main():
    cs_sidebar()
    cs_body()

    return None

# def img_to_bytes(img_path):
#     img_bytes = Path(img_path).read_bytes()
#     encoded = base64.b64encode(img_bytes).decode()
#     return encoded
    
##########################
# SIDEBAR
##########################
def cs_sidebar():
    # st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://streamlit.io/)'''.format(img_to_bytes("logomark_website.png")), unsafe_allow_html=True)
    st.sidebar.header('Adventurework Dashboard')
    tahun = list(range(2019, 2025))
    tahun_dipilih = st.sidebar.selectbox("__Pilih tahun__", tahun)

    return None

##########################
# Main body of cheat sheet
##########################
def cs_body():
    col1, col2, col3 = st.columns(3)
    
    #######################################
    # COLUMN 1
    #######################################
    
    # Comparison (Line Chart)
    col1.subheader('Comparison (Line Chart)')
    col1.markdown('Melihat perkembangan penjualan dari bulan ke bulan.')

    
    
    # # Membuat kursor untuk eksekusi query SQL
    # cursor = conn.cursor()
    
    # # Query SQL Comparison
    # comparison = """
    #     SELECT 
    #         t.MonthNumberOfYear AS Month,
    #         SUM(fs.OrderQuantity) AS Total_Order_Quantity 
    #     FROM 
    #         factinternetsales fs 
    #     JOIN 
    #         dimtime t ON fs.OrderDateKey = t.TimeKey 
    #     GROUP BY 
    #         t.MonthNumberOfYear
    #     ORDER BY 
    #         t.MonthNumberOfYear;
    # """
    
    # # Eksekusi query
    # cursor.execute(comparison)
    
    # # Mengambil hasil query
    # results = cursor.fetchall()
    
    # # Memproses hasil query ke dalam format yang sesuai untuk grafik
    # month = []
    # total_product_by_month = []
    # for row in results:
    #     month.append(row[0])  
    #     total_product_by_month.append(row[1])     
    
    # # Plot grafik
    # plt.plot(month, totals, marker='o')
    # plt.xlabel('Month')
    # plt.ylabel('Total Product')
    # plt.title('Total Products by Month')
    # plt.xticks(month)
    # plt.tight_layout()
    # plt.show()
     
    # Perlu? 1
    col1.subheader('Percobaan')

    #######################################
    # COLUMN 2
    #######################################

    # Display interactive widgets
    col2.subheader('Display interactive widgets')
    
    #######################################
    # COLUMN 3
    #######################################

    # Connect to data sources
    col3.subheader('Connect to data sources')
    
    return None
    
##########################
# Run main()
##########################
if __name__ == '__main__':
    main()
