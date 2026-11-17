import streamlit as st

st.title("Perhitungan Biaya Laundry Kiloan")

# Input
nim = st.text_input("NIM (10 digit)", key="nim")
berat = st.number_input("Berat Cucian (kg)", key="berat", value=None, step=1)


def reset():
    st.session_state.nim = ""
    st.session_state.berat = None


col1, col2 = st.columns(2)
hitung = col1.button("Hitung")
col2.button("Reset", on_click=reset)

if hitung:
    # Validasi
    if len(nim) != 10 or not nim.isdigit():
        st.error("NIM tidak valid! Harus 10 digit angka.")
    elif berat is None or berat <= 0:
        st.error("Berat tidak valid! Harus bilangan bulat lebih dari 0.")
    else:
        # Perhitungan
        tarif = 5000 + int(nim[-1]) * 500
        genap = 0
        for d in nim:
            if int(d) % 2 == 0:
                genap = genap + 1
        diskon = genap  # persen
        normal = berat * tarif
        potongan = diskon / 100 * normal
        total = normal - potongan

        # Output
        st.subheader("Hasil Perhitungan")
        st.write("Tarif per kg :", f"Rp {tarif:,.0f}")
        st.write("Persen diskon :", f"{diskon} %")
        st.write("Biaya normal :", f"Rp {normal:,.0f}")
        st.write("Potongan :", f"Rp {potongan:,.0f}")
        st.success(f"Total bayar : Rp {total:,.0f}")
