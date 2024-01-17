import streamlit as st
from spleeter.separator import Separator
from pydub import AudioSegment, effects
import time


def remove_vocals(input_audio, output_audio, output_format='mp3'):
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(input_audio, output_audio, codec=output_format)

def remove_instrumentals(input_audio, output_audio, output_format='mp3'):
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(input_audio, output_audio, codec=output_format)

def combine_audio(vocal_file, instrumental_file, output_file, bitrate='320k'):
    vocal = AudioSegment.from_file(vocal_file)
    instrumental = AudioSegment.from_file(instrumental_file)

    # Adjust the volume of vocal and instrumental tracks as needed
    combined = vocal.overlay(instrumental)

    # Apply a simple low-pass filter for noise reduction
    combined = combined.low_pass_filter(1000)

    # Export the combined audio with increased quality and as MP3
    combined.export(output_file, format='mp3', bitrate=bitrate)

def loading_animation():
    st.text("Hold a Minitue ! Your Music is Generating......")
    progress_bar = st.progress(0)

    for i in range(51):
        time.sleep(0.1)
        progress_bar.progress(i * 2)

def main():
    st.title("Arthur Ai Music Mashup Generator")

    uploaded_song_a = st.file_uploader("Upload Song A (with vocals)", type=["mp3", "wav"])
    uploaded_song_b = st.file_uploader("Upload Song B (instrumental)", type=["mp3", "wav"])

    if uploaded_song_a and uploaded_song_b:
        loading_animation()

        vocal_output = "vocal"
        instrumental_output = "instrument"
        combined_output = "combine/combined_song.mp3"

        # Save uploaded files
        with open("music/song_a.mp3", "wb") as f:
            f.write(uploaded_song_a.read())

        with open("music/song_b.mp3", "wb") as f:
            f.write(uploaded_song_b.read())

        # Remove vocals and instrumentals in MP3 format
        remove_vocals("music/song_a.mp3", vocal_output, output_format='mp3')
        remove_instrumentals("music/song_b.mp3", instrumental_output, output_format='mp3')

        # Combine the vocal and instrumental tracks and apply a simple low-pass filter for noise reduction
        combine_audio(vocal_output + "/song_a/vocals.mp3",
                      instrumental_output + "/song_b/accompaniment.mp3",
                      combined_output,
                      bitrate='320k')

        st.subheader("Result:")
        st.audio(combined_output, format="audio/mp3")

if __name__ == "__main__":
    main()
