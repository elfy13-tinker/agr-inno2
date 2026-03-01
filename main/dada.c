#include <stdint.h>

#define LED_PIN 13

void delay(volatile uint32_t count) {
    while (count--) {
        __asm__("nop");
    }
}

int main(void) {
    // pseudo register
    volatile uint8_t LED = 0;

    while (1) {
        LED ^= 1;      // toggle LED
        delay(100000);
    }
}