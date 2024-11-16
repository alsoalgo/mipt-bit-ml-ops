#include "LinearAlgebra.h"
#include <iostream>
#include <vector>

std::vector<double> LinearAlgebra::cumSum(const std::vector<double>& vec) {
    std::vector<double> cumSum(vec.size(), 0.);
    cumSum[0] = vec[0];
    for (size_t i = 1; i < vec.size(); ++i) {
        cumSum[i] = cumSum[i - 1] + vec[i];
    }
    return cumSum;
}