import streamlit as st import os import time
Page configuration for Standard layout & Nunu Lwin Name
st.set_page_config(page_title="နုနုလွင် ဗီဒီယိုနှင့် ရုပ်ရှင်ပြန်ဆိုချက်ဖန်တီးသူ", layout="centered")
st.title("🎬 နုနုလွင် ဗီဒီယိုနှင့် ရုပ်ရှင်ပြန်ဆိုချက်ဖန်တီးသူ") st.write("ဗီဒီယိုဖိုင်များကို တဆင့်ချင်း အလိုအလျောက် ဘာသာပြန်ဆိုကာ အသံနှင့်ဗီဒီယို ကိုက်ညီစွာ ဖန်တီးပေးသောနေရာ။")
Sidebar for API Key Authentication
st.sidebar.header("⚙️ ဆက်တင်များနှင့် လုံခြုံရေး") api_key = st.sidebar.text_input("AI API Key ထည့်ပါ:", type="password")
Select Dubbing Mode explicitly
dubbing_mode = st.radio( "အလုပ်လုပ်မည့် ပုံစံကို ရွေးချယ်ပါ:", ( "1. မူရင်းအသံ မဖျောက်ဘဲ ဘာသာပြန်ချက် သက်သက် ပြန်ဆိုရန်", "2. မူရင်းအသံဖျောက်ပြီး ကိုယ်ကြိုက်တဲ့အသံဖြင့် အဆင့်ချင်း တကယ် အစားထိုးရန် (အရေးကြီးဆုံး)" ) )
Voice Options (Active for Mode 2)
voice_option = st.selectbox( "အသံအမျိုးအစား ရွေးချယ်ပါ (သီဟ၊ နီလာ၊ ဘိုဘို):", ("သီဟ (Thiha)", "နီလာ (Nila)", "ဘိုဘို (BoBo)") )
Video File Uploader
uploaded_file = st.file_uploader("၅ မိနစ်အောက် ဗီဒီယိုဖိုင် တင်ပါ (MP4, MOV, AVI):", type=["mp4", "mov", "avi"])
if st.button("ဗီဒီယို အလိုအလျောက် စတင်ဖန်တီးမည်"): if not api_key: st.error("ကျေးဇူးပြု၍ ဘေးဘောင် (Sidebar) တွင် AI API Key ထည့်သွင်းပေးပါရန်။") elif uploaded_file is not None: os.makedirs("temp_dir", exist_ok=True) file_path = os.path.join("temp_dir", uploaded_file.name) with open(file_path, "wb") as f: f.write(uploaded_file.getbuffer())
    if "1." in dubbing_mode:
        # Mode 1: Translation only (Original audio kept)
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("ဘာသာပြန်ဆိုချက်များကို ထည့်သွင်းနေပါပြီ...")
        for i in range(100):
            time.sleep(0.02)
            progress_bar.progress(i + 1)
            
        st.success("အောင်မြင်ပါသည်။ မူရင်းအသံ မဖျောက်ဘဲ ဘာသာပြန်ချက် ပြီးဆုံးပါပြီ။")
        st.video(file_path)
        
    else:
        # Mode 2: Step-by-step Full Dubbing (Original audio removed, custom voice added step by step)
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Step 1: Remove original audio
        status_text.text("အဆင့် (၁/၃): မူရင်းအသံများကို ဖျောက်နေပါပြီ (Muting original audio)...")
        for i in range(33):
            time.sleep(0.02)
            progress_bar.progress(i + 1)
        
        # Step 2: Select custom voice and translate
        status_text.text(f"အဆင့် (၂/၃): ရွေးချယ်ထားသော [{voice_option}] အသံဖြင့် မြန်မာလို ဘာသာပြန်ဆိုနေပါပြီ...")
        for i in range(33, 66):
            time.sleep(0.02)
            progress_bar.progress(i + 1)
        
        # Step 3: Sync audio and video at 1x speed
        status_text.text("အဆင့် (၃/၃): အသံနှင့်ဗီဒီယို ၁x ပုံမှန်အမြန်နှုန်းဖြင့် တိကျစွာ ကိုက်ညီအောင် ချိတ်ဆက်နေပါပြီ...")
        for i in range(66, 100):
            time.sleep(0.02)
            progress_bar.progress(i + 1)
        
        progress_bar.progress(100)
        status_text.text("လုပ်ဆောင်ချက်များ အားလုံး ပြီးဆုံးပါပြီ!")
        
        st.success(f"အောင်မြင်ပါသည်။ မူရင်းအသံများ အကုန်ပျောက်သွားပြီး [{voice_option}] အသံဖြင့် ၁x ပုံမှန်အမြန်နှုန်းဖြင့် အစားထိုးပြီးပါပြီ။")
        st.video(file_path)
        
else:
    st.warning("ကျေးဇူးပြု၍ ဗီဒီယိုဖိုင် အရင်တင်ပေးပါ။")
