#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "pico/stdlib.h"
#include "hardware/pio.h"
#include "hardware/clocks.h"
#include "ws2812.pio.h"

#define NUM_PIXELS 150
#define WS2812_PIN 2

static inline void put_pixel(uint32_t pixel_rgb) {
    pio_sm_put_blocking(pio0, 0, pixel_rgb << 8u);
}

static inline uint32_t urgb_u32(uint8_t r, uint8_t g, uint8_t b) {
    return
            ((uint32_t) (r) << 8) |
            ((uint32_t) (g) << 16) |
            (uint32_t) (b);
}

int main() {
    stdio_init_all();
    //freopen(NULL, "rb", stdin);

    PIO pio = pio0;
    int sm = 0;
    uint offset = pio_add_program(pio, &ws2812_program);
    ws2812_program_init(pio, sm, offset, WS2812_PIN, 800000, true);

    uint8_t buf[3 * NUM_PIXELS] = "\0";

    sleep_ms(10);
    while (1) {
        for (int i = 0; i < sizeof(buf); i++) {
            buf[i] = (uint8_t) getchar();
        }
        for (int i = 0; i < sizeof(buf); i += 3) {
            uint8_t r = buf[i+1];
            uint8_t g = buf[i+2];
            uint8_t b = buf[i];
            put_pixel(urgb_u32( r, g, b));
        }
    }
}
