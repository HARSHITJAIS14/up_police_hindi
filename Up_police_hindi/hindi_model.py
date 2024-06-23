import os
import wave
import json
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment

def convert_audio_to_wav(audio_path):
    audio = AudioSegment.from_file(audio_path)
    wav_path = audio_path.rsplit('.', 1)[0] + '.wav'
    audio = audio.set_channels(1).set_frame_rate(16000)
    audio.export(wav_path, format='wav')
    return wav_path

def transcribe_audio_chunk(model, audio_chunk):
    rec = KaldiRecognizer(model, audio_chunk.getframerate())
    results = []
    
    while True:
        data = audio_chunk.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results.append(json.loads(rec.Result()))
    
    results.append(json.loads(rec.FinalResult()))
    transcription = " ".join([result.get("text", "") for result in results])
    return transcription

def transcribe_audio(audio_path, output_path, chunk_length_ms=20000):
    model_path = "/home/harshit/Desktop/Pclub/Up_police_hindi/model/vosk-model-hi-0.22"  # Update this path with the correct model path
    model = Model(model_path)
    wav_path = convert_audio_to_wav(audio_path)

    audio = AudioSegment.from_wav(wav_path)
    
    full_transcription = ""
    
    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i + chunk_length_ms]
        chunk_path = f"chunk_{i}.wav"
        chunk.export(chunk_path, format="wav")
        
        with wave.open(chunk_path, "rb") as wf:
            transcription = transcribe_audio_chunk(model, wf)
            full_transcription += transcription + " "
        
        os.remove(chunk_path)  
    
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(full_transcription.strip())
    
    print("Transcription: ", full_transcription.strip())

if __name__ == "__main__":

    audio_path = "/home/harshit/Desktop/Pclub/Up_police_hindi/atal-bihari-vajpayee-greatest-speech-ever-in-indian-parliament-manastars-128-ytshorts.savetube.me.wav"  # wav would be better than mp3
 
    output_path = "vosk_atal.txt"  
    
    transcribe_audio(audio_path, output_path)
