import eurostat


class Pop:

    @staticmethod
    def pop(start_year, end_year, year_ago):
        my_filter_pars_pop = {'startPeriod': start_year,
                              'endPeriod': end_year,
                              'geo': ['IT'],
                              'freq': 'A',
                              'unit': 'NR',
                              'age': 'TOTAL',
                              'sex': 'T',
                              }

        df_pop = eurostat.get_data_df('DEMO_GIND', filter_pars=my_filter_pars_pop)
        pop_l = [df_pop.at[0, str(end_year - n)] for n in range(year_ago)]
        pop_l_delta = [round(
            ((pop_l[i] - pop_l[i + 1]) / pop_l[i + 1]) * 100, 2
        ) if pop_l[i] is not None else pop_l[i]
                       for i in range(len(pop_l) - 1)]
        return pop_l, pop_l_delta
