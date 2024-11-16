#include "LinearAlgebra.h"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(linalg_core, m) {
  m.doc() = R"doc(
    Python bindings for LinearAlgebra library
  )doc";

  py::class_<LinearAlgebra>(m, "LinearAlgebra")
  .def_static("cumSum", &LinearAlgebra::cumSum, R"doc(
        Calculates cumulative sum of vector elements using pure C++.

        Parameters:
          vec : vector of double
              Vector to calculate cumulative sum.

        Returns:
          vec : vector of double
              Cumulative sum of vector elements (prefix-sum).
  )doc");
}