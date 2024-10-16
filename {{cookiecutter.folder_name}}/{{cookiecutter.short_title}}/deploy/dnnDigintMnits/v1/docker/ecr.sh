#!/bin/bash

REGION="us-east-1"
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
ECR_NAME="champion"
DOCKER_NAME='chapion'
ECR_TAG="latest"
BACKEND="podman"

bentoml build

OUTPUT=$(bentoml containerize ${DOCKER_NAME}:latest --backend ${BACKEND})

ACTUAL_TAG=$(echo "$OUTPUT" | grep -oP 'detector-lstm-v1-bhp:\K[^ ]+')
ACTUAL_TAG=$(echo "$ACTUAL_TAG" | tr -d '"')

aws ecr get-login-password --region ${REGION} | ${BACKEND} login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com

if ! ${BACKEND} images | grep -q "${DOCKER_NAME}:${ACTUAL_TAG}"; then
  echo "Error: Docker image ${DOCKER_NAME}:${ACTUAL_TAG} does not exist."
  exit 1
fi

${BACKEND} tag ${DOCKER_NAME}:${ACTUAL_TAG} ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${ECR_NAME}:${ECR_TAG}

${BACKEND} push ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${ECR_NAME}:${ECR_TAG}

if [ $? -eq 0 ]; then
  echo "Successfully pushed ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${ECR_NAME}:${ECR_TAG}"
else
  echo "Failed to push image to ECR."
  exit 1
fi
