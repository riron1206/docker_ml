docker build -t docker_ml -f Dockerfile .
docker run -p 8889:8889 -it -v $PWD/docker_ml:/docker_ml --rm docker_ml /bin/bash