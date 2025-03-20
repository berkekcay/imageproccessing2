import streamlit as st
import requests
import json

# Sightengine API Bilgileri
API_USER = "844129611"
API_SECRET = "muoN6nmb9nGzdxEPanBSSE62o8H4N7FH"

def analyze_image(image_url):
    """Sightengine API'yi kullanarak görseli analiz eder."""
    params = {
        'url': image_url,
        'models': 'properties,quality,faces',
        'api_user': API_USER,
        'api_secret': API_SECRET
    }
    r = requests.get('https://api.sightengine.com/1.0/check.json', params=params)
    return json.loads(r.text)

def main():
    st.set_page_config(page_title="AI Destekli Sosyal Medya Optimizasyonu", layout="wide")

    # Özel CSS ile stil ayarları
    st.markdown("""
    <style>
    :root {
        --primary-color: #FF9800;
        --secondary-color: #2C2F33;
        --accent-color: #FF9800;
        --background-color: #23272A;
        --text-color: #EAEAEA;
    }
    .stApp {
        background-color: var(--background-color);
        color: var(--text-color);
    }
    .stButton>button {
        background-color: var(--primary-color);
        color: var(--secondary-color);
        font-weight: bold;
        border-radius: 8px;
    }
    .stFileUploader {
        background-color: var(--secondary-color);
        padding: 10px;
        border-radius: 10px;
    }
    .stMetric {
        background-color: var(--accent-color);
        padding: 5px;
        border-radius: 8px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("📸 AI Destekli Sosyal Medya İçerik Optimizasyonu")
    st.subheader("AI destekli analiz ile sosyal medya görsellerinizi optimize edin ve daha fazla etkileşim alın!")

    # Görsel yükleme alanı
    st.markdown("<h3 style='text-align: center;'>📤 Bir Görsel Yükleyin</h3>", unsafe_allow_html=True)
    uploaded_image = st.file_uploader("📤 Bir görsel yükleyin", type=["jpg", "png", "jpeg"])  # Kullanıcıdan görsel URL al

    if st.button("🔍 Analiz Başlat"):
        if uploaded_image:
            with st.spinner("Görsel analiz ediliyor..."):
                results = analyze_image(uploaded_image)

            # Görseli göster
            st.image(uploaded_image, caption="Analiz Edilen Görsel", use_column_width=True)
            st.success("✅ Analiz Tamamlandı!")

            # Analiz Sonuçları
            st.markdown("---")
            st.subheader("📊 Analiz Sonuçları")

            # Parlaklık ve Netlik
            if "quality" in results:
                brightness = results["quality"].get("brightness", "Bilinmiyor")
                sharpness = results["quality"].get("sharpness", "Bilinmiyor")

                col1, col2 = st.columns(2)
                col1.metric(label="🌟 Parlaklık", value=f"{brightness:.2f}")
                col2.metric(label="🔍 Netlik", value=f"{sharpness:.2f}")

            # Renk Kompozisyonu
            if "colors" in results:
                st.subheader("🎨 Renk Dağılımı")
                for color in results["colors"]["dominant"]:
                    st.write(f"🟢 **Renk:** {color['hex']} - **Yoğunluk:** {color['percent']:.2f}%")

            # Yüz Tespiti
            if "faces" in results and results["faces"]["count"] > 0:
                st.subheader("🙂 Yüz Algılama")
                st.write(f"👥 Görselde **{results['faces']['count']}** yüz algılandı.")

            # Optimizasyon Önerileri
            st.markdown("---")
            st.subheader("💡 Optimizasyon Önerileri")

            if brightness < 30:
                st.warning("📢 Parlaklık düşük! Görseli biraz daha aydınlatabilirsiniz.")
            if sharpness < 30:
                st.warning("📢 Görselin netliği düşük! Daha yüksek çözünürlüklü bir görsel kullanabilirsiniz.")

        else:
            st.error("Lütfen geçerli bir görsel URL'si girin.")

if __name__ == "__main__":
    main()
