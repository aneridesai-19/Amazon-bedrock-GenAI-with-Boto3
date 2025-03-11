The provided code is already in a fixed format and does not require any modifications.

Here is the fixed code:

#TITAN TEXT EXPRESS MODEL

import json
import boto3
import time

def getResponse():
    # Set up the Amazon Bedrock client
    bedrock_client = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1"
    )

    model_id = "amazon.titan-text-express-v1"
    prompt = "What is generative ai?"

    payload