import streamlit as st
import streamlit_pianoroll
from datasets import load_dataset
from fortepyan import MidiPiece

dataset = load_dataset("epr-labs/maestro-sustain-v2", split="train")
idx = st.number_input(
    label="Piece IDX",
    min_value=0,
    max_value=len(dataset) - 1,
    value=420,
)
piece = MidiPiece.from_huggingface(dataset[idx])

streamlit_pianoroll.from_fortepyan(piece[:500])