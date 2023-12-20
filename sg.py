import streamlit as st
st.title("Te Queiro")
st.text("1618033988749895")
nama = st.text_input("input nama ygy.. :D")
nim = st.text_input("input nim ygy.. :D, harus 10 digit")
if len(nim) != 10:
    st.text("ERROR!!")
else:
    st.text("NIM : "+ nim)

if nama:
    st.text("Nama : " + nama)

iniKotak = st.selectbox('Matkul', ['English', "Arabic", "Germany"])
st.write(iniKotak)
age = st.slider("age", 0, 120, 50)
st.text(age)
gender = st.radio('Gender', ['Male', 'Female'])
list_hobi = st.text_area("HOBBIES", "Singing , Painting, Eating, Sleeping")
list_hobi = [x.strip() for x in list_hobi.split(",")]
st.write(list_hobi)


st.image("https://www.seiu1000.org/sites/main/files/main-images/camera_lense_0.jpeg", caption=st.markdown('[melihat masa depan](https://www.seiu1000.org/sites/main/files/main-images/camera_lense_0.jpeg)'))

import pandas as pd
data = {'Occupancy' : ['DataScientist', 'Doctor', 'Engineer'],
        'Tier' : ['C', 'B','A']}
st.dataframe(data, use_container_width=True)
df  = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)
file = st.file_uploader('Choose Picture', type=['png','csv'])
if file is not None:
    # if file.type == "png":
    #     st.image(file)
    # else:
    #     data = pd.read_csv(file)
    #     st.dataframe(data)
    try:
        st.image(file)
    except:
        data = pd.read_csv(file)
        st.dataframe(data)

st.title("CALCULATOR")
angka1 = st.number_input("Masukkan Angka 1 :")
angka2 = st.number_input("Masukkan Angka 2:")
operasi = st.radio("pilih operasi", ['perkalian x', 'pembagian :', 'pengurangan -', 'penjumlahan +'])
if operasi=='perkalian x' :
    st.write(angka1 * angka2)
elif operasi == 'penjumlahan +':
    st.write(angka1 + angka2)
elif operasi == 'pengurangan -':
    st.write(angka1 - angka2)
elif operasi == 'pembagian :':
    if angka2 == 0:
        st.write("Cannot Divide By Zero")
    else:
        st.write(angka1/angka2)
st.sidebar.header('fitur kiri')
if st.sidebar.checkbox('Biodata'):
    st.sidebar.write(f'Nama : {nama}')
    if gender=="Male":
        st.sidebar.write("Hola Mr "+nama)
    else:   
        st.sidebar.write("Hola Ms " + nama)
    if nim[:3]=="130":
        st.s.write("Anak IF")
    else:
        st.write("jurusan lain")
