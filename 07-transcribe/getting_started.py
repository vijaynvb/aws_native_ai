# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Purpose

Shows how to use AWS SDK for Python (Boto3) to call Amazon Transcribe to make a
transcription of an audio file.

This script is intended to be used with the instructions for getting started in the
Amazon Transcribe Developer Guide here:
    https://docs.aws.amazon.com/transcribe/latest/dg/getting-started.html.
"""

# snippet-start:[transcribe.python.start-transcription-job]
import time
import boto3


def transcribe_file(job_name, file_uri, transcribe_client):
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={"MediaFileUri": file_uri},
        MediaFormat="mp3",
        LanguageCode="en-US",
    )

    max_tries = 60
    while max_tries > 0:
        max_tries -= 1
        job = transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
        job_status = job["TranscriptionJob"]["TranscriptionJobStatus"]
        if job_status in ["COMPLETED", "FAILED"]:
            print(f"Job {job_name} is {job_status}.")
            if job_status == "COMPLETED":
                print(
                    f"Download the transcript from\n"
                    f"\t{job['TranscriptionJob']['Transcript']['TranscriptFileUri']}."
                )
            break
        else:
            print(f"Waiting for {job_name}. Current status is {job_status}.")
        time.sleep(10)


def main():
    """
    Uploads the bundled sample audio file to a new S3 bucket, then runs a
    transcription job against it. Creates and deletes its own bucket so it
    works without any pre-existing AWS resources.
    """
    transcribe_client = boto3.client("transcribe")
    s3_resource = boto3.resource("s3")

    bucket_name = f"transcribe-getting-started-{time.time_ns()}"
    media_file_name = ".media/Jabberwocky.mp3"
    media_object_key = "Jabberwocky.mp3"

    print(f"Creating bucket {bucket_name}.")
    region_name = transcribe_client.meta.region_name
    create_bucket_args = {"Bucket": bucket_name}
    if region_name != "us-east-1":
        create_bucket_args["CreateBucketConfiguration"] = {
            "LocationConstraint": region_name
        }
    bucket = s3_resource.create_bucket(**create_bucket_args)
    print(f"Uploading {media_file_name}.")
    bucket.upload_file(media_file_name, media_object_key)
    file_uri = f"s3://{bucket_name}/{media_object_key}"

    try:
        transcribe_file(f"Example-job-{time.time_ns()}", file_uri, transcribe_client)
    finally:
        print(f"Deleting bucket {bucket_name}.")
        bucket.objects.delete()
        bucket.delete()


if __name__ == "__main__":
    main()
# snippet-end:[transcribe.python.start-transcription-job]
