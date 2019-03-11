import logging
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse


class SeleniumMiddleware():
    def __init__(self, timeout=None, service_args=[]):
        self.logger = logging.getLogger(__name__)
        self.timeout = timeout
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.PhantomJS(service_args=service_args)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close()

    def process_request(self, request, spider):
        self.logger.debug('PhantomJS is Starting')
        try:
           self.browser.get(request.url)
           return None
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)
