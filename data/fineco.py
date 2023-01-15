import eurostat


class Fineco:

    @staticmethod
    def gdp(start_year, end_year, year_ago):
        # Query Italian gdp Data from Eurostat
        my_filter_pars_gdp = {'startPeriod': start_year,
                              'endPeriod': end_year,
                              'geo': ['IT'],
                              'na_item': 'B1GQ',
                              'unit': 'CP_MEUR'}

        df_gdp = eurostat.get_data_df('nama_10_gdp', filter_pars=my_filter_pars_gdp)
        gdp_l = [df_gdp.at[0, str(end_year - n)] for n in range(year_ago)]
        gdp_l_delta = [round(
            ((gdp_l[i] - gdp_l[i + 1]) / gdp_l[i + 1]) * 100, 2
        ) if gdp_l[i] is not None else gdp_l[i]
                       for i in range(len(gdp_l) - 1)]
        return gdp_l, gdp_l_delta

    @staticmethod
    def gdpcapita(start_year, end_year, year_ago):
        # Query Italian gdp for capita Data from Eurostat
        my_filter_pars_pop = {'startPeriod': start_year,
                              'endPeriod': end_year,
                              'geo': ['IT'],
                              'freq': 'A',
                              'unit': 'CP_EUR_HAB',
                              'NA_ITEM': 'B1GQ',
                              }

        df_gdp_cap = eurostat.get_data_df('NAMA_10_PC', filter_pars=my_filter_pars_pop)
        gdp_cap_l = [df_gdp_cap.at[0, str(end_year - n)] for n in range(year_ago)]
        gdp_cap_l_delta = [round(
            ((gdp_cap_l[i] - gdp_cap_l[i + 1]) / gdp_cap_l[i + 1]) * 100, 2
        ) if gdp_cap_l[i] is not None else gdp_cap_l[i]
                           for i in range(len(gdp_cap_l) - 1)]
        return gdp_cap_l, gdp_cap_l_delta


