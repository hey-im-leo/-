from selenium import webdriver
import time
#执行登录

browser = webdriver.Chrome()#注意这里的Chrome驱动要和你的电脑上浏览器的版本一致，否则会报错
browser.maximize_window()
browser.get("http://wfw.tjut.edu.cn/orange/app/grmrjktzyd/index.html#/jrtb")#这是健康填报的网址
username  = "123456"# 你的学号
password = "*******" #你的登录密码
browser.implicitly_wait(10)
elem=browser.find_element_by_name("username")
elem.send_keys(username)
elem=browser.find_element_by_id("password")
elem.click()
elem.send_keys(password)
elem=browser.find_element_by_class_name("auth_login_btn")
elem.click()

#跳转到健康填报网页了
elem = browser.find_element_by_class_name("copy")
elem.click()
browser.implicitly_wait(10)
elems = browser.find_elements_by_class_name("van-uploader__input")
elems[0].send_keys(r"C:\jktb\健康码.jpg")#这里是你的健康码截图路径
elems[1].send_keys(r"C:\jktb\行程码.jpg")#这里是行程码截图路径
time.sleep(3)
button = browser.find_element_by_class_name("mobile-button").find_elements_by_class_name("van-button")
button[0].click()