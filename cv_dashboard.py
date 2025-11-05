import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px

# ==============================================================================
# PHASE 1: DATA SIMULATION (The Core of Your Game Analytics Project)
# ==============================================================================

@st.cache_data
def generate_mock_game_data(num_records=1000):
    """Generates a DataFrame of simulated Subway Surfers-like game events."""
    start_date = datetime.now() - timedelta(days=30)
    
    data = {
        'player_id': np.random.randint(1000, 2000, num_records),
        # Simulate timestamps over the last 30 days
        'timestamp': [start_date + timedelta(hours=i * 0.75) for i in range(num_records)],
        # The key events for a runner game
        'event_type': np.random.choice(['run_start', 'coin_collect', 'crash', 'powerup_used', 'ad_watch'], 
                                       num_records, 
                                       p=[0.2, 0.4, 0.1, 0.2, 0.1]),
        'coins_gained': np.random.randint(0, 50, num_records),
        'score': np.random.randint(500, 50000, num_records),
    }
    df = pd.DataFrame(data)
    df['date'] = df['timestamp'].dt.date
    return df

game_df = generate_mock_game_data()

# ==============================================================================
# PHASE 2: CUSTOM STYLING FUNCTIONS AND CSS INJECTION
# ==============================================================================

def score_box(col, label, value, delta_text, color):
    """Generates a custom HTML score box with a game theme."""
    col.markdown(f"""
        <div style='
            background-color: {color}; 
            padding: 10px; 
            border-radius: 8px; 
            text-align: center; 
            border: 3px solid #000; 
            margin-bottom: 10px; 
            box-shadow: 5px 5px 0 #1c1c1c; 
            min-height: 100px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        '>
            <p style='font-size: 0.8rem; color: #fff; margin: 0; font-weight: bold; text-shadow: 1px 1px 0 #000;'>{label}</p>
            <h2 style='color: #fff; margin: 5px 0; font-family: "Arial Black", sans-serif; text-shadow: 2px 2px 0 #000;'>{value}</h2>
            <p style='font-size: 0.7rem; color: #eee; margin: 0;'>{delta_text}</p>
        </div>
    """, unsafe_allow_html=True)

# 1. Page Configuration
st.set_page_config(layout="wide", page_title="Vaishnavi's Player Profile", initial_sidebar_state="collapsed")

