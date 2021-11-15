import os
import xml.etree.ElementTree as ET

from dateutil.parser import parse


def bug_reports_preprocessing(bug_reports_base):

    dir_path = os.walk(bug_reports_base)
    for parent_dir, dir_name, file_names in dir_path:
        
        if file_names[0].split(".")[-1].strip() == "xml":
            
            all_root = ET.Element("bugrepository", {"name": parent_dir.split("/")[-1].strip()})
            for file_name in file_names:
                tree = ET.parse(os.path.join(parent_dir, file_name))
                root = tree.getroot()
                for child in root:
                    all_root.append(child)

            all_root[:] = sorted(all_root, key=lambda child: parse(child.get("fixdate"), ignoretz=True).isoformat())
            new_root =  ET.Element(all_root.tag, {"name": parent_dir.split("/")[-1].strip()})
            for i, child in enumerate(all_root):
                bug_attrib = child.attrib
                bug_attrib["id"] = child.get("id")
                bug_attrib["fixdate"] = str(parse(child.get("fixdate"), ignoretz=True))
                bug = ET.SubElement(new_root, "bug", bug_attrib)
                title = ET.SubElement(bug, "title")
                if child[0].text:
                    title.text = child[0].text
                description = ET.SubElement(bug, "description")
                if child[1].text:
                    description.text = child[1].text
                fixed_files = ET.SubElement(bug, "fixedfiles")
                for file_path in child[2].findall("file"):
                    files = ET.SubElement(fixed_files, "file")
                    files.text = file_path.text
            new_tree = ET.ElementTree(new_root)
            new_tree.write(os.path.join(bug_reports_base, "bugs.xml"), encoding="utf-8", xml_declaration=True)
                

if __name__ == "__main__":

    bias_1_mis = ["ambari", "solr", "spark"]
    bias_1_not_mis = ["ambari", "bigtop", "cassandra", "hbase", "hive", "solr", "spark", "sqoop", "tez", "zookeeper"]
    for proj in bias_1_mis:
        bug_reports_preprocessing(os.path.join("./Bias_1_misclassified", proj))
    for proj in bias_1_not_mis:
        bug_reports_preprocessing(os.path.join("./Bias_1_not_misclassified", proj))