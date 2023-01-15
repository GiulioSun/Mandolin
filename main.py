import streamlit as st

from data import Fineco, Pop
from viz.metric import Metric


# Function for set date list

option_menu = ['Economia e finanza', 'Popolazione', 'Trasporti', 'Agricoltura', 'Industria', 'Energia', 'Tecnologia']

if __name__ == '__main__':

    # Dash header
    st.title('''
    Mandolin data
    ''')

    choice = st.sidebar.selectbox('Menu', option_menu)

    if choice == 'Economia e finanza':
        tab1, tab2 = st.tabs(['Metriche', 'Andamenti'])

        with tab1:
            start_year, end_year = Metric.start_end_year(10)
            gdp, delta_gdp = Fineco.gdp(start_year, end_year, 4)
            gdp_capita, delta_capita = Fineco.gdp(start_year, end_year, 4)
            Metric.metric(end_year, gdp, delta_gdp, label='PIL', label_value='€', label_delta='%')
            Metric.metric(end_year, gdp_capita, delta_capita, label='PIL pro capite', label_value='€', label_delta='%')

        with tab2:
            pass
    elif choice == 'Popolazione':
        tab1, tab2 = st.tabs(['Metriche', 'Andamenti'])

        with tab1:
            start_year, end_year = Metric.start_end_year(10)
            pop, delta_pop = Pop.pop(start_year, end_year, 4)
            Metric.metric(end_year, pop, delta_pop, label='Popolazione', label_delta='%')



        with tab2:
            pass
