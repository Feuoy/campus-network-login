# campus-network-login

中国电信校园网模拟登录，python + selenium

## 环境安装

### Anaconda3

- 如果pip install失败
- 可以尝试修改anaconda权限，Anaconda3目录//属性/安全/编辑
- [Anaconda3（Python 3.7 version）](https://www.anaconda.com/distribution/)

### Tesseract

- 只需下载包，不需安装
- 将Tesseract-OCR/tessdata，复制到Aanaconda3/
- 替换模型，Aanaconda3/tessdata/eng.traineddata -> 该本项目根目录下的eng.traineddata
- [Tesseract（(MAYBE)tesseract-ocr-w64-setup-v4.1.0-bibtag19）](https://digi.bib.uni-mannheim.de/tesseract/)

### Tesserocr

- [Tesserocr（tesserocr-2.4.0-cp37-cp37m-win_amd64.whl）](https://github.com/simonflueckiger/tesserocr-windows_build/releases/)

### webdriver
- webdriver需要对应chrome版本，版本查询 http://npm.taobao.org/mirrors/chromedriver/ 
- chromedriver.exe放到anaconda3/，与python.exe同目录
- [webdriver（LATEST_RELEASE_74.0.3729）](http://chromedriver.storage.googleapis.com/index.html)

### PIL，selenium，etc.

- pip install package
- 如果import失败，可能需要最新版

## cmd本地连接

```bash
# 断开
ipconfig/release
# 开启
ipconfig/renew
```

