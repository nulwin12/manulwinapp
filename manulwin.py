import streamlit as st

st.title("🎬 မာန်ဦးလွင် ဗီဒီယိုနှင့် ရုပ်ရှင်ပြန်ဆိုချက်ဖန်တီးသူ")
st.write("ဗီဒီယိုဖိုင် တိုက်ရိုက်တင်၍ မြန်မာအသံဖြင့် ပြန်ဆိုချက်ပြုလုပ်နိုင်သော နေရာ။")

uploaded_file = st.file_uploader("ဗီဒီယိုဖိုင် (Video File) တင်ပါ:", type=["mp4", "mov", "avi"])

voice_option = st.selectbox(
    "အသံအမျိုးအစား ရွေးချယ်ပါ:",
    ("သီဟ (Thiha)", "နီလာ (Nila)", "ဘိုဘို (BoBo)")
)

if st.button("ဗီဒီယို စတင်ဖန်တီးမည်"):
    if uploaded_file is not None:
        st.success(f"အောင်မြင်ပါသည်! တင်ထားသော ဗီဒီယိုနှင့် ရွေးချယ်ထားသော အသံ ({voice_option}) ဖြင့် စတင်ဆောင်ရွက်နေပါပြီ။")
    else:
        st.warning("ကျေးဇူးပြု၍ ဗီဒီယိုဖိုင် အရင်တင်ပေးပါ။")
