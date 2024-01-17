from spleeter.separator import Separator
from pydub import AudioSegment

def remove_vocals(input_audio, output_audio):
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(input_audio, output_audio)

def remove_instrumentals(input_audio, output_audio):
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(input_audio, output_audio)

def combine_audio(vocal_file, instrumental_file, output_file, bitrate='320k', sample_width=2):
    vocal = AudioSegment.from_file(vocal_file)
    instrumental = AudioSegment.from_file(instrumental_file)

    # Adjust the volume of vocal and instrumental tracks as needed
    combined = vocal.overlay(instrumental)

    # Export the combined audio with increased quality
    combined.export(output_file, format='mp3', bitrate=bitrate, parameters=["-ac", "2", "-ar", "44100"])


if __name__ == "__main__":
    song_a = "music/song_a.mp3"
    song_b = "music/song_b.mp3"
    vocal_output = "vocal"
    instrumental_output = "instrument"
    combined_output = "combine/combined_song.mp3"

    remove_vocals(song_a, vocal_output)
    remove_instrumentals(song_b, instrumental_output)

    combine_audio(vocal_output + "/song_a/vocals.wav",
              instrumental_output + "/song_b/accompaniment.wav",
              combined_output,
              bitrate='320k',  # Adjust the bitrate as needed
              sample_width=2)  # Adjust the sample width as needed
