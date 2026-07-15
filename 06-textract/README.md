# Amazon Textract example

## What this example does

`textract_demo.py` sends a local document image (PNG or JPG) to Amazon
Textract and prints the results:

- Detects lines of text (`DetectDocumentText`)
- Detects form key/value pairs and tables (`AnalyzeDocument` with FORMS and
  TABLES features)

Amazon Textract is serverless, so nothing needs to be provisioned in AWS
beforehand — this calls the live service directly with the image bytes, no
S3 bucket required.

## Prerequisites

1. **Configure AWS credentials**, if you haven't already:
   ```
   aws configure
   ```
   You'll need an AWS access key, secret key, and default region. The IAM
   user/role needs permission to call:
   - `textract:DetectDocumentText`
   - `textract:AnalyzeDocument`

   (The AWS managed policy `AmazonTextractFullAccess` covers this for
   experimentation.)

2. **Install dependencies:**
   ```
   python -m pip install -r requirements.txt
   ```

3. **A document image** — any local PNG or JPG file containing text (a
   scanned form, receipt, invoice, screenshot, etc.).

## How to run

```
cd aws_examples/python/example_code/textract
python textract_demo.py path/to/your/document.png
```

Optionally pass `--region` to override your configured default Region:

```
python textract_demo.py path/to/your/document.png --region us-east-1
```

⚠ This calls the real AWS Textract service and may result in charges to
your AWS account.

---

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: Apache-2.0
