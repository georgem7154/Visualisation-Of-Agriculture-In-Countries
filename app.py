import streamlit as st
import plotly.express as px
from process import clean_data

data = clean_data()

st.set_page_config(layout='wide')
st.title('Agriculture Analysis')


with st.sidebar:
    with st.expander('Select Country'):
        country = data['Country'].unique()
        selected_country = st.selectbox(options=country, index=None, label='')


if selected_country is not None:
    st.write(f'This dashboard displays the Agriculture data for {selected_country}.')

    current_country = data[data['Country'] == selected_country]
    indiagroup = current_country.groupby('Year')['Economic_Impact_Million_USD'].sum().reset_index()
    Country = selected_country
    topic = f'Economic Impact Made By {Country} Over The Years'
    fig1 = px.line(indiagroup, x='Year', y=['Economic_Impact_Million_USD'], color_discrete_sequence=['green'],
                   title=topic)
    max_value = indiagroup['Economic_Impact_Million_USD'].max()
    min_value = indiagroup['Economic_Impact_Million_USD'].min()
    year_min = indiagroup['Year'][
        indiagroup['Economic_Impact_Million_USD'] == indiagroup['Economic_Impact_Million_USD'].min()]
    min = year_min.values[0]
    year_max = indiagroup['Year'][
        indiagroup['Economic_Impact_Million_USD'] == indiagroup['Economic_Impact_Million_USD'].max()]
    max = year_max.values[0]
    fig1.add_annotation(x=indiagroup['Year'].iloc[indiagroup['Economic_Impact_Million_USD'].idxmax()],
                        y=max_value,
                        text=f'Max: {max_value:.2f}, year = {max}',
                        showarrow=True,
                        arrowhead=1)

    fig1.add_annotation(x=indiagroup['Year'].iloc[indiagroup['Economic_Impact_Million_USD'].idxmin()],
                        y=min_value,
                        text=f'Min: {min_value:.2f}, year = {min}',
                        showarrow=True, ax=150,
                        arrowhead=1)
    st.plotly_chart(fig1)

    crops_group = current_country.groupby('Crop_Type')['Crop_Yield_MT_per_HA'].sum().reset_index()
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'yellow', 'pink', 'brown', 'gray', 'cyan']
    fig2 = px.bar(crops_group, x="Crop_Type", y="Crop_Yield_MT_per_HA", color="Crop_Type",
                  color_discrete_sequence=colors, title="Total yeild of the crops from 1990 to 2024(Bar Chart)")
    st.plotly_chart(fig2)

    colors = ['red', 'blue', 'green', 'orange', 'purple', 'yellow', 'pink', 'brown', 'gray', 'cyan']
    fig3 = px.pie(crops_group, names="Crop_Type", values="Crop_Yield_MT_per_HA", color_discrete_sequence=colors,
                  title="Total yeild of the crops from 1990 to 2024(Pie Chart)")
    st.plotly_chart(fig3)

    sugarcane_revenue = current_country[current_country['Crop_Type'] == 'Sugarcane']
    fig4 = px.scatter(sugarcane_revenue, x="Crop_Yield_MT_per_HA", y="Economic_Impact_Million_USD",
                      title="How Yield affects Revenue")
    st.plotly_chart(fig4)

    fertiliser_usage = current_country.groupby('Year')[
        ['Fertilizer_Use_KG_per_HA', 'Pesticide_Use_KG_per_HA', 'Soil_Health_Index']].sum().reset_index()
    fig5 = px.line(fertiliser_usage, x='Year',
                   y=['Fertilizer_Use_KG_per_HA', 'Pesticide_Use_KG_per_HA', 'Soil_Health_Index'],
                   color_discrete_sequence=['blue', 'red', 'pink'],
                   title='Fertiliser and Pesticide Use In The Country And How It Affects Soil Health')
    st.plotly_chart(fig5)

    fertiliser_usage = current_country.groupby('Year')[['Average_Temperature_C', 'CO2_Emissions_MT']].sum().reset_index()
    fig6 = px.line(fertiliser_usage, x='Year', y=['Average_Temperature_C', 'CO2_Emissions_MT'],
                   color_discrete_sequence=['red', 'green'],
                   title='Correlation Between Average Temperature and co2 Emmision in the Country')
    st.plotly_chart(fig6)

else:
   st.write("Select a city to check data")


