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

    payload = {
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 200,
            "temperature": 0.7,
            "topP": 1
        }
    }

    # Retry mechanism with exponential backoff
    max_retries = 5
    base_delay = 2  # seconds

    for attempt in range(max_retries):
        try:
            response = bedrock_client.invoke_model(
                modelId=model_id,
                body=json.dumps(payload)
            )

            result = json.loads(response["body"].read().decode("utf-8"))
            generated_text = result["results"][0]["outputText"]

            print(f"Response: {generated_text}")
            return  # Exit function if successful

        except bedrock_client.exceptions.ServiceUnavailableException:
            wait_time = base_delay * (2 ** attempt)  # Exponential backoff
            print(f"Service unavailable, retrying in {wait_time} seconds...")
            time.sleep(wait_time)

    print("Max retries reached. Bedrock is still unavailable.")

if __name__ == "__main__":
    getResponse()
