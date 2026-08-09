import streamlit as st

st.title("--ALAT PENGHITUNG LUAS SEGITIGA--")
st.subheader("----BY Hanendra----")
st.markdown("---")

alas = st.number_input("Masukkan alas (cm)", min_value=0.0, format="%.2f")
tinggi = st.number_input("Masukkan tinggi (cm)", min_value=0.0, format="%.2f")

if st.button("--HITUNG--", type="primary"):
    if alas > 0 and tinggi > 0:
        luas = 0.5 * alas * tinggi
        st.success(f"✅ Luas segitiga = {luas:.2f} cm²")
    else:
        st.error("⚠️ MASUKKAN ANGKA YANG VALID!!")
