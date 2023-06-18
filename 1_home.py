import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report



def setup_page():
    """Set up the Streamlit page with custom configuration."""

    # Configure Streamlit page settings
    st.set_page_config(
        page_title='Significant Cyber Incidents - CSIS',
        layout="wide",
        # page_icon="AI"
    )

def customize_css():
    """Customize CSS for the Streamlit page."""
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: visible;}
                footer {visibility: hidden;
                }
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

setup_page()
customize_css()

st.title('Significant Cyber Incidents - CSIS')
st.warning("Experiment to convert [Significant Cyber Incidents](https://www.csis.org/programs/strategic-technologies-program/significant-cyber-incidents) data from CSIS into parsable format. Likely not perfect")

# Load the file as a dataframe
df = pd.read_csv('parsed_incidents.csv')
# Remove the index column from the csv for better visualization
del df[df.columns[0]]

# The csv had some inconsistency with NaN and Unknown. Make it consistent
df = df.fillna('Unknown')

# Print the dataframe
st.dataframe(df, hide_index=True)

# Print the profile report - https://pypi.org/project/streamlit-pandas-profiling/
pr = df.profile_report()
st_profile_report(pr)