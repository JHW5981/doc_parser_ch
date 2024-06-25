import cv2
from paddleocr import PaddleOCR
import os
from pdf2imgs import pdf2imgs
import argparse
from tqdm import tqdm
import shutil

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf_name", type=str, default="/home/jihuawei/jhw2024spring/AceParser/pdf_parser_cn/样例/文字版PDF/现代地图学_廖克.pdf")
    return parser.parse_args()

def parse_pdf(pdf_name):
    ocr_model = PaddleOCR(use_angle_cls=True, lang="ch", show_log=False)     
    pdf2imgs(pdf_name) # convert pdf to images
    txt = ""
    img_names = os.listdir(pdf_name.strip('.pdf'))      
        
    for img_name in tqdm(img_names):
        img_path = os.path.join(pdf_name.strip('.pdf'), img_name)
        image = cv2.imread(img_path)
        image = image[..., ::-1]  
        try:
            results = ocr_model.ocr(image)
            txt_ = ""
            for i in range(len(results[0])):
                txt_ += results[0][i][-1][0].strip() + "\n"
            txt += txt_
            txt += "\n\n"
        except:
            pass
        with open(f"{pdf_name.split('.')[0]}.txt", "a", encoding="utf-8") as f:
            f.write(txt_ + "\n\n")
    shutil.rmtree(pdf_name.strip('.pdf'))
    return txt

if __name__ == "__main__":
    args = get_args()
    pdf_name = args.pdf_name
    txt = parse_pdf(pdf_name)
    print(txt)  

