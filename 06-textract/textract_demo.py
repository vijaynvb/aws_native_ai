# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

## To run this example you need to configure your AWS credentials and default region.
## To execute this example, run the following commands in your terminal:
## python -m pip install -r requirements.txt
## python textract_demo.py path/to/your/document.png


"""
Purpose

Runs TextractWrapper against the real Amazon Textract service to detect
text, form, and table elements in a local document image (PNG or JPG).

Usage:
    python textract_demo.py <path-to-image> [--region us-east-1]

This calls the synchronous Textract APIs (DetectDocumentText and
AnalyzeDocument), so no S3 bucket, SNS topic, or SQS queue is required.
Running this script calls the real AWS Textract service and may incur
charges on your AWS account.
"""

import argparse
import logging

import boto3

from textract_wrapper import TextractWrapper

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def print_lines(response):
    lines = [block["Text"] for block in response["Blocks"] if block["BlockType"] == "LINE"]
    print(f"\nDetected {len(lines)} lines of text:")
    for line in lines:
        print(f"  {line}")


def print_forms_and_tables(response):
    key_values = [block for block in response["Blocks"] if block["BlockType"] == "KEY_VALUE_SET"]
    tables = [block for block in response["Blocks"] if block["BlockType"] == "TABLE"]
    print(f"\nDetected {len(key_values)} form key/value elements and {len(tables)} tables.")


def main():
    parser = argparse.ArgumentParser(description="Run Amazon Textract on a local image file.")
    parser.add_argument("document", help="Path to a local PNG or JPG document image.")
    parser.add_argument(
        "--region", default=None, help="AWS Region to use (defaults to your configured region)."
    )
    args = parser.parse_args()

    textract_client = boto3.client("textract", region_name=args.region)
    wrapper = TextractWrapper(textract_client, None, None)

    print(f"Sending {args.document} to Textract for text detection...")
    text_response = wrapper.detect_file_text(document_file_name=args.document)
    print_lines(text_response)

    print(f"\nSending {args.document} to Textract for form and table analysis...")
    analysis_response = wrapper.analyze_file(
        ["FORMS", "TABLES"], document_file_name=args.document
    )
    print_forms_and_tables(analysis_response)


if __name__ == "__main__":
    main()
