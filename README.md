### Instalando docker-ce=17.12.0~ce-0~ubuntu

```
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common -y;
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable";
sudo apt-get update;
sudo apt-get install docker-ce=17.12.0~ce-0~ubuntu -y;
```

### Instalando docker-compose=1.19.0

```
sudo curl -L https://github.com/docker/compose/releases/download/1.19.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose;
sudo chmod +x /usr/local/bin/docker-compose;
```

### Habilitar as credenciais para fazer pull das imagens do docker registry do google

Pesquisar na internet

### Instalando o mongodb client

```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4;
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list;
sudo apt-get update;
sudo apt-get install -y mongodb-org-shell;
```

### Logar no mongo com o mongo client:

```
mongo --authenticationDatabase admin -u root -p UycjvlH5R54cJHfy44XGbvtXfGtXKweQ 35.232.243.78:27017
```
