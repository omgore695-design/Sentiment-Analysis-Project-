# import streamlit as st
# import pickle
# import time
# import random
# import plotly.graph_objects as go
# from textblob import TextBlob
# from streamlit_lottie import st_lottie
# from streamlit_mic_recorder import mic_recorder
# import requests

# # =========================================
# # PAGE CONFIG
# # =========================================

# st.set_page_config(
#     page_title="AI Sentiment Analyzer",
#     page_icon="🤖",
#     layout="wide"
# )

# # =========================================
# # LOAD MODEL
# # =========================================

# model = pickle.load(open("models/model.pkl", "rb"))
# vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

# # =========================================
# # LOAD LOTTIE ANIMATION
# # =========================================

# def load_lottie(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# lottie_ai = load_lottie(
#     "https://assets2.lottiefiles.com/packages/lf20_xvrofzfk.json"
# )

# # =========================================
# # CUSTOM CSS
# # =========================================

# st.markdown("""
# <style>

# .stApp {
#     background-image: url("https://images.unsplash.com/photo-1516321318423-f06f85e504b3");
#     background-size: cover;
#     background-position: center;
#     background-attachment: fixed;
# }

# .main-box {
#     background: rgba(0,0,0,0.7);
#     padding: 30px;
#     border-radius: 25px;
#     backdrop-filter: blur(10px);
# }

# .title {
#     text-align:center;
#     font-size:55px;
#     color:#00FFD1;
#     font-weight:bold;
#     text-shadow:2px 2px 10px black;
# }

# .subtitle {
#     text-align:center;
#     color:white;
#     font-size:22px;
#     margin-bottom:30px;
# }

# .stTextArea textarea {
#     background-color: rgba(38,39,48,0.9);
#     color:white;
#     border-radius:15px;
#     border:2px solid #00FFD1;
#     font-size:18px;
# }

# .stButton>button {
#     width:100%;
#     background: linear-gradient(to right,#00FFD1,#00C9FF);
#     color:black;
#     font-size:22px;
#     font-weight:bold;
#     border:none;
#     border-radius:15px;
#     height:3.5em;
# }

# .stButton>button:hover {
#     background: linear-gradient(to right,#FF4B4B,#FF9F1C);
#     color:white;
#     transform:scale(1.02);
#     transition:0.3s;
# }

# .footer {
#     text-align:center;
#     color:white;
#     margin-top:40px;
#     font-size:16px;
# }

# </style>
# """, unsafe_allow_html=True)

# # =========================================
# # HEADER
# # =========================================

# st.markdown(
#     '<div class="title">🤖 AI Sentiment Analyzer</div>',
#     unsafe_allow_html=True
# )

# st.markdown(
#     '<div class="subtitle">Analyze Human Emotions using Artificial Intelligence 🚀</div>',
#     unsafe_allow_html=True
# )

# # =========================================
# # LOTTIE ANIMATION
# # =========================================

# st_lottie(lottie_ai, height=250)

# # =========================================
# # TYPING EFFECT
# # =========================================

# typing_text = "💡 AI can understand emotions from text instantly..."

# placeholder = st.empty()

# typed = ""

# for char in typing_text:
#     typed += char
#     placeholder.markdown(f"## {typed}")
#     time.sleep(0.03)

# # =========================================
# # INPUT SECTION
# # =========================================

# st.markdown("## ✍️ Enter Tweet")

# text = st.text_area(
#     "",
#     height=180,
#     placeholder="Type your tweet here..."
# )

# # =========================================
# # VOICE INPUT
# # =========================================

# st.markdown("### 🎤 Voice Input")

# audio = mic_recorder(
#     start_prompt="🎙️ Start Recording",
#     stop_prompt="⏹️ Stop Recording",
#     key='recorder'
# )

# # =========================================
# # PREDICT BUTTON
# # =========================================

# if st.button("🚀 Analyze Sentiment"):

