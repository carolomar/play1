# Import necessary libraries
import streamlit as st
import openai  # For interacting with the OpenAI API

# Initialize the app
def main():
    st.title("Content Creator Workflow Suite")
    st.sidebar.title("Features Menu")

    # API Key Input
    api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")
    if not api_key:
        st.warning("Please enter your OpenAI API key to use the app.")
        st.stop()
    else:
        openai.api_key = api_key

    # Sidebar menu
    menu = st.sidebar.selectbox(
        "Select a Feature",
        ["Idea Generator", "Script Builder", "Content Calendar Planner", "Repurposing Assistant", "Engagement Tracker"]
    )

    # Feature functionality
    if menu == "Idea Generator":
        idea_generator()
    elif menu == "Script Builder":
        script_builder()
    elif menu == "Content Calendar Planner":
        content_calendar_planner()
    elif menu == "Repurposing Assistant":
        repurposing_assistant()
    elif menu == "Engagement Tracker":
        engagement_tracker()

# Feature 1: Idea Generator
def idea_generator():
    st.header("Idea Generator")
    topic = st.text_input("Enter your topic or theme:")
    audience = st.text_input("Who is your target audience?")
    if st.button("Generate Ideas"):
        if topic:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an idea generator for content creators."},
                    {"role": "user", "content": f"Generate 5 unique video ideas for the topic '{topic}' targeting '{audience}'."}
                ]
            )
            st.write(response.choices[0].message.content)
        else:
            st.warning("Please enter a topic to generate ideas.")

# Feature 2: Script Builder
def script_builder():
    st.header("Script Builder")
    video_title = st.text_input("Enter your video title or idea:")
    tone = st.selectbox("Select the tone of the script:", ["Friendly", "Professional", "Humorous"])
    style = st.text_input("Describe your writing style (optional):")
    if st.button("Generate Script"):
        if video_title:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a script generator for videos."},
                    {"role": "user", "content": f"Generate a step-by-step script for a video titled '{video_title}' in a {tone} tone. Writing style: {style if style else 'General'}"}
                ]
            )
            st.write(response.choices[0].message.content)
        else:
            st.warning("Please enter a video title to generate a script.")

# Feature 3: Content Calendar Planner
def content_calendar_planner():
    st.header("Content Calendar Planner")
    num_videos = st.number_input("How many videos do you want to plan?", min_value=1, max_value=50, step=1)
    topics = st.text_area("Enter your video topics or themes (one per line):")
    if st.button("Generate Calendar"):
        if topics:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a content calendar planner for YouTube creators."},
                    {"role": "user", "content": f"Plan a content calendar for {num_videos} videos using the following topics: {topics}."}
                ]
            )
            st.write(response.choices[0].message.content)
        else:
            st.warning("Please enter topics to generate a calendar.")

# Feature 4: Repurposing Assistant
def repurposing_assistant():
    st.header("Repurposing Assistant")
    content = st.text_area("Paste your long-form content (e.g., blog or video script):")
    format = st.selectbox("Select the format to repurpose into:", ["Instagram Post", "LinkedIn Article", "YouTube Short"])
    if st.button("Repurpose Content"):
        if content:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a repurposing assistant for content creators."},
                    {"role": "user", "content": f"Repurpose the following content into a {format}: {content}"}
                ]
            )
            st.write(response.choices[0].message.content)
        else:
            st.warning("Please paste content to repurpose.")

# Feature 5: Engagement Tracker
def engagement_tracker():
    st.header("Engagement Tracker")
    st.write("Coming Soon! Track metrics like views, likes, comments, and more.")

# Run the app
if __name__ == "__main__":
    main()
