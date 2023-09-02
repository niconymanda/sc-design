from bs4 import BeautifulSoup
from urllib.request import urlopen
from collections import OrderedDict
from urllib.error import URLError, HTTPError
from typing import List
from pathlib import Path
import json
from inputs import parent_folder

class Webscraping:

    def __init__(self, url):
        self.url = url

    def get_soup(url) -> BeautifulSoup:
        """
        Input:
            url: The URL of the webpage to retrieve.
        Purpose:
            Retrieves the HTML content from the specified URL and returns a BeautifulSoup object.
        Returns:
            soup: A BeautifulSoup object representing the parsed HTML content.
        Raises:
            URLError: If there is an error in accessing the URL or retrieving the HTML content.
            HTTPError: If the server returns an HTTP error code.
        """
        try:
            html = urlopen(url)
            soup = BeautifulSoup(html, "html.parser")
            return soup
        except (URLError, HTTPError) as e:
            raise e
        
    
    def create_json(page_content: str, metadata: dict) -> dict:
        """
        Input:
            page_content: string of the content (main content we might want to reutn) description 
            metadata: a dictionary of the data describing the content
        Purpose:
            Turn variables into json format
        Output:
            dictionary of the given mission information
        """
        json = {
            "page_content" : page_content,
            "metadata" : metadata
        }
        return json
    
    def get_unique_dictionaries(lst: List[dict]) -> List[dict]:
        """
        Input:
            lst: The input list of dictionaries.
        Purpose:
            Retrieves a list of unique dictionaries from the input list.
        Returns:
            unique_dicts: A list of unique dictionaries, where each dictionary has unique values.
        """
        unique_set = set(frozenset(d.items()) for d in lst)
        unique_dicts = [dict(item) for item in unique_set]
        return unique_dicts
    
    def save_json(file_name: str, dict_to_save: List[dict]):
        """
        Input:
            file_name: The name of the output file (without extension).
            dict_to_save: The list of dictionaries of the pdf file to save as a JSON.
        Purpose:
            Save a list of dictionaries (i.e. the scraped data) as JSON data to a file.
        """
        json_object = json.dumps(dict_to_save)
        with open(Path("D:\TUM\sc_design") / f"{file_name}.json", "w") as outfile:
        # with open(parent_folder / "webscraping" / "Scraper_files" / f"{file_name}.json", "w") as outfile:
            outfile.write(json_object)