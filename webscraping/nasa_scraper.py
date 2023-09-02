from webscraping_class import Webscraping
from bs4 import BeautifulSoup
import requests


from typing import List, Tuple, Dict

def get_all_nasa_mission_hrefs(soup: BeautifulSoup) -> List[str]:
    """
    Input:
        soup: The BeautifulSoup object representing the HTML content.
    Purpose:
        Extracts the mission hrefs from the provided BeautifulSoup object. Note: this is tailored to the Nasa page.
    Returns:
        list: A list of hrefs for all the mission names.
    """
    mission_name = []
    all_links_to_scour = []
    
    for row in soup.body.find_all('table')[2].find_all('tr')[1:]:
    # Collapse all data such that we only search through the first if the mission name is already in predefined list
        tmp_mission_name = row.find_all("td")[-2].text.replace("\n", "")

        # The cassini mission doesnt contain any mission information. 
        if tmp_mission_name not in mission_name and tmp_mission_name != 'CASSINI-HUYGENS MISSION TO SATURN AND TITAN' and tmp_mission_name != 'N/A':
            all_links_to_scour.append(row.a['href'])
            mission_name.append(tmp_mission_name)
    
    return(all_links_to_scour)


def get_all_instrument_hrefs(soup: BeautifulSoup) -> List[str]:
    """
    Input:
        soup: The BeautifulSoup object representing the HTML content.
        mission: The name of the mission to retrieve href links for.
    Purpose:
        Retrieves all href links for a specific mission from the provided BeautifulSoup object.
    Returns:
        A list of href links to be scoured.
    """
    instr_mission_name = []
    all_links_to_scour = []
    
    for row in soup.body.find_all('table')[2].find_all('tr')[1:]:
    # Collapse all data such that we only search through the first if the mission name is already in predefined list
        tmp_instr_mission_name = row.find_all("td")[-2].text.replace("\n", "")+row.find_all("td")[-1].text.replace("\n", "")
    
        if tmp_instr_mission_name not in instr_mission_name and tmp_instr_mission_name != 'N/A':
            all_links_to_scour.append(row.a['href'])
            instr_mission_name.append(tmp_instr_mission_name)
    
    return(all_links_to_scour)


def find_tab_elem(soup: BeautifulSoup, row_name: str) -> List[BeautifulSoup]:
    """
    Input:
        soup: The BeautifulSoup object representing the HTML content.
        row_name: The name of the row to search for.
    Purpose:
        Finds table elements in the provided BeautifulSoup object that match the specified row name.
    Returns:
        A list of BeautifulSoup objects representing the matching table elements.
    """
    ls = [name for name in soup.body.find_all("table")[1].find_all("tr") if name.find("td").text == row_name]
    return ls


def get_mission_information(soup: BeautifulSoup) -> Tuple[str, str, str]:
    """
    Input:
        soup: The BeautifulSoup object representing the HTML content of the mission page.
    Purpose:
        Retrieves mission information from the provided BeautifulSoup object.
    Returns:
        A tuple containing the mission name, mission description, and mission objectives.
    """
    mission_name = find_tab_elem(soup, "MISSION_NAME")[0].find_all("td")[1].text.replace("\n", "").lstrip()
    mission_desc = find_tab_elem(soup, "MISSION_DESCRIPTION")[0].find("tt").text
    mission_obj = find_tab_elem(soup, "MISSION_OBJECTIVES_SUMMARY")[0].find("tt").text
    return mission_name, mission_desc, mission_obj


def get_instr_information(soup: BeautifulSoup) -> Tuple[str, str]:
    """
    Input:
        soup: The BeautifulSoup object representing the HTML content of the instrument page.
    Purpose:
        Retrieves instrument information from the provided BeautifulSoup object.
    Returns:
        A tuple containing the instrument name and instrument description.
    """
    instr_name = find_tab_elem(soup, "INSTRUMENT_NAME")[0].find_all("td")[1].text.replace("\n", "").replace("\t", "").lstrip()
    instr_desc = find_tab_elem(soup, "INSTRUMENT_DESC")[0].find("tt").text
    return instr_name, instr_desc


def scrape_all_mission_info(all_missions: List) -> List:
    """
    Input:
        all_missions: A list of mission URLs.
    Purpose:
        Scrapes mission information from a list of mission URLs and creates a formatted JSON representation for each mission.
    Returns:
        A list of dictionaries, where each dictionary represents the mission information in a formatted JSON structure.

    """
    all_mission_information = []

    for mission in all_missions:
        intermediate_mission_soup = BeautifulSoup(requests.get(mission).text, 'html.parser')
        
        # Find the mission information of this mission 
        mission_descr_url = 'https://pds.nasa.gov'+[tab_elem for tab_elem in intermediate_mission_soup.body.find_all("tr") if tab_elem.find("td").text == "Mission Information"][0].a['href'].replace(" ", "%20")
        mission_soup = BeautifulSoup(requests.get(mission_descr_url).text, 'html.parser')
        mission_name, mission_desc, mission_obj = get_mission_information(mission_soup)

        final_format = Webscraping.create_json(f"{mission_desc} \n {mission_obj}", {"mission_name": mission_name, "mission_url": mission_descr_url})

        all_mission_information.append(final_format)
    
    return all_mission_information


def scrape_all_instruments_info(all_instruments: List) -> List:
    """
    Input:
        all_instruments: A list of instrument URLs.
    Purpose:
        Scrapes instrument information from a list of instrument URLs and creates a formatted JSON representation for each instrument.
    Output:
        A list of dictionaries, where each dictionary represents the instrument information in a formatted JSON structure.
    """
    all_instrument_information = []

    for instrument in all_instruments:

        intermediate_instr_soup = BeautifulSoup(requests.get(instrument).text, 'html.parser')
        mission_name = find_tab_elem(intermediate_instr_soup, "Mission Information")[0].find_all("td")[1].text.replace("\n", "").lstrip()

        try:

            instrument_desc_url = 'https://pds.nasa.gov'+[tab_elem for tab_elem in intermediate_instr_soup.body.find_all("tr") if tab_elem.find("td").text == "Instrument Information"][0].a['href'].replace(" ", "%20")
            instrument_soup = BeautifulSoup(requests.get(instrument_desc_url).text, 'html.parser')
            instr_name, instr_desc = get_instr_information(instrument_soup)

            final_format = Webscraping.create_json(instr_desc, {"mission_name": mission_name, "instrument_name": instr_name, "instrument_url": instrument_desc_url})

            all_instrument_information.append(final_format)

        except: pass
    
    return all_instrument_information


def wrapper_get_all_nasa_missions(soup: BeautifulSoup) -> List[dict]:
    """
    Input:
        soup: The BeautifulSoup object, derived from the nasa page
    Purpose:
        Wrapper function, which retrieves all NASA information about missions and their corresponding instruments.
    Returns:
        A list of dictionaries representing the mission and instrument information. Each dictionary contains the following information: 
        page_content (mission descriptions, instrument descriptions), metadata (data about the missions)
    """
    all_missions = get_all_nasa_mission_hrefs(soup)
    print("found all missions hrefs")
    all_instruments = get_all_instrument_hrefs(soup)
    print("found all instruments hrefs")

    all_mission_info = scrape_all_mission_info(all_missions)
    print("done1")
    all_instrument_info = scrape_all_instruments_info(all_instruments)

    print("done2")
    final_mission_information = all_mission_info+all_instrument_info

    return final_mission_information