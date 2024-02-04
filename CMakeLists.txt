cmake_minimum_required(VERSION 3.13)

file(MAKE_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/generated)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
set( CMAKE_EXPORT_COMPILE_COMMANDS ON )
pico_sdk_init()

add_executable(hello
    hello.c
)

pico_enable_stdio_usb(hello 1)

pico_generate_pio_header(hello ${CMAKE_CURRENT_LIST_DIR}/ws2812.pio OUTPUT_DIR ${CMAKE_CURRENT_LIST_DIR}/generated)
target_sources(hello PRIVATE hello.c)

target_link_libraries(hello
    pico_stdlib
    pico_cyw43_arch_none
    hardware_pio
)

pico_add_extra_outputs(hello)

add_custom_target(pio_ws2812_datasheet DEPENDS ${CMAKE_CURRENT_LIST_DIR}/generated/ws2812.py)
add_custom_command(OUTPUT ${CMAKE_CURRENT_LIST_DIR}/generated/ws2812.py
    DEPENDS ${CMAKE_CURRENT_LIST_DIR}/ws2812.pio
    COMMAND Pioasm -o python ${CMAKE_CURRENT_LIST_DIR}/ws2812.pio ${CMAKE_CURRENT_LIST_DIR}/generated/ws281
    VERBATIM)

    add_dependencies(hello pio_ws2812_datasheet)
