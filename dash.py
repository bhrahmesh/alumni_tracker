import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("Aggregated_Alumni_Skills.csv")

# Clean company names
df['Company'] = df['Company'].str.strip()

# Streamlit App
st.title("Skill Analysis Dashboard")

# Dropdown to select a company
company_list = df['Company'].dropna().unique()
selected_company = st.selectbox("Select a company:", company_list)

# Display skills required for the selected company
if selected_company:
    skills_required = df[df['Company'] == selected_company]['Cleaned Skills'].values
    skill_frequency = df[df['Company'] == selected_company]['Skill Frequency'].values
    
    if len(skills_required) > 0:
        st.subheader("Skills Required:")
        st.write(skills_required[0])
        
        # Process skill frequency for plotting
        skill_counts = {}
        for skill in skill_frequency[0].split(", "):
            parts = skill.rsplit(" (", 1)
            if len(parts) == 2:
                skill_name, count = parts[0], parts[1].rstrip(")")
                skill_counts[skill_name] = int(count)
        
        # Plot skill distribution
        if skill_counts:
            st.subheader("Skill Distribution for Placed Students")
            fig, ax = plt.subplots()
            ax.bar(skill_counts.keys(), skill_counts.values(), color='skyblue')
            plt.xticks(rotation=45, ha='right')
            plt.ylabel("Number of Students")
            plt.xlabel("Skills")
            plt.title(f"Skill Distribution in {selected_company}")
            st.pyplot(fig)
