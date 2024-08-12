# digitalia-aiko-cluetail
Codes for a demo available via https://memorylab.fi/AIKO/cluetail-demo/

## Steps to run
* Ensure that you have Docker installed, if not find a tutorial
* Clone the repo
* Compile the code, e.g. with `sudo docker build -t cluetail .`
* Run with e.g. `sudo docker run -p 8084:8084 --name cluetail -d --restart unless-stopped cluetail`
* If you want to run this on localhost without https, check the end of [cluetailFullDemo.py](https://github.com/xamkfi/digitalia-aiko-cluetail/blob/main/cluetailFullDemo.py), lines 116 and 117
* **If you need more instructions then learn more docker..**
