'''
Author: guofeng
Date: 2021-04-22 14:54:22
LastEditTime: 2021-04-28 10:28:08
LastEditors: guofeng
Description: 
FilePath: /markdown-notes/giteePagesUpdate.py
symbol_custom_string_obkoro1: 
'''
# -*- coding: UTF-8 -*-

# from playwright import sync_playwright
from playwright.sync_api import sync_playwright
import time
USERNAME = '18730870725'
PASSWORD = 'GUOFENGliying862'
GITEE_PAGES_URL = 'https://gitee.com/gf530142771/markdown-notes/pages'


def main():
    with sync_playwright() as p:
        for browser_type in [p.chromium]:
            browser = browser_type.launch(headless=False)
            page = browser.new_page()
            page.goto('https://gitee.com/login')

            page.click('input[name="user[login]"]')
            page.fill('input[name="user[login]"]', USERNAME)
            page.click('input[name="user[login]"]')
            page.fill('input[name="user[password]"]', PASSWORD)
            page.click("input[value='登 录']")
            time.sleep(3)
            page.goto(GITEE_PAGES_URL)
            page.on("dialog", lambda dialog: dialog.accept())
            page.click(".update_deploy")
            page.wait_for_selector(
                'span:text("已开启 Gitee Pages 服务")', timeout=60 * 1000, state='visible')
            # page.goto('https://gitee.com/login')
            input('')
            # browser.close()


if __name__ == '__main__':
    main()
