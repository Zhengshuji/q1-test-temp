"""tools/hygiene/backup_before_edit.py

Copy a file to trash/ (timestamped) before it is overwritten.
Usage: python tools/hygiene/backup_before_edit.py <path> [...]
"""
import os
import shutil
import sys
import time


def main(paths):
    os.makedirs('trash', exist_ok=True)
    for p in paths:
        if not os.path.exists(p):
            print('skip (missing):', p)
            continue
        base = os.path.basename(p)
        stamp = time.strftime('%Y%m%d_%H%M%S')
        dst = os.path.join('trash', base + '.' + stamp + '.bak')
        shutil.copy2(p, dst)
        print('backed up', p, '->', dst)
    print('')
    print('Reminder: register the backup in trash/README.md if the file is replaced.')


if __name__ == '__main__':
    main(sys.argv[1:])