#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
import pandas as pd
import time

import identifyRandcode
import getValidAccount

class Cn_SignIn():
    """这个类模拟登录校园网
    """

    def __init__(self, username, password, current_ip):
        """ __init__

        :param username: 账号
        :param password: 密码
        :param randcode: 验证码
        :param current_ip: 本机当前ip，cmd//ipconfig查询，如10.19.170.01
        :param url: 登录网址，需要参数current_ip
        """

        self.username = username
        self.password = password
        self.randcode = 1000
        self.current_ip = current_ip
        self.url = ''



    def __main__(self):
        """__main__
        """

        # self.username = input("请输入学号：")
        # self.password = input("请输入密码：")

        self.randcode = 1000

        # self.current_ip = input("请输入当前IP地址：")
        self.url = "http://enet.10000.gd.cn:10001/login.jsp?wlanuserip=" \
                   + self.current_ip + "&wlanacip=61.145.225.11"

        # self.username = ''
        # self.password = ''
        # self.randcode = 1000
        # self.current_ip = ''
        # self.url = ''

        bool_sign_in = self.sign_in()
        return bool_sign_in




    def cut_picture(self,img1_path, img2_path):
        """
        剪裁图片

        :param img1_path: 需要剪裁图片路径
        :param img2_path: 剪裁后图片存放路径
        """

        # 选择验证码所在页面的像素边界
        left = int(800)
        top = int(225)
        right = int(885)
        bottom = int(255)

        # 通过Image剪裁图像
        im = Image.open(img1_path)
        im = im.crop((left, top, right, bottom))
        im.save(img2_path)



    def transfer_picture_format(self, img1_path, img2_path):
        """
        转换图片格式

        :param img1_path: 原png格式图片路径
        :param img2_path: 转换后jpg图片存放路径
        """

        # png转jpg
        img = Image.open(img1_path)
        bg = Image.new("RGB", img.size, (255, 255, 255))
        bg.paste(img, img)
        bg.save(img2_path)



    def sign_in(self):
        """通过webdriver模拟登入
        """

        # 打开webdriver
        driver = webdriver.Chrome()

        # 先打开校园网
        driver.get(self.url)

        # 再打开百度,保留窗口，并验证是否成功联网
        # driver.execute_script('window.open("https://www.baidu.com/")')

        # 获取整个校园网登入页面截图
        driver.get_screenshot_as_file('image/screenshot_PNG.png')

        # 以下代码执行前，需要该signIn.py同目录下，存在image文件夹
        # 剪裁图片
        self.cut_picture('image/screenshot_PNG.png', 'image/screenshot_randcode_PNG.png')

        # 转换图片格式
        self.transfer_picture_format("image/screenshot_randcode_PNG.png", "image/screenshot_randcode_JPG.jpg")

        # 识别图片，获取验证码
        self.randcode = identifyRandcode.identify_randcode('image/screenshot_randcode_JPG.jpg',
                                                      'image/screenshot_randcode_JPG_adjusted.jpg')[0:4]


        # 模拟填入账号，密码，验证码
        driver.find_elements_by_xpath('//*[@id="userName1"]')[0].send_keys(self.username)
        driver.find_elements_by_xpath('//*[@id="password1"]')[0].send_keys(self.password)
        driver.find_elements_by_xpath('//*[@id="rand"]')[0].send_keys(self.randcode)

        # 模拟点击登录
        driver.find_element_by_xpath('//*[@id="login1"]/table/tbody/tr/td/table[1]/tbody/tr[4]/td[2]/img').click()

        time.sleep(1)

        # 判断是否登录成功
        if driver.current_url == 'http://enet.10000.gd.cn:10001/success.jsp':
            print(self.username + '登录成功')

        else:
            driver.close()
            print(self.username + '登录失败')
            return 'login failure'



        # # 关闭窗口
        # driver.close()

        return driver



    def sign_out(self,driver):

        if type(driver) == type("aa"):
            return

        # 模拟点击下线
        driver.find_element_by_xpath('//*[@id="logout"]').click()

        # # 回车确定
        # driver.find_element_by_id('kw').send_keys(Keys.ENTER)

        # 处理弹窗确定
        alert = driver.switch_to_alert()
        time.sleep(1)   # 一定要等待
        print(alert.text)  # 打印警告对话框内容
        alert.accept()

        time.sleep(1)

        # 判断是否下线成功
        if driver.current_url == 'http://enet.10000.gd.cn:10001/logoutsuccess.jsp':
            print(self.username + '下线成功')
            driver.close()
        else:
            print(self.username + '下线失败')
            driver.close()
        return "end"




"""
测试多个ip
@1和@2需设置设置参数
"""
if __name__ == '__main__':
    start = time.clock()
    valid_data_test = getValidAccount.valid_data
    result = pd.DataFrame(data=[])
    print(len(valid_data_test))
	## @1----下面两个i：控制测试范围
    i = 550
    # while i < len(valid_data_test):
    while i < 600:
        print(i)
        signIn = Cn_SignIn(valid_data_test[0][i], valid_data_test[2][i][-8:], '10.19.188.60')
        bool_sign_in = signIn.__main__()
        if bool_sign_in == 'login failure':
            i = i + 1
            continue
        else:
            is_sign_out = signIn.sign_out(bool_sign_in)
            temp = [valid_data_test[0][i], valid_data_test[2][i]]
            # 忽视索引连接
            result = result.append([temp], ignore_index=True)
        time.sleep(2)
        i = i + 1
    print(result)
	## @2----下面两个i：控制测试范围，文件命名
    # list保存至csv，命名
    result.to_csv('result_550_600.csv', encoding='gbk')
    close = time.clock()
    print(close - start)


"""
main
"""
if __name__ == '__main__':
    signIn = Cn_SignIn()
    bool_sign_in = signIn.__main__()
    
    end = bool_sign_in.signOut()
    print(end)
    