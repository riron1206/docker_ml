cd /mnt/c/Users/81908/MyGitHub/docker_ml/docker_ml
docker build -t docker_ml -f Dockerfile .
docker run -it -m 8g -v $PWD/code:/code --rm docker_ml /bin/bash