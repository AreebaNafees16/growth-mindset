import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

# Web App Title
st.title("🌱 Growth Mindset Challenge")

# Introduction
st.write("""
## Do You Have a Growth Mindset?
Your abilities can improve through continuous effort, experience, and learning.
This app will help you enhance your Growth Mindset with interactive features!
""")

# Input Section
name = st.text_input("Enter your name")
if st.button("Submit"):
    st.success(f"🎉 Thank you {name}! You have taken the first step!")

# Challenges and Advice
st.subheader("🔥 Key Principles to Adopt a Growth Mindset:")
st.markdown("- **Embrace Challenges** 🚀")
st.markdown("- **Learn from Mistakes** 🧠")
st.markdown("- **Stay Positive and Persistent** 💪")
st.markdown("- **Seek Feedback and Improve** 💡")

# Random Motivational Quote Generator
def get_random_quote():
    quotes = [
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Believe you can and you're halfway there.",
        "Your limitation—it's only your imagination.",
        "Push yourself, because no one else is going to do it for you.",
        "Dream it. Wish it. Do it."
    ]
    return random.choice(quotes)

st.subheader("🌟 Daily Motivation:")
st.info(get_random_quote())

# Progress Chart
data = pd.DataFrame({"Week": ["Week 1", "Week 2", "Week 3", "Week 4"], "Progress": [10, 30, 50, 80]})
fig, ax = plt.subplots()
ax.plot(data["Week"], data["Progress"], marker="o", linestyle="--", color="b")
ax.set_title("📈 Your Growth Progress")
ax.set_xlabel("Week")
ax.set_ylabel("Progress (%)")

# Display Chart
st.pyplot(fig)

# Interactive Quiz
def growth_mindset_quiz():
    st.subheader("🧠 Quick Growth Mindset Quiz!")
    question = "What should you do when you make a mistake?"
    options = ["Ignore it", "Learn from it", "Give up"]
    answer = st.radio(question, options)
    if st.button("Check Answer"):
        if answer == "Learn from it":
            st.success("✅ Correct! Learning from mistakes is key to growth.")
        else:
            st.error("❌ Incorrect. Try again and remember to embrace challenges!")

growth_mindset_quiz()
