/*

  JTAG programmer using Arduino
    Dario Fagotto, 2019

  Version 1.0

    Based on https://github.com/mattdibi/Programmatore-JTAG-per-Xilinx/blob/master/JTAG/JTAG.ino
      by Mattia Dal Ben
      by Mattia Marson
      by Manuel Guglielmini
 
    Extended command set:
      *!       -> tms bit
      .,       -> tdi bit
      [0-9a-f] -> tdi nibble (sent LSB first)
      :;       -> tdi end bit
      <>       -> start and stop tdo output
      #        -> sync and flush
      I        -> print FPGA id code

    Test sequence to read ID code:
      !!!!!* !!** 9.. !* !* <0000000...:> !*

*/


// Board configuration

// Use SerialUSB instead of Serial (usually faster if available!)
#define USE_USB

// Select BAUDRATE (maximum reliable on ~any chip 115200)
#define BAUDRATE 500000

// Clock delay (delay between clock edges in us)
#define TCKWAIT 1
// If missing define CLK_DELAY() macro, eg:
//#define CLK_DELAY() asm volatile ( "nop":: )

template <int pin, bool level>
class Pin {
  public:
    void operator()(const bool val) {
      digitalWrite(pin, val ^ !level); // Use sth faster?
    }
    operator bool() {
      return digitalRead(pin) ^ !level; // Use sth faster?
    }
    void input() {
      pinMode(pin, INPUT);
    }
    void output() {
      pinMode(pin, OUTPUT);
    }
};

// Pin and levels
Pin< 8, HIGH> tms;
Pin< 9, HIGH> tdi;
Pin<10, HIGH> tdo;
Pin<11, HIGH> tck;


// Program

#ifdef USE_USB
  #define SERIAL SerialUSB
#else
  #define SERIAL Serial
#endif

#ifdef TCKWAIT
  #define CLK_DELAY() delayMicroseconds(TCKWAIT)
#endif

uint32_t get_id();
uint8_t hex2num(char c);
char num2hex(uint8_t val);
template <typename T>
void printHex(T val, Stream& s);

void setup()
{
  tms.output();
  tdi.output();
  tdo.input();
  tck.output();

  SERIAL.begin(BAUDRATE);
  while(!SERIAL);
}

bool showRead = false;

template <int n = 1>
inline void clk() {
  for(int i = n; i > 0; --i) {
    tck(true);
    CLK_DELAY();
    tck(false);
    CLK_DELAY();
  }
}

template <int n = 1, bool output = true>
inline uint8_t tdx(uint8_t val) {
  uint8_t res = 0;
  for(uint8_t mask = 1; mask != (uint8_t)(1 << n); mask <<= 1) {
    tdi(val & mask);
    clk<>();
    if(output && tdo)
      res |= mask;
  }
  return res;
}

void loop() {
  if(SERIAL.available()) {
    uint8_t res;
    char c = SERIAL.read();
    switch(c) {
      case '*': tms(0); clk<>(); break;
      case '!': tms(1); clk<>(); break;

      case ':': tms(1);
      case '.': res = tdx<>(0); if(showRead) SERIAL.write(res ? ',' : '.'); break;

      case ';': tms(1);
      case ',': res = tdx<>(1); if(showRead) SERIAL.write(res ? ',' : '.'); break;

      case '<': showRead = true; break;
      case '>': showRead = false; break;

      case '#': SERIAL.write('#'); SERIAL.flush(); break;

      case 'I':
        SERIAL.print("\nChip ID: 0x");
        printHex(get_id(), SERIAL);
        SERIAL.print("\n");
        break;

      default:
        res = hex2num(c);
        if(res != 0xFF) {
          res = tdx<4>(res);
          if(showRead) SERIAL.write(num2hex(res));
        } else {
          // Error?
        }
    }
  }
}

// Protocol functions

inline void tms_rst() {
  tms(1);
  clk<5>();
  tms(0);
  clk<>();
}

inline void tms_idle() {
  tms(0);
  clk<>();
}

inline void tms_dr() {
  tms(1);
  clk<>();
  tms(0);
  clk<>();
}


inline void tms_ir() {
  tms(1);
  clk<2>();
  tms(0);
  clk<2>();
}

uint32_t get_id() {
  tms_rst();
  tms_dr();
  uint32_t id = 0;
  for(int curr_byte = 0; curr_byte < 4; ++curr_byte) {
    id |= tdx<8>(0xFF) << (curr_byte * 8);
  }
  // Exit bit
  tms(1);
  clk<>();
  tms_dr(); // Each transaction ends with dr
  return id;
}

// Helper functions

uint8_t hex2num(char c) {
  if(c >= '0' && c <= '9')
    return c - '0';
  if(c >= 'a' && c <= 'f')
    return c - 'a' + 0xA;
  return 0xFF;
}

char num2hex(uint8_t val) {
  if(val < 10)
    return val + '0';
  if(val < 16)
    return val + 'a' - 0xA;
  return '?';
}

template <typename T> void printHex(T val, Stream& s) {
  // Little endian!
  uint8_t* val_p = (uint8_t*)&val;
  for(int i = sizeof(val) - 1; i >= 0; --i) {
    s.write(num2hex(val_p[i] >> 4));
    s.write(num2hex(val_p[i] & 0xF));
  }
}

