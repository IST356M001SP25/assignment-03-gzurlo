'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''
import streamlit as st
import sys
import os

# Ensure Python can find the 'code' directory
sys.path.append(os.path.abspath("code"))

# Import the function from the correct module
from packaging import parse_package, calc_total_units  

st.title("Package Data Parser")

# Input for package data
package_input = st.text_input("Enter package data:")

if package_input:
    try:
        package_info = parse_package(package_input)  # Parsing the package string
        st.json(package_info)  # Display parsed data

        # Calculate and display total package size
        total_size = calc_total_units(package_info)  # Calculate total size
        st.write(f"**Total Package Size:** {total_size} units")

    except Exception as e:
        st.error(f"Error parsing package: {e}")