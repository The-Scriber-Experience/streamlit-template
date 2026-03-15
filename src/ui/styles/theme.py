# src/ui/styles/theme.py

import streamlit as st
from pathlib import Path
import base64

# --------------------------------------------------
# Project root detection
# --------------------------------------------------

ROOT = Path(__file__).resolve().parents[4]
ASSETS = ROOT / "assets"
IMAGES = ASSETS / "images"

CSS_PATH = ASSETS / "css" / "main.css"
BACKGROUND_PATH = IMAGES / "wisp.jpg"

# --------------------------------------------------
# Utilities
# --------------------------------------------------
@st.cache_data
def encode_image(path: Path) -> str:
    """Encode image to base64 for CSS embedding."""
    return base64.b64encode(path.read_bytes()).decode()

@st.cache_data
def load_css() -> str:
    """Load CSS file content."""
    return CSS_PATH.read_text()

# --------------------------------------------------
# Public API
# --------------------------------------------------
def load_theme():
    """Load custom Streamlit theme."""

    if not CSS_PATH.exists():
        st.error(f"✖️ CSS not found at {CSS_PATH}")
        return

    css_content = load_css()

    st.markdown(
        f"<style>{css_content}<style>",
        unsafe_allow_html=True,
    )