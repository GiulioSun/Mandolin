import datetime

import streamlit as st


class Metric:

    @staticmethod
    def start_end_year(n_years):
        # set end year
        end_year = datetime.date.today().year
        # set start year
        start_year = end_year - n_years
        # list of selected years
        years = [year for year in range(start_year, end_year)]
        # set graphics object for select year
        col_date1, col_data2 = st.columns(2)
        end_year_input = col_date1.selectbox("Seleziona l'anno", years)
        # set start and end years select
        if end_year_input != end_year:
            end_year = end_year_input
        start_year = end_year - n_years
        return start_year, end_year

    @staticmethod
    def metric(end_year, value_list, delta_list, label, label_value='', label_delta=''):
        # DataViz PIL
        col1, col2, col3 = st.columns(3)

        col1.metric(
            label=f'{label} {str(end_year)}',
            value=f'{str(value_list[0])} {label_value}',
            delta=f'{str(delta_list[0])} {label_delta}',
        )

        col2.metric(
            label=label + ' ' + str(end_year - 1),
            value=str(value_list[1]) + ' €',
            delta=str(delta_list[1]) + ' %',
        )

        col3.metric(
            label=label + ' ' + str(end_year - 2),
            value=str(value_list[2]) + ' €',
            delta=str(delta_list[2]) + ' %',
        )
