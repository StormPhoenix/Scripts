import argparse
import exifread

def ReadImgExif(file):
    tags = None
    with open(file, 'rb') as fr:
        tags = exifread.process_file(fr, details=True) 
    return tags


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some inputs.')
    parser.add_argument('--file', type=str, required=True)
    args = parser.parse_args()

    print(ReadImgExif(args.file))
