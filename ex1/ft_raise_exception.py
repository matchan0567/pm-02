#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    if temperature < 0
        raise Exception(Caught input_temperature error: 100°C is too hot for plants (max 40°C))
    return int(temp_str)


def test_temperature() -> None:
    temp_str = '25'
    print(f"Input data is '{temp_str}'")
    try:
        temperature = input_temperature(temp_str)
        print(f"Temperature is now {temperature}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    temp_str = '100'
    print(f"Input data is '{temp_str}'")
    try:
        temperature = input_temperature(temp_str)
        print(f"Temperature is now {temperature}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature()
