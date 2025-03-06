# Amazon Bedrock - Generative AI with Boto3

## Overview
This project demonstrates how to build generative AI applications using **Amazon Bedrock** with the **AWS SDK for Python (Boto3)**. It covers setting up your environment, authenticating with AWS, selecting foundation models (Titan Text Lite and Titan Text Express), sending prompts, handling responses, and implementing a retry mechanism.

## Features
- Use **Amazon Bedrock** to access generative AI models.
- Supports **Titan Text Lite** and **Titan Text Express** models.
- Send text prompts and receive AI-generated responses.
- Implements **exponential backoff retry mechanism** for handling service unavailability.
- Integrate **Boto3**, AWS's SDK for Python.

## Prerequisites
- **AWS Account** with access to Amazon Bedrock.
- **Python 3.8+** installed.
- **Boto3 and AWS CLI** installed.
- AWS credentials configured via `aws configure`.
- An IAM user with necessary permissions to access and invoke models.

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
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # macOS/Linux
   ```
5. Install dependencies:
   ```sh
   pip install boto3
   ```

## Usage
### 1. Titan Text Lite Model
This script interacts with the **Titan Text Lite** model on Amazon Bedrock:

```python
import json
import boto3

def getResponse():
    # Set up the Amazon Bedrock client
    bedrock_client = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1"
    )

    model_id = "amazon.titan-text-lite-v1"
    prompt = "What is generative AI?"

    payload = {
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 200,
            "temperature": 0.7,
            "topP": 1  # Keep only topP
        }
    }

    response = bedrock_client.invoke_model(
        modelId=model_id,
        body=json.dumps(payload)
    )

    result = json.loads(response["body"].read())
    generated_text = result["results"][0]["outputText"]
    
    print(f"Response: {generated_text}")

if __name__ == "__main__":
    getResponse()
```

### 2. Titan Text Express Model (with Retry Mechanism)
This script interacts with **Titan Text Express** model and includes a retry mechanism:

```python
import json
import boto3
import time

def getResponse():
    bedrock_client = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1"
    )

    model_id = "amazon.titan-text-express-v1"
    prompt = "What is generative AI?"

    payload = {
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 200,
            "temperature": 0.7,
            "topP": 1
        }
    }

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
```

## Expected Output
When you run the code, you’ll receive an AI-generated response, such as:
```sh
Response: 
Generative AI refers to artificial intelligence models that generate new content, such as text, images, or code, based on learned patterns.
```

## Model Comparison
Below is a comparison of **Titan Text Lite** and **Titan Text Express** based on test cases:

| Test Case | Titan Text Lite | Titan Text Express |
|-----------|----------------|--------------------|
| Basic Prompt ("What is generative AI?") | Provides a concise response | Provides a more detailed response |
| Response Time | Faster | Slightly slower due to retry mechanism |
| Handling Service Unavailability | No retry mechanism | Implements exponential backoff retry |
| Token Limit | 200 | 200 |
| Best Use Case | Quick and lightweight text generation | More robust and reliable responses |

## Notes
- The **Titan Text Lite** model provides fast and cost-effective text generation.
- The **Titan Text Express** model offers more robust text generation and includes a retry mechanism for handling service unavailability.
- The exponential backoff mechanism ensures the system retries failed requests with increasing wait time.

## Conclusion
This project showcases how to interact with **Amazon Bedrock** using **Boto3** to send prompts and process responses from **Titan Text Lite** and **Titan Text Express** models. The retry mechanism enhances reliability when using Bedrock models.

