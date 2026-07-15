# Amazon Rekognition example

## What this example does

`rekognition_image_detection.py` runs several Amazon Rekognition APIs
against sample images (bundled locally in `.media/`, plus two fetched over
HTTP) and displays the results as annotated images with bounding boxes:

- Detects faces (age range, gender, emotions, etc.)
- Detects labels (objects, scenes, activities)
- Recognizes celebrities
- Compares faces between two images
- Detects moderation labels (inappropriate content)
- Detects text in an image

Amazon Rekognition is serverless, so nothing needs to be provisioned in AWS
beforehand — this calls the live service directly, no S3 bucket required.

## Prerequisites

1. **Configure AWS credentials**, if you haven't already:
   ```
   aws configure
   ```
   You'll need an AWS access key, secret key, and default region. The IAM
   user/role needs permission to call:
   - `rekognition:DetectFaces`
   - `rekognition:DetectLabels`
   - `rekognition:DetectModerationLabels`
   - `rekognition:DetectText`
   - `rekognition:RecognizeCelebrities`
   - `rekognition:CompareFaces`

   (The AWS managed policy `AmazonRekognitionReadOnlyAccess` covers this.)

2. **Install dependencies** (includes Pillow, used to draw and display the
   annotated images):
   ```
   python -m pip install -r requirements.txt
   ```

## How to run

```
cd aws_examples/python/example_code/rekognition
python rekognition_image_detection.py
```

The script pauses between steps with `Press Enter to continue.` and opens
each annotated image in your default image viewer — switch back to the
terminal and press Enter to move on to the next detection.

⚠ This calls the real AWS Rekognition service and may result in charges to
your AWS account.

---

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: Apache-2.0
