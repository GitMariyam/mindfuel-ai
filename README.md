# MindFuel AI 🧠✨

A lightweight, containerized API that delivers daily tips and facts to boost your mindset, productivity, and well-being — powered by Python and Docker.

## 🔧 Tech Stack

- Python 3.11
- Flask
- Gunicorn (for production server)
- Docker (multi-stage build)
- [Optional: AWS deployment coming soon]

## 🚀 How to Run

### 1. Build the Docker image

```bash
docker build -t mindfuel-ai .

2. Run the container
docker run -d -p 8000:8000 mindfuel-ai

3. Test the API
Open your browser or use curl:
curl http://localhost:8000/fact

You’ll get back a motivational or educational fact to fuel your mind.

📦 Project Structure
mindfuel-ai/
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md

📤 Available Docker Images
docker.io/YOUR_USERNAME/mindfuel-ai

(Replace with your actual Docker Hub username)

🛠 To-Do
 Add AI-generated facts via OpenAI or Hugging Face API

 Add unit tests

 Deploy to AWS Lambda & ECS (coming soon)

 Add CI/CD pipeline

📤 Author
Built as part of a cloud engineering practise  project to demonstrate:

Dockerized microservice design

Real-world API setup

Future integration with serverless and AI

Feel free to fork, clone, or contribute!


🚀 Target Architecture Overview (AWS Free Tier-Friendly)

🧠 Core Microservices (AI, Logger)

Service        | AWS Option | Why it’s used                                | Free Tier?
ai-service     | AWS Lambda | Stateless, lightweight — perfect for AI tips | ✅ Yes
logger-service | AWS Lambda | Simple function to log to a DB or file       | ✅ Yes

🌐 Routing & Access

Component           | AWS Option         | Why it's used                             | Free Tier?
API Gateway         | Amazon API Gateway | Route /fact to ai-service, /log to logger | ✅ Yes
Frontend (optional) | S3 + CloudFront    | Host a static frontend if needed          | ✅ Yes

🗃️ Data & Storage
Purpose          | AWS Service  | Why it's used                               | Free Tier?
Log storage      | DynamoDB     | Lightweight, scalable, and serverless NoSQL | ✅ Yes
AI Model or Tips | S3 or inline | If needed, store prompts, facts, etc.       | ✅ Yes

📦 DevOps / CI/CD (Later stage)

Purpose            | AWS Option                         Why it's used                      | Free Tier?
CI/CD              | GitHub Actions + AWS CLI         | Automate deploy to Lambda          | ✅ Yes
Container Registry | ECR (Elastic Container Registry) | Store Docker images for Lambda/ECS | ✅ Yesreadme