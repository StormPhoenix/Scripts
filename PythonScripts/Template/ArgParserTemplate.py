import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some inputs.')
    ## example
    ## parser.add_argument('--file')
    args = parser.parse_args()
