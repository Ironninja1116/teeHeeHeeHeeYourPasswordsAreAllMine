ARGUMENTS
--password [string]
--hash [string]
--passwordlength [int]
--uppercase [boolean]
--lowercase [boolean]
--numbers [boolean]
--symbols [boolean]
--encryption [string] options: 'md5', 'bcrypt', and 'sha256'
--dictionary [boolean]
--bruteforce [boolean]

All arguments are technically optional, but some are required in a few cases:
-if a hash (--hash) or nothing is used instead of a password (--password), the password's length (--passwordlength) must be specified; also, you must include --uppercase, --lowercase, --symbols, and/or --numbers if they show up in the password. If you aren't sure what types of characters are in the password, use all 4 of the arguments.
-A dictionary attack (--dictionary) and/or a brute force attack (--bruteforce) must be used

examples:
./main.py --password N7ss --bruteforce True
./main.py --password James --dictionary True --bruteforce True
./main.py --password James --encryption sha256 --dictionary True
./main.py --hash 5f4dcc3b5aa765d61d8327deb882cf99 --encryption md5 --dictionary True --passwordlength 8 --lowercase True
./main.py --passwordlength 4 --uppercase True --lowercase True --numbers True --symbols True --dictionary True --bruteforce True


DEPENDENCIES:
python
hashlib
bcrypt
argparse


