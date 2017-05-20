docker build --network=host -t rpi-zbar rpi-zbar
docker build -t sonos-scanner scanner
docker build --network=host -t sonos-controller controller
