from pydub import AudioSegment
import simpleaudio as sa

# Memuat file audio
audio = AudioSegment.from_file('mysong.mp3')

clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('clipped_chapter2_result.mp3', format='mp3')

combined_audio = audio + clipped_audio
combined_audio.export('combined_chapter2_result.mp3', format='mp3')

louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('louder_chapter2_result.mp3', format='mp3')

# Mengonversi ke WAV (opsional, jika formatnya bukan WAV)
audio.export('resultChapter2audio.wav', format='wav')

# Memutar audio
wave_obj = sa.WaveObject.from_wave_file('resultChapter2audio.wav')
play_obj = wave_obj.play()

# Menunggu sampai audio selesai diputar
play_obj.wait_done()