# Amazon Polly example

## What this example does

`polly_lipsync.py` is a desktop GUI application (Tkinter) that:

- Lets you type text and pick an engine, language, and voice
- Sends the text to Amazon Polly to synthesize speech
- Plays the synthesized audio
- Animates a simple face that lip-syncs along with the speech, using viseme
  timing data returned by Polly

Amazon Polly is serverless, so nothing needs to be provisioned in AWS
beforehand — short text is synthesized synchronously with no S3 bucket
required. (Only if you enter text too long for synchronous synthesis will
it ask for an S3 bucket to run an asynchronous job.)

## Prerequisites

1. **Configure AWS credentials**, if you haven't already:
   ```
   aws configure
   ```
   You'll need an AWS access key, secret key, and default region. The IAM
   user/role needs permission to call:
   - `polly:DescribeVoices`
   - `polly:SynthesizeSpeech`

   (The AWS managed policy `AmazonPollyReadOnlyAccess` covers this.)

2. **Install dependencies:**
   ```
   python -m pip install -r requirements.txt
   ```

## How to run

```
cd aws_examples/python/example_code/polly
python polly_lipsync.py
```

Type some text in the box, choose an engine/language/voice, then click
**Say it!** to hear and see the synthesized speech.

⚠ This calls the real AWS Polly service and may result in charges to your
AWS account.

---

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: Apache-2.0
