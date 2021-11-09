# Class with visualization methods
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:

    def __init__(self) -> None:
        pass

    ######################################################
    # As input needs dataframe containing the advertisements GROUPED BY DAY!
    # Can be done for individual politicians or even groups like reps or dems
    def spend_over_time_cum(self, by_day: pd.DataFrame, title: str):
        # https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas/
        # This graph: https://swdevnotes.com/python/2020/display-line-chart-range/
        politician = title
        # df_c = u5mr_df.loc[([country]), :]
        df_c = by_day
        days = df_c.ad_creation_time
        lower = df_c.sum_spend_lo.cumsum()
        average = df_c.avg_spend.cumsum()
        upper = df_c.sum_spend_hi.cumsum()

        title = f'Cumulative spend of {politician}'

        fig, ax = plt.subplots(figsize = (8,5), facecolor = plt.cm.Blues(.2))
        fig.suptitle(title, fontsize = 'xx-large',  fontweight = 'bold')

        ax.set_facecolor(plt.cm.Blues(.2))
        ax.plot(days, upper, label = 'Upper')
        ax.plot(days, average, label = 'Average')
        ax.plot(days, lower, label = 'Lower')
        ax.legend(bbox_to_anchor = (0.9, 0.9),
                loc = 'lower left',
                frameon = False,
                fontsize = 'small')
        ax.set_ylabel('Cumulated spend in $', fontsize = 'large')
        ax.set_xlabel('Time', fontsize=14)
        # Hide the right and top spines
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.fill_between(days, lower, upper, alpha=0.2)
        plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees
        plt.show()


    ######################################################
    # needs ads grouped by day for each party
    def both_parties_spend_over_time_cum(self, republicans: pd.DataFrame, democrats: pd.DataFrame):
        
        title = f'Cumulative spend per party'
        fig, ax1 = plt.subplots(figsize = (8,5), facecolor = plt.cm.Blues(.2))
        fig.suptitle(title, fontsize = 'xx-large',  fontweight = 'bold')
        ax1.set_facecolor(plt.cm.Blues(.2))

        # First plot
        df_1 = republicans
        days = df_1.ad_creation_time
        lower = df_1.sum_spend_lo.cumsum()
        average = df_1.avg_spend.cumsum()
        upper = df_1.sum_spend_hi.cumsum()

        ax1.plot(days, upper, label = 'Republicans', color="red")
        ax1.plot(days, average, color="red")
        ax1.plot(days, lower, color="red")
        ax1.set_ylabel('Cumulated spend in $', fontsize = 'large')
        ax1.set_xlabel('Time', fontsize=14)
                # Hide the right and top spines
        ax1.spines['right'].set_visible(False)
        ax1.spines['top'].set_visible(False)
        ax1.fill_between(days, lower, upper, alpha=0.2, color="red")

        # Second plot
        df_2 = democrats
        days_2 = df_2.ad_creation_time
        lower_2 = df_2.sum_spend_lo.cumsum()
        average_2 = df_2.avg_spend.cumsum()
        upper_2 = df_2.sum_spend_hi.cumsum()

        ax1.plot(days_2, upper_2, label = 'Democrats', color="blue")
        ax1.plot(days_2, average_2, color="blue")
        ax1.plot(days_2, lower_2,color="blue")
        ax1.fill_between(days_2, lower_2, upper_2, alpha=0.2, color="blue")

        ax1.legend(bbox_to_anchor = (0.9, 0.9),
                        loc = 'lower right',
                        frameon = False,
                        fontsize = 'medium')

        plt.xticks(rotation = 45) # Rotates X-ax1is Ticks by 45-degrees
        plt.show()

    ######################################################
    # As input needs dataframe containing the advertisements GROUPED BY DAY!
    # Can be done for individual politicians or even groups like reps or dems
    def impressions_over_time_cum(self, by_day: pd.DataFrame, title: str):
        # https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas/
        # This graph: https://swdevnotes.com/python/2020/display-line-chart-range/
        politician = title
        # df_c = u5mr_df.loc[([country]), :]
        df_c = by_day
        days = df_c.ad_creation_time
        lower = df_c.sum_impressions_lo.cumsum()
        average = df_c.avg_impressions.cumsum()
        upper = df_c.sum_impressions_hi.cumsum()

        title = f'Cumulative impressions of {politician}'

        fig, ax = plt.subplots(figsize = (8,5), facecolor = plt.cm.Blues(.2))
        fig.suptitle(title, fontsize = 'xx-large',  fontweight = 'bold')

        ax.set_facecolor(plt.cm.Blues(.2))
        ax.plot(days, upper, label = 'Upper')
        ax.plot(days, average, label = 'Average')
        ax.plot(days, lower, label = 'Lower')
        ax.legend(bbox_to_anchor = (0.9, 0.9),
                loc = 'lower left',
                frameon = False,
                fontsize = 'small')
        ax.set_ylabel('Cumulated impressions', fontsize = 'large')
        ax.set_xlabel('Time', fontsize=14)
        # Hide the right and top spines
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.fill_between(days, lower, upper, alpha=0.2)
        plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees
        plt.show()

    ######################################################
    # for both parties
    def both_parties_impressions_over_time_cum(self, republicans: pd.DataFrame, democrats=pd.DataFrame):
        df_c = republicans
        days = df_c.ad_creation_time
        lower = df_c.sum_impressions_lo.cumsum()
        average = df_c.avg_impressions.cumsum()
        upper = df_c.sum_impressions_hi.cumsum()

        title = f'Cumulative impressions of both parties'

        fig, ax = plt.subplots(figsize = (8,5), facecolor = plt.cm.Blues(.2))
        fig.suptitle(title, fontsize = 'xx-large',  fontweight = 'bold')

        ax.set_facecolor(plt.cm.Blues(.2))
        ax.plot(days, upper, label = 'Republicans', color="red")
        ax.plot(days, average, color="red")
        ax.plot(days, lower, color="red")  

        ax.set_ylabel('Cumulated impressions', fontsize = 'large')
        ax.set_xlabel('Time', fontsize=14)
                # Hide the right and top spines
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.fill_between(days, lower, upper, alpha=0.2, color="red")

        # Second plot
        df_2 = democrats
        days_2 = df_2.ad_creation_time
        lower_2 = df_2.sum_impressions_lo.cumsum()
        average_2 = df_2.avg_impressions.cumsum()
        upper_2 = df_2.sum_impressions_hi.cumsum()

        ax.plot(days_2, upper_2, label = 'Democrats', color="blue")
        ax.plot(days_2, average_2, color="blue")
        ax.plot(days_2, lower_2,color="blue")
        ax.fill_between(days_2, lower_2, upper_2, alpha=0.2, color="blue")

        ax.legend(bbox_to_anchor = (0.9, 0.9),
                        loc = 'lower right',
                        frameon = False,
                        fontsize = 'medium')

        plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees
        plt.show()

    ######################################################  
    # Makes boxplots of impressions per dollar spend for climate vs non-climate related advertisements
    def boxplot_impr_per_dollar_comparison(self, climate_ads: pd.DataFrame, non_climate_ads: pd.DataFrame):
        #helper
        def calc_spend_per_impr(x):
            return x.impressions/x.spend
        # calc impr per dollat
        climate_ads["impr_per_dollar"] = climate_ads.apply(lambda x: calc_spend_per_impr(x), axis=1)
        non_climate_ads["impr_per_dollar"] = non_climate_ads.apply(lambda x: calc_spend_per_impr(x), axis=1)

        fig, (ax, ax1) = plt.subplots(1, 2, sharey=True, figsize=(10,5))
        fig.suptitle('Comparison impressions per dollar')
        ax.set_title('Non-climate-related ads')
        ax1.set_title('Climate-related ads')
        sns.set_theme(style="darkgrid")
        sns.boxplot(ax=ax, y=non_climate_ads["impr_per_dollar"], color="purple", showmeans=True)
        sns.boxplot(ax= ax1, y=climate_ads["impr_per_dollar"],color="teal", showmeans=True)
        ax.set_yscale('log')
        ax1.set_yscale('log')