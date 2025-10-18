# app.py
import streamlit as st
from main import generate_report

st.set_page_config(page_title="Project Chronos", page_icon="🏛️")
st.title("🏛️ Project Chronos: The AI Archeologist")
st.write("Enter a piece of fragmented or obscure text from old internet sources. The AI will reconstruct it, estimate its time period, and find visual and text-based context.")

fragment = st.text_input("Enter Fragmented Text:", placeholder="e.g., smh at the top 8 drama. g2g, ttyl.")

if st.button("Reconstruct"):
    if fragment:
        with st.spinner("Excavating digital history... This may take a moment."):
            report = generate_report(fragment)
        
        st.divider()
        st.header("Archeological Findings")

        if "error" in report:
            st.error(f"An error occurred: {report['error']}")
        else:
            st.subheader("Original Fragment")
            st.markdown(f"> {report['original']}")

            st.subheader("AI-Reconstructed Text")
            st.success(f"**{report['reconstructed']}**")

            st.info(f"**Estimated Time Period:** {report.get('period', 'N/A')}")
            
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
        st.warning("Please enter some text to reconstruct.")