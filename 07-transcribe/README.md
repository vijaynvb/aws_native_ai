# Amazon Transcribe examples

## What these examples do

Two runnable scripts, both self-contained — each creates its own temporary
S3 bucket, uploads the bundled sample audio file (`.media/Jabberwocky.mp3`,
a reading of the Lewis Carroll poem), runs one or more transcription jobs,
prints the results, and deletes the bucket afterward.

- **`getting_started.py`** — the simplest path: uploads the audio, starts
  one transcription job, waits for it to complete, and prints the transcript
  URI. Takes about 1-2 minutes.

- **`transcribe_basics.py`** — a fuller scenario: runs a plain transcription
  job, then creates a custom vocabulary (a phrase list of the poem's
  invented words like "brillig" and "slithy"), re-runs the job with that
  vocabulary, refines the vocabulary with pronunciation hints, and runs it
  a third time — showing how a custom vocabulary improves accuracy on
  unusual words. Takes about 3-6 minutes.

## Prerequisites

1. **Configure AWS credentials**, if you haven't already:
   ```
   aws configure
   ```
   You'll need an AWS access key, secret key, and default region. The IAM
   user/role needs permission to call:
   - `transcribe:StartTranscriptionJob`
   - `transcribe:GetTranscriptionJob`
   - `transcribe:ListTranscriptionJobs`
   - `transcribe:DeleteTranscriptionJob`
   - `transcribe:CreateVocabulary`
   - `transcribe:GetVocabulary`
   - `transcribe:ListVocabularies`
   - `transcribe:UpdateVocabulary`
   - `transcribe:DeleteVocabulary`
   - `s3:CreateBucket`, `s3:PutObject`, `s3:GetObject`, `s3:DeleteObject`,
     `s3:DeleteBucket`

   (The AWS managed policies `AmazonTranscribeFullAccess` and
   `AmazonS3FullAccess` cover this for experimentation.)

2. **Install dependencies:**
   ```
   python -m pip install -r requirements.txt
   ```

## How to run

```
cd aws_examples/python/example_code/transcribe
python getting_started.py
```

or for the fuller custom-vocabulary scenario:

```
python transcribe_basics.py
```

⚠ These call the real AWS Transcribe and S3 services and may result in
charges to your AWS account. Each script creates and deletes its own S3
bucket, so no leftover resources should remain after a successful run.

---

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: Apache-2.0
