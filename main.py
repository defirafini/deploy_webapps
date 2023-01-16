import streamlit as st

page_bg_img = '''
<style>
[data-testid='stAppViewContainer'] {
background-color: #f2e4fa;
opacity: 0.7;
background-image: radial-gradient(#5c2f78 0.5px, #f2e4fa 0.5px);
background-size: 10px 10px;
}
</style>
'''

from PIL import Image

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title('Achemtools🧪')
st.markdown('''
Barang ada di tangan kapanpun kamu butuhkan!''')

title = st.text_input('Alamat E-mail'),('Alamat E-mail Kamu')

title = st.text_input('Nama'),('Nama Kamu')

kelas= st.selectbox(
    'Kelas',
    ('1A', '1B', '1C', '1D', '1E', '1F', '1G', '2A', '2B', '2C', '2D', '2E', '2F', '2G', '3A', '3B', '3C', '3D', '3E', '3F', '3G'))

tempat= st.selectbox(
    'Tempat Pengambilan',
    ('Gedung B', 'Gedung C', 'Gedung D', 'Gedung E', 'Gedung F', 'Gedung G'))

waktu= st.number_input('Waktu Pengambilan Pukul (Selama Jam Perkuliahan)')

st.header('Produk')

st.subheader('1. Tabung Reaksi')

tab1, tab2, tab3 = st.tabs(['Tabung Reaksi Biasa', 'Tabung Reaksi Ulir', 'Tabung Reaksi Besar'])

with tab1:
    st.subheader('Tabung Reaksi')
    st.image('https://www.labconco.com/images/cms/extralarge/2304005_straight_digestion_tubes_250ml_single_oct2_2018_web_rgb.jpg')
    st.write('Tabung reaksi dengan merk Iwaki lebih menahan panas dibandingkan dengan merk lain.')
    st.write('Rp.15.000')

with tab2:
    st.subheader('Tabung Reaksi Ulir')
    st.image('https://images.tokopedia.net/img/cache/500-square/product-1/2019/8/9/35575003/35575003_fb7196ab-3f7f-4f7f-83af-36014ca7a8b2_900_900?ect=4g')
    st.write('Tabung reaksi Ulir dengan merk iwaki dengan menggunakan tutup yang aman.')
    st.write('Rp.30.000')

with tab3:
    st.subheader('Tabung Reaksi Besar')
    st.image('https://th.bing.com/th/id/OIP.aNxB32uW8VDtaevzAPCpjgAAAA?pid=ImgDet&rs=1')
    st.write('Tabung reaksi besar dengan merk iwaki dengan menggunakan tutup yang aman.')
    st.write('Rp.65.000')

st.subheader('2. Pipet')

tab1, tab2, tab3 = st.tabs(['Pipet Tetes', 'Pipet Volume', 'Pipet Mohr'])

with tab1:
    st.subheader('Pipet Tetes')
    st.image('https://s4.bukalapak.com/img/9421525312/w-1000/aHR0cHM6Ly9lY3M3LnRva29wZWRpYS5uZXQvaW1nL3Byb2R1Y3QtMS8yMDE3.jpg')
    st.write('Pipet tetes dengan kaca berkualitas dan panjang 17cm.')
    st.write('Rp.3.000')


with tab2:
    st.subheader('Pipet Volume')
    st.image('https://th.bing.com/th/id/OIP.W6nIvfkvMh9BPSmdTNZiTwHaHa?pid=ImgDet&rs=1')
    st.write('Pipet volume dengan kaca berkualitas tahan terhadap panas dan bahan kimia.')
    st.write('Rp.35.000')


with tab3:
    st.subheader('Pipet Mohr')
    st.image('https://cdn7.bigcommerce.com/s-zgzol/images/stencil/1280x1280/products/9206/17097/SIBATA_2010A_Pipet_Image__29873.1396468035.1280.1280__75312.1461588471.jpg?c=2&imbypass=on')
    st.write('Pipet mohr dengan pengukuran yang lebih akurat dapat menahan panas dan bahan kimia.')
    st.write('Rp.45.000')

st.subheader('3. Cawan')

tab1, tab2, tab3 = st.tabs(['Cawan petri', 'Cawan Porselein', 'Cawan Cursible'])

with tab1:
    st.subheader('Cawan Petri')
    st.image('https://s0.bukalapak.com/img/085146509/w-1000/Petridish_60x15_mm_ANUMBRA___Cawan_Petri.jpg')
    st.write('Cawan Petri dengan sodalime glass memiliki ukuran 90x15mm.')
    st.write('Rp.25.000')

with tab2:
    st.subheader('Cawan Porselein')
    st.image('https://ecs7.tokopedia.net/img/cache/700/product-1/2015/5/10/12432094/12432094_cd0471b2-f72c-11e4-9a83-f98c64efb121.jpg')
    st.write('Cawan porselein dengan merk Iwaki lebih menahan panas dibandingkan dengan merk lain.')
    st.write('Rp.15.000')

