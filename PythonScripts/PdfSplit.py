import argparse
from PyPDF2 import PdfReader, PdfWriter
import os

def split_pdf(input_path, output_path, start_page, end_page):
    """
    拆分PDF文件，提取指定页数范围并保存为新文件
    :param input_path: 输入PDF文件路径
    :param output_path: 输出PDF文件路径
    :param start_page: 起始页码(从1开始)
    :param end_page: 结束页码
    """
    try:
        # 读取PDF文件
        reader = PdfReader(input_path)
        total_pages = len(reader.pages)
        
        # 验证页码范围
        if start_page < 1 or start_page > total_pages:
            raise ValueError(f"起始页码必须在1到{total_pages}之间")
        if end_page < start_page or end_page > total_pages:
            raise ValueError(f"结束页码必须在{start_page}到{total_pages}之间")
        
        # 创建PDF写入器
        writer = PdfWriter()
        
        # 添加指定页数范围
        for page_num in range(start_page - 1, end_page):
            writer.add_page(reader.pages[page_num])
        
        # 保存新PDF文件
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        
        print(f"成功保存: {output_path} (第{start_page}页到第{end_page}页)")
        return True
    
    except Exception as e:
        print(f"处理PDF时出错: {e}")
        return False

def main():
    # 创建参数解析器
    parser = argparse.ArgumentParser(description='PDF拆分工具 - 提取指定页数范围并保存为新PDF')
    
    # 添加必需参数
    parser.add_argument('--input', help='输入的PDF文件路径', required=True)
    parser.add_argument('--start', type=int, help='起始页码(从1开始)', required=True)
    parser.add_argument('--end', type=int, help='结束页码', required=True)
    
    # 添加可选参数
    parser.add_argument('--output', help='输出PDF文件路径(默认: 输入文件名_页码范围.pdf)')
    
    # 解析参数
    args = parser.parse_args()
    
    # 处理输出文件名
    if args.output:
        output_path = args.output
    else:
        # 自动生成输出文件名: 原文件名_起始页-结束页.pdf
        base_name = os.path.splitext(os.path.basename(args.input))[0]
        output_path = f"{base_name}_p{args.start}-{args.end}.pdf"

    print('output: ' + output_path)

    # 调用拆分函数
    success = split_pdf(args.input, output_path, args.start, args.end)
    
    if not success:
        exit(1)

if __name__ == "__main__":
    main()