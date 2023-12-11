Python and bcrypt MUST be installed before using

Steps to use
1: Download the zip file or pull the git database
2: unzip the file if necessary
3: In the terminal, cd into the repository and navigate to the passwordCracker folder
4: From the passwordCracker folder, run commands as listed bwlow

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

As all arguments are optional rather than positional, they may be placed in ANY order

examples:
python3 main.py --password N7ss --bruteforce True
python3 main.py --password James --dictionary True --bruteforce True
python3 main.py --dictionary True --bruteforce True --password James
python3 main.py --hash '5f4dcc3b5aa765d61d8327deb882cf99' --encryption bcrypt --dictionary True --passwordlength 8 --lowercase True
python3 main.py --hash '5f4dcc3b5aa765d61d8327deb882cf99' --encryption bcrypt --dictionary True --passwordlength 8 --lowercase True --uppercase True --bruteforce True
python3 main.py --passwordlength 4 --uppercase True --lowercase True --numbers True --symbols True --bruteforce True

Limitations:
- The program takes a long time to solve passwords of 6+ characters (especially when multiple character types are used)
- A bcrypt hash encrypted with many rounds will take a full second to decipher, making bcrypt passwords of all lengths take much longer to solve
- Cannot be applied to any files
- Only with md5, bcrypt, and sha-256

Things that could be improved in the future:
- Improve my algorithm so that it takes less time, maybe through the use of others' libraries
- Add an argument that allows users to choose whether every password check is printed or not
- Make output look cleaner
- Add more types of hashes.
