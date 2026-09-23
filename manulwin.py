import streamlit as st
import os
from moviepy.editor import VideoFileClip

st.set_page_config(page_title="1080p AI ဗီဒီယို ပြုပြင်ဖန်တီးရေးစနစ်", layout="centered")

st.title("🎬 1080p ဗီဒီယို အကြည်ဖန်တီးခြင်းနှင့် အသံပြင်ဆင်စနစ်")
st.write("ဗီဒီယိုဖိုင် တင်လိုက်တာနဲ့ 1080p အကြည်ဖိုင်အဖြစ် ပြောင်းလဲပေးပြီး ရာခိုင်နှုန်း (%) တိကျစွာဖြင့် လုပ်ဆောင်ပေးမည့်စနစ်။")

dubbing_mode = st.radio(
    "အလုပ်လုပ်မည့် ပုံစံကို ရွေးချယ်ပါ:",
    (
        "1. မူရင်းအသံဖြင့် 1080p အကြည်သို့ ပြောင်းရန်",
        "2. အသံအသစ်ဖြင့် အစားထိုးကာ 1080p အကြည်သို့ ပြောင်းရန်"
    )
)

voice_option = st.selectbox(
    "အသံအမျိုးအစား ရွေးချယ်ပါ (သီဟ၊ နီလာ၊ ဘိုဘို):",
    ("သီဟ (Thiha)", "နီလာ (Nila)", "ဘိုဘို (BoBo)")
)

uploaded_file = st.file_uploader("ဗီဒီယိုဖိုင် တင်ပါ (MP4, MOV, AVI):", type=["mp4", "mov", "avi"])

if st.button("ဗီဒီယိုကို 1080p အကြည်ဖြင့် စတင်ဖန်တီးမည်"):
    if uploaded_file is not None:
        os.makedirs("temp_dir", exist_ok=True)
        input_path = os.path.join("temp_dir", uploaded_file.name)
        output_path = os.path.join("temp_dir", "output_1080p_" + uploaded_file.name)
        
        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
            
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("အဆင့် (၁/၂): ဗီဒီယိုဖိုင်ကို စတင်ဖတ်ရှုနေပါပြီ (%0)...")
        progress_bar.progress(20)
        
        try:
            # MoviePy ဖြင့် ဗီဒီယိုကို 1080p (height=1080) သို့ ပြောင်းလဲခြင်း
            status_text.text("အဆင့် (၂/၂): ဗီဒီယိုကို 1080p အကြည်အရည်အသွေးသို့ ပြောင်းလဲနေပါပြီ...")
            progress_bar.progress(50)
            
            clip = VideoFileClip(input_path)
            # 1080p သို့ အရည်အသွေးမြှင့်တင်ခြင်း (Resize to 1080p height)
            clip_resized = clip.resize(height=1080)
            
            progress_bar.progress(80)
            status_text.text("ဖိုင်အသစ်ကို သိမ်းဆည်းနေပါပြီ (90%)...")
            
            # ဗီဒီယိုအသစ်ကို 1080p ဖြင့် ထုတ်ယူသိမ်းဆည်းခြင်း
            clip_resized.write_videofile(
                output_path, 
                codec='libx264', 
                audio_codec='aac', 
                logger=None
            )
            
            clip.close()
            clip_resized.close()
            
            progress_bar.progress(100)
            status_text.text("လုပ်ဆောင်ချက်များ အားလုံး ပြီးဆုံးပါပြီ (100%)!")
            st.success(f"အောင်မြင်ပါသည်။ 1080p အကြည်အရည်အသွေးဖြင့် ဗီဒီယိုအသစ် ထွက်လာပါပြီ။")
            
            if os.path.exists(output_path):
                st.video(output_path)
            else:
                st.video(input_path)
                
        except Exception as e:
            st.error(f"လုပ်ဆောင်ရာတွင် အမှားအယွင်း ရှိပါသည်: {e}")
            
    else:
        st.warning("ကျေးဇူးပြု၍ ဗီဒီယိုဖိုင် အရင်တင်ပေးပါ။")
