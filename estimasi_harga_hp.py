import pickle
import streamlit as st

model = pickle.load(open('estimasi_harga_hp.sav', 'rb'))

st.title('Estimasi Harga HP')

#weight , thickness, ram , internal_mem , cpu_core , cpu_freq , RearCam, Front_Cam, ppi, battery
weight = st.number_input('Input Berat (gr)')
thickness = st.number_input('Input Ketebalan (inch)')
ram = st.number_input('Input RAM (GB)')
internal_mem = st.number_input('Input Memori Internal (GB)')
cpu_core = st.number_input('Input Jumlah CPU CORE')
cpu_freq = st.number_input('Input Frekuensi CPU (GHz)')
RearCam = st.number_input('Input Resolusi Kamera Belakang (MP)')
Front_Cam = st.number_input('Input Resolusi Kamera Depan (MP)')
ppi = st.number_input('Input Pixel Layar')
battery = st.number_input('Input Kapasitas Baterai (mAH)')


predict = ''

if st.button('Estimasi'):
    predict = model.predict(
        [[weight , thickness, ram , internal_mem , cpu_core , cpu_freq , RearCam, Front_Cam, ppi, battery]]
    )
    st.write ('Estimasi Harga HP : ', predict,)
    st.write ('Estimasi Harga HP Rupiah (IDR) : ', predict*0.35,)