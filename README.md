# 🧮 Denklem Çözücü (AI Math Solver)

Bu proje, kameradan çekilen matematiksel denklemleri yapay zeka kullanarak okuyan ve anında çözen web tabanlı bir Python uygulamasıdır. Kullanıcıların herhangi bir kütüphane veya dil indirmesine gerek kalmadan doğrudan tarayıcı üzerinden denklemlerini çözmelerini sağlar.

## 🚀 Özellikler

* **Kamera Entegrasyonu:** Cihazın kamerasına doğrudan tarayıcı üzerinden erişim ve fotoğraf çekme.
* **Yapay Zeka Destekli OCR:** Görüntü işleme ve `pix2tex` (LaTeX-OCR) modeli kullanılarak, el yazısı veya basılı karmaşık denklemlerin yüksek doğrulukla dijital metne (LaTeX) dönüştürülmesi.
* **Güçlü Matematik Motoru:** Okunan formüllerin `latex2sympy2` köprüsüyle saf matematiğe çevrilmesi ve `SymPy` motoruyla çözülmesi.
* **Akıllı Hata Yakalama:** Kameranın bulanık olduğu veya denklemin okunamadığı durumlarda sistemin çökmesini engelleyen güvenli mimari (Try-Except).
* **Modern Arayüz:** Streamlit ile geliştirilmiş sade, hızlı ve tamamen mobil uyumlu (responsive) tasarım.

## 🛠️ Kullanılan Teknolojiler

* **Dil:** Python 3.x
* **Arayüz (Frontend):** Streamlit
* **Yapay Zeka (AI / OCR):** Pix2Tex (LaTeX-OCR), PyTorch tabanlı
* **Matematik Çözümleme:** SymPy, latex2sympy2
* **Görüntü İşleme:** Pillow
* 