with tab3:
    st.subheader('Cawan Cursible')
    st.image('https://s2.bukalapak.com/img/7773657861/w-1000/Cawan_Porselen_100_cc_Porselin_Dish_Alat_Praktikum_Laborator.jpg')
    st.write('Cawan Cursible dengan tutup terbuat dari porselein tahan panas dan memiliki kapasitas 50mL.')
    st.write('Rp.20.000')  

st.subheader('4. Bulb')

tab1, tab2, tab3 = st.tabs(['Rubber Bulb', 'Tensi Bulb', 'Bulb Pipet Tetes'])

with tab1:
    st.subheader('Rubber Bulb')
    st.image('https://cf.shopee.com.my/file/c702ccb27eae6eb0c64d86784fd80744_tn')
    st.write('Bulb dengan kualitas karet yang baik untuk dipasangkan pada pipet volume dan pipet mohr.')
    st.write('Rp.40.000')
    
with tab2:
    st.subheader('Tensi Bulb')
    st.image('https://th.bing.com/th/id/OIP.x7MiebYpvDrLS26akX9yiwAAAA?pid=ImgDet&rs=1')
    st.write('Bulb dengan kualitas karet yang baik dan digunakan secara manual.')
    st.write('Rp.20.000')

with tab3:
    st.subheader('Bulb Pipet Tetes')
    st.image('https://i.ebayimg.com/00/s/MTAwMFgxMDAw/z/5IsAAOSweqdeeJQY/$_10.JPG?set_id=2')
    st.write('Bulb pipet tetes dengan kualitas karet yang baik dan variasi warna yang cantik.')
    genre=st.radio(
        'Warna bulb yang diinginkan:',
        ('Merah', 'Kuning', 'Biru'))
    st.write('Rp.2.000')

st.subheader('5. Gelas Ukur')
st.image('https://s2.bukalapak.com/img/2195526921/w-1000/Gelas_Ukur_Pyrex_100_ML.jpg')
st.write('Gelas ukur terbuat dari kaca pyrex borocylicate dan menahan panas dengan baik.')
ukuran = st.selectbox(
    'Ukuran dan Harga Gelas Ukur',
    ('10mL-Rp.30.000','25mL-Rp.35.000','50mL-Rp.40.000','100mL-Rp.50.000','250mL-Rp.90.000'))
    
st.subheader('6. Gelas Piala')
st.image('https://2.bp.blogspot.com/-cOMiqFfgEog/WJAA0blP9CI/AAAAAAAAAXs/10BhiHqRqPA1ee2TeuL3Th5fzBZMg2z9gCLcB/s1600/71lFxQVyauL._SX522_.jpg')
st.write('Gelas piala terbuat dari kaca pyrex borocylicate dan menahan panas dengan baik dibandingkan dengan merk lain.')
ukuran = st.selectbox(
    'Ukuran dan Harga Gelas Piala',
    ('50mL-Rp.22.000','100mL-Rp.25.000','250mL-Rp.30.000','500mL-Rp.40.000'))

st.subheader('7. Batang Pengaduk')
st.image('https://www.medicalogy.com/images/product/batang-pengaduk.png')
st.write('Batang pengaduk dengan bahan kaca berkualitas, diameter 6mm dan panjang 60cm.')
st.write('Rp.6.000')

st.subheader('8. Alu dan Mortar')
st.image('https://th.bing.com/th/id/OIP.q-EQSmOiN_7BoC1egaSQtAHaHa?pid=ImgDet&w=788&h=788&rs=1')
st.write('Alu dan Mortar terbuat dari porselein tebal ukuran 16cm untuk menghaluskan sampel.')
st.write('Rp.60.000')

st.subheader('9. Corong')
st.image('https://4.bp.blogspot.com/-K1BLho2ShFY/Wg09Sw5k8FI/AAAAAAAAEto/gKimuQPJkpoxAQPYxd1hmUNguGTcxMqZgCLcBGAs/s1600/corong%2Bpisah.png')
st.write('Corong terbuat dari bahan borocylicate berkualitas memiliki kapasitas 50mL.')
st.write('Rp.25.000')

st.subheader('10. Erlenmeyer')
st.write('Erlenmeyer')
st.image('https://images-na.ssl-images-amazon.com/images/I/412jJ-EIpLL._AC_US1000_.jpg')
ukuran = st.selectbox(
    'Ukuran dan Harga Erlenmeyer',
    ('50mL-Rp.30.000','100mL-Rp.35.000','125mL-Rp.37.000','250mL-Rp.40.000','300mL-Rp.45.000','500mL-Rp.62.000'))

st.header('Cek Pesanan')

st.write("Tanggal Pengambilan Pesananmu")
st.date_input('Pilih tanggal')

metodepembayaran = st.selectbox(
    'Metode Pembayaran',
    ('Transfer Bank','Dana : 0897654321', 'OVO : 0897654321', 'Gopay : 0897654321', 'Bayar di tempat'))

opsipengiriman = st.selectbox(
    'Opsi Pengiriman',
    ('JNT','Sicepat','Wahana','Ambil di tempat'))

st.write('Total Pesanan')

title = st.text_input('Barang dan Jumlah Pesanan'),('Nama Barang')

if st.button('Select'):
    st.write('Pesanan Kamu Akan di Proses')