import boto3 
import time
transcribe = boto3.client('transcribe', region_name='us-east-1')

transcription_job_name = "MyTranscriptionJob20"
media_file_uri = "s3://u13-s3-vijay-058264295817-us-east-1-an/audio/audio.mp3"

print("Transcription job started. Job name:", transcription_job_name)
response = transcribe.start_transcription_job(
    TranscriptionJobName=transcription_job_name,
    Media={'MediaFileUri': media_file_uri},
    MediaFormat='mp3',
    LanguageCode='en-US'
)
print("Transcription job response:", response)

# fetch the transcription result
while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=transcription_job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Transcription job in progress...")
    time.sleep(5)

if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
    transcript_file_uri = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
    print("Transcription completed. Transcript file URI:", transcript_file_uri)

# read the transcript from the S3 URI
import requests 

response = requests.get(transcript_file_uri)
print("Transcript content:", response.text)