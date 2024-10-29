import numpy as np
import streamlit as st
import streamlit_pianoroll
from fortepyan import MidiPiece

st.set_page_config(
    page_title="PianoRoll Demo",
    page_icon=":musical_keyboard:",
)


def main():
    piano_music_demo()


def piano_music_demo():
    piece = MidiPiece.from_file("haydn.mid")
    # TODO Improve fortepyan to make this cleaner
    piece.time_shift(-piece.df.start.min())

    st.write("## Display a PianoRoll player")
    st.write("""
    The core functionality of pianorolls includes music playback and visualization.
    If you have a MIDI file with piano music, see here for instructions on interacting with it using Streamlit components.
    """)

    code = """
    import streamlit_pianoroll
    from fortepyan import MidiPiece

    piece = MidiPiece.from_file("haydn.mid")
    streamlit_pianoroll.from_fortepyan(piece)
    """
    st.code(code, language="python")
    streamlit_pianoroll.from_fortepyan(piece)
    st.info(
        body="This component is dedicated to piano music, there's no way to interract with multiple instruments.",
        icon="🎹",
    )

    st.write("## Conditional coloring")
    st.write("""
    To create a pianoroll with different notes in separate colors,
    create two `MidiPiece` objects, each containing the notes for one color.
    """)
    st.write("#### Absolute pitch value condition")
    st.write("""
    Here's how to highlight notes with pitch above or below a certain threshold.
    Value of pitch 60 corresponds to the middle C (C4) on a piano keyboard
    ([refrence table](https://inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies)).
    """)

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

    part_a = df[ids].copy()
    part_b = df[~ids].copy()
    piece_a = MidiPiece(df=part_a)
    piece_b = MidiPiece(df=part_b)

    streamlit_pianoroll.from_fortepyan(
        piece=piece_a,
        secondary_piece=piece_b,
    )

    st.write("#### Note duration condition")
    st.write("""
    Here's how to highlight notes based on their absolute duration, which can differentiate between fast and slow notes.
    """)

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
        label="duration threshold [s]",
        min_value=0.05,
        max_value=5.,
        value=0.25,
    )

    ids = df.duration > duration_threshold

    part_a = df[ids].copy()
    part_b = df[~ids].copy()
    piece_a = MidiPiece(df=part_a)
    piece_b = MidiPiece(df=part_b)

    streamlit_pianoroll.from_fortepyan(
        piece=piece_a,
        secondary_piece=piece_b,
    )

    st.write("#### Music generation")
    st.write("""
    Here's how to show the results of a generative algorithm designed to respond to a musical input prompt.
    We can use notes with pitches below 72 (C5) as the prompt and display them alongside the generated output.
    This example performs a random shuffle of note pitch values, so the results are not musically appealing
    (your algorithms should produce better results).
    """)

    code = """
    df = piece.df.copy()

    ids = df.pitch < 72

    prompt_df = df[ids].copy()
    prompt_piece = MidiPiece(df=part_a)

    # Use your implementation here
    generated_df = music_generation_algorithm(prompt_df)

    generated_piece = MidiPiece(df=generated_df)

    streamlit_pianoroll.from_fortepyan(
        piece=prompt_piece,
        secondary_piece=generated_piece,
    )
    """
    st.code(code, language="python")

    df = piece.df.copy()

    ids = df.pitch < 72

    part_a = df[ids].copy()
    piece_a = MidiPiece(df=part_a)

    # Fake random algorithm
    part_b = df[~ids].copy()
    part_b.pitch = np.random.permutation(part_b.pitch)
    part_b.velocity = np.random.permutation(part_b.velocity)
    piece_b = MidiPiece(df=part_b)

    streamlit_pianoroll.from_fortepyan(
        piece=piece_a,
        secondary_piece=piece_b,
    )


if __name__ == "__main__":
    main()
