'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''
import streamlit as st
import json
import sys
import os

# Ensure Python can find 'code' module
sys.path.append(os.path.abspath("code"))

from packaging import parse_package  

st.title("Process Multiple Package Files")

# Initialize session state if not already done
if "file_count" not in st.session_state:
    st.session_state.file_count = 0
if "line_count" not in st.session_state:
    st.session_state.line_count = 0

uploaded_files = st.file_uploader("Upload multiple package data files", type=["txt"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        try:
            packages = []
            line_count = 0
            for line in file:
                line = line.decode("utf-8").strip()  # Convert bytes to string
                if line:
                    package_info = parse_package(line)
                    packages.append(package_info)
                    line_count += 1

            # Write to JSON file
            output_file = f"{file.name}.json"
            with open(output_file, "w") as f:
                json.dump(packages, f, indent=4)

            # Update session state
            st.session_state.file_count += 1
            st.session_state.line_count += line_count

            st.success(f"Processed {len(packages)} packages. Data saved to {output_file}.")

        except Exception as e:
            st.error(f"Error processing file {file.name}: {e}")

# Display summary of all files processed
st.write(f"**Total Files Processed:** {st.session_state.file_count}")
st.write(f"**Total Lines Processed:** {st.session_state.line_count}")