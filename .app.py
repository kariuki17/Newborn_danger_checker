import streamlit as st
from fuzzywuzzy import fuzz
from datetime import datetime

# Danger signs dictionary with synonyms
danger_signs = {
    "fever": {
        "advice": "Your baby has a fever. This can be serious in newborns. Seek medical attention immediately.",
        "urgency": "urgent",
        "keywords": ["fever", "hot body", "high temperature", "warm to touch"]
    },
    "hypothermia": {
        "advice": "Low body temperature can be dangerous. Keep the baby warm and visit a clinic urgently.",
        "urgency": "urgent",
        "keywords": ["cold body", "low temperature", "hypothermia", "shivering"]
    },
    "difficulty breathing": {
        "advice": "Breathing problems require immediate attention. Please go to a hospital now.",
        "urgency": "urgent",
        "keywords": ["difficulty breathing", "breathing fast", "struggling to breathe", "wheezing", "gasping"]
    },
    "convulsions": {
        "advice": "Convulsions are a medical emergency. Seek urgent care.",
        "urgency": "urgent",
        "keywords": ["convulsions", "fits", "seizures", "shaking uncontrollably"]
    },
    "poor feeding": {
        "advice": "If your baby is not feeding well, it may be a danger sign. Visit a clinic immediately.",
        "urgency": "urgent",
        "keywords": ["poor feeding", "refusing to feed", "not breastfeeding", "not eating"]
    },
    "vomiting everything": {
        "advice": "Persistent vomiting is dangerous. Take your baby to a healthcare provider.",
        "urgency": "urgent",
        "keywords": ["vomiting everything", "throwing up all", "can't keep milk down", "projectile vomiting"]
    },
    "lethargy": {
        "advice": "If your baby is unusually sleepy or unresponsive, seek urgent care.",
        "urgency": "urgent",
        "keywords": ["lethargy", "very sleepy", "unresponsive", "weak", "no energy"]
    },
    "diarrhoea": {
        "advice": "Dehydration from diarrhoea can be life-threatening in newborns. Get medical help.",
        "urgency": "urgent",
        "keywords": ["diarrhoea", "watery stool", "loose stool", "frequent stool"]
    },
    "jaundice": {
        "advice": "If your baby's skin or eyes look yellow, seek medical advice immediately.",
        "urgency": "warning",
        "keywords": ["jaundice", "yellow skin", "yellow eyes"]
    }
}

st.set_page_config(page_title="Newborn Danger Sign Checker", page_icon="🍼")

st.title("🍼 Newborn Danger Sign Checker")
st.write("Describe your baby's symptoms below to check for possible danger signs.")

# User input
symptom_input = st.text_area("Enter symptoms (e.g., 'baby breathing fast, yellow eyes'):")

# Function to find matches
def find_matches(user_text):
    detected = []
    for sign, details in danger_signs.items():
        for keyword in details["keywords"]:
            if fuzz.partial_ratio(keyword.lower(), user_text.lower()) >= 80:
                detected.append(sign)
                break
    return list(set(detected))

if st.button("Check Danger Signs"):
    if symptom_input.strip():
        matches = find_matches(symptom_input)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if matches:
            st.subheader(f"🕒 Check done at {timestamp}")
            urgent_signs = [s for s in matches if danger_signs[s]["urgency"] == "urgent"]
            warning_signs = [s for s in matches if danger_signs[s]["urgency"] == "warning"]

            if urgent_signs:
                st.error("🚨 **Urgent Danger Signs Detected:**")
                for s in urgent_signs:
                    st.markdown(f"**{s.title()}** → {danger_signs[s]['advice']}")

            if warning_signs:
                st.warning("⚠️ **Warning Signs Detected:**")
                for s in warning_signs:
                    st.markdown(f"**{s.title()}** → {danger_signs[s]['advice']}")

        else:
            st.success("✅ No matching danger signs found. However, if you are worried, please consult a doctor.")
    else:
        st.warning("Please enter a symptom description.")

# Disclaimer
st.caption("⚠️ This tool is for informational purposes only and is not a substitute for professional medical advice.")
