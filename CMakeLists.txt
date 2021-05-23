cmake_minimum_required(VERSION 3.16)

project(catch2_template VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 14)

include(CTest)
include(FetchContent)

if(BUILD_TESTING)
	include(${CMAKE_CURRENT_SOURCE_DIR}/cmake/fetch_catch.cmake)
endif()

add_subdirectory(example_lib)
