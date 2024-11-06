# Import necessary libraries
import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd

# Add custom styling
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    div[data-testid="stSidebarNav"] {
        background-color: #262730;
        padding: 1rem;
    }
    div[data-testid="stSidebarContent"] {
        background-color: #262730;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Title and Introduction ---
st.markdown("""
    <h1 style='text-align: center; 
               color: #4CAF50; 
               padding: 1rem; 
               margin-bottom: 2rem;
               text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>
        Interactive Visualizations with Plotly and Streamlit
    </h1>
    """, unsafe_allow_html=True)

# --- Input for Author Information ---
st.sidebar.markdown("""
    <h2 style='color: #4CAF50; 
               text-align: center; 
               padding: 0.5rem;'>
        Visualization skill workshop - Plotly
    </h2>
    """, unsafe_allow_html=True)

# ... existing input fields ...

# Update author information styling
if name and usn and instructor_name:
    st.markdown(
        f"""
        <div style='background-color: #262730; 
                    padding: 1.5rem; 
                    border-radius: 10px; 
                    margin: 1rem 0;
                    border: 1px solid #4CAF50;'>
            <h5 style='color: #4CAF50; margin-bottom: 0.8rem;'>Created by:</h5>
            <p style='color: #FAFAFA; margin: 0.3rem 0;'>{name} (USN: {usn})</p>
            <p style='color: #FAFAFA; margin: 0.3rem 0;'>Instructor: {instructor_name}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ... existing dataset loading ...

# Style the dataset overview
st.markdown("""
    <h2 style='color: #4CAF50; 
               margin-top: 2rem;'>
        Dataset Overview
    </h2>
    """, unsafe_allow_html=True)
st.write(tips.head())

# Update bar chart styling
st.markdown("""
    <h3 style='color: #4CAF50; 
               margin-top: 2rem;'>
        Task 2: Bar Chart - Average Tip by Day
    </h3>
    """, unsafe_allow_html=True)

# Enhanced bar chart
fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_dark'  # Changed to dark template
)

# Enhance the figure layout
fig2.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    title_font_color='#4CAF50',
    title_font_size=24,
    showlegend=True,
    legend=dict(
        bgcolor='rgba(0,0,0,0)',
        bordercolor='#4CAF50',
        borderwidth=1
    ),
    hoverlabel=dict(
        bgcolor="#262730",
        font_size=12,
        font_color="white"
    ),
    margin=dict(t=50, l=50, r=50, b=50)
)

# Update bar styling
fig2.update_traces(
    marker_line_color='#4CAF50',
    marker_line_width=1.5,
    opacity=0.8
)

# Display the chart
st.plotly_chart(fig2, use_container_width=True)

 
