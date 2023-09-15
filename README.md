# Predict Loan Default Customers

**Dataset** : [source](https://www.rakamin.com/virtual-internship-experience/data-scientist-home-credit-indonesia) <br>
**Notebook** : [view](https://github.com/faizns/HCI-vix-project/blob/main/HCI_VIX.ipynb)<br>
**Presentation deck** : [view](https://www.canva.com/design/DAFsyNotg5E/RKJjuTM0nGTpKF7CuaAcWg/view?utm_content=DAFsyNotg5E&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)

<br>

**Table of Contents**
- [Business Understanding](https://github.com/faizns/HCI-vix-project/blob/main/README.md#-business-understanding)
- [Workflow](https://github.com/faizns/HCI-vix-project/blob/main/README.md#-workflow)
- [Insight](https://github.com/faizns/HCI-vix-project/blob/main/README.md#-insight)
- [Modeling and Evaluation](https://github.com/faizns/HCI-vix-project/blob/main/README.md#-modeling-and-evaluation)
- [Model Simulation using Streamlit](https://github.com/faizns/HCI-vix-project/blob/main/README.md#-model-simulation-using-streamlit)
<br>


## 📂 Business Understanding
### Problem Statement
Home Credit Indonesia merupakan perusahaan yang memberikan layanan kredit  yang mudah, cepat, dan terjangkau kepada masyarakat. Salah satu permasalahan yang terjadi pada perusahaan ini adalah adanya nasabah yang gagal dalam pembayaran kredit. Apabila banyak pelanggan yang mengalami masalah ini, maka akan berdampak secara signifikan bagi perusahaan.

Menurut artikel yang diterbitkan di Harvard Business Review, dinyatakan bahwa "*Non-payment by consumers can set off a chain reaction of bad debts, lower profits, layoffs, and even bankruptcies, ultimately affecting entire industries and even economies.*" 

Oleh karena itu, mengidentifikasi nasabah yang memiliki kemungkinan besar mengalami kegagalan dalam membayar kredit penting untuk dilakukan. Hal ini dapat menjadi tindakan preventif bagi perusahaan dan memastikan pelanggan yang mampu melakukan pelunasan tidak ditolak ketika melakukan pengajuan pinjaman.

### Goals
- Loss Reduction, mengurangi dampak kerugian yang ditimbulkan oleh "Default Customer" yang memiliki potensi gagal bayar.
- Memutuskan bahwa pengajuan pinjaman dapat diterima atau ditolak
  
### Objectives
- Membuat prediktif model untuk memprediksi dan mengklasifikasikan nasabah berpotensi gagal bayar atau tidak
- Mengidentifikasi karakteristik nasabah yang berpotensi gagal bayar
<br>


## 📂 Workflow
<p align="center">
    <kbd> <img width="1000" alt="workflow" src="https://github.com/faizns/HCI-vix-project/assets/115857221/8d64b89f-f0d0-4276-9a51-82a1adb0c9a8.jpg"> </kbd> <br>
    Gambar 1 — Workflow Pembuatan Model
</p>
<br>

## 📂 Insight
- Tingkat default kredit nasabah dari dataset mencapai 9%
- Karakteristik mayoritas nasabah yang cenderung mengalami masalah dalam pembayaran kredit yaitu:
  - Laki-laki
  - Kelompok pendidikan rendah, "lower secondary"
  - Rentang usia 25 - 40 tahun
  - Lama bekerja 1 - 5 tahun
  - Tipe kredit "Cash Loan"
<br>

## 📂 Modeling and Evaluation
- Split dataset dengan rasio 80% Train : 20% Test
- Mengatasi data Train yang tidak seimbang menggunakan RandomUnderSampler
- Scaling data dengan RobustScaler
- Eksperimen menggunakan beberapa algoritma Logistic Regression, Random Forest, dan XGBoost
- Best fit model didapatkan menggunakan Logistic Regression dengan hyperparameter tuning, menghasilkan akurasi 87% dan AUC 73%

<br>
<p align="center">
    <kbd> <img width="800" alt="feats" src="https://github.com/faizns/HCI-vix-project/assets/115857221/a4daeca8-49f8-4c55-8cdd-3f3ad0486f18"> </kbd> <br>
    Gambar 2 — Feature Importance
</p>
<br>


## 📂 Model Simulation using Streamlit

<p align="center">
    <kbd> > <img width="1000" alt="st1" src="https://github.com/faizns/HCI-vix-project/assets/115857221/d7a67ea8-1d82-4ccc-884f-d99e57c335b8"></kbd> <br>
    Gambar 3 — Screenshot Part 1
</p>

<br>
<p align="center">
    <kbd> >  <img width="1000" alt="st2" src="https://github.com/faizns/HCI-vix-project/assets/115857221/045e4d1f-2b64-4e65-9018-8b6e8142c7cb"> </kbd> <br>
    Gambar 4 — Screenshot Part 2
</p>
<br>

## 📂 Recommendations
- Mempertimbangkan untuk membuat Credit Scorecard, menggunakan Information Value dan Feature Engineering menggunakan Weight of Evidence
- Melakukan analisis kredit yang lebih mendalam 
- Meningkatkan seleksi calon peminjam dengan memperketat persyaratan dan mengumpulkan informasi yang lebih lengkap tentang calon peminjam
