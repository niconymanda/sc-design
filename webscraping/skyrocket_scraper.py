from bs4 import BeautifulSoup
from urllib.request import urlopen
from webscraping_class import Webscraping
from typing import List

def get_all_hrefs(href: str, find_id: List, primary_url: str) -> List[str]:
    """
    Input:
        href: the website href, whose hrefs need to be found
        find_id: the element within the body, where the href is located. List of one entry.
            finding missions:  ["table", {"id": "satflist"}]
            finding platforms: ["table", {"class": "index"}]
        primary_url: the url which lies to basis of any of the pages belonging to the site.
    Purpose:
        Find all the hrefs on a given page.
    Returns:
        A list of all hrefs.
    """
    html = urlopen(href)
    soup = BeautifulSoup(html, "html.parser")
    all_hrefs = [
        href.get("href").replace('..', primary_url) 
        for href in soup.body.find(find_id[0]).find_all("a", href=True) 
        if href.get("href")[0:8] == "../doc_s"
    ]
    return(all_hrefs)


def get_page_content(data_to_scrape: BeautifulSoup) -> str:
    """
    Input:
        data_to_scrape: BeautifulSoup object containing mission HTML.
    Purpose:
        Extracts the mission description from a BeautifulSoup object representing a mission page.
    Returns:
        Extracted mission description.
    """
    if data_to_scrape.body.find("div", {"id": "satdescription"}):
        mission_desc = " \n ".join([m_descr.text for m_descr in data_to_scrape.body.find("div", {"id": "satdescription"}).find_all("p")[1:]])
    else: 
        mission_desc = ""
    
    return mission_desc

def get_metadata(data_to_scrape: BeautifulSoup, mission_url: str) -> dict:
    """
    Input:
        data_to_scrape: BeautifulSoup object containing mission HTML.
        mission_url: URL of the current mission.
    Purpose:
        Extracts metadata from a mission page and compiles it into a dictionary.  
    Returns:
        Metadata dictionary including mission details.
    """
    data_dict = {}
    mission_name = data_to_scrape.body.h1.text
    data_dict["mission_name"] = mission_name
    data_dict["mission_url"] = mission_url

    try:    
        for row in data_to_scrape.body.find("table", {"id": "satdata"}).find_all("tr"):
            key = row.th.text
            value = row.td.text
            data_dict[key] = value
    except: pass

    return data_dict


def scrape_data(data_to_scrape: BeautifulSoup, mission_url: str) -> dict:
    """
    Input: 
        data_to_scrape: BeautifulSoup object, which contains the Mission HTML to scrape
        mission_url: the url of the current mission
    Purpose:
        Scrape the data from BeautifulSoup object and create a json from it
    Returns:
        json containing the page content as well the metadata from the webpage.
    """
    page_content = get_page_content(data_to_scrape)
    metadata = get_metadata(data_to_scrape, mission_url)
    scraped_data = Webscraping.create_json(page_content, metadata)

    return scraped_data


def wrapper_get_mission_hrefs(platforms: List[str], primary_url: str) -> List[str]:
    """
    Input:
        platforms: list of URLs of platforms containing mission links.
        primary_url: the url which lies to basis of any of the pages belonging to the site.
    Purpose:
        Collects all mission URLs from a list of platform URLs.
    Returns:
        List of mission URLs extracted from the provided platforms.
    """
    missions = []
    
    for platform in platforms:
        mission = get_all_hrefs(href = platform, find_id = ["table", {"id": "satflist"}], primary_url = primary_url)
        missions.extend(mission)
    missions = list(set(missions))
    
    return missions


def wrapper_get_all_skyrocket_missions(primary_url: str, platform_url: str) -> List[dict]:
    """
    Input:
        primary_url: the url which lies to basis of any of the pages belonging to the site.
        platform_url: URL of the platform.
    Purpose:
        Collects scraped data for multiple missions from a given platform URL.
    Returns:
        List of dictionaries containing scraped data for each mission.
    """
    final_mission_information = []
    platforms = list(set(get_all_hrefs(href = platform_url, find_id = ["table", {"class": "index"}], primary_url = primary_url)))
    missions = wrapper_get_mission_hrefs(platforms, primary_url)
    
    for mission in missions:
        data_to_scrape = Webscraping.get_soup(mission)
        scraped_data = scrape_data(data_to_scrape, mission)
        final_mission_information.append(scraped_data)
    
    return final_mission_information