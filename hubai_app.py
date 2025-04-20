import streamlit as st
from PIL import Image

# --- Page Configuration ---
st.set_page_config(
    page_title="HubAI - Your All-in-One AI Platform",
    page_icon="🧠",
    layout="wide"
)

# --- Custom CSS for styling ---
st.markdown("""
<style>
/* Main background */
body { background: #121212; color: #e0e0e0; }
/* Sidebar styling */
[data-testid="stSidebar"] { background-color: #1f1f1f; color: #fff; padding-top: 30px; }
/* Header styling */
.header { text-align: center; font-size: 3rem; font-weight: 700; margin: 10px 0; }
.subheader { text-align: center; font-size: 1.25rem; color: #bbbbbb; margin-bottom: 40px; }
/* Card container */
.card { background: linear-gradient(145deg, #2a2a2a, #222222); border-radius: 20px; padding: 30px; box-shadow: 8px 8px 16px #1a1a1a, -8px -8px 16px #333333; transition: transform 0.3s ease, box-shadow 0.3s ease; display: flex; flex-direction: column; align-items: center; justify-content: center; margin: 10px; }
.card:hover { transform: translateY(-10px); box-shadow: 12px 12px 24px #161616, -12px -12px 24px #3a3a3a; }
.card-icon { font-size: 2.5rem; margin-bottom: 15px; }
.card-title { font-size: 1.5rem; font-weight: 600; margin-bottom: 8px; }
.card-desc { font-size: 1rem; color: #cccccc; text-align: center; margin-bottom: 20px; }
.card-btn { background-color: #e94560; color: #ffffff; padding: 10px 20px; border: none; border-radius: 12px; font-size: 1rem; cursor: pointer; text-decoration: none; display: inline-block; }
.card-btn:hover { background-color: #ff2e4c; }
.footer { text-align: center; color: #666666; margin: 60px 0 30px; }
</style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("📂 HubAI")
pages = ["Home", "About", "Privacy Policy"]
selection = st.sidebar.radio("Navigate to", pages)

# AI details for Home
ai_details = {
    "Rufus AI": {"desc": "Your GenZ Tutor", "url": "https://rufusai.streamlit.app", "icon": "📝"},
    "TherAI": {"desc": "Your AI Therapist", "url": "https://therai.streamlit.app", "icon": "💬"},
    "StartItAI": {"desc": "Your Startup Sidekick", "url": "https://startitai.streamlit.app", "icon": "🚀"},
    "PlanPal AI": {"desc": "Your Life & Event Planner", "url": "https://planpalai.streamlit.app", "icon": "📅"},
    "Designo AI": {"desc": "Your Creative Brainstormer", "url": "https://designoai.streamlit.app", "icon": "🎨"},
    "Knowva AI": {"desc": "Your Curiosity Buddy", "url": "https://knowvaai.streamlit.app", "icon": "🔍"},
    "CrushAI": {"desc": "Your Flirty Life Coach", "url": "https://crushai.streamlit.app", "icon": "❤️"},
}

# --- Page Rendering ---
if selection == "Home":
    st.markdown("<div class='header'>🧠 Welcome to HubAI</div>", unsafe_allow_html=True)
    st.markdown("<div class='subheader'>Your central platform for all AI assistants</div>", unsafe_allow_html=True)
    # Always use 3 columns for equal card widths
    items = list(ai_details.items())
    for i in range(0, len(items), 3):
        cols = st.columns(3, gap="large")
        for idx, col in enumerate(cols):
            with col:
                if i + idx < len(items):
                    name, info = items[i + idx]
                    card_html = f"""
                    <div class='card'>
                        <div class='card-icon'>{info['icon']}</div>
                        <div class='card-title'>{name}</div>
                        <div class='card-desc'>{info['desc']}</div>
                        <a href='{info['url']}' target='_blank' class='card-btn'>Launch {name}</a>
                    </div>
                    """
                    st.markdown(card_html, unsafe_allow_html=True)
                else:
                    st.markdown("<div style='margin:10px;'></div>", unsafe_allow_html=True)
elif selection == "About":
    st.markdown("<div class='header'>About HubAI</div>", unsafe_allow_html=True)
    st.write(
        "HubAI is the ultimate AI hub for domains from education to mental health, startups to creativity. "
        "Select an AI on Home to launch its dedicated experience."
    )
    st.write("\nDeveloped by AdityaCodess | © 2025 HubAI")
elif selection == "Privacy Policy":
    st.markdown("<div class='header'>Privacy Policy</div>", unsafe_allow_html=True)
    st.write("**Data Collection**: We do not store personal data on this site.")
    st.write("**AI Interactions**: All AI calls occur on their own domains—HubAI does not retain user inputs.")
    st.write("**Contact**: For questions, email support@hubai.com")
# Footer
st.markdown("<div class='footer'>Thank you for exploring HubAI!</div>", unsafe_allow_html=True)
