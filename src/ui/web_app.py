import streamlit as st
from ai_matte import MathTutor
import random

class WebApp:
    def __init__(self, engine: str = "local"):
        self.engine = engine

    def run(self):
        st.set_page_config(page_title="AI-Matteforklarer", page_icon="🧮")
        st.title("🧮 AI-Matteforklarer")

        problem = st.text_area("Skriv inn en oppgave:", "3x + 5 = 11")
        if st.button("Forklar"):
            tutor = MathTutor(engine=self.engine)

            with st.spinner(random.choice([
                "🧮 Mattelæreren tenker …",
                "📚 La meg finne stegene …",
                "✏️ Regner ut løsningen for deg …"
            ])):
                result = tutor.explain(problem)

            st.success("✅ Forklaring klar!")
            st.text(result)

