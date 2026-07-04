import streamlit as st

st.set_page_config(page_title="Vacation Planner", layout="centered", page_icon="🌸")

st.markdown("""
<style>

.main {
    background-color: #f6f8fc;
}

.card {
    padding:20px;
    border-radius:15px;
    background:white;
    color:#222222;          
    border:2px solid #e5e7eb;
    text-align:center;
    box-shadow:0 2px 8px rgba(0,0,0,0.08);
    margin-bottom:10px;
}

.big-title{
    text-align:center;
    font-size:38px;
    font-weight:bold;
    color:#2c3e50;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:30px;
}
            
div.stButton {
    display: flex;
    justify-content: center;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Options
# -----------------------------
flight_pref = [
    "Indigo (9800/- but it flights at 8, 9:30, 11, 12, 1)",
    "Akasa (8700/- but flight only at 1:00 pm)"
]

hotel_options = [
    "Airbnb - 3000 per night",
    "Woodpecker - 2400 per night",
    "MMT options - 3500 per night",
    "Fine Touch by One Tree - 3700 per night"
]

activities = [
    "Free Time",
    "Collect Gown",
    "Dinner with Vihang",
    "Visit Soni Aunty",
    "Meet Anu"
]

# -----------------------------
# Session State
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = 0
    st.session_state.flight = None
    st.session_state.hotel = None
    st.session_state.schedule = None

# -----------------------------
# Page 1
# -----------------------------
if st.session_state.page == 0:
    
    left, center, right = st.columns([3, 2, 3])
    with center:
        st.markdown('<p class="big-title">🌸 Vacation Planner</p>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">Plan your vacation in 3 simple steps!</p>', unsafe_allow_html=True)

        if st.button("Start Planning", use_container_width=True):
            st.session_state.page = 1
            st.rerun()

elif st.session_state.page == 1:

    st.markdown('<p class="big-title">Select your preferred flight</p>', unsafe_allow_html=True)

    col1,col2 = st.columns([2,1], gap="medium")
    # Resize the images to fit the column width

    with col1:
        st.image("images/indigo.jpg", width=200)
        st.markdown("### Indigo")
        st.caption("₹9800\n\n8, 9:30, 11, 12, 1")
        if st.button("Choose Indigo"):
            st.session_state.flight = flight_pref[0]

    with col2:
        st.image("images/akasa_air.png", width=200)
        st.markdown("### Akasa")
        st.caption("₹8700\n\n1 PM only")
        if st.button("Choose Akasa"):
            st.session_state.flight = flight_pref[1]

    if st.session_state.flight:
        st.session_state.page=2
        st.rerun()

# -----------------------------
# Page 2
# -----------------------------
if st.session_state.page == 2:

    st.markdown('<p class="big-title">Select your preferred hotel</p>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4, gap="medium")
    # Resize the images to fit the column width

    with col1:
        st.image("images/airbnb.jpg", width=200)
        st.markdown("### Basil Stays - Airbnb")
        st.caption("₹3500 per night")
        st.caption("7 min from campus")
        if st.button("Choose Airbnb"):
            st.session_state.hotel = hotel_options[0]

    with col2:
        st.image("images/woodpecker.jpg", width=200)
        st.markdown("### Woodpecker on MMT")
        st.caption("₹2400 per night")
        st.caption("10 min from campus")
        if st.button("Choose Woodpecker"):
            st.session_state.hotel = hotel_options[1]

    with col3:
        st.image("images/hkv_vibes.jpg", width=200)
        st.markdown("### HKV Luxury Vibes")
        st.caption("₹3700 per night")
        st.caption("12 min from campus")
        if st.button("Choose Luxury Vibes",use_container_width=True):
            st.session_state.hotel = hotel_options[2]

    with col4:
        st.image("images/fine_touch.jpg", width=200)
        st.markdown("### Fine Touch - One Tree")
        st.caption("₹3700 per night")
        st.caption("9 min from campus")
        if st.button("Choose Fine Touch",use_container_width=True):
            st.session_state.hotel = hotel_options[3]

    if st.session_state.hotel:
        st.session_state.page=3
        st.rerun()


# -----------------------------
# Page 3
# -----------------------------
elif st.session_state.page == 3:

    slots = [
        "Thursday Evening",
        "Friday Daytime",
        "Friday Evening",
        "Saturday Daytime",
        "Saturday Evening"
    ]

    fixed={"Saturday Daytime": "Convocation Ceremony"}

    if "Akasa" in st.session_state.flight:
        fixed={
            "Saturday Daytime": "Convocation Ceremony",
            "Thursday Evening": "Free Time",
            "Friday Daytime": "Collect Gown"
        }

    schedule={}
    used=[]

    for slot in slots:

        if slot in fixed:

            st.text_input(
                slot,
                value=fixed[slot],
                disabled=True
            )

            schedule[slot]=fixed[slot]
            used.append(fixed[slot])

            continue

        options=[
            a for a in activities
            if a not in used
        ]

        choice=st.selectbox(
            slot,
            options,
            key=slot
        )

        schedule[slot]=choice
        used.append(choice)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Back"):
            st.session_state.page = 2
            st.session_state.schedule = None
            st.rerun()

    with col2:
        if st.button("Generate Plan"):
            st.session_state.schedule = schedule
            st.session_state.page = 4
            st.rerun()

# -----------------------------
# Page 4
# -----------------------------
elif st.session_state.page == 4:

    st.markdown(
        "<h3 style='text-align:center;'>✈️ Flight</h3>",
        unsafe_allow_html=True
    )
    
    left, center, right = st.columns([1, 2, 1])
    with center:
        st.markdown(f"""
            <div class="card">
            <b>{st.session_state.flight}</b>
            </div>""",
            unsafe_allow_html=True, width=400)

    st.markdown(
        "<h3 style='text-align:center;'>🏨 Hotel</h3>",
        unsafe_allow_html=True
    )
    
    left, center, right = st.columns([1, 2, 1])
    with center:
        st.markdown(f"""
            <div class="card">
            <b>{st.session_state.hotel}</b>
            </div>""",
            unsafe_allow_html=True, width=400)

    # Align the schedule section to center
    st.markdown(
        "<h3 style='text-align:center;'>📅 Schedule</h3>",
        unsafe_allow_html=True
    )       

    left, center, right = st.columns([1, 2, 1])
    with center:
        for slot,activity in st.session_state.schedule.items():
            st.markdown(f"""
                <div class="card">
                <b>{slot} - {activity}</b>
                </div>""",
                unsafe_allow_html=True, width=400)
