add_executable(example_tests example_test.cpp)

target_link_libraries(example_tests PRIVATE example_lib Catch2::Catch2)

add_test(example_tests example_tests)