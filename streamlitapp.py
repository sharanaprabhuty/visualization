# --- Title and Introduction ---
st.title("📊 Interactive Visualizations with Plotly and Streamlit")

# --- Input for Author Information ---
st.sidebar.header("🧑‍🏫 Visualization Skill Workshop - Plotly")
name = st.sidebar.text_input("Enter your name:")
usn = st.sidebar.text_input("Enter your roll no:")
instructor_name = st.sidebar.text_input("Course Instructor Name:")

# Display author information if provided with dark theme styling
if name and usn and instructor_name:
    st.markdown(
        f"<h5 style='color: #1ABC9C;'>Created by:</h5>"
        f"<p style='color: #ECF0F1;'>{name} (USN: {usn})</p>"
        f"<p style='color: #ECF0F1;'>Instructor: {instructor_name}</p>",
        unsafe_allow_html=True
    )

# --- Load Dataset ---
tips = sns.load_dataset('tips')  # Loading the tips dataset

# Display the first few rows of the dataset with customized color styling
st.write("## 🗂 Dataset Overview")
st.write(tips.head())

# --- Task 2: Interactive Bar Chart ---
st.subheader("📅 Task 2: Bar Chart - Average Tip by Day")

# Dark-themed Bar Chart with animation for better visualization
fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_dark',  # Set to dark template for professional look
    animation_frame='day',  # Adds a slight movement effect
)

# Customize font and title size for readability
fig2.update_layout(
    title_font_size=20,
    font_color="#ECF0F1",
    title_font_color="#1ABC9C",
    hoverlabel=dict(bgcolor="black", font_size=12, font_color="white"),
)

# Display the chart with animation in Streamlit
st.plotly_chart(fig2)

 
