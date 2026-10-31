from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
import os

import streamlit as st
from dotenv import load_dotenv
from streamlit.errors import StreamlitSecretNotFoundError

load_dotenv()


def _get_setting(name: str, default: str = "") -> str:
    value = os.getenv(name)
    if value:
        return value.strip()

    try:
        value = st.secrets.get(name)
    except (KeyError, StreamlitSecretNotFoundError):
        value = None

    return str(value).strip() if value else default


@dataclass(frozen=True)
class Settings:
    gemini_api_key: str
    gemini_model: str

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings(
        gemini_api_key=_get_setting("GEMINI_API_KEY"),
        gemini_model=_get_setting("GEMINI_MODEL", "models/gemini-3.5-flash"),
    )
