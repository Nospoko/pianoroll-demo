import streamlit as st
import streamlit_pianoroll
from fortepyan import MidiPiece

piece = MidiPiece.from_file("haydn.mid")

st.write("## Display a PianoRoll player")

code = """
import streamlit_pianoroll
from fortepyan import MidiPiece

piece = MidiPiece.from_file("haydn.mid")
streamlit_pianoroll.from_fortepyan(piece)
"""
st.code(code, language="python")
streamlit_pianoroll.from_fortepyan(piece)

st.write("## Conditional coloring")
st.write("#### Absolute pitch value condition")

code = """
df = piece.df
ids = df.pitch > pitch_threshold

part_a = df[ids]
part_b = df[~ids]
piece_a = MidiPiece(df=part_a)
piece_b = MidiPiece(df=part_b)

streamlit_pianoroll.from_fortepyan(
    piece=piece_a,
    secondary_piece=piece_b,
)
"""
st.code(code, language="python")

df = piece.df.copy()

pitch_threshold = st.number_input(
    label="pitch_threshold",
    min_value=df.pitch.min(),
    max_value=df.pitch.max(),
    value=60,
)
ids = df.pitch > pitch_threshold

part_a = df[ids]
part_b = df[~ids]
piece_a = MidiPiece(df=part_a)
piece_b = MidiPiece(df=part_b)

streamlit_pianoroll.from_fortepyan(
    piece=piece_a,
    secondary_piece=piece_b,
)

st.write("#### Note duration condition")

code = """
df = piece.df

ids = df.duration > duration_threshold

part_a = df[ids]
part_b = df[~ids]
piece_a = MidiPiece(df=part_a)
piece_b = MidiPiece(df=part_b)

streamlit_pianoroll.from_fortepyan(
    piece=piece_a,
    secondary_piece=piece_b,
)
"""
st.code(code, language="python")

df = piece.df.copy()

duration_threshold = st.number_input(
    label="duration threshold",
    min_value=0.05,
    max_value=5.,
    value=0.25,
)

ids = df.duration > duration_threshold

part_a = df[ids]
part_b = df[~ids]
piece_a = MidiPiece(df=part_a)
piece_b = MidiPiece(df=part_b)

streamlit_pianoroll.from_fortepyan(
    piece=piece_a,
    secondary_piece=piece_b,
)
