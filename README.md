# qr_generator
Python QR generator and e-mail notification application. 

## Table of Contents
 - [Installation](#installation)
 - [Configuration](#configuration)
 - [Usage](#usage)
 - [Contributing](#contributing)
 - [References](#references)

## Installation

First of all install the required Python libraries:
```shell
    $ sudo pip install pil qrcode
```

## Configuration

The following tweaks are needed in order to make it work:

1. Modify the following lines according to your needs:
```python
# Global variables
qr_filename = "test_qr_code.png"
fromaddr = "<e-mail FROM address>"
toaddr = "<e-mail TO address>"
mail_passwd = "<e-mail FROM address' PASSWD>"
```

## Usage

Just run it as follows:
``` shell
$ python qr_generator <text_to_add_to_the_QR_code>
```
For more help:
``` shell
$ python qr_generator --help
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## References

The following is a list of useful references used for the development of the application:
* [Python and QR Codes](http://blog.matael.org/writing/python-and-qrcodes/)
* [PIL and PILLOW](http://stackoverflow.com/questions/32772596/pip-install-pil-fails)
* [Send e-mail with Python](http://naelshiab.com/tutorial-send-email-python/)
