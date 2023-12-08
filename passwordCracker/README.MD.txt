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
-if a hash is used, it's encryption (--encryption) type MUST be specified

examples:
./main.py --password N7ss --bruteforce True
./main.py --password James --dictionary True --bruteforce True
./main.py --password James --encryption sha256 --dictionary True
./main.py --hash '5f4dcc3b5aa765d61d8327deb882cf99' --encryption bcrypt --dictionary True --passwordlength 8 --lowercase True
./main.py --passwordlength 4 --uppercase True --lowercase True --numbers True --symbols True --bruteforce True

DEPENDENCIES:
python
hashlib
bcrypt
argparse

Limitations:
- The program takes a long time to solve passwords of 6+ characters (especially when multiple character types are used)
- A bcrypt hash encrypted with many rounds will take a full second to decipher, making passwords of all lengths take much longer to solve
- Cannot be applied to any files
- Only with md5, bcrypt, and sha-256

Things that could be improved in the future
- Improve my algorithm so that it takes less time, maybe through the use of others' libraries
- Have cleaner display settings, and add an argument to turn off every password test
- Add more types of hashes.
