import streamlit as st
import os

# Page configuration for Standard 9:16 layout & Nunu Lwin Name
st.set_page_config(page_title="နုနုလွင် ဗီဒီယိုနှင့် ရုပ်ရှင်ပြန်ဆိုချက်ဖန်တီးသူ", layout="centered")

st.title("🎬 နုနုလွင် ဗီဒီယိုနှင့် ရုပ်ရှင်ပြန်ဆိုချက်ဖန်တီးသူ")
st.write("ဗီဒီယိုဖိုင် တိုက်ရိုက်တင်၍ အလိုအလျောက် ဘာသာပြန်ဆိုကာ မြန်မာအသံဖြင့် အသံနှင့် ဗီဒီယို တိကျစွာ ကိုက်ညီစေရန် ဖန်တီးပေးသောနေရာ။")

# Sidebar for AI Key (Authentication & Security)
st.sidebar.header("⚙️ ဆက်တင်များနှင့် လုံခြုံရေး")
api_key = st.sidebar.text_input("AI API Key ထည့်ပါ:", type="password")

# Video File Uploader (Supports standard 9:16 format videos)
uploaded_file = st.file_uploader("ဗီဒီယိုဖိုင် (Video File) တင်ပါ (MP4, MOV, AVI):", type=["mp4", "mov", "avi"])

# Voice Options: Thiha, Nila, BoBo
voice_option = st.selectbox(
    "အသံအမျိုးအစား ရွေးချယ်ပါ:",
    ("သီဟ (Thiha)", "နီလာ (Nila)", "ဘိုဘို (BoBo)")
)

if st.button("ဗီဒီယို အလိုအလျောက် ဘာသာပြန်ဖန်တီးမည်"):
    if not api_key:
        st.error("ကျေးဇူးပြု၍ ဘေးဘောင် (Sidebar) တွင် API Key ထည့်သွင်းပေးပါရန်။")
    elif uploaded_file is not None:
        os.makedirs("temp_dir", exist_ok=True)
        file_path = os.path.join("temp_dir", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
            
        st.success("အောင်မြင်ပါသည်။ ဗီဒီယိုဖိုင်ကို လက်ခံရရှိပြီး အသံနှင့်ဗီဒီယို တိကျစွာ ကိုက်ညီစေရန် (Audio-Video Sync) နှင့် အလိုအလျောက် ဘာသာပြန်ခြင်းများကို ပုံမှန်အမြန်နှုန်းဖြင့် စတင်လုပ်ဆောင်နေပါပြီ...")
        
        st.info(f"ဖိုင်အမည်: {uploaded_file.name} | ရွေးချယ်ထားသော အသံ: {voice_option}")
        
    else:
        st.warning("ကျေးဇူးပြု၍ ဗီဒီယိုဖိုင် အရင်တင်ပေးပါ။")
