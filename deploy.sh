#!/bin/bash

PROJECT_ID=$(gcloud config list --format 'value(core.project)' 2>/dev/null)
gcloud builds submit --tag gcr.io/"${PROJECT_ID}"/listener
gcloud compute instances create-with-container archive-listener --container-image gcr.io/spartan-theorem-328817/listener:latest --service-account  listener-contract@spartan-theorem-328817.iam.gserviceaccount.com --scopes "https://www.googleapis.com/auth/cloud-platform" --zone europe-west4-c


