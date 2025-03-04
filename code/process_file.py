'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''
import streamlit as st
import json
import sys
import os

# Ensure the correct import path
sys.path.append(os.path.abspath("code"))

from packaging import parse_package  

st.title("Process Package File")

uploaded_file = st.file_uploader("Upload a package data file", type=["txt"])

if uploaded_file is not None:
    try:
        packages = []
        for line in uploaded_file:
            line = line.decode("utf-8").strip()  # Convert bytes to string
            if line:
                package_info = parse_package(line)
                packages.append(package_info)

        # Display parsed data
        st.json(packages)

        # Write to JSON file
        output_file = "parsed_packages.json"
        with open(output_file, "w") as f:
            json.dump(packages, f, indent=4)

        st.success(f"Processed {len(packages)} packages. Data saved to {output_file}.")

    except Exception as e:
        st.error(f"Error processing file: {e}")