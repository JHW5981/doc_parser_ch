# 环境配置
## 下面是我的环境
- CUDA Version: 11.6
- python3.8 
- torch2.2.1+cu121
- paddlepaddle-gpu==2.3.2
- paddleocr==2.7.3

上面几个是必备的包，其他包在requirements.txt里面。

如果是你自己的环境的话，配置流程如下：

1. 创建一个新的conda环境，python版本建议选择3.8
2. 根据你的cuda版本选择合适的[pytorch](https://pytorch.org/)，注意pytorch的高版本是兼容低版本的cuda的，从上面我的环境可以看出来，我的CUDA VERSION是11.6，而我的pytorch的cuda是121的。
3. 安装paddlepallde，这个库非常难适配，版本必须卡上，卡上了有时候还不行，还得降低版本，比如我的CUDA VERSION是11.6，那我的paddlepaddle-gpu的版本就必须是11.6的，否则会报各种各样莫名其妙的错误。。。具体的可以去[这里](https://www.paddlepaddle.org.cn/install/old?docurl=/documentation/docs/zh/install/pip/linux-pip.html#old-version-anchor-20-%E7%8E%AF%E5%A2%83%E6%94%AF%E6%8C%81)找，类似于下面这条命令，post116指的是对应的cuda版本，不要用最新的版本，2.5的版本能跑通，但是跑不出来结果。


`python -m pip install paddlepaddle-gpu==2.3.2.post116 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html`

4. 安装paddleocr

`pip install paddleocr`

5. 检验是否安装成功

```
python
import paddle
paddle.__version__
import paddleocr
```

6. 上面的都ok了就可以跑了

-------------------------
其中运行`main.py`函数就可以了。直接把包含pdf的文件路径给它，它会自己找到pdf文件，然后解析。

```
python main.py --pdf_name /home/jihuawei/jhw2024spring/AceParser/pdf_parser_cn/样例
```
