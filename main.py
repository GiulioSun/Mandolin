import datetime

import eurostat
import streamlit as st


# Function for set date list
def set_years(last_years):
    end = datetime.date.today().year
    start = end - last_years
    years = [year for year in range(start, end)]
    return years


if __name__ == '__main__':

    # Set years
    __year_ago = 4
    __endYear = datetime.date.today().year - 2

    # Dash header
    st.title('''
    Mandolin data
    ''')

    # Containers
    colDate1, colData2 = st.columns(2)
    endYearInput = colDate1.selectbox(
        "Seleziona l'anno",
        (set_years(10)))

    if endYearInput != __endYear:
        __endYear = endYearInput
    startYear = __endYear - __year_ago

    # Query Italian gdp Data from Eurostat
    my_filter_pars_gdp = {'startPeriod': startYear,
                          'endPeriod': __endYear,
                          'geo': ['IT'],
                          'na_item': 'B1GQ',
                          'unit': 'CP_MEUR'}

    df_gdp = eurostat.get_data_df('nama_10_gdp', filter_pars=my_filter_pars_gdp)
    gdp_l = [df_gdp.at[0, str(__endYear - n)] for n in range(__year_ago)]
    gdp_l_delta = [round(
        ((gdp_l[i] - gdp_l[i + 1]) / gdp_l[i + 1]) * 100, 2
    ) if gdp_l[i] is not None else gdp_l[i]
                   for i in range(len(gdp_l) - 1)]

    # Query Italian population Data from Eurostat
    my_filter_pars_pop = {'startPeriod': startYear,
                          'endPeriod': __endYear,
                          'geo': ['IT'],
                          'freq': 'A',
                          'unit': 'NR',
                          'age': 'TOTAL',
                          'sex': 'T',
                          }

    df_pop = eurostat.get_data_df('DEMO_GIND', filter_pars=my_filter_pars_pop)
    pop_l = [df_pop.at[0, str(__endYear - n)] for n in range(__year_ago)]
    pop_l_delta = [round(
        ((pop_l[i] - pop_l[i + 1]) / pop_l[i + 1]) * 100, 2
    ) if pop_l[i] is not None else pop_l[i]
                   for i in range(len(pop_l) - 1)]

    # Query Italian gdp for capita Data from Eurostat
    my_filter_pars_pop = {'startPeriod': startYear,
                          'endPeriod': __endYear,
                          'geo': ['IT'],
                          'freq': 'A',
                          'unit': 'CP_EUR_HAB',
                          'NA_ITEM': 'B1GQ',
                          }

    df_gdp_cap = eurostat.get_data_df('NAMA_10_PC', filter_pars=my_filter_pars_pop)
    gdp_cap_l = [df_gdp_cap.at[0, str(__endYear - n)] for n in range(__year_ago)]
    gdp_cap_l_delta = [round(
        ((gdp_cap_l[i] - gdp_cap_l[i + 1]) / gdp_cap_l[i + 1]) * 100, 2
    ) if gdp_cap_l[i] is not None else gdp_cap_l[i]
                       for i in range(len(gdp_cap_l) - 1)]

    # DataViz PIL
    col1, col2, col3 = st.columns(3)

    col1.metric(
        label='PIL ' + str(__endYear),
        value=str(gdp_l[0]) + ' €',
        delta=str(gdp_l_delta[0]) + ' %',
    )

    col2.metric(
        label='PIL ' + str(__endYear - 1),
        value=str(gdp_l[1]) + ' €',
        delta=str(gdp_l_delta[1]) + ' %',
    )

    col3.metric(
        label='PIL ' + str(__endYear - 2),
        value=str(gdp_l[2]) + ' €',
        delta=str(gdp_l_delta[2]) + ' %',
    )

    # DataViz GDP capita
    col1.metric(
        label='PIL pro capite ' + str(__endYear),
        value=str(gdp_cap_l[0]) + ' €',
        delta=str(gdp_cap_l_delta[0]) + ' %',
    )

    col2.metric(
        label='PIL pro capite ' + str(__endYear - 1),
        value=str(gdp_cap_l[1]) + ' €',
        delta=str(gdp_cap_l_delta[1]) + ' %',
    )

    col3.metric(
        label='PIL pro capite ' + str(__endYear - 2),
        value=str(gdp_cap_l[2]) + ' €',
        delta=str(gdp_cap_l_delta[2]) + ' %',
    )

    # DataViz Population
    col1.metric(
        label='Popolazione ' + str(__endYear),
        value=str(pop_l[0]),
        delta=str(pop_l_delta[0]) + ' %',
    )

    col2.metric(
        label='Popolazione ' + str(__endYear - 1),
        value=str(pop_l[1]),
        delta=str(pop_l_delta[1]) + ' %',
    )

    col3.metric(
        label='Popolazione ' + str(__endYear - 2),
        value=str(pop_l[2]),
        delta=str(pop_l_delta[2]) + ' %',
    )
