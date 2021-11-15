import os
import json
import xml.etree.ElementTree as ET
from dateutil.parser import parse
from src.text_processor import text_processor

def bug_reader(bug_report_path, code_base_path, file_type, storage_path):

    bug_data = {}

    tree = ET.parse(bug_report_path)
    root = tree.getroot()
   
    for child in root:

        # get contents
        if child[1].text:
            bug_content = text_processor(child[0].text + child[1].text)
        else:
            bug_content = text_processor(child[0].text)
        
        # get fixed files
        fixed_files = []
        for file_path in child[2].findall("file"):
            if file_path.text:
                if file_path.text.split(".")[-1].strip() in file_type:
                    fixed_files.append(os.path.join(code_base_path, file_path.text))

        # get fix date
        fix_date = parse(child.get("fixdate"), ignoretz=True).isoformat()
        bug_data[child.get("id")] = {"content": bug_content, "fixed_files": fixed_files, "fixdate": fix_date}

    return bug_data