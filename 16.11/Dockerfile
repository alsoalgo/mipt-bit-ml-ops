FROM python:3.9

RUN apt-get update && apt-get install -y cmake g++ pybind11-dev && pip install --upgrade pip

RUN pip install pybind11 setuptools wheel build pytest numpy

WORKDIR /app

COPY . .

RUN ls -R /app

RUN mkdir build && cd build && cmake .. && make

RUN python3 -m build 
RUN pip install dist/*.whl

CMD ["python3", "test_linalg.py"]
