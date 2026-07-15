# Amazon Comprehend example

## What this example does

`comprehend_detect.py` runs several Amazon Comprehend APIs against a sample
text file (`detect_sample.txt`) and prints the results:

- Detects the dominant language
- Detects entities (people, places, organizations, etc.)
- Detects key phrases
- Detects personally identifiable information (PII)
- Detects sentiment
- Detects syntax (parts of speech)

Amazon Comprehend is serverless, so nothing needs to be provisioned in AWS
beforehand — this calls the live service directly.

## Prerequisites

1. **Configure AWS credentials**, if you haven't already:
   ```
   aws configure
   ```
   You'll need an AWS access key, secret key, and default region. The IAM
   user/role needs permission to call:
   - `comprehend:DetectDominantLanguage`
   - `comprehend:DetectEntities`
   - `comprehend:DetectKeyPhrases`
   - `comprehend:DetectPiiEntities`
   - `comprehend:DetectSentiment`
   - `comprehend:DetectSyntax`

   (The AWS managed policy `ComprehendReadOnly` covers this.)

2. **Install dependencies:**
   ```
   python -m pip install -r requirements.txt
   ```

## How to run

```
cd aws_examples/python/example_code/comprehend
python comprehend_detect.py
```

⚠ This calls the real AWS Comprehend service and may result in charges to
your AWS account.

---

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: Apache-2.0
