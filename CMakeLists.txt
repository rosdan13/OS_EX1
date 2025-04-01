cmake_minimum_required(VERSION 3.27)
project(EX1)

set(CMAKE_CXX_STANDARD 11)

add_executable(EX1
        measure.h
        measure.cpp
        memory_latency.cpp
        memory_latency.h)
