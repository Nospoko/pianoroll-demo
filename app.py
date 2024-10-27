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

    part_a = df[ids].copy()
    part_b = df[~ids].copy()
    piece_a = MidiPiece(df=part_a)
    piece_b = MidiPiece(df=part_b)

    streamlit_pianoroll.from_fortepyan(
        piece=piece_a,
        secondary_piece=piece_b,
    )


if __name__ == "__main__":
    main()
