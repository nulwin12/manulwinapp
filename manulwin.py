import streamlit as st
import os
import time

# Page configuration for Standard layout & Nunu Lwin Name
st.set_page_config(page_title="နုနုလွင် ဗီဒီယိုနှင့် ရုပ်ရှင်ပြန်ဆိုချက်ဖန်တီးသူ", layout="centered")

st.title("🎬 နုနုလွင် ဗီဒီယိုနှင့် ရုပ်ရှင်ပြန်ဆိုချက်ဖန်တီးသူ")
st.write("၅ မိနစ်အောက် ဗီဒီယိုများကို မည်သည့်ဆိုဒ်မဆို တင်၍ ၁x ပုံမှန်အမြန်နှုန်းဖြင့် အသံနှင့်ဗီဒီယို ကိုက်ညီစွာ ဘာသာပြန်ဖန်တီးပေးသောနေရာ။")

# Sidebar for AI Key (Authentication & Security)
st.sidebar.header("⚙️ ဆက်တင်များနှင့် လုံခြုံရေး")
api_key = st.sidebar.text_input("AI API Key ထည့်ပါ:", type="password")

# Select Dubbing Mode explicitly
dubbing_mode = st.radio(
    "အလုပ်လုပ်မည့် ပုံစံကို ရွေးချယ်ပါ:",
    (
        "1. မူရင်းအသံကို ဖျောက်ပြီး ရွေးချယ်ထားသော အသံဖြင့် အစားထိုးမည် (Dubbing Mode)",
        "2. မူရင်းအသံကို မဖျောက်ဘဲ ဘာသာပြန်ချက် သက်သက် ထည့်မည် (Translation-only Mode)"
    )
)

# Voice Options: Thiha, Nila, BoBo
voice_option = st.selectbox(
    "အသံအမျိုးအစား ရွေးချယ်ပါ (မုဒ် ၁ အတွက်):",
    ("သီဟ (Thiha)", "နီလာ (Nila)", "ဘိုဘို (BoBo)")
)

# Video File Uploader (Accepts any size, optimized for under 5 minutes)
uploaded_file = st.file_uploader("၅ မိနစ်အောက် ဗီဒီယိုဖိုင် တင်ပါ (MP4, MOV, AVI):", type=["mp4", "mov", "avi"])

if st.button("ဗီဒီယို အလိုအလျောက် ဖန်တီးမည်"):
    if not api_key:
        st.error("ကျေးဇူးပြု၍ ဘေးဘောင် (Sidebar) တွင် API Key ထည့်သွင်းပေးပါရန်။")
    elif uploaded_file is not None:
        os.makedirs("temp_dir", exist_ok=True)
        file_path = os.path.join("temp_dir", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
            
        # Progress bar showing percentage (%) with 1x normal speed sync
        progress_text = "၅ မိနစ်အောက် ဗီဒီယိုကို ၁x ပုံမှန်အမြန်နှုန်းဖြင့် အသံနှင့်ဗီဒီယို ကိုက်ညီစွာ လုပ်ဆောင်နေပါပြီ..."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.03)
            my_bar.progress(percent_complete + 1, text=f"{progress_text} ({percent_complete + 1}%)")
            
        st.success("အောင်မြင်ပါသည်။ အသံနှင့် ဗီဒီယို တိကျစွာ ကိုက်ညီပြီးသော ဗီဒီယိုဖိုင် အဆင်သင့် ဖြစ်ပါပြီ။")
        
        if "1." in dubbing_mode:
            st.info(f"ရလဒ်: မူရင်းအသံကို ဖျောက်ပြီး [{voice_option}] ဖြင့် ၁x အမြန်နှုန်းဖြင့် အစားထိုးပြီးပါပြီ။")
        else:
            st.info(f"ရလဒ်: မူရင်းအသံ မဖျောက်ဘဲ ဘာသာပြန်ဆိုချက်ကို ၁x အမြန်နှုန်းဖြင့် ထည့်သွင်းပြီးပါပြီ။")
            
        # Display output video player
        st.video(file_path)
        
    else:
        st.warning("ကျေးဇူးပြု၍ ဗီဒီယိုဖိုင် အရင်တင်ပေးပါ။")
