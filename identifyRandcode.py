#coding:utf-8

import tesserocr
from PIL import Image


def adjust_randcodeImage(original_path, adjusted_path):
    """
    调整截取的验证码图片，利于后续识别

    :param original_path: 原始图片路径
    :param adjusted_path: 调整后图片路径
    """

    img = Image.open(original_path)
    # print(img.mode)

    # convert mode，P -> RGB
    if img.mode == "P":
        img = img.convert('RGB')
    # print(img.mode)

    # 读取原始图片size
    # 定义标准width
    # 根据标准width计算height
    (x, y) = img.size
    x_s = int(76)
    y_s = int(y * x_s / x)

    # 调整原始图片size
    img_ = img.resize((x_s, y_s), Image.ANTIALIAS)
    img_.save(adjusted_path)



def get_randcodeImage(img_path):
    """
    通过Image获取图片文件

    :param img_path: 调整过的验证码图片路径
    :return: Image图片文件
    """

    img = Image.open(img_path)
    return img



def image_grayscale_deal(img):
    """
    图片转灰度处理

    :param img: 图片文件
    :return: 转灰度处理后的图片文件
    """

    img = img.convert('L')
    # image.show()
    return img



def image_thresholding_method(img):
    """
    图片二值化处理

    :param img: 转灰度处理后的图片文件
    :return: 二值化处理后的图片文件
    """

    # 阈值，控制二值化程度，不能超过256
    threshold = 160
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    # 图片二值化，此处第二个参数为数字一
    img = img.point(table, '1')
    # image.show()
    return img



def captcha_tesserocr_crack(img):
    """
    图像识别

    :param img: 二值化处理后的图片文件
    :return: 识别结果
    """

    # 通过tesserocr，使用语言库eng识别，第二个参数缺省eng
    randcode = tesserocr.image_to_text(img, "eng")
    return randcode



def identify_randcode(original_path, adjusted_path):
    """
    这个类的主调函数，
    输入预先调整过的验证码图片地址，返回验证码

    :param original_path: 原始图片路径
    :param adjusted_path: 调整后图片路径

    :return: 验证码识别结果
    """

    # 调整截取的验证码图片
    adjust_randcodeImage(original_path, adjusted_path)

    # 图像获取
    img = get_randcodeImage(adjusted_path)

    # 图像转灰度处理
    img1 = image_grayscale_deal(img)

    # 图片二值化处理
    img2 = image_thresholding_method(img1)

    #  图像识别
    randcode = captcha_tesserocr_crack(img2)
    print(randcode)

    return randcode
