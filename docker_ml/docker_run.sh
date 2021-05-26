docker build -t docker_ml -f Dockerfile .
docker run -p 8889:8889 -p 8502:8502 -it -v $PWD/docker_ml:/docker_ml --rm docker_ml /bin/bash