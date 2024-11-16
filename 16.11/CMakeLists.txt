cmake_minimum_required(VERSION 3.10)
project(linalg)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(pybind11 REQUIRED)

add_library(linalg_core MODULE
    linalg/src/LinearAlgebra.cpp
    linalg/python/bindings.cpp
)

target_include_directories(linalg_core PRIVATE
    linalg/src
)

target_link_libraries(linalg_core PRIVATE pybind11::module)

set_target_properties(linalg_core PROPERTIES
    PREFIX ""
    SUFFIX ".so"
)
