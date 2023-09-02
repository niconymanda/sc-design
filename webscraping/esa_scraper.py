from bs4 import BeautifulSoup
from webscraping_class import Webscraping
import re
from typing import List

def get_all_esa_mission_hrefs(soup: BeautifulSoup) -> List[str]:
    """
    Input:
        soup: The BeautifulSoup object representing the HTML content.
    Purpose:
        Extracts the mission hrefs from the provided BeautifulSoup object. Note: this is tailored to the ESA page.
    Returns:
        list: A list of hrefs for all the mission names.
    """
    all_table_elements = soup.body.find("div", {"class": "clearfix journal-content-article"}).table.find_all("td")
    all_hrefs = list(set([elem.a["href"] for elem in all_table_elements[1:19]]))
    # Adding the base-url for all of the found urls
    all_mission_urls = list(map(lambda x: "https://www.cosmos.esa.int"+x, all_hrefs))
    
    return all_mission_urls


def get_mission_metadata(mission_name: str, mission_url: str, source: str) -> dict:
    """
    Input:
        mission_name: The name of the mission.
        mission_url: The URL of the mission.
        source: The source of the metadata (e.g., "Mission Main Page").
    Purpose:
        Create and return a metadata dictionary for a mission.
    Returns:
        metadata: A dictionary containing the mission metadata.
    """
    metadata = {
        "mission_name": mission_name,
        "mission_url": mission_url,
        "source": source
    }
    return metadata


def get_mission_dict_from_mainpage(mission_soup: BeautifulSoup, mission_url: str, final_mission_information: List) -> List[dict]:
    """
    Input:
        mission_soup: The BeautifulSoup object of the mission's main page.
        mission_url: URL of the mission's main page.
        final_mission_information: List containing the thus far collected mission information.
    Purpose:
        Extracts mission information from the main page of the mission and adds it to the final mission information list.
    Returns:
        Updated final mission information list.
    """
    mission_name = mission_soup.h1.text
    metadata = get_mission_metadata(mission_name, mission_url, "Mission Main Page")
    page_content = "\n".join([text_elem.text for text_elem in mission_soup.find_all("p")])
    mission_dict = Webscraping.create_json(page_content = page_content, metadata = metadata)
    final_mission_information.append(mission_dict)
    
    return final_mission_information


def get_mission_dict_from_catalogue(mission_soup: BeautifulSoup, final_mission_information: List) -> List[dict]:
    """
    Input:
        mission_soup: The BeautifulSoup object of the mission's main page.
        final_mission_information: List containing final mission information.
    Purpose:
        Extracts mission information from the mission's catalogue links and adds it to the final mission information list.
    Returns:
        Updated final mission information list.
    """
    mission_name = mission_soup.h1.text
    catalogue_urls = [url["href"] for url in mission_soup.find_all("a") if "Catalog" in url.text]
    
    if catalogue_urls:
        
        for url in catalogue_urls:
            mission_text = re.sub("\s\s+|--+|==+|\|\|+", "", Webscraping.get_soup(url).text)
            metadata = get_mission_metadata(mission_name, url, "Mission Catalogue")
            mission_dict = Webscraping.create_json(page_content = mission_text, metadata = metadata)
            final_mission_information.append(mission_dict)
    
    return final_mission_information


def get_mission_dict(mission_url: str, final_mission_information: List) -> List[dict]:
    """
    Input:
        mission_url: URL of the mission's main page.
        final_mission_information: List containing final mission information.
    Purpose:
        Acts as a wrapper to collect all mission information for one mission.
    Returns:
        Updated final mission information list.
    """
    mission_soup = Webscraping.get_soup(mission_url).body.find("div", {"id": "mission-header"})
    fmi = get_mission_dict_from_mainpage(mission_soup, mission_url, final_mission_information)
    fmi = get_mission_dict_from_catalogue(mission_soup, fmi)
    
    return fmi


def get_instrument_metadata(mission_name: str, instrument_url: str, submission_name: str, instrument_name: str, source: str) -> dict:
    """
    Input:
        mission_name: The name of the mission.
        instrument_url: The URL of the instrument.
        submission_name: The name of the submission.
        instrument_name: The name of the instrument.
        source: The source of the metadata (e.g., "Mission Main Page", "Instrument Catalogue").
    Purpose:
        Create and return a metadata dictionary for an instrument.
    Returns:
        metadata: A dictionary containing the mission metadata.
    """
    metadata = {
        "mission_name": mission_name,
        "instrument_url": instrument_url,
        "submission_name": submission_name,
        "instrument_name": instrument_name,
        "source": source
    }
    return metadata


