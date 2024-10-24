import streamlit as st
import streamlit_pianoroll
from datasets import load_dataset
from fortepyan import MidiPiece

dataset = load_dataset("epr-labs/maestro-sustain-v2", split="train")
piece = MidiPiece.from_huggingface(dataset[312])

streamlit_pianoroll.from_fortepyan(piece[:5000])