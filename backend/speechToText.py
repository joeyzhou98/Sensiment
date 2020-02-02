import io
import os
from google.cloud import speech

def speechToText(content):
    client = speech.SpeechClient()
    audio = {"content": content}
    # config = speech.types.RecognitionConfig(
    #     encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
    #     sample_rate_hertz=8000,
    #     language_code='en-US')
    config = {
        "encoding": speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
        "sample_rate_hertz": 8000,
        "language_code": 'en-US'
    }
    response = client.recognize(config, audio)
    return response
    # res = ""
    # for result in response.results:
    #     # First alternative is the most probable result
    #     res += result.alternatives[0].transcript
    return res