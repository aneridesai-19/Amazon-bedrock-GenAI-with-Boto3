# Amazon Bedrock - Generative AI with Boto3

## Overview
This project demonstrates how to build generative AI applications using **Amazon Bedrock** with the **AWS SDK for Python (Boto3)**. It covers how to set up your environment, authenticate with AWS, select a foundation model, send prompts, and process AI-generated responses.

## Features
- Use **Amazon Bedrock** to access generative AI models.
- Send text prompts and receive AI-generated responses.
- Integrate **Boto3**, AWS's SDK for Python.

## Prerequisites
- **AWS Account** with access to Amazon Bedrock.
- **Python 3.8+** installed.
- **Boto3 and AWS CLI** installed.
- AWS credentials configured via `aws configure`.

## Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/aneridesai-19/Amazon-bedrock-GenAI-with-Boto3
   ```
2. Configure AWS credentials:
   ```sh
   aws configure
   ```
3. Create virtual environment:
   ```sh
   python -m venv venv
   ```
4. Activate virtual environment:
   ```sh
   venv\Script\activate
   ```
5. Install dependencies:
   ```sh
   pip install boto3
   ```

## Usage
Run the following script to interact with a foundation model on Amazon Bedrock:

```python
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
            "topP": 1  # Keep only topP
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
```

## Expected Output
When you run the code, you’ll receive an AI-generated response:
```sh
Response: 
I am Amazon Titan, a large language model built by AWS. I was designed to assist you with tasks or answer any questions you may have. How may I help you?
```
