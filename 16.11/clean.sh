#!/bin/bash

docker rm $(docker ps -a -q --filter "ancestor=linalg_test")
docker rmi linalg_test
