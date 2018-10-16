sudo docker-compose stop;
sudo gcloud docker -- pull gcr.io/smart-car-insurance-hybrid/api-gateway:latest;
sudo gcloud docker -- pull gcr.io/smart-car-insurance-hybrid/gps-service:latest;
sudo gcloud docker -- pull gcr.io/smart-car-insurance-hybrid/ui-service:latest;
sudo docker-compose up -d;
