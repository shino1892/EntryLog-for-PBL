from __future__ import print_function

import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from felica import get_felica_idm

if __name__ == '__main__':
    idm = get_felica_idm()
    print("IDm", idm)