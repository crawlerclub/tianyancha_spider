# -*- coding:utf-8 -*-
import os

__author__ = 'zhaojm'

from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from config import implicitly_wait


def new_webdriver(proxy_type, proxy_ip, proxy_port):
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    )
    service_args = [
        '--proxy=%s:%s' % (proxy_ip, proxy_port),
        '--proxy-type=%s' % proxy_type,
    ]
    driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=service_args)
    # driver = webdriver.PhantomJS(desired_capabilities=dcap)

    #driver = webdriver.Chrome(chromedriver)
    #driver = webdriver.Firefox()

    driver.implicitly_wait(implicitly_wait)  # seconds

    driver.maximize_window()  # 窗口最大化, 这一步很重要,否则响应式网页,有部分菜单自动隐藏,访问不到
    return driver
