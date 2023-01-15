import datetime

import streamlit as st


class Metric:

    @staticmethod
    def start_and_year_box(n_years):
        # set end year
        end_year = datetime.date.today().year - 1
        # set start year
        start_year = end_year - n_years
        # list of selected years
        years = [year for year in range(end_year, start_year, -1)]
        # set graphics object for select year
        col_date1, col_data2 = st.columns(2)
        end_year_input = col_date1.selectbox("Seleziona l'anno", years)
        # set start and end years select
        if end_year_input != end_year:
            end_year = end_year_input
        start_year = end_year - n_years
        return start_year, end_year, years

    @staticmethod
    def start_and_year(n_years):
        # set end year
        end_year = datetime.date.today().year - 2
        # set start year
        start_year = end_year - n_years
        # list of selected years
        years = [year for year in range(end_year, start_year, -1)]
        start_year = end_year - n_years
        return start_year, end_year, years

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
            label=f'{label} {str(end_year - 1)}',
            value=f'{str(value_list[1])} {label_value}',
            delta=f'{str(delta_list[1])} {label_delta}',
        )

        col3.metric(
            label=f'{label} {str(end_year - 2)}',
            value=f'{str(value_list[2])} {label_value}',
            delta=f'{str(delta_list[2])} {label_delta}',
        )
