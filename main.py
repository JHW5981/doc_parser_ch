from parse_pdf import parse_pdf
import argparse
from tqdm import tqdm
import glob
import os

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf_path", type=str, default="/home/jihuawei/jhw2024spring/AceParser/pdf_parser_cn/样例")
    return parser.parse_args()

def main():
    args = get_args()
    pdf_files = glob.glob(os.path.join(args.pdf_path, '**', '*.pdf'), recursive=True)
    print("PDFs to be parsed:")
    print("\n".join(pdf_files))
    for pdf_path in tqdm(pdf_files):
        parse_pdf(pdf_path)
        print(f"{pdf_path} 解析完成")

if __name__ == "__main__":
    main()
        