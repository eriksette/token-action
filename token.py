import os
import argparse
import sys
import jwt
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('pem', type=argparse.FileType('rb'),
                        help='Dry run only. Dumps generated i2c command.')
args = parser.parse_args()
print(args)
pk = args.pem.read()

sk = jwt.jwk_from_pem(pk)