def get_instrument_dict_from_mainpage(mission_name: str, instrument_url: str, submission_name: str, instrument_name: str, p_elements: List[BeautifulSoup], final_mission_information: List[dict]) -> List[dict]:
    """
    Input:
        mission_name: Name of the mission.
        instrument_url: URL of the instrument.
        submission_name: Name of the submission.
        instrument_name: Name of the instrument.
        p_elements: List of <p> elements containing instrument information.
        final_mission_information: List of mission information dictionaries.
    Purpose:
        Extracts instrument information from the main page.
    Returns:
        Updated list of mission information dictionaries.
    """
    metadata = get_instrument_metadata(mission_name, instrument_url, submission_name, instrument_name, source = "Mission Main Page")
    instrument_text = "".join([p.text for p in p_elements])
    instrument_dict = Webscraping.create_json(page_content = instrument_text, metadata = metadata)
    final_mission_information.append(instrument_dict)

    return final_mission_information


def get_instrument_dict_from_catalogue(mission_name: str, instrument_url: str, submission_name: str, instrument_name: str, catalogue_url: str, final_mission_information: List[dict]) -> List[dict]:
    """
    Input:
        mission_name: Name of the mission.
        instrument_url: URL of the instrument.
        submission_name: Name of the submission.
        instrument_name: Name of the instrument.
        catalogue_url: URL of the instrument catalogue.
        final_mission_information: List of mission information dictionaries.
    Purpose:
        Extracts instrument information from the instrument catalogue.
    Returns:
        Updated list of mission information dictionaries.
    """
    metadata = get_instrument_metadata(mission_name, instrument_url, submission_name, instrument_name, source = "Instrument Catalogue")
    instrument_text = re.sub("\s\s+|--+|==+|\|\|+", "", Webscraping.get_soup(catalogue_url).text)
    instrument_dict = Webscraping.create_json(page_content = instrument_text, metadata = metadata)
    final_mission_information.append(instrument_dict)

    return final_mission_information


def get_instrument_dict(mission_url: str, final_mission_information: List)-> List[dict]:
    """
    Input:
        mission_url: URL of the mission.
        final_mission_information: List of mission information dictionaries.
    Purpose:
        Extracts instrument information from a mission URL.
    Returns:
        Updated list of mission information dictionaries.
    """
    mission_soup = Webscraping.get_soup(mission_url)
    mission_name = mission_soup.h1.text
    all_instrument_tables = mission_soup.body.find("div", {"id": "column-2"}).find("div", {"class": "portlet-body"}).find_all("table")
    
    for table_elem in all_instrument_tables:
        submission_name = table_elem.find_previous_sibling("h2").text

        for instr in table_elem.find_all("div", {"class": "instrument-box"}):
            if instr.find("div", {"class": "instr-name"}):
                instr_name = instr.find("div", {"class": "instr-name"}).text + " (" + instr.find("h3").text + ")"
            else: 
                instr_name = instr.find("h3").text
            fmi = get_instrument_dict_from_mainpage(mission_name, mission_url, submission_name, instr_name, instr.find_all("p"), final_mission_information)
            
            for cat in instr.find_all("li", {"class": "cat"}):
                try:
                    instrument_url = cat.a["href"]
                    fmi = get_instrument_dict_from_catalogue(mission_name, instrument_url, submission_name, instr_name, cat.a["href"], fmi)
                except: pass
    return fmi


def wrapper_get_all_esa_missions(soup: BeautifulSoup) -> List[dict]:
    """
    Input:
        soup: BeautifulSoup object representing the web page with ESA mission information.
    Purpose:
        Extracts mission and instrument information for all ESA missions from a given BeautifulSoup object.
    Returns:
        List of dictionaries containing mission and instrument information.
    """
    final_mission_information = []
    all_mission_hrefs = get_all_esa_mission_hrefs(soup)
    
    for mission_href in all_mission_hrefs:
        final_mission_information.extend(get_mission_dict(mission_href, final_mission_information))
        final_mission_information.extend(get_instrument_dict(mission_href, final_mission_information))
    
    return final_mission_information