#     if text.strip() == "":
#         st.warning("⚠️ Please enter some text!")
#     else:

#         with st.spinner("🧠 AI is analyzing emotion..."):
#             time.sleep(2)

#             vector = vectorizer.transform([text])

#             prediction = model.predict(vector)

#         # =========================================
#         # LIVE SENTIMENT SCORE
#         # =========================================

#         polarity = TextBlob(text).sentiment.polarity

#         sentiment_score = (polarity + 1) * 50

#         fig = go.Figure(go.Indicator(
#             mode="gauge+number",
#             value=sentiment_score,
#             title={'text': "Sentiment Meter"},
#             gauge={
#                 'axis': {'range': [0, 100]},
#                 'bar': {'color': "cyan"},
#                 'steps': [
#                     {'range': [0, 40], 'color': "red"},
#                     {'range': [40, 60], 'color': "yellow"},
#                     {'range': [60, 100], 'color': "green"},
#                 ]
#             }
#         ))

#         st.plotly_chart(fig)

#         # =========================================
#         # PIE CHART
#         # =========================================

#         if prediction[0] == 1:
#             labels = ['Positive', 'Negative']
#             values = [85, 15]
#         else:
#             labels = ['Positive', 'Negative']
#             values = [20, 80]

#         pie = go.Figure(
#             data=[go.Pie(labels=labels, values=values, hole=.4)]
#         )

#         st.plotly_chart(pie)

#         # =========================================
#         # RESULT
#         # =========================================

#         if prediction[0] == 1:

#             st.balloons()

#             st.success("😍 POSITIVE SENTIMENT DETECTED")

#             st.markdown("""
#             # 🌈✨😊🔥🎉💖🚀
#             """)

#         else:

#             st.error("😡 NEGATIVE SENTIMENT DETECTED")

#             st.markdown("""
#             # 💔😢⚠️😡🥀
#             """)

# # =========================================
# # SIDEBAR
# # =========================================

# st.sidebar.title("📌 Project Features")

# st.sidebar.success("""
# ✅ Machine Learning

# ✅ NLP

# ✅ TF-IDF

# ✅ Logistic Regression

# ✅ Voice Input

# ✅ Lottie Animation

# ✅ Sentiment Meter

# ✅ Pie Chart

# ✅ Glassmorphism UI
# """)

# # =========================================
# # TWITTER/X LOGO
# # =========================================

# st.sidebar.image(
#     "https://cdn-icons-png.flaticon.com/512/5969/5969020.png",
#     width=100
# )

# # =========================================
# # FOOTER
# # =========================================

# st.markdown("""
# <div class="footer">
# Made with ❤️ by Om Gore | AI + NLP + Streamlit
# </div>
# """, unsafe_allow_html=True)
# from streamlit_lottie import st_lottie
import streamlit as st
import pickle
import time
import random
import plotly.graph_objects as go
from textblob import TextBlob
from streamlit_lottie import st_lottie
from streamlit_mic_recorder import mic_recorder
import requests

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="AI Sentiment Analyzer",
    page_icon="🤖",
    layout="wide"
)

# =========================================
# LOAD MODEL
# =========================================

model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

# =========================================
# LOAD LOTTIE ANIMATION
# =========================================

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_ai = load_lottie(
    "https://assets2.lottiefiles.com/packages/lf20_xvrofzfk.json"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0F172A,
        #111827,
        #1E293B
    );
}

.main-box {
    background: rgba(0,0,0,0.7);
    padding: 30px;
    border-radius: 25px;
    backdrop-filter: blur(10px);
}

.title {
    text-align:center;
    font-size:55px;
    color:#00FFD1;
    font-weight:bold;
    text-shadow:2px 2px 10px black;
}

.subtitle {
    text-align:center;
    color:white;
    font-size:22px;
    margin-bottom:30px;
}

.stTextArea textarea {
    background-color: rgba(38,39,48,0.9);
    color:white;
    border-radius:15px;
    border:2px solid #00FFD1;
    font-size:18px;
}

