import streamlit as st
from ai_matte import MathTutor
import random

class WebApp:
    def __init__(self, engine: str = "local"):
        self.engine = engine

    def run(self):
        st.set_page_config(page_title="AI-Matteforklarer", page_icon="🧮")
        st.title("🧮 AI-Matteforklarer")

        problem = st.text_area("Skriv inn en oppgave:", "3x + 5 = 11", height=120)

        if "loading" not in st.session_state: st.session_state.loading = False
        if "result"  not in st.session_state: st.session_state.result  = ""

        btn_ph   = st.empty()
        status_ph= st.empty()
        out_ph   = st.empty()

        tutor = MathTutor(engine=self.engine)

        if st.session_state.loading:
            btn_ph.button("⏳ Forklarer...", disabled=True)
            with st.spinner(random.choice([
                "🧮 Mattelæreren tenker …",
                "📚 La meg finne stegene …",
                "✏️ Regner ut løsningen for deg …"
            ])):
                st.session_state.result = tutor.explain(problem)
            status_ph.success("✅ Forklaring klar!")
            out_ph.text(st.session_state.result)
            st.session_state.loading = False
            btn_ph.button("📄 Forklar oppgaven")
        else:
            if btn_ph.button("📄 Forklar oppgaven"):
                st.session_state.loading = True
                st.rerun()

