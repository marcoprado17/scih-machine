sudo docker-compose -f /home/marco/scih-machine/docker-compose.yaml stop;
sudo gcloud docker -- pull gcr.io/smart-car-insurance-hybrid/api-gateway:latest;
sudo gcloud docker -- pull gcr.io/smart-car-insurance-hybrid/gps-service:latest;
sudo gcloud docker -- pull gcr.io/smart-car-insurance-hybrid/ui-service:latest;
sudo docker-compose -f /home/marco/scih-machine/docker-compose.yaml up -d;
