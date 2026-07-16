# access aws bedrock model mistral 7b
import json
import os

import boto3
import dotenv

dotenv.load_dotenv()

client = boto3.client("bedrock-runtime")


def build_invoke_params(payload, model_id="mistral.mistral-large-3-675b-instruct"):
    params = {
        "modelId": model_id,
        "contentType": "application/json",
        "accept": "application/json",
        "body": json.dumps(payload).encode("utf-8"),
    }

    guardrail_id = os.getenv("BEDROCK_GUARDRAIL_ID") 
    guardrail_version = os.getenv("BEDROCK_GUARDRAIL_VERSION") 

    if guardrail_id and guardrail_version:
        params["guardrailIdentifier"] = guardrail_id
        params["guardrailVersion"] = guardrail_version
        params["trace"] = os.getenv("BEDROCK_GUARDRAIL_TRACE", "ENABLED")
    #print(f"Built invoke params: {params}")

    return params


def invoke_model(payload, model_id="mistral.mistral-large-3-675b-instruct"):
    print(f"Invoking model {model_id} with payload: {payload}")
    params = build_invoke_params(payload, model_id)
    print(f"Invoking model with params: {params}")
    response = client.invoke_model(**params)
    return response["body"].read().decode("utf-8")


if __name__ == "__main__":
    payload = {
        "messages": [
            {"role": "user", "content": "Write a poem about the beauty of nature."}
        ]
    }

    print(invoke_model(payload))
