import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    # Gantikan dengan URL data set Anda
    url = "https://raw.githubusercontent.com/Kajaxssss/projekdataa/main/main_data.xls"
    df = pd.read_csv(url)
    df.columns = df.columns.str.replace(' ', '_').str.lower()
    return df
def draw_visualization(df):
    # Gambar histogram
    st.subheader('Histogram')
    st.write(df.hist())

    # Gambar diagram garis
    st.subheader('Line Chart')
    st.line_chart(df)

    # Gambar scatter plot
    st.subheader('Scatter Plot')
    st.scatter_plot(df)

    # Gambar heatmap
    st.subheader('Heatmap')
    st.heatmap(df.corr())
def main():
    # Mengambil data
    df = load_data()

    # Menggambar visualisasi
    draw_visualization(df)
if __name__ == "__main__":
    main()    
