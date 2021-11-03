# Class with visualization methods
import pandas as pd
import matplotlib.pyplot as plt
class Visualizer:

    def __init__(self) -> None:
        pass

    
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

