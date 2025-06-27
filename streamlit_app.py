import streamlit as st
from streamlit_option_menu import option_menu
import smtplib
from email.message import EmailMessage
import datetime
import time

# ---------- Page Config ----------
st.set_page_config(page_title="About Me", page_icon="💻", layout="wide")

# ---------- Sidebar Navigation ----------
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["About Me", "Projects", "Contact Me"],
        icons=["person", "code", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"background-color": "#111111"},
            "icon": {"color": "#FFFFFF", "font-size": "25px"},
            "nav-link": {
                "font-size": "18px",
                "text-align": "left",
                "margin": "10px",
                "--hover-color": "#6c63ff",
                "color": "white",
            },
            "nav-link-selected": {"background-color": "#6c63ff"},
        },
    )

# ---------- About Me Page ----------
if selected == "About Me":
    st.markdown("<h1 style='color: #6c63ff;'>👋 Hi, I'm Koshin Nassib</h1>", unsafe_allow_html=True)
    st.image("https://beyondexclamation.com/wp-content/uploads/2020/12/10-1.jpg", use_container_width=True)

    st.markdown("""
    <div style='color: white; font-size: 18px;'>
        I'm a passionate developer who loves creating web apps, automation tools, and AI-driven projects.
        <br><br>
        I specialize in <b>Python</b>, <b>Streamlit</b>, and <b>Machine Learning</b>.
        <br><br>
        Welcome to my personal portfolio! 🚀
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    col1.metric("📁 Projects", "8+")
    col2.metric("💻 Experience", "3 Years")
    col3.metric("🧠 Skills", "Python, ML, Streamlit")

# ---------- Projects Page ----------
elif selected == "Projects":
    st.markdown("<h1 style='color: #6c63ff;'>💼 Projects</h1>", unsafe_allow_html=True)

    project_data = [
        {
            "title": "AI Chatbot",
            "desc": "A chatbot built with NLP techniques and OpenAI API integration.",
            "link": "https://github.com/koshin-ai/chatbot"
        },
        {
            "title": "Portfolio Website",
            "desc": "A fully responsive Streamlit-powered personal website.",
            "link": "https://github.com/koshin-ai/portfolio"
        },
        {
            "title": "Auto Email Sender",
            "desc": "Python automation script for sending bulk emails with templates.",
            "link": "https://github.com/koshin-ai/email-sender"
        }
    ]

    for project in project_data:
        with st.container():
            st.subheader(f"🔹 {project['title']}")
            st.write(project['desc'])
            st.markdown(f"[GitHub Repo]({project['link']})")
            st.markdown("---")

# ---------- Contact Me Page ----------
elif selected == "Contact Me":
    st.markdown("<h1 style='color: #6c63ff;'>📨 Contact Me</h1>", unsafe_allow_html=True)

    with st.form(key="contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")

        if submitted:
            if name and email and message:
                try:
                    # Replace these with your actual credentials
                    sender_email = "wspmybro123@gmail.com"
                    sender_password = "k_1033262"
                    recipient_email = "wspmybro123@gmail.com"
                    msg = EmailMessage()
                    msg["Subject"] = "New Contact Form Submission"
                    msg["From"] = sender_email
                    msg["To"] = recipient_email
                    msg.set_content(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")

                    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                        server.login(sender_email, sender_password)
                        server.send_message(msg)

                    st.success("Thanks for reaching out! I'll get back to you soon.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.warning("Please fill out all fields.")

    st.markdown("---")
    st.info("Alternatively, connect with me on [LinkedIn](https://linkedin.com/in/yourusername)")

# ---------- Footer ----------
st.markdown("""
<hr style="border: 0.5px solid #6c63ff;">
<div style="text-align: center; color: gray;">
    &copy; 2025 Koshin Nassib | Built with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)
