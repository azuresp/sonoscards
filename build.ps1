Remove-Item export\*
"***** ZBAR build"
docker build -t rpi-zbar rpi-zbar
"***** Scanner add-ons"
docker build -t sonos-scanner scanner
"***** Exporting Scanner"
docker image save sonos-scanner:latest -o export\sonos-scanner.tar
"***** Doing controller (this is fast!)"
docker build -t sonos-controller controller
docker image save sonos-controller:latest -o export\sonos-controller.tar