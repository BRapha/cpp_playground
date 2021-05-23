cmake_minimum_required(VERSION 3.16)

project(playground VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 14)

include(CTest)
include(FetchContent)

if(BUILD_TESTING)
	include(${CMAKE_CURRENT_SOURCE_DIR}/cmake/fetch_catch.cmake)
	add_subdirectory(catch_with_main)
endif()

add_subdirectory(example_lib)