.stButton>button {
    width:100%;
    background: linear-gradient(to right,#00FFD1,#00C9FF);
    color:black;
    font-size:22px;
    font-weight:bold;
    border:none;
    border-radius:15px;
    height:3.5em;
}

.stButton>button:hover {
    background: linear-gradient(to right,#FF4B4B,#FF9F1C);
    color:white;
    transform:scale(1.02);
    transition:0.3s;
}

.footer {
    text-align:center;
    color:white;
    margin-top:40px;
    font-size:16px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.markdown(
    '<div class="title">🤖 AI Sentiment Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Analyze Human Emotions using Artificial Intelligence 🚀</div>',
    unsafe_allow_html=True
)

# =========================================
# LOTTIE ANIMATION
# =========================================

st_lottie(lottie_ai, height=250)

# =========================================
# TYPING EFFECT
# =========================================

typing_text = "💡 AI can understand emotions from text instantly..."

placeholder = st.empty()

typed = ""

for char in typing_text:
    typed += char
    placeholder.markdown(f"## {typed}")
    time.sleep(0.03)

# =========================================
# INPUT SECTION
# =========================================

st.markdown("## ✍️ Enter Tweet")

text = st.text_area(
    "",
    height=180,
    placeholder="Type your tweet here..."
)

# =========================================
# VOICE INPUT
# =========================================

st.markdown("### 🎤 Voice Input")

audio = mic_recorder(
    start_prompt="🎙️ Start Recording",
    stop_prompt="⏹️ Stop Recording",
    key='recorder'
)

# =========================================
# PREDICT BUTTON
# =========================================

if st.button("🚀 Analyze Sentiment"):

    if text.strip() == "":
        st.warning("⚠️ Please enter some text!")
    else:

        with st.spinner("🧠 AI is analyzing emotion..."):
            time.sleep(2)

            vector = vectorizer.transform([text])

            prediction = model.predict(vector)

        # =========================================
        # LIVE SENTIMENT SCORE
        # =========================================

        polarity = TextBlob(text).sentiment.polarity

        sentiment_score = (polarity + 1) * 50

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=sentiment_score,
            title={'text': "Sentiment Meter"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "cyan"},
                'steps': [
                    {'range': [0, 40], 'color': "red"},
                    {'range': [40, 60], 'color': "yellow"},
                    {'range': [60, 100], 'color': "green"},
                ]
            }
        ))

        st.plotly_chart(fig)

        # =========================================
        # PIE CHART
        # =========================================

        if prediction[0] == 1:
            labels = ['Positive', 'Negative']
            values = [85, 15]
        else:
            labels = ['Positive', 'Negative']
            values = [20, 80]

        pie = go.Figure(
            data=[go.Pie(labels=labels, values=values, hole=.4)]
        )

        st.plotly_chart(pie)

        # =========================================
        # RESULT
        # =========================================

        if prediction[0] == 1:

            st.balloons()

            st.success("😍 POSITIVE SENTIMENT DETECTED")

            st.markdown("""
            # 🌈✨😊🔥🎉💖🚀
            """)

        else:

            st.error("😡 NEGATIVE SENTIMENT DETECTED")

            st.markdown("""
            # 💔😢⚠️😡🥀
            """)

# =========================================
# SIDEBAR
# =========================================

st.sidebar.title("📌 Project Features")

st.sidebar.success("""
✅ Machine Learning

✅ NLP

✅ TF-IDF

✅ Logistic Regression

✅ Voice Input

✅ Lottie Animation

✅ Sentiment Meter

✅ Pie Chart

✅ Glassmorphism UI
""")

# =========================================
# TWITTER/X LOGO
# =========================================

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/5969/5969020.png",
    width=100
)

# =========================================
# FOOTER
# =========================================

st.markdown("""
<div class="footer">
Made with ❤️ by Om Gore | AI + NLP + Streamlit
</div>
""", unsafe_allow_html=True)