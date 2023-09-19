// Ultrasonic.h

class Ultrasonic {
private:
    int trigger_pin, echo_pin;
public:
    Ultrasonic(int trigger_pin, int echo_pin);
    int get_distance();
    ~Ultrasonic();
};

Ultrasonic::Ultrasonic(int trigger_pin, int echo_pin) {
    this->trigger_pin = trigger_pin;
    this->echo_pin = echo_pin;
    pinMode(trigger_pin, OUTPUT);
    pinMode(echo_pin, INPUT);
}

int Ultrasonic::get_distance() {
    int distance, duration;
    digitalWrite(this->trigger_pin, LOW);
    delayMicroseconds(2);
    digitalWrite(this->trigger_pin, HIGH);
    delayMicroseconds(10);
    digitalWrite(this->trigger_pin, LOW);
    duration = pulseIn(this->echo_pin, HIGH);
    distance = duration * 0.034 / 2;
    return distance;
}

Ultrasonic::~Ultrasonic() {
}
