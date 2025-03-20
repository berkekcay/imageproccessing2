import streamlit as st
import requests
import json

# Sightengine API Bilgileri
API_USER = "844129611"
API_SECRET = "muoN6nmb9nGzdxEPanBSSE62o8H4N7FH"
API_URL = "https://api.sightengine.com/1.0/check.json"

def analyze_image(image_path):
    """Sightengine API'yi kullanarak görsel analizi yapar."""
    params = {
        'models': 'properties,quality,faces',
        'api_user': API_USER,
        'api_secret': API_SECRET
    }
    with open(image_path, 'rb') as img_file:
        files = {'media': img_file}
        response = requests.post(API_URL, files=files, data=params)
    return json.loads(response.text)

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
    uploaded_image = st.file_uploader("📤 Bir görsel yükleyin", type=["jpg", "png", "jpeg"])

    if uploaded_image and st.button("🔍 Analiz Başlat"):
        with st.spinner("Görsel analiz ediliyor..."):
            # Görseli geçici olarak kaydet
            temp_image_path = "./temp_image.jpg"
            with open(temp_image_path, "wb") as f:
                f.write(uploaded_image.getbuffer())

            # API'ye yükleyip analiz yap
            results = analyze_image(temp_image_path)

        # Görseli ekranda göster
        st.image(uploaded_image, caption="Analiz Edilen Görsel", use_container_width=True)
        st.success("✅ Analiz Tamamlandı!")

        # Analiz Sonuçları
        st.markdown("---")
        st.subheader("📊 Analiz Sonuçları")

        # Parlaklık ve Netlik kontrolü
        brightness = results.get("quality", {}).get("brightness")
        sharpness = results.get("quality", {}).get("sharpness")

        col1, col2 = st.columns(2)
        col1.metric(label="🌟 Parlaklık", value=f"{brightness:.2f}" if brightness else "-")
        col2.metric(label="🔍 Netlik", value=f"{sharpness:.2f}" if sharpness else "-")

        # Renk Kompozisyonu (Güvenli hale getirildi)
        colors = results.get("colors", {}).get("dominant", [])
        if colors:
            st.subheader("🎨 Renk Dağılımı")
            for color in colors:
                hex_value = color.get("hex", "Bilinmiyor")
                percent = color.get("percent", 0)
                st.write(f"🟢 **Renk:** {hex_value} - **Yoğunluk:** {percent:.2f}%")
        else:
            st.warning("📢 Renk analizi yapılamadı. API'den uygun veri alınamadı.")

        # Yüz Tespiti
        face_count = results.get("faces", {}).get("count", 0)
        if face_count > 0:
            st.subheader("🙂 Yüz Algılama")
            st.write(f"👥 Görselde **{face_count}** yüz algılandı.")

        # Optimizasyon Önerileri
        st.markdown("---")
        st.subheader("💡 Optimizasyon Önerileri")

        if isinstance(brightness, (int, float)) and brightness < 30:
            st.warning("📢 Parlaklık düşük! Görseli biraz daha aydınlatabilirsiniz.")
        if isinstance(sharpness, (int, float)) and sharpness < 30:
            st.warning("📢 Görselin netliği düşük! Daha yüksek çözünürlüklü bir görsel kullanabilirsiniz.")

if __name__ == "__main__":
    main()
