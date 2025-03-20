import streamlit as st
import random

def main():
    st.set_page_config(page_title="📊 AI Destekli Sosyal Medya Optimizasyonu", layout="wide")
    
    # Özel CSS ile renkleri ayarlıyoruz
    st.markdown("""
    <style>
    :root {
        --primary-color: #FF9800; /* Turuncu */
        --secondary-color: #2C2F33; /* Koyu Gri */
        --accent-color: #FFC107; /* Sarı */
        --background-color: #23272A; /* Koyu Arka Plan */
        --text-color: #EAEAEA; /* Açık Gri */
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
        padding: 10px;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: var(--accent-color);
    }
    
    .stFileUploader {
        background-color: var(--secondary-color);
        padding: 10px;
        border-radius: 10px;
    }
    
    .stMetric {
        background-color: var(--accent-color);
        padding: 10px;
        border-radius: 8px;
        font-weight: bold;
    }
    
    .stSidebar {
        background-color: var(--secondary-color);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Kenar Çubuğu (Sidebar)
    st.sidebar.title("🔧 Dashboard Ayarları")
    mode = st.sidebar.radio("📌 Mod Seçin:", ["Ana Sayfa", "İçerik Analizi", "İstatistikler", "Etkileşim Simülasyonu", "Ayarlar"])
    
    if mode == "Ana Sayfa":
        st.title("📸 AI Destekli Sosyal Medya Optimizasyonu")
        st.subheader("AI destekli analiz ile sosyal medya görsellerinizi optimize edin ve daha fazla etkileşim alın!")
        st.image("https://via.placeholder.com/800x400", caption="Örnek Görsel", use_container_width=True)
    
    elif mode == "İçerik Analizi":
        st.title("📊 İçerik Analizi")
        uploaded_image = st.file_uploader("📤 Bir görsel yükleyin", type=["jpg", "png", "jpeg"])
        if uploaded_image:
            st.image(uploaded_image, caption="Yüklenen Görsel", use_container_width=True)
            st.success("✅ Analiz tamamlandı! AI önerileri oluşturuldu.")
            st.write("**Öneriler:**")
            st.write("✔ Daha yüksek kontrast kullanın")
            st.write("✔ Hashtagleri optimize edin")
            st.write("✔ Yüzey parlaklığını artırın")
        else:
            st.info("Henüz bir görsel yüklenmedi.")
    
    elif mode == "İstatistikler":
        st.title("📈 İstatistikler")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="🌟 Ortalama Beğeni", value=f"{random.randint(800, 1500)}", delta="+15%")
        with col2:
            st.metric(label="📢 Etkileşim Oranı", value=f"{random.uniform(5, 12):.2f}%", delta="+2.3%")
        with col3:
            st.metric(label="📊 Paylaşım Sayısı", value=f"{random.randint(200, 500)}", delta="+10")
    
    elif mode == "Etkileşim Simülasyonu":
        st.title("🔮 AI Tabanlı Etkileşim Simülasyonu")
        st.write("**Bu mod, belirli parametrelere göre içeriğinizin sosyal medyada nasıl performans gösterebileceğini tahmin eder.**")
        engagement = random.randint(500, 2000)
        st.progress(engagement / 2000)
        st.write(f"Tahmini Etkileşim: {engagement} beğeni / yorum")
        if engagement > 1500:
            st.success("İçeriğiniz yüksek etkileşim alabilir! 🎉")
        else:
            st.warning("İçeriğinizde bazı iyileştirmeler yapabilirsiniz. 💡")
    
    elif mode == "Ayarlar":
        st.title("⚙ Ayarlar")
        theme_choice = st.selectbox("Tema Seçin:", ["Karanlık Mod", "Açık Mod"])
        st.slider("Parlaklık Seviyesi", 0, 100, 50)
        st.text_input("Kullanıcı Adınızı Girin:")
        st.button("Kaydet")
    
    st.sidebar.markdown("---")
    st.sidebar.write("📌 Daha iyi etkileşim almak için AI önerilerini dikkate alın ve içeriğinizi optimize edin!")
    
if __name__ == "__main__":
    main()
