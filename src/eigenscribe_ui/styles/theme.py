# src/eigenscribe_ui/styles/theme.py

import streamlit as st

from pathlib import Path

import os

import base64

__all__: list[str] = [
    "load_theme",
]

def load_theme():
    root_path = Path(os.getcwd())
    css_path = root_path / "assets" / "css" / "main.css"
    background_path = root_path / "assets" / "images" / "wisp.jpg"

    if css_path.exists():
        css_content = css_path.read_text()

        # If the image exists, encode it and inject it into the CSS.
        if background_path.exists():
            with open(background_path, "rb") as image_file:
                encode_string = base64.b64encode(image_file.read()).decode()

            # This replaces a placeholder in your CSS with the actual background image data.
            css_content = css_content.replace("REPLACE_WITH_WISP_BASE64", encode_string)

        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

    else:
        st.error(f"✖️ CSS file not found at {css_path}")
