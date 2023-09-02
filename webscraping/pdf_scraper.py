from PyPDF2 import PdfReader, PdfWriter
import re
from pathlib import Path
from webscraping_class import Webscraping
from typing import List

class Scrape_pdf:

    def open_pdf(path: Path) -> PdfReader:
        """
        Input:
            path: The path to the PDF file which should be prepared.
        Purpose:
            Open a PDF file and return the PdfReader object. This allows a page-wise editing.
        Returns:
            The PdfReader object for the opened PDF file.
        """
        opened_pdf = open(path, 'rb')
        pdf_reader = PdfReader(opened_pdf)
        return pdf_reader
    
    def discard_introduction(doc: PdfReader, start_pg_no: int, last_pg_no: int) -> PdfReader:
        """
        Input:
            doc: The PdfReader object representing the PDF.
            start_pg_no: The page number before which should be discarded.
            last_pg_no: The page number until which should be discarded.
        Purpose:
            Discard the first and last couple of pages (table of contents, preface, references, ...) from the pdf file. 
        Returns:
            The shortened PdfReader object with selected pages.
        """

        pdf = doc.pages[start_pg_no:last_pg_no]

        shortened_pdf = PdfWriter()
        for page in pdf:
            shortened_pdf.add_page(page)

        return shortened_pdf
    
    def convert_to_text(pdf: PdfReader) -> List[str]:
        """
        Input:
            pdf: The PdfReader object representing the PDF.
        Purpose:
            Convert PdfReader to a list of strings.
        Returns:
            A list containing the extracted text from each page.
        """
        all_text = []
        for page in pdf.pages:
            all_text.append(page.extract_text())
        
        return all_text

    def clean_pdf(pdf_texts: List[str], pattern: str) -> List[str]:
        """
        Input:
            pdf_texts: A list containing the text content of each page.
            pattern: The pattern to be removed from each page.
        Purpose:
            Clean the text content of PDF pages by removing specific patterns.
        Returns:
            A list containing the cleaned text content of each page.
        """

        # Delete occurrences of --, ~
        cleaned_1 = [re.sub("(--+(~| -)*)*", "", page) for page in pdf_texts]

        # delete recurring pattern (header / footers)
        cleaned_2 = [re.sub(pattern, "", page) for page in cleaned_1]

        return cleaned_2
    
    
    def get_chapter_metadata(pdf: List[str], chapter_pattern: str) -> List[List[str]]:
         """
        Input:
            pdf_texts: A list containing the text content of each page.
            chapter_pattern: The pattern to identify chapters in the text.
        Purpose:
            Extract chapter metadata from the text content of PDF pages.
        Returns:
            Each chapter metadata [Chapter Number, Chapter Title].
        """
         # get a list of the chapter names, found using the chapter pattern
         chapter_names = [item for sublist in [re.findall(chapter_pattern, page) for page in pdf] for item in sublist]
         # clean the list for spaces and new lines
         cleaned_chapter_names = [re.sub("\n\s|\n+|\s\s+$", "", chapter_name) for chapter_name in chapter_names]
         # divide into a list of lists, where the first element is the chapter number (if exists), the latter the chapter name.
         metadata = [
            [chap_text for chap_text in re.split(r"C[hb]apter\s?(\d+)|(\d+)", chapter_name, 1) if chap_text != "" and chap_text is not None]
            if re.findall(r"\d", chapter_name) 
            else ["", chapter_name] for chapter_name in cleaned_chapter_names
         ]
         return metadata
    

    def turn_to_txt(pdf_texts: List[str]) -> str:
        """
        Input:
            pdf_texts: A list containing the text content of each page.
        Purpose:
            Convert a list of text content from PDF pages into a single string. This allows for 
        Returns:
            The concatenated text content as a single string.
        """
        text = "".join(pdf_texts)
        return text
    
    def gather_page_content_and_metadata(pdf: List[str], chapter_pattern: str, source = "SMAD") -> List[dict]:
        """
        Input:
            pdf: A list containing the cleaned text content of each page.
            chapter_pattern: The pattern to identify chapters in the text.
            source: The source of the content (default is "SMAD").
        Purpose:
                Gather page content and metadata from the text content of PDF pages.
        Returns:
            A list of dictionaries containing page content and metadata. Return format is the standardised format.
        """
        pdf_text = Scrape_pdf.turn_to_txt(pdf)

        page_content = re.split(chapter_pattern, pdf_text)[1:]

        metadata = Scrape_pdf.get_chapter_metadata(pdf, chapter_pattern)

        all_chapters = []
        for i in range(len(metadata)):
            all_chapters.append(Webscraping.create_json(page_content[i], {"source": source, "Chapter": metadata[i][0], "Chapter Title": metadata[i][1]}))

        return all_chapters
    
    def wrapper_transform_pdf(path: Path, header_pattern: str, chapter_pattern: str, source: str, start_from: int = None, end_at: int = None) -> dict:
        """
        Input:
            path: The path to the original SMAD file.
            start_from: The page number to start extracting data from.
            end_at: The page number to end extracting data at.
            header_pattern: The pattern to be removed from each page header.
            chapter_pattern: The pattern to identify chapters in the text.
        Purpose:
            Wrap the process to get all pdf data from a PDF file and turn it into tangiable dictionary.
        Returns:
            A list of dictionaries containing SMAD data.
        """
        opened_pdf = Scrape_pdf.open_pdf(path = path)

        if start_from is not None:
            opened_pdf = Scrape_pdf.discard_introduction(doc = opened_pdf, start_pg_no = start_from, last_pg_no = end_at)
        
        pdf_list = Scrape_pdf.convert_to_text(pdf = opened_pdf)
        cleaned_list = Scrape_pdf.clean_pdf(pdf_texts = pdf_list, pattern = header_pattern)

        final_dict = Scrape_pdf.gather_page_content_and_metadata(pdf = cleaned_list, chapter_pattern = chapter_pattern, source = source)

        return final_dict