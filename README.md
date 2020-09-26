# HTTP Status Check

Python script to check multiple URL routes against an expected HTTP status code.

## Requirements

* Python3 >=3.7
* pip3

## Installation

Install required modules.

````shell
$ pip3 install -r requirements.txt
````

## Configuration

Create configuration file.

````shell
$ cp dist/config.yaml.dist config.yaml
````

Fit configuration for your needs.

````yaml
domain: https://my-domain.com
expectedHttpStatusCode: 200
routes:
  - /index.html
  - /my/sub/dir/index.html
````

## Usage

Run check script with your configuration.

````shell
$ python3 http_status_check.py --config=/<path>/config.yaml
````

Enable debug output by adding `--debug` flag.

## Parameters

### --config

### --debug

## Example

**Configuration (`./test/config.yaml`):**
`````yaml
domain: https://www.google.de
expectedHttpStatusCode: 200
routes:
  - /
  - /imghp?hl=de&tab=wi&ogbl
`````

**Execution:**
````shell
$ python3 http_status_check.py --config=./test/config.yaml
````

**Output:**
````shell
[INFO] Read configuration from ./test/config.yaml
[INFO] Run checks
[OK] https://www.google.de/ returns HTTP status 200
[OK] https://www.google.de/imghp?hl=de&tab=wi&ogbl returns HTTP status 200
[OK] Done.
````