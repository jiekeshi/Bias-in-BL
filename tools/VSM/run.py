import os
import argparse
from src.vsm import vsm

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="A incremental bug localization tool")
    parser.add_argument("vsm_root", help = "root")
    parser.add_argument("bug_report_path", help="Bug report path")
    parser.add_argument("code_base_path", help="Codebase directory")
    parser.add_argument("-ft", "--file_type", nargs="+", help="Suffixes of files to be processed", default=["java", "py"])
    parser.add_argument("-sp", "--storage_path", nargs="?", help="storage intermediate file", default="")
    args = parser.parse_args()

    vsm_root = args.vsm_root
    bug_report_path = args.bug_report_path
    code_base_path = args.code_base_path
    file_type = args.file_type
    if args.storage_path == "":

        storage_path = os.path.join(vsm_root, ".vsm-data" + "/"+ code_base_path.split("/")[-1])
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)
    else:
        storage_path = args.storage_path
    vsm = vsm(bug_report_path, code_base_path, file_type, storage_path, vsm_root)
    vsm.localization()