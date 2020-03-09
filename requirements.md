# Anaconda3

* 若后续不可pip install package
* 尝试修改anaconda权限，目录Anaconda3//属性/安全/编辑

[Anaconda3（Python 3.7 version）](https://www.anaconda.com/distribution/)






# Tesseract

* （可不安装）
* 语言包可选，选择默认
* 安装的tesseract，生成了Tesseract-OCR文件夹
* 将Tesseract-OCR/tessdata复制到Aanaconda3/
* 这个word同目录下有eng.traineddata语言库
* 将这个语言库替换Aanaconda3/tessdata/eng.traineddata

[Tesseract（(MAYBE)tesseract-ocr-w64-setup-v4.1.0-bibtag19）](https://digi.bib.uni-mannheim.de/tesseract/)






# Tesserocr

* untitled.whl文件放到anaconda3文件下
* anaconda prompt 命令 pip install untitled.whl
* 若找不到文件使用绝对路径

[Tesserocr（tesserocr-2.4.0-cp37-cp37m-win_amd64.whl）](https://github.com/simonflueckiger/tesserocr-windows_build/releases/)






# webdriver

* webdriver需要对应chrome，版本查询 http://npm.taobao.org/mirrors/chromedriver/ 
* chromedriver.exe放到anaconda3/，与python.exe同目录

[webdriver（LATEST_RELEASE_74.0.3729）](http://chromedriver.storage.googleapis.com/index.html)






# PIL，selenium，etc.

* pip install package
* 若不可import，一般要需要最新版，先pip uninstall package再pip install package


