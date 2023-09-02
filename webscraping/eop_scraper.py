from bs4 import BeautifulSoup
from webscraping_class import Webscraping
from inputs import eop_primary_url
from typing import List, Tuple
import re

def get_all_sat_hrefs(eo_portal_url: str) -> List[str]:
    """
    Input:
        eo_portal_url: URL of the EO Portal.
    Purpose:
        Retrieve all satellite hrefs from the EO Portal URL.
    Returns:
        List of strings containing satellite hrefs.
    """
    eo_soup = Webscraping.get_soup(eo_portal_url)
    all_href_bodies = eo_soup.body.find_all("div", {"class": "css-1k0d5em"})
    all_hrefs = []
    
    for body in all_href_bodies:
        all_hrefs.extend([eop_primary_url + li.a["href"] for li in body.find_all("li")])
    
    return all_hrefs


def _gather_aux_information_from_soup_(sat_soup: BeautifulSoup) -> Tuple[List[str], List[int]]:
    """
    Input:
        sat_soup: BeautifulSoup object representing a satellite page.
    Purpose: 
        Gather auxiliary information from BeautifulSoup object of a satellite page.
    Returns:
        A tuple containing:
        - List of strings: All text content from h2 and p elements.
        - List of integers: Indices where h2 elements are found within the list.
    """
    h2s = [elem.text for elem in sat_soup.find_all("h2") if elem.text != "" and elem.text != "FAQ"]
    all_h2_p_elems = [elem.text for elem in sat_soup.findAll(re.compile(r'(h2|p)')) if elem.text != '']
    all_h2_splits = [all_h2_p_elems.index(h2) for h2 in h2s]

    return all_h2_p_elems, all_h2_splits


def get_metadata(chapter: str, satellite_name: str, satellite_url: str) -> dict:
    """
    Input:
        chapter: Chapter or section name.
        satellite_name: Name of the satellite.
        satellite_url: URL of the satellite page.
    Purpose: 
        Create metadata dictionary for satellite information.
    Returns:
        Dictionary containing the metadata.
    """
    metadata = {
        "chapter": chapter,
        "satellite_name": satellite_name,
        "satellite_url": satellite_url
    }
    return metadata


def get_information_from_page(satellite_url: str) -> List[dict]:
    """
    Input:
        satellite_url: URL of the satellite page.
    Purpose: 
        Extract and organise information from a satellite page.
    Returns:
        List of dictionaries, each containing extracted page content and metadata.
    """
    sat_soup = Webscraping.get_soup(satellite_url)
    
    satellite_name = sat_soup.title.text
    all_h2_p_elems, all_h2_splits = _gather_aux_information_from_soup_(sat_soup)
    result_list = []

    for i in range(len(all_h2_splits) - 1):
        start_index = all_h2_splits[i] + 1
        end_index = all_h2_splits[i + 1]

        page_content = '. '.join(all_h2_p_elems[start_index:end_index])
        
        chapter = all_h2_p_elems[all_h2_splits[i]]
        metadata = get_metadata(chapter, satellite_name, satellite_url)

        result_list.append(Webscraping.create_json(page_content, metadata))

    return result_list


def wrapper_get_all_eop_satellites(eo_portal_url: str) -> List[dict]:

    """
    Input:
        eo_portal_url: URL of the EO Portal.
    Purpose: 
        Wrapper function to retrieve information from all EO Portal satellite pages.
    Returns:
        List of dictionaries containing page content and metadata from all satellite pages.
    """
    
    result_list = []
    all_hrefs = get_all_sat_hrefs(eo_portal_url)
    all_hrefs.remove("https://www.eoportal.org/satellite-missions/gcp-reccap-2")
    
    for href in all_hrefs:
        result_list.extend(get_information_from_page(href))
    
    return result_list