#!/usr/bin/env python3
"""Interface Web Streamlit pour lancer la veille."""

import streamlit as st
import subprocess

st.title("Assistant Cyber")

if st.button("Lancer la veille"):
    st.write("Execution en cours...")
    result = subprocess.run(["python3", "main.py"], capture_output=True, text=True)
    st.text(result.stdout)
    if result.stderr:
        st.text(result.stderr)
