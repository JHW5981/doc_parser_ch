import os
import pymupdf
from tqdm import tqdm

def pdf2imgs(pdf_path):
    # convert pdf to images
    # pdf_path: path to pdf file
    filename = os.path.basename(pdf_path).strip('.pdf')
    savename = f"{os.path.dirname(pdf_path)}/{filename}"
    os.makedirs(savename, exist_ok=True)
    doc = pymupdf.open(pdf_path)
    for page in doc:  # iterate through the pages
        pix = page.get_pixmap(dpi=70)  # render page to an image
        pix.save(f"{savename}/page-%i.png" % page.number)  # store image as a PNG

if __name__ == "__main__":
    pdf2imgs("/home/jihuawei/jhw2024spring/AceParser/pdf_parser_cn/样例/文字版PDF/空间数据分析教程(第二版)_王劲峰.pdf")