#include "mbed.h"

DigitalOut led1(LED1);

// main() runs in its own thread in the OS
int main() {

  double t1 = 1.0;
  double t2 = 1.0;
  double t3 = 1.0;
  double t4 = 1.0;


  led1 = 1;
  wait(0.1);

  led1 = 0;
  wait(0.1);

  led1 = 1;
  wait(0.1);

  led1 = 0;
  wait(0.1);

  led1 = 1;
  wait(0.1);
  
  

  while (true) {
	led1 = !led1;
	wait(0.5);
  }


}

