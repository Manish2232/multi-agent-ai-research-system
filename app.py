"""
Multi-Agent AI Research System
================================
A professional, dark-themed Streamlit front end for the existing
`run_research_pipeline(topic: str) -> dict` backend defined in pipeline.py.

Run with:
    streamlit run app.py
"""

from __future__ import annotations

import datetime as dt
from typing import Any

import streamlit as st

from pipeline import run_research_pipeline


# ──────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Multi-Agent AI Research System",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ──────────────────────────────────────────────────────────────────────────
# STYLES
# ──────────────────────────────────────────────────────────────────────────
def inject_css() -> None:
    
    st.markdown(
        """
        <style>
        .devotional-corner {
    position: fixed;
    right: 18px;
    bottom: 18px;
    z-index: 99999;
    width: 300px;
    padding: 0.95rem 1rem;
    border-radius: 18px;
    background: linear-gradient(
        135deg,
        rgba(124, 58, 237, 0.28),
        rgba(34, 211, 238, 0.18),
        rgba(244, 114, 182, 0.18)
    );
    border: 1px solid rgba(255, 255, 255, 0.14);
    box-shadow: 0 12px 28px rgba(0, 0, 0, 0.35);
    backdrop-filter: blur(10px);
}

.devotional-corner .label {
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #f5d0fe;
    font-weight: 700;
    margin-bottom: 0.3rem;
}

.devotional-corner .name {
    font-size: 0.92rem;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.35;
}

.devotional-corner .sub {
    font-size: 0.8rem;
    color: #e0f2fe;
    line-height: 1.3;
    margin-top: 0.15rem;
}
        .stApp {
            background: linear-gradient(180deg, #0d1117 0%, #0a0e14 100%);
            color: #e6e6e6;
        }
        #MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; }

        .app-title {
            font-size: 2.1rem;
            font-weight: 700;
            background: linear-gradient(90deg, #8b5cf6, #22d3ee);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.15rem;
        }
        .app-subtitle {
            color: #9aa0ac;
            font-size: 0.98rem;
            margin-bottom: 1.5rem;
        }

        .card {
            background: #131820;
            border: 1px solid #232a35;
            border-radius: 14px;
            padding: 1.1rem 1.3rem;
            margin-bottom: 1rem;
        }

        .step-card {
            border-radius: 12px;
            border: 1px solid #232a35;
            background: #10141c;
            padding: 0.9rem 1rem;
            height: 100%;
        }
        .step-card.running { border-color: #22d3ee; background: #0d1a20; }
        .step-card.completed { border-color: #34d399; background: #0d1a15; }
        .step-card.failed { border-color: #f87171; background: #1a0d0d; }

        .step-name { font-weight: 600; font-size: 0.95rem; color: #f0f0f0; }
        .step-desc { font-size: 0.78rem; color: #8a909c; margin: 4px 0 8px 0; }
        .step-badge {
            display: inline-block;
            font-size: 0.72rem;
            font-weight: 600;
            padding: 2px 10px;
            border-radius: 999px;
        }
        .badge-idle { background: #232a35; color: #9aa0ac; }
        .badge-running { background: rgba(34,211,238,0.15); color: #22d3ee; }
        .badge-completed { background: rgba(52,211,153,0.15); color: #34d399; }
        .badge-failed { background: rgba(248,113,113,0.15); color: #f87171; }

        .result-card {
            background: #10141c;
            border: 1px solid #232a35;
            border-radius: 10px;
            padding: 0.85rem 1rem;
            margin-bottom: 0.6rem;
        }
        .result-title { color: #c4b5fd; font-weight: 600; font-size: 0.95rem; }
        .result-url { color: #22d3ee; font-size: 0.75rem; margin: 2px 0 6px 0; word-break: break-all; }
        .result-snippet { color: #b6bac2; font-size: 0.85rem; line-height: 1.5; }

        .scroll-box {
            max-height: 400px;
            overflow-y: auto;
            background: #10141c;
            border: 1px solid #232a35;
            border-radius: 10px;
            padding: 1rem 1.1rem;
            font-size: 0.85rem;
            line-height: 1.6;
            color: #c9cbd3;
            white-space: pre-wrap;
        }

        .history-item {
            background: #10141c;
            border: 1px solid #232a35;
            border-radius: 10px;
            padding: 0.5rem 0.7rem;
            font-size: 0.8rem;
            margin-bottom: 0.4rem;
            color: #cfd2d8;
        }

        div[data-testid="stButton"] > button[kind="primary"] {
            background: linear-gradient(90deg, #7c3aed, #22d3ee);
            border: none;
            color: #0a0e14;
            font-weight: 700;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    


# ──────────────────────────────────────────────────────────────────────────
# CONSTANTS
# ──────────────────────────────────────────────────────────────────────────
SUGGESTED_TOPICS = [
    "AI jobs in Bengaluru",
    "Latest LLM research",
    "India semiconductor mission",
    "Climate change in 2026",
    "Mistral AI updates",
]

PIPELINE_STEPS = [
    ("search", "Search Agent", "Finds relevant sources for the topic.", "search_result"),
    ("reader", "Reader Agent", "Scrapes and cleans page content.", "scraped_content"),
    ("writer", "Writer Chain", "Synthesizes findings into a report.", "report"),
    ("critic", "Critic Chain", "Reviews and scores the final report.", "feedback"),
]

MAX_HISTORY = 10


# ──────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ──────────────────────────────────────────────────────────────────────────
def init_state() -> None:
    defaults: dict[str, Any] = {
        "current_topic": "",
        "topic_input_value": "",
        "results": None,
        "history": [],
        "status": "idle",  # idle | running | completed | failed
        "step_statuses": {key: "idle" for key, *_ in PIPELINE_STEPS},
        "error_message": None,
        "rerun_requested_topic": None,
        "active_detail": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_state() -> None:
    st.session_state.current_topic = ""
    st.session_state.topic_input_value = ""
    st.session_state.results = None
    st.session_state.status = "idle"
    st.session_state.step_statuses = {key: "idle" for key, *_ in PIPELINE_STEPS}
    st.session_state.error_message = None
    st.session_state.active_detail = None


def add_to_history(topic: str) -> None:
    history = st.session_state.history
    history = [t for t in history if t.lower() != topic.lower()]
    history.insert(0, topic)
    st.session_state.history = history[:MAX_HISTORY]


# ──────────────────────────────────────────────────────────────────────────
# PIPELINE EXECUTION
# ──────────────────────────────────────────────────────────────────────────
def execute_pipeline(topic: str) -> None:
    """Calls the backend pipeline and updates session state accordingly."""
    st.session_state.status = "running"
    st.session_state.error_message = None
    st.session_state.active_detail = None
    st.session_state.step_statuses = {key: "running" for key, *_ in PIPELINE_STEPS}

    try:
        with st.spinner("Running multi-agent research pipeline… this may take a moment."):
            result = run_research_pipeline(topic)

        if not isinstance(result, dict):
            raise ValueError("Pipeline did not return a dictionary as expected.")

        # Mark each step completed/failed based on whether its key is present and non-empty.
        step_statuses = {}
        for key, _name, _desc, result_key in PIPELINE_STEPS:
            value = result.get(result_key)
            step_statuses[key] = "completed" if value not in (None, "", [], {}) else "failed"
        st.session_state.step_statuses = step_statuses

        st.session_state.results = result
        st.session_state.current_topic = topic
        st.session_state.status = "completed"
        add_to_history(topic)

    except Exception as exc:  # noqa: BLE001 — surface any backend failure cleanly
        st.session_state.status = "failed"
        st.session_state.step_statuses = {key: "failed" for key, *_ in PIPELINE_STEPS}
        st.session_state.error_message = str(exc)


# ──────────────────────────────────────────────────────────────────────────
# UI HELPERS
# ──────────────────────────────────────────────────────────────────────────
def render_header() -> None:
    st.markdown('<div class="app-title">Multi-Agent AI Research System</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="app-subtitle">Autonomous research powered by cooperating AI agents — '
        "search, scrape, write, and critique — turning any topic into a structured report.</div>",
        unsafe_allow_html=True,
    )


def render_sidebar() -> None:
    with st.sidebar:
        st.markdown("### 🧠 Multi-Agent AI Research System")
        st.caption(
            "A four-stage AI pipeline that searches the web, reads sources, "
            "writes a report, and critiques its own output."
        )
        st.markdown("---")

        st.markdown("**Backend status**")
        st.success("pipeline.py loaded")

        st.markdown("**Pipeline status**")
        status_labels = {
            "idle": ("⚪", "Idle"),
            "running": ("🔵", "Running"),
            "completed": ("🟢", "Completed"),
            "failed": ("🔴", "Failed"),
        }
        icon, label = status_labels.get(st.session_state.status, ("⚪", "Idle"))
        st.write(f"{icon} {label}")

        st.markdown("---")
        if st.button("🗑️ Clear / Reset", use_container_width=True):
            reset_state()
            st.rerun()

        st.markdown("---")
        st.markdown("**Recent topics**")
        if st.session_state.history:
            for topic in st.session_state.history:
                cols = st.columns([4, 1])
                cols[0].markdown(f'<div class="history-item">{topic}</div>', unsafe_allow_html=True)
                if cols[1].button("↻", key=f"sidebar_rerun_{topic}", help="Rerun this topic"):
                    st.session_state.rerun_requested_topic = topic
                    st.rerun()
        else:
            st.caption("No research run yet.")


def render_input_section() -> str | None:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("##### Start a New Research Task")

    col1, col2 = st.columns([4, 1.3])
    with col1:
        topic = st.text_input(
            "Research topic",
            value=st.session_state.topic_input_value,
            placeholder="e.g. AI jobs in Bengaluru",
            label_visibility="collapsed",
            key="topic_text_field",
        )
    with col2:
        start_clicked = st.button("Start Research", type="primary", use_container_width=True)

    st.caption("Or try a suggested topic:")
    chip_cols = st.columns(len(SUGGESTED_TOPICS))
    chip_selected = None
    for col, suggestion in zip(chip_cols, SUGGESTED_TOPICS):
        with col:
            if st.button(suggestion, key=f"chip_{suggestion}", use_container_width=True):
                chip_selected = suggestion

    st.markdown("</div>", unsafe_allow_html=True)

    if chip_selected:
        return chip_selected

    if start_clicked:
        if not topic or not topic.strip():
            st.warning("⚠️ Please enter a research topic before starting.")
            return None
        return topic.strip()

    return None


def render_pipeline_status() -> None:
    st.markdown("##### Pipeline Status")
    cols = st.columns(4)
    for col, (key, name, desc, _result_key) in zip(cols, PIPELINE_STEPS):
        status = st.session_state.step_statuses.get(key, "idle")
        with col:
            st.markdown(
                f"""
                <div class="step-card {status}">
                    <div class="step-name">{name}</div>
                    <div class="step-desc">{desc}</div>
                    <span class="step-badge badge-{status}">{status.capitalize()}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_search_results(search_result: Any) -> None:
    if isinstance(search_result, list) and search_result:
        for item in search_result:
            if isinstance(item, dict):
                title = item.get("title", "Untitled result")
                url = item.get("url", "")
                snippet = item.get("snippet") or item.get("content") or ""
                st.markdown(
                    f"""
                    <div class="result-card">
                        <div class="result-title">{title}</div>
                        <div class="result-url">{url}</div>
                        <div class="result-snippet">{snippet}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(f'<div class="result-card">{item}</div>', unsafe_allow_html=True)
    elif isinstance(search_result, str) and search_result.strip():
        st.markdown(f'<div class="scroll-box">{search_result}</div>', unsafe_allow_html=True)
    else:
        st.info("No search results were returned.")


def render_scraped_content(scraped_content: Any) -> None:
    if isinstance(scraped_content, str) and scraped_content.strip():
        st.markdown(f'<div class="scroll-box">{scraped_content}</div>', unsafe_allow_html=True)
    elif scraped_content:
        st.write(scraped_content)
    else:
        st.info("No scraped content was returned.")


def render_report(report: Any) -> None:
    if isinstance(report, str) and report.strip():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(report)
        st.markdown("</div>", unsafe_allow_html=True)
        st.download_button(
            "⬇️ Download Report",
            data=report,
            file_name=f"{st.session_state.current_topic.replace(' ', '_') or 'report'}.md",
            mime="text/markdown",
        )
    else:
        st.info("No report was generated.")


def render_feedback(feedback: Any) -> None:
    if isinstance(feedback, dict) and feedback:
        score = feedback.get("score", "N/A")
        strengths = feedback.get("strengths", [])
        improvements = feedback.get("improve") or feedback.get("weaknesses") or []
        verdict = feedback.get("verdict", "")

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(f"**Score:** {score}")
        if verdict:
            st.markdown(f"**Verdict:** {verdict}")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Strengths**")
            if strengths:
                for s in strengths:
                    st.markdown(f"- {s}")
            else:
                st.caption("None listed.")
        with col2:
            st.markdown("**Areas to Improve**")
            if improvements:
                for i in improvements:
                    st.markdown(f"- {i}")
            else:
                st.caption("None listed.")
        st.markdown("</div>", unsafe_allow_html=True)

    elif isinstance(feedback, str) and feedback.strip():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write(feedback)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("No critic feedback was returned.")


def render_results_section() -> None:
    results = st.session_state.results
    if not results:
        return

    detail_options = [
        ("search_result", "🔎 Search Results"),
        ("scraped_content", "📖 Scraped Content"),
        ("feedback", "🧪 Critic Feedback"),
    ]

    chip_cols = st.columns(len(detail_options))
    for col, (key, label) in zip(chip_cols, detail_options):
        with col:
            if st.button(label, key=f"detail_chip_{key}", use_container_width=True):
                # Toggle: clicking the active chip again closes it.
                st.session_state.active_detail = (
                    None if st.session_state.active_detail == key else key
                )

    st.markdown(f"##### Results for: *{st.session_state.current_topic}*")

    active = st.session_state.active_detail
    if active == "search_result":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        render_search_results(results.get("search_result"))
        st.markdown("</div>", unsafe_allow_html=True)
    elif active == "scraped_content":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        render_scraped_content(results.get("scraped_content"))
        st.markdown("</div>", unsafe_allow_html=True)
    elif active == "feedback":
        render_feedback(results.get("feedback"))

    render_report(results.get("report"))


# ──────────────────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────────────────
def main() -> None:
    init_state()
    inject_css()
    render_sidebar()
    render_header()

    # Handle a rerun request triggered from the history sidebar.
    if st.session_state.rerun_requested_topic:
        topic_to_run = st.session_state.rerun_requested_topic
        st.session_state.rerun_requested_topic = None
        execute_pipeline(topic_to_run)

    topic_to_run = render_input_section()
    if topic_to_run:
        execute_pipeline(topic_to_run)

    render_pipeline_status()

    if st.session_state.status == "failed" and st.session_state.error_message:
        st.error(f"Pipeline execution failed: {st.session_state.error_message}")
    elif st.session_state.status == "completed":
        st.success(f"Research completed at {dt.datetime.now().strftime('%H:%M:%S')}.")

    st.markdown("---")
    render_results_section()
    st.markdown(
    """
    <div class="devotional-corner">
        <div class="label">Kind Obeisances</div>
        <div class="name">To Srila Prabhupada Ji</div>
        <div class="sub">With humble respect and gratitude</div>
        <div class="name">To my Guru Maharaj</div>
        <div class="sub">H.H. Bhakti Pramod Bhagvat Swami Maharaj Ji</div>
    </div>
    """,
    unsafe_allow_html=True,
)


if __name__ == "__main__":
    main()