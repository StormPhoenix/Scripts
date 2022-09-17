import argparse
import hashlib

def encrypt(file, encryption):
    algorithm = hashlib.sha256()
    if encryption == 'md5':
        algorithm = hashlib.md5()
        print('using encryption: md5')
    elif encryption == 'sha1':
        algorithm = hashlib.sha1()
        print('using encryption: sha1')
    else:
        print('using encryption: sha256')

    sha256sum = ''
    with open(file, 'rb') as fr:
        algorithm.update(fr.read())
        sha256sum = algorithm.hexdigest()

    return sha256sum
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some inputs.')
    parser.add_argument('--file', type=str, required=True)
    parser.add_argument('--encryption', type=str, default='sha256', help='encryption algorithm')
    args = parser.parse_args()

    print('Result: {0}'.format(encrypt(args.file, args.encryption)))
