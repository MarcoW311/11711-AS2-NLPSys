import os
import traceback
import argparse
import pandas as pd
from tqdm.auto import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


class ACLAnthologyCrawler(object):
    def __init__(self, chrome_driver_path="./chromedriver/chromedriver.exe", output_dir="./output"):
        self.chrome_driver_path = chrome_driver_path

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_experimental_option("prefs", {
            "download.default_directory": output_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True
        })
        self.web_driver = webdriver.Chrome(options=options)
        self.web_driver.implicitly_wait(10)

    def generate_url(self, event_name, year):
        if event_name == "acl":
            url = f"https://aclanthology.org/events/{event_name}-{year}/#{year}{event_name}-long"
        else:
            raise NotImplementedError(event_name)
        return url

    def crawling(self, event_name, year):
        try:
            conference_url = self.generate_url(event_name, year)
            print(conference_url)
            self.web_driver.get(conference_url)

            webelements_list = self.web_driver.find_elements(By.LINK_TEXT, "pdf")
            paper_list = []
            for webelement in webelements_list:
                paper_list.append(webelement.get_attribute("href"))
            paper_list = paper_list[2:]

            for paper_url in paper_list:
                self.web_driver.get(paper_url)
                time.sleep(10) # wait for the download to end
        except:
            traceback.print_exc()
        finally:
            self.web_driver.quit()

        return "Success"
    

def prepare_dir(dir_name):
    if not os.path.exists(dir_name): os.makedirs(dir_name)


if __name__ == '__main__':
    event_names = ["acl"]

    parser = argparse.ArgumentParser()

    parser.add_argument("--year", type=str, required=True,
                        help="year (yyyy)")
    parser.add_argument("--output_dir", type=str, default="./output",
                        help="path to output directory")
    parser.add_argument("--chrome_driver_path", type=str, default="./chromedriver/chromedriver.exe",
                        help="path to ChromeDriver")

    args = parser.parse_args()

    # create output dir if not exist
    prepare_dir(args.output_dir)

    for event_name in event_names:
        crawler = ACLAnthologyCrawler()
        ret = crawler.crawling(event_name=event_name, year=args.year)
