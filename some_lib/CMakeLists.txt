add_library(some_lib STATIC include/some_lib/template.h src/template.cpp)

target_include_directories(some_lib
                           PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
                                  $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

if(BUILD_TESTING)
	add_subdirectory(tests)
endif()
