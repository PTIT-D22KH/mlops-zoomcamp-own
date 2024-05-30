#!/bin/bash

PROJECT_NAME=homework_03 \
  MAGE_CODE_PATH=/workspaces/mlops-zoomcamp-own/03-orchestration/homework_03/src \
  SMTP_EMAIL=$SMTP_EMAIL \
  SMTP_PASSWORD=$SMTP_PASSWORD \
  docker compose up