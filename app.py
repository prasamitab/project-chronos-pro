# app.py
import streamlit as st
from main import generate_report

st.set_page_config(page_title="Project Chronos", page_icon="🏛️")

st.title("🏛️ Project Chronos: The AI Archeologist")
st.write("Enter a piece of fragmented text from the early internet. Our AI will excavate its meaning, estimate its time period, and find visual context.")

fragment = st.text_input("Enter Fragmented Text:", placeholder="e.g., w00t! that n00b got pwned on Counter-Strike.")

if st.button("Excavate ⛏️"):
    if fragment:
        with st.spinner("Analyzing digital artifacts... This may take a moment."):
            report = generate_report(fragment)
        
        st.divider()
        st.header("Archeological Findings")

        if "error" in report:
            st.error(f"An error occurred during excavation: {report['error']}")
        else:
            st.subheader("Original Fragment")
            st.markdown(f"> {report['original']}")

            st.subheader("AI-Reconstructed Text")
            st.success(f"**{report['reconstructed']}**")

            st.info(f"**Estimated Time Period:** {report.get('period', 'N/A')}")
            st.info(f"**Slang Category:** {report.get('category', 'N/A')}")
            
            st.subheader("Visual Context")
            if report.get('image'):
                st.image(report['image'], caption="AI-found Visual Context", use_column_width=True)
            else:
                st.write("No direct visual context found.")

            st.subheader("Contextual Sources")
            if report['links']:
                for link in report['links']:
                    st.markdown(f"* [{link}]({link})")
            else:
                st.write("No relevant text sources found.")
    else:
        st.warning("Please enter some text to analyze.")
