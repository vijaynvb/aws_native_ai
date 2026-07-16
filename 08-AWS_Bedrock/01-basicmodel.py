# access aws bedrock model mistral 7b
import json
import os

import boto3
import dotenv

dotenv.load_dotenv()

client = boto3.client("bedrock-runtime")

if __name__ == "__main__":
    payload = {
        "messages": [
            {"role": "user", "content": "Write a poem about the beauty of nature."}
        ]
    }
    print(client.invoke_model(
        modelId="mistral.mistral-large-3-675b-instruct",
        contentType="application/json",
        accept="application/json",
        body=json.dumps(payload).encode("utf-8"),
        guardrailIdentifier= 'q2mxqkez9fdc',
        guardrailVersion= '1',
        trace= "ENABLED"
    )
    )["body"].read().decode("utf-8")
