import argparse
import os
import re

subtitle_postfix = {'.ass'}
sorted_postfix = []

video_postfix = ['.mkv', '.mp4']

re_pattern = r'\[\d+\]'

def find_subtitle(filename):
    for postfix in sorted_postfix:
        if filename.endswith(postfix):
            return postfix 
    return None

def find_video(filename):
    for postfix in video_postfix:
        if filename.endswith(postfix):
            return postfix
    return None

def parse_videos(dir):
    os.chdir(dir)

    files = os.listdir(dir)
    for file in files:
        subtitle_postfix = find_subtitle(file)
        video_postfix = find_video(file)
        if subtitle_postfix == None and video_postfix == None:
            continue

        result = re.findall(re_pattern, file)
        if len(result) <= 0:
            continue
        
        name = re.findall(r'\d+', result[0])
        if len(name) <= 0:
            continue

        keyname = name[0]
        postfix = ""
        if subtitle_postfix != None:
            print("analyse, keyname=" + keyname + " postfix=" + subtitle_postfix + " raw=" + file)
            postfix = subtitle_postfix
        elif video_postfix != None:
            print("analyse, keyname=" + keyname + " postfix=" + video_postfix+ " raw=" + file)
            postfix = video_postfix
        else:
            continue

        print("=> " + keyname + postfix)
        src = os.path.join(dir, file)
        dst = os.path.join(dir, keyname + postfix)
        os.rename(src, dst)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some inputs.')
    parser.add_argument('--dir', required=True)
    parser.add_argument('--pattern', required=False)
    parser.add_argument('--subtitle', required=False, nargs='+')
    args = parser.parse_args()

    user_define_subtitle = args.subtitle
    if user_define_subtitle is not None:
        subtitle_postfix.update(user_define_subtitle)

    sorted_postfix = sorted(list(subtitle_postfix), key=lambda postfix:len(postfix), reverse=True)
    # print(sorted_postfix)

    if args.pattern is not None:
        re_pattern = args.pattern

    print(re_pattern)

    parse_videos(args.dir)
