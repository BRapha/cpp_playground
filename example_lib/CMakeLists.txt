add_library(example_lib STATIC include/example_lib/example.h src/example.cpp)

target_include_directories(example_lib
                           PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
                                  $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

if(BUILD_TESTING)
	add_subdirectory(tests)
endif()
