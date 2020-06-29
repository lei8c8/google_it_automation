import os
os.environ.get("HOME", "")

import subprocess

result = subprocess.run(["ls", "this_file_does_not_exist.txt"])
print(result.returncode)

# leichen@Leis-MBP google_it_automation % python3
# Python 3.7.3 (default, Apr 24 2020, 18:51:23) 
# [Clang 11.0.3 (clang-1103.0.32.62)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import subprocess
# >>> result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
# >>> print(result.returncode)
# 0
# >>> print(result.stdout)
# b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'
# >>> print(result.stdout.decode().split())
# ['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']