sudo docker run --device=/dev/vchiq --network host -d --restart unless-stopped sonos-scanner:latest
sudo docker run -p 5000:5000 --network host -d --restart unless-stopped sonos-controller:latest

