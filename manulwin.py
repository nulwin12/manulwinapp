import streamlit as st
import os
import time
import google.generativeai as genai

st.set_page_config(page_title="Gemini AI ဗီဒီယို မြန်မာဘာသာပြန်စနစ်", layout="centered")

st.title("🎬 Gemini AI ဗီဒီယို မြန်မာဘာသာပြန်စနစ်")
st.write("Gemini API Key ဖြင့် ဗီဒီယိုဖိုင်များကို တင်၍ မြန်မာလို အလိုအလျောက် ဘာသာပြန်ဆိုပေးမည့်နေရာ။")

# Sidebar - Gemini API Key ထည့်ရန်
api_key = st.sidebar.text_input("Gemini API Key ထည့်ပါ:", type="password")

uploaded_file = st.file_uploader("ဗီဒီယိုဖိုင် တင်ပါ (MP4, MOV, AVI):", type=["mp4", "mov", "avi"])

if st.button("ဗီဒီယိုကို မြန်မာလို စတင်ဘာသာပြန်မည်"):
    if not api_key:
        st.error("ကျေးဇူးပြု၍ ဘေးဘောင် (Sidebar) တွင် Gemini API Key ထည့်သွင်းပေးပါရန်။")
    elif uploaded_file is not None:
        # API Key ကို ချက်ချင်းချိတ်ဆက်ခြင်း
        genai.configure(api_key=api_key)
        
        os.makedirs("temp_dir", exist_ok=True)
        file_path = os.path.join("temp_dir", uploaded_file.name)
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
            
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("အဆင့် (၁/၂): ဗီဒီယိုဖိုင်ကို စနစ်အတွင်းသို့ ထည့်သွင်းနေပါပြီ (30%)...")
        progress_bar.progress(30)
        time.sleep(1)
        
        try:
            status_text.text("အဆင့် (၂/၂): Gemini AI ဖြင့် မြန်မာဘာသာသို့ ဘာသာပြန်ဆိုနေပါပြီ (70%)...")
            progress_bar.progress(70)
            
            # Gemini AI သို့ ဗီဒီယိုဖိုင် ပို့ဆောင်ခြင်း (Google AI Gemini File API)
            video_file = genai.upload_file(file_path)
            
            # မော်ဒယ်ကို ခေါ်ယူပြီး မြန်မာလို ဘာသာပြန်ခိုင်းခြင်း
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(
                [video_file, "ဤဗီဒီယိုထဲတွင် ပါဝင်သော ပြောစကားများနှင့် အကြောင်းအရာများကို မြန်မာဘာသာဖြင့် အသေးစိတ် ဘာသာပြန်ဆိုပေးပါ။"]
            )
            
            progress_bar.progress(100)
            status_text.text("ဘာသာပြန်ဆိုခြင်း ပြီးဆုံးပါပြီ (100%)!")
            
            st.success("အောင်မြင်ပါသည်။ ရရှိလာသော မြန်မာဘာသာပြန်ဆိုချက်များ:")
            st.write(response.text)
            
            # ဗီဒီယိုကိုပါ ပြန်လည်ပြသပေးမည်
            st.video(file_path)
            
        except Exception as e:
            st.error(f"လုပ်ဆောင်ရာတွင် အမှားအယွင်း ရှိပါသည်: {e}")
            
    else:
        st.warning("ကျေးဇူးပြု၍ ဗီဒီယိုဖိုင် အရင်တင်ပေးပါ။")
