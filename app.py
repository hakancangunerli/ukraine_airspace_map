import streamlit as st
import pandas as pd
from visualize import visualize
from api_call import api_call
st.set_page_config(layout="wide")

#AREA EXTENT COORDINATE WGS4


# '''
# lon_min = 21.654 # left side of ukraine
# lat_min = 47.493888  # left side of ukraine
# lon_max = 39.924722 # right side of ukraine
# lat_max = 49.170  # right side of ukraine

# '''

st.write('''
# Flight map @hakancangunerli
#### __*Uses OpenSky REST API to get data from the server and visualize it using Plotly Express*__
''')


region = st.selectbox('Select region:',
                      ['world', 'europe', 'asia', 'africa', 'north america'], key='<selectbox1a>')


def measurement():
    lat_min = st.text_input(
        "Enter the area extent coordinate latitude min ", None, key='<lat_min>')
    lat_max = st.text_input(
        "Enter the area extent coordinate latitude max", None, key='<lat_max>')
    lon_min = st.text_input(
        "Enter the area extent coordinate longitude min ", None, key='<lon_min>')
    lon_max = st.text_input(
        "Enter the area extent coordinate longitude max", None, key='<lon_max>')
    return lat_min, lat_max, lon_min, lon_max


lat_min, lon_min, lon_max, lat_max = measurement()


try:
    response = api_call(lat_min, lon_min, lat_max, lon_max)


#LOAD TO PANDAS DATAFRAME
    col_name = ['icao24', 'callsign', 'origin_country',
            'time_position', 'last_contact', 'long', 'lat', 'x', 'on_ground']


    flight_df = pd.DataFrame(response['states'])
    flight_df = flight_df.iloc[:, 0:len(col_name)]
    flight_df.columns = col_name
    flight_df = flight_df.fillna('No Data')  # replace NAN with No Data
    flight_df = flight_df.drop(columns=['x'])


    fig = visualize(flight_df, region)

    st.plotly_chart(fig)

except:
    if lat_max == None or lon_max == None or lat_min == None or lon_min == None:
        st.error('Please enter all the coordinates')
