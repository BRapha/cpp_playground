#define CATCH_CONFIG_MAIN

#include <catch2/catch.hpp>

#include <example_lib/example.h>

TEST_CASE("Test Example::return2"){
    const Example example;
    REQUIRE(example.return2() == 2);
}