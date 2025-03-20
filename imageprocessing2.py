import streamlit as st

def main():
    st.set_page_config(page_title="AI Destekli Sosyal Medya Optimizasyonu", layout="wide")
    
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
    </style>
    """, unsafe_allow_html=True)
    
    st.title("📸 AI Destekli Sosyal Medya İçerik Optimizasyonu")
    st.subheader("AI destekli analiz ile sosyal medya görsellerinizi optimize edin ve daha fazla etkileşim alın!")
    
    if "analyzed" not in st.session_state:
        st.session_state.analyzed = False
    
    col1, col2 = st.columns([1, 2])
    with col1:
        uploaded_image = st.file_uploader("📤 Bir görsel yükleyin", type=["jpg", "png", "jpeg"])
        analyze_button = st.button("🔍 Analiz Başlat")
    
    if analyze_button and uploaded_image:
        st.session_state.analyzed = True
        st.switch_page("analysis")  # Analiz sonuçlarını ayrı bir sayfada gösterme
    
    if uploaded_image:
        st.image(uploaded_image, caption="Yüklenen Görsel", use_container_width=True)
        st.success("✅ Görsel başarıyla yüklendi!")
    else:
        st.info("Henüz bir görsel yüklenmedi.")

if __name__ == "__main__":
    main()
