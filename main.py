import pandas as pd
import streamlit as st
import eurostat

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
        start_year, end_year, list_year = Metric.start_and_year(25)
        tab1, tab2, tab3 = st.tabs(['PIL', 'PIL Pro capite', 'PIL e Popolazione'])

        with tab1:
            gdp, delta_gdp = Fineco.gdp(start_year, end_year, 25)
            Metric.metric(end_year, gdp, delta_gdp, label='PIL', label_value='€', label_delta='%')
            df_gdp = pd.DataFrame({'PIL in €': gdp, 'Anno': list_year})
            st.text('')
            st.header('Andamento del PIL')
            st.area_chart(df_gdp, x='Anno', y='PIL in €')

        with tab2:
            gdp_capita, delta_capita = Fineco.gdpcapita(start_year, end_year, 25)
            Metric.metric(end_year, gdp_capita, delta_capita, label='PIL pro capite', label_value='€', label_delta='%')
            df_gdp_capita = pd.DataFrame({'PIL pro capite in €': gdp_capita, 'Anno': list_year})
            st.text('')
            st.header('Andamento del PIL pro capite')
            st.area_chart(df_gdp_capita, x='Anno', y='PIL pro capite in €')

        with tab3:
            country_list = eurostat.get_par_values('DEMO_GIND', 'geo')
            st.multiselect(
                'Seleziona i paesi',
                country_list
            )


    elif choice == 'Popolazione':
        start_year, end_year, list_year = Metric.start_and_year(10)
        tab1, tab2 = st.tabs(['Popolazione', 'Distribuzione per sesso'])

        with tab1:
            pop, delta_pop = Pop.pop(start_year, end_year, 10)
            Metric.metric(end_year, pop, delta_pop, label='Popolazione', label_delta='%')
            df_pop = pd.DataFrame({'Popolazione': pop, 'Anno': list_year})
            st.text('')
            st.header('Andamento della popolazione')
            st.area_chart(df_pop, x='Anno', y='Popolazione')

        with tab2:
            pop_m, delta_pop_m = Pop.pop(start_year, end_year, 10, sex='M')
            pop_f, delta_pop_f = Pop.pop(start_year, end_year, 10, sex='F')
            df_pop = pd.DataFrame({'Maschi': pop_m, 'Femmine': pop_f, 'Anno': list_year})
            st.text('')
            st.header('Andamento della popolazione')
            st.bar_chart(df_pop, x='Anno')
