import argparse
from PIL import Image

def resize_image(input_path, output_path, target_width, target_height):
    try:
        # 打开输入图像
        image = Image.open(input_path)

        # 调整图像大小
        resized_image = image.resize((target_width, target_height), Image.ANTIALIAS)

        # 保存调整后的图像
        resized_image.save(output_path)

        print("图像已成功调整大小并保存到", output_path)
    except Exception as e:
        print("出现错误：", e)


def main():
    parser = argparse.ArgumentParser(description="调整图像大小")
    parser.add_argument("--i", help="输入图像路径", required=True)
    parser.add_argument("--o", help="输出图像路径", required=True)
    parser.add_argument("--w", type=int, help="目标宽度", required=True)
    parser.add_argument("--h", type=int, help="目标高度", required=True)

    args = parser.parse_args()

    resize_image(args.i, args.o, args.w, args.h)


if __name__ == "__main__":
    main()