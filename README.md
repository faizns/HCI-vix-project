# Predict Loan Default Customers

**Dataset** : <br>
**Notebook** : <br>
**Presentation deck** : [view](https://www.canva.com/design/DAFsyNotg5E/RKJjuTM0nGTpKF7CuaAcWg/view?utm_content=DAFsyNotg5E&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)

<br>

**Table of Contents**
- [Business Understanding]()
- [Workflow]()
- [Data Visualization and Insight]()
- [Modeling and Evaluation]()
- [Model Simulation]()
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


## 📂 Data Visualization and Insight


## 📂 Modeling and Evaluation
- Split dataset dengan rasio 80% Train : 20% Test
- Mengatasi data Train yang tidak seimbang menggunakan RandomUnderSampler
- Scaling data dengan RobustScaler
- Eksperimen menggunakan beberapa algoritma Logistic Regression, Random Forest, dan XGBoost
- Best fit model didapatkan menggunakan Logistic Regression dengan hyperparameter tuning, menghasilkan akurasi 87% dan AUC 73%

## 📂 Simulations
