#!/bin/bash

docker build -t linalg_test .
docker run -it linalg_test bash -c "cd /app && python3 test_linalg.py"