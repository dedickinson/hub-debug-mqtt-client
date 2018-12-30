# hub-debug-mqtt-client
A container to help test MQTT queues

To run:

    docker run --rm -it --network kraken-net --volume $(pwd):/app hub-debug-mqtt-client:latest /bin/bash

## References

- [Paho MQTT](https://pypi.org/project/paho-mqtt/)