# 2. Game-Themed Title Banner and Styling (CSS Injection)
st.markdown("""
    <style>
    /* 1. Global Background (Dark Blue/Grey for Urban feel) */
    .stApp {
        background-color: #2c3e50; 
    }
    /* 2. Main title banner (Orange/Red Graffiti style) */
    .game-banner {
        background-color: #f39c12; 
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border: 5px solid #e74c3c; 
        box-shadow: 0 10px 0 #c0392b; 
        color: white;
        font-family: 'Arial Black', sans-serif; 
        text-shadow: 4px 4px 0 #2c3e50;
        margin-bottom: 15px;
    }
    /* 3. Mission Objective Text */
    .mission-text {
        color: #ecf0f1; 
        font-size: 1.1rem;
        text-align: center;
        margin-top: 15px;
        font-style: italic;
    }
    /* 4. Main Headers */
    h1, h2, h3, h4 {
        color: #fff; /* White headers */
        text-shadow: 2px 2px 2px #000;
    }
    /* 5. Separator line */
    hr {
        border-top: 3px solid #f1c40f; /* Yellow/Gold separator */
    }
    /* 6. Style the Tabs to look like menu selectors */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px; /* Space between tabs */
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #34495e; /* Dark Tab Background */
        border-radius: 8px 8px 0 0;
        border: 2px solid #2c3e50;
        padding: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #f39c12; /* Active Tab Color (Orange) */
        color: white;
        border-bottom: 5px solid #e67e22;
        box-shadow: 0 2px 0 #c0392b;
    }
    /* 7. Streamlit Button Styling (Optional: use if you add st.button later) */
    .stButton>button {
        background-color: #e74c3c; 
        color: white;
        border: 4px solid #c0392b; 
        border-radius: 12px;
        box-shadow: 0 5px 0 #922b21; 
        padding: 10px 20px;
        font-weight: bold;
        text-shadow: 1px 1px 0 #000;
    }
    </style>
    <div class='game-banner'>
        <h1 style='margin:0;'>VAISHNAVI S: DATA ENGINEER PLAYER PROFILE</h1>
    </div>
    <p class='mission-text'>
        🎯 MISSION START: Aspiring Data Engineer passionate about real-time data pipelines and gaming analytics. building strong foundation in Python, SQL, and data systems, I am aiming to power data-driven decisions behind global games like **Subway Surfers**.
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# 3. Key Performance Indicators (KPIs / Player Stats)
st.header("⚡ Player Stats & Key Achievements")

col1, col2, col3, col4 = st.columns(4)

# Data based on your CV content
score_box(col1, "🎓 High Score (Expected Graduation)", "2026", "B.Tech AIML", "#1abc9c") # Teal
score_box(col2, "💰 Coins Collected (Projects)", "3", "Level 3 Cleared", "#f1c40f") # Yellow
score_box(col3, "🔑 Power-Ups Unlocked (Achievements)", "2", "Deloitte & IBM", "#9b59b6") # Purple
score_box(col4, "🚀 Best Run Time (Core Languages)", "Python, SQL, Java", "Data Tools Ready", "#e74c3c") # Red

st.markdown("---")

# 4. Levels Cleared (Projects)
st.header("🕹️ Levels Cleared: Project Portfolio")

tab1, tab2, tab3 = st.tabs(["LEVEL 1: GAME ANALYTICS", "LEVEL 2: BEAUTY BRAND INSIGHTS", "LEVEL 3: IMDB CLASSIFIER"])

# --- Tab 1: Game Analytics Visualization (MOST IMPORTANT SECTION) ---
with tab1:
    st.markdown("### 🎮 Game Analytics Pipeline Simulation (still developing)")
    st.markdown("""
        **Objective:** Simulating player event data to build a real-time pipeline using **Python**, **Spark**, and **Firebase** — processing 'run', 'coin', and 'crash' events like *Subway Surfers* gameplay to demonstrate foundational skills in game telemetry.
    """)

    # Data Aggregation for the chart
    event_counts = game_df.groupby('date')['event_type'].value_counts().unstack(fill_value=0)
    chart_data = event_counts[['run_start', 'crash', 'coin_collect']].reset_index()

    # Create the Plotly Chart: Demonstrates visualization skill
    fig = px.line(
        chart_data, 
        x='date', 
        y=['run_start', 'crash', 'coin_collect'], 
        title='Game Events Over Time (Last 30 Days)',
        labels={'value': 'Event Count', 'date': 'Date', 'variable': 'Event Type'},
        color_discrete_map={'run_start': '#1abc9c', 'crash': '#e74c3c', 'coin_collect': '#f1c40f'}
    )
    st.plotly_chart(fig, use_container_width=True)

    # Displaying a key metric (Crash Rate & DAU)
    avg_crash = chart_data['crash'].mean()
    dau = game_df.groupby('date')['player_id'].nunique().mean()
    
    col_insight_1, col_insight_2 = st.columns(2)
    with col_insight_1:
        st.info(f"**🔥 Average Daily Crash Events:** **{avg_crash:.1f}** (Insight needed to optimize level design)")
    with col_insight_2:
        st.info(f"**🧑‍🤝‍🧑 Average Daily Active Players (DAU):** **{int(dau)}**")


# --- Tab 2: Beauty Brand Insights ---
with tab2:
    st.markdown("### 🛍️ Beauty Brand Insights Dashboard (Streamlit, Pandas, Plotly, Firebase)")
    st.markdown("""
        **Objective:** Built an interactive analytics dashboard showing product trends and recommendations, with **real-time updates** via Firebase. 
        This demonstrates the ability to connect a frontend dashboard to a dynamic data source.
    """)
    st.markdown("**Key Skills Shown:** Full-stack dashboard design, Plotly visualization, Real-time data handling (Firebase), **Business Intelligence (BI)**.")
    
# --- Tab 3: IMDB Movie Reviews Classifier ---
with tab3:
    st.markdown("### 🎬 IMDB Movie Reviews Classifier (Python, Scikit-learn, NLP)")
    st.markdown("""
        **Objective:** Created an end-to-end machine learning model to classify movie review sentiments using Scikit-learn and **Natural Language Processing (TF-IDF vectorization)**.
        This demonstrates your Machine Learning foundation.
    """)
    st.markdown("**Key Skills Shown:** Machine Learning lifecycle, Data Preprocessing, NLP techniques, Model training/evaluation.")
    
    # Placeholder for model results
    st.info("Insight: Model achieved **85% Accuracy** in sentiment classification (demonstrating model evaluation).")


st.markdown("---")

# 5. Power-Ups (Skills Visualization)
st.header("🛠️ Power-Ups Acquired (Technical Skills)")

skills_data = {
    'Category': ['Languages', 'Data Processing', 'Cloud & DB', 'Version Control'],
    'Proficiency Score (1-5)': [5, 4, 3, 5], 
    'Details': ['Python, SQL, Java', 'Pandas, NumPy, Scikit-learn, PySpark (learning)', 'Firebase Firestore, Google Cloud (beginner)', 'Git, GitHub, VSCode']
}
skills_df = pd.DataFrame(skills_data)

col_skills_chart, col_skills_table = st.columns([1, 2])

with col_skills_chart:
    # Bar chart to visually show skill spread
    fig_skills = px.bar(
        skills_df, 
        x='Category', 
        y='Proficiency Score (1-5)', 
        color='Category', 
        title="Skill Proficiency Rating",
        color_discrete_sequence=px.colors.qualitative.D3 
    )
    st.plotly_chart(fig_skills, use_container_width=True)
    
with col_skills_table:
    st.subheader("Skill Inventory")
    st.table(skills_df[['Category', 'Details']])
    st.markdown("Visualization Tools: **Plotly**, **Streamlit** | Pipeline Tools: **Airflow**, **Kafka** (exploring)")


st.markdown("---")

# 6. Next Mission / Contact Info
st.header("🚀 NEXT MISSION: Ready to Deploy")
st.markdown("""
    <div style='background-color:#1abc9c; padding: 10px; border-radius: 5px; color: #fff; border: 2px solid #000;'>
        Seeking an internship or entry-level opportunity in Data Engineering / Gaming Analytics — ready to build and optimize real-time data systems that make global gaming experiences smarter and more fun.
    </div>
""", unsafe_allow_html=True)


st.markdown("### 📞 Contact Portal (Respawn Point)")
st.markdown(f"""
<div style='color: #ecf0f1;'>
* 🗺️ **Location:** Hyderabad, Telangana, India
* 📧 **Email:** **vaishnavivs285@gmail.com**
* 📞 **Phone:** +91-9346528810
* 🔗 **LinkedIn:** [vaishnavii28](https://www.linkedin.com/in/vaishnavii28/)
* 💻 **GitHub:** [vaishnavivs285](https://github.com/vaishnavivs285)
</div>
""", unsafe_allow_html=True)