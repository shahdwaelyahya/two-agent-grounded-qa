import streamlit as st

from app.workflow import run_qa_workflow


st.set_page_config(
    page_title="Rich Dad Poor Dad Q&A",
    page_icon="📚",
    layout="centered",
)


st.title("📚 Rich Dad Poor Dad")
st.subheader("Two-Agent Grounded Q&A Assistant")

st.write(
    "Ask a question about the book. "
    "The Researcher finds relevant passages, "
    "then the Reviewer checks the answer."
)


question = st.text_input(
    "Your question",
    placeholder="What is financial education?",
)


if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Researcher is searching and Reviewer is checking..."):
            result = run_qa_workflow(question)

        st.markdown("### Final Review")
        st.write(result["review"])

        st.markdown("### Sources")

        if result["sources"]:
            for page in result["sources"]:
                st.write(f"📖 Page {page}")
        else:
            st.write("No page sources found.")
