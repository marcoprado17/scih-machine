sudo docker-compose -f /home/marco/machines/scih-machine/docker-compose.yaml stop;
cd /home/marco/nodejs/scih-ui-service;
sudo docker build -f devops/Dockerfile -t gcr.io/smart-car-insurance-hybrid/ui-service:latest .;
cd /home/marco/nodejs/scih-api-gateway;
sudo docker build -f devops/Dockerfile -t gcr.io/smart-car-insurance-hybrid/api-gateway:latest .;
cd /home/marco/nodejs/scih-gps-service;
sudo docker build -f devops/Dockerfile -t gcr.io/smart-car-insurance-hybrid/gps-service:latest .;
sudo docker-compose -f /home/marco/machines/scih-machine/docker-compose.yaml up;
