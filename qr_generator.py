#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SYNOPSIS

    TODO helloworld [-h,--help] [-v,--verbose] [--version]

DESCRIPTION

    ACIO program to dynamically generate QR codes and send them via Gmail.

EXAMPLES

    Ex.:

      $python acio_qr_generator.py <text_to_include>
      $python acio_qr_generator.py <16.777.777-A>

    TODO: Show some examples of how to use this script.

EXIT STATUS

    TODO: List exit codes

AUTHOR

    Etxahun Sanchez Bazterretxea <etxahun.sanchez@gmail.com>

LICENSE

    This script is in the public domain, free from copyrights or restrictions.

VERSION

    $v0.1$
"""

import sys, os, traceback, optparse
import time
import re
#from pexpect import run, spawn

# Required libraries for QR generation
from qrcode import *

# Required libraries for email submision
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

# Global variables
qr_filename = "test_qr_code.png"
fromaddr = "<e-mail FROM address>"
toaddr = "<e-mail TO address>"
mail_passwd = "<e-mail FROM address' PASSWD>"

# Functions

def qr_gen(text):
    qr = QRCode(version=20, error_correction=ERROR_CORRECT_L)
    qr.add_data(text)
    qr.make() # Generate the QRCode itself

    # im contains a PIL.Image.Image object
    im = qr.make_image()

    # To save it
    im.save(qr_filename)

def send_qr():

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Your QR Code"

    body = "Please, find attached your QR code."

    msg.attach(MIMEText(body, 'plain'))

    # Path donde se encuentra la imagen QR (incluyendo el nombre del fichero)
    # En caso de encontrarse en el mismo directorio de este programa, bastará con
    # el nombre de la imagen QR:
    #    open("/path/qr_filename")
    attachment = open(qr_filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % qr_filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, mail_passwd)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


def main ():

    global options, args

    # Comprobramos si se ha introducido algun texto a incluir en el código QR
    if len(sys.argv) > 1:
        # QR generation with the string passed by the user
        qr_gen(str(sys.argv[1]))

        # Email notification to the user with the previously generated QR attached
        send_qr()
    else:
        print "\n ERROR: You haven't introduced any text argument.\n\n Usage: \n -----\n\n   $python qr_generator.py <texto_a_introducir>\n"

if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'], version='v0.1')
        parser.add_option ('-v', '--verbose', action='store_true', default=False, help='verbose output')
        (options, args) = parser.parse_args()
        #if len(args) < 1:
        #    parser.error ('missing argument')
        if options.verbose: print time.asctime()
        main()
        if options.verbose: print time.asctime()
        if options.verbose: print 'TOTAL TIME IN MINUTES:',
        if options.verbose: print (time.time() - start_time) / 60.0
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)
