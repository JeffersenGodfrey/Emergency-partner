import streamlit as st
import json
from nlp_engine import detect_emergency

# Set page configuration
st.set_page_config(page_title="Emergency Resource Finder", page_icon="🚨", layout="centered")

# Inject custom CSS for dropdown arrow + pointer fix
st.markdown("""
    <style>
    div[data-baseweb="select"] > div {
        cursor: pointer !important;
    }
    .stSelectbox > div > div {
        border-radius: 10px;
        border: 1px solid #aaa;
    }
    .stSelectbox label {
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
with open("data/emergency_data.json", "r") as file:
    DATA = json.load(file)

# Title
st.title("🚨 AI Emergency Resource Finder")
st.caption("Find emergency help nearby instantly — powered by offline data and simple AI.")

st.markdown("---")

# City-to-location mapping
city_map = {
    "Chennai": ["T Nagar", "Anna Nagar", "Velachery", "Saidapet", "Guindy", "Mylapore", "Chennai Central"],
    "Delhi": ["Connaught Place", "Central Delhi", "Rajiv Chowk", "Ansari Nagar"],
    "Mumbai": ["Andheri East", "Vikhroli", "Byculla"],
    "Bangalore": ["Bannerghatta", "Anekal", "Majestic"],
    "Pune": ["Wakad"],
    "Kolkata": ["Park Street", "Kolkata North"],
    "Tirupati": ["Tirupati"],
    "Nagpur": ["Nagpur"]
}

# Emergency form
with st.form("emergency_form"):
    st.subheader("📋 Emergency Search Form")
    
    city = st.selectbox("📍 Your City", ["", *city_map.keys()])
    emergency_type = st.selectbox("🚨 Emergency Type", ["", "Medical Emergency", "Flood Help", "Charging Station"])
    description = st.text_area("✏️ Describe Your Emergency (Optional)", placeholder="e.g. Need ambulance near T Nagar")

    submitted = st.form_submit_button("🔍 Find Help")

# Handle search
if submitted:
    st.markdown("---")

    if not city:
        st.error("Please select your city.")
    elif not emergency_type and not description:
        st.warning("Please choose an emergency type or describe the emergency.")
    else:
        # NLP fallback
        if not emergency_type and description:
            emergency_type = detect_emergency(description)

        st.subheader(f"🔎 Results for: **{emergency_type or 'General Emergency'} in {city}**")

        locations = city_map[city]
        results = [
            r for r in DATA
            if r["category"].lower() == emergency_type.lower()
            and r["location"] in locations
        ]

        if results:
            st.success(f"✅ Found {len(results)} resource(s) in {city}")
            for r in results:
                with st.expander(f"🔹 {r['name']} - {r['location']}"):
                    st.markdown(f"📞 **Contact:** {r['contact']}")
                    st.markdown(f"🏷️ **Type:** {r['category']}")
                    st.markdown(f"🧰 **Services:** {', '.join(r['services'])}")
                    st.caption(f"🕒 Last Updated: {r['last_updated']}")
        else:
            st.warning(f"⚠️ No matching emergency resources found in {city} for this type.")
            st.caption("Try changing the emergency type or providing more details.")
            
# Footer
st.markdown("---")
st.caption("💡 Built by Jeffersen | Works offline using local data | Demo-ready & fast 🚀")


