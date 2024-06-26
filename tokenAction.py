import os
import argparse
import sys
import jwt

parser = argparse.ArgumentParser(description='')
parser.add_argument('pem', type=argparse.FileType('r'),
                        help='Dry run only. Dumps generated i2c command.', default=sys.stdin)
args = parser.parse_args()
pk = args.pem.read()
sk = jwt.jwk_from_pem(str.encode(pk))
print("token=%s" % sk)
