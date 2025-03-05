import json
import boto3

def getResponse():
    # Set up the Amazon Bedrock client
    bedrock_client = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1"
    )

    # Define the model ID
    model_id = "amazon.titan-text-lite-v1"

    # Prepare the input prompt
    prompt = "Who are you?"

    # Prepare the request payload (without topK)
    payload = {
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 200,
            "temperature": 0.7,
            "topP": 1  # ✅ Keep only topP
        }
    }

    # Invoke the Amazon Bedrock model
    response = bedrock_client.invoke_model(
        modelId=model_id,
        body=json.dumps(payload)
    )

    # Process the response
    result = json.loads(response["body"].read())
    generated_text = result["results"][0]["outputText"]
    
    print(f"Response: {generated_text}")

if __name__ == "__main__":
    getResponse()
