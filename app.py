import streamlit as st
import streamlit_pianoroll
from fortepyan import MidiPiece

piece = MidiPiece.from_file("haydn.mid")

st.write("## Display a PianoRoll player")
streamlit_pianoroll.from_fortepyan(piece)

st.write("## Conditional coloring")
st.write("Absolute pitch value condition")
df = piece.df.copy()

ids = df.pitch > 60

part_a = df[ids]
part_b = df[~ids]
piece_a = MidiPiece(df=part_a)
piece_b = MidiPiece(df=part_b)

streamlit_pianoroll.from_fortepyan(
    piece=piece_a,
    secondary_piece=piece_b,
)

st.write("Note duration condition")

df = piece.df.copy()

ids = df.duration > 0.23

part_a = df[ids]
part_b = df[~ids]
piece_a = MidiPiece(df=part_a)
piece_b = MidiPiece(df=part_b)

streamlit_pianoroll.from_fortepyan(
    piece=piece_a,
    secondary_piece=piece_b,
)
