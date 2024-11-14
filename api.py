import os
import requests
import base64

from prompt import lireSon, prompt_user




def transcribe_audio(audio_file_path):
    url = "https://api.runpod.ai/v2/faster-whisper/runsync"

    try:
        with open(audio_file_path, "rb") as file:
            audio_base64 = base64.b64encode(file.read()).decode("utf-8")
    except FileNotFoundError as e:
        print(f"Error: File not found at path {audio_file_path}. {e}")
        return None

    payload = {
        "input": {
            "audio_base64": audio_base64,
            "model": "base",
            "transcription": "plain_text",
            "translate": False,
            "language": "fr",
            "temperature": 0.2,
            "best_of": 5,
            "beam_size": 5,
            "patience": 1,
            "suppress_tokens": "-1",
            "condition_on_previous_text": True,
            "temperature_increment_on_fallback": 0.2,
            "compression_ratio_threshold": 2.4,
            "logprob_threshold": -1,
            "no_speech_threshold": 0.6,
            "word_timestamps": False,
            
        },
        "enable_vad": False
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "JDE7KIT7HBADIQZ32571BRKLO9RVVDIL5DILXHG1"
    }

    response = requests.post(url, json=payload, headers=headers)

    print("Response Status Code:", response.status_code)

    if response.status_code == 200:
        response_json = response.json()
        transcription_result = response_json.get("output", {}).get("transcription", "")

        return transcription_result
    else:
        print("Transcription Failed. Check the response for details.")
        print("Reponse Text:", response.text)
        return None





if __name__ == "__main__":
    # lireSon()
    audio_file_path = os.path.abspath("menu.wav")
    transcription_result = transcribe_audio(audio_file_path)
    print("utilisateur a dir : {} \n".format(transcribe_audio))
    print('Prompt' +prompt_user(transcription_result))
    
    
