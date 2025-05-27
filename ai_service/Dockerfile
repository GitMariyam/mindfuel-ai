FROM public.ecr.aws/lambda/python:3.11

# Copy app and dependencies
COPY app.py ./
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command for Lambda
CMD ["app.lambda_handler"]


