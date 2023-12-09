import pandas as pd
from collections import Counter
# from categorization import *
from definition import *

# ==================================
# ||            HELPER            ||
# ==================================
# Aggreate daily data for one entry into a dict
def daily_data_to_row(date, total_visits, most_visited_url,
                most_visited_count, broad_percentages, narrow_percentages):
    row = {'date': date,
           'total_visits': total_visits,
           'most_visited_url': most_visited_url,
           'most_visited_count': most_visited_count}
    
    for key, value in broad_percentages.items():
        row[key] = round(value, 4)
    
    for key, value in narrow_percentages.items():
        row[key] = round(value, 4)

    return row

def daily_analysis(df):
    daily_df = pd.DataFrame(columns=daily_columns)
    daily_ranking_df = pd.DataFrame(columns=ranking_columns)

    # ==================================
    # ||            DAILY             ||
    # ==================================

    grouped_df = df.groupby('date')
    for daily_date, daily_data in grouped_df:
        # `daily_date` is the current date of the group
        # `daily_data` is a DataFrame with data for that date

        daily_total_visits = daily_data.shape[0]
        daily_domain_visit_counts = Counter(daily_data['domain'])
        daily_most_visited_url = daily_domain_visit_counts.most_common(1)[0][0]
        daily_most_visited_count = daily_domain_visit_counts[daily_most_visited_url]

        daily_broad_percentages = daily_data['broad_category'].value_counts(normalize=True) 
        daily_narrow_percentages = daily_data['narrow_category'].value_counts(normalize=True) 

        daily_entry = daily_data_to_row(daily_date, daily_total_visits, daily_most_visited_url,
                                 daily_most_visited_count, daily_broad_percentages,
                                 daily_narrow_percentages)

        # Ensure daily_entry has all the columns with default values
        daily_entry = {col: daily_entry.get(col, daily_default[col]) for col in daily_columns}


        daily_df = daily_df.append(daily_entry, ignore_index=True)

        daily_domain_visited_rank = daily_domain_visit_counts.most_common()
        # Append entries: One entry per domain
        for domain, counts in daily_domain_visited_rank:
            row = {'date': daily_date, 'domain': domain, 'counts': counts}
            daily_ranking_df = daily_ranking_df.append(row, ignore_index=True)

        return daily_df, daily_ranking_df