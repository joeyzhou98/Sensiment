import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
def speechToText(content):
    # # Instantiates a client
    client = speech.SpeechClient()

    # # The name of the audio file to transcribe
    # audio = speech.types.RecognitionAudio(uri = uri)
    
    # config = speech.types.RecognitionConfig(
    #         encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
    #         language_code='en-US',
    #         sample_rate_hertz=44100)

    # # Detects speech in the audio file
    # response = client.recognize(config, audio)
    # # print(response)
    # return response
    # return response.results.alternatives[0].transcript

    audio = speech.types.RecognitionAudio(content=content)
    print(content)
    config = speech.types.RecognitionConfig(
        encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US')
    response = client.recognize(config, audio)
    return response

if __name__ == "__main__":
    speechToText()