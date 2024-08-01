import requests
import torch
from transformers import pipeline
import gradio as gr


'''USE THE FOLLOWING PART OF CODE TO DOWNLOAD A SAMPLE AUDIO FILE'''
# # url of the audio file to be downloaded
# url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX04C6EN/Testing%20speech%20to%20text.mp3"

# # download the file
# response = requests.get(url)

# # define the local file path where the audio file will be saved
# audio_file = "downloaded_audio.mp3"

# # check if the request was successful (status code 200)
# if response.status_code == 200:
#     # if successful, write the content to a file
#     with open(audio_file, "wb") as file:
#         file.write(response.content)
#     print("File downloaded successfully")
# else:
#     # if the request failed, print an error
#     print("Failed to download file")


'''USE THE FOLLOWING PART OF CODE TO TEST THE PIPELINE'''
# initialize the speech-to-text pipeline from HuggingFace Transformers

# This uses the "openai/whisper-tiny.en" model for automatic speech recognition (ASR)
# The `chunk_length_s` parameter specifies the chunk length in seconds for processing

# pipe = pipeline(
#     "automatic-speech-recognition",
#     model="openai/whisper-tiny.en",
#     chunk_length_s=30,
# )

# # define the path to the audio file that needs to be transcribed
# sample = "downloaded_audio.mp3"

# # perform speech recognition on the audio file
# # the 'batch_size=8' parameter indicates how many chunks are processed at a time
# # the result is stored in 'prediction' with the "text" containing the transcribed text
# prediction = pipe(sample, batch_size=8)['text']

# # print the transcribed text to the console 
# print(prediction)

'''MAIN CODE'''

# function to transcribe audio 
def transcribe_audio(audio_file):
    # initialize pipeline
    pipe = pipeline(
        'automatic-speech-recognition',
        model='openai/whisper-tiny.en',
        chunk_length_s=30,
    )
    result = pipe(audio_file, batch_size=8)['text']
    return result

# set up gradio interface
# audio input
audio_input = gr.Audio(sources='upload', type='filepath')

# text output
output_text = gr.Textbox()

# create the gradio interface with the function
iface = gr.Interface(
    fn=transcribe_audio,
    inputs=audio_input,
    outputs=output_text,
    title='Audio Transcription App',
    description='Upload the audio file'
)

# launch gradio app
iface.launch(server_name='0.0.0.0', server_port=5000)