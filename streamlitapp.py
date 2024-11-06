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
 
