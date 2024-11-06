# ... existing imports ...
import plotly.io as pio

# Set default plotly theme to dark
pio.templates.default = "plotly_dark"

# Configure Streamlit page
st.set_page_config(
    page_title="Interactive Visualizations",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS for dark theme
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .sidebar .sidebar-content {
        background-color: #262730;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Title and Introduction with animation ---
st.markdown("""
    <h1 style='text-align: center; color: #00CED1; 
    animation: fadeIn 2s;'>
    Interactive Visualizations with Plotly and Streamlit
    </h1>
    """, unsafe_allow_html=True)

# ... existing sidebar code ...

# Update the bar chart with enhanced styling
fig2 = px.bar(
    tips, 
    x='day', 
    y='tip', 
    color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_dark',
    animation_frame=None,  # Remove if you don't want animation
    hover_data=['total_bill'],  # Add extra info on hover
)

# Enhance the figure layout
fig2.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    showlegend=True,
    hovermode='x unified',
    hoverlabel=dict(bgcolor="white", font_size=12),
    transition_duration=500
)

# Add interactivity
fig2.update_traces(
    marker_line_color='rgb(8,48,107)',
    marker_line_width=1.5,
    opacity=0.8
)

# Display the chart with animation in Streamlit
st.plotly_chart(fig2)

 
