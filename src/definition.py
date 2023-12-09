scoring_columns = [
    'domain',
    'total_visits',
    'typed',
    'auto_bookmark',
    'form_submit',
    'link',
    'reload',
    'auto_toplevel',
    'generated',
    'score'
]

scoring_default = {
    'domain': 'N/A',
    'total_visits': 0,
    'typed': 0,
    'auto_bookmark': 0,
    'form_submit': 0,
    'link': 0,
    'reload': 0,
    'auto_toplevel': 0,
    'generated': 0,
    'score': 0
}

day_analysis_columns = [
    'day_type',
    'total_visits',
    'average_visits_per_day',
    'most_visited_url',
    'most_visisted_count',
    'study(%)', # Broad
    'entertainment(%)',            # Broad
    'other_broad(%)',              # Broad
    'coding(%)',                   # Narrow
    'streaming(%)',                # Narrow
    'medical(%)',                  # Narrow
    'financial(%)',                # Narrow
    'educational(%)',              # Narrow
    'gaming(%)',                   # Narrow
    'social_media(%)',             # Narrow
    'news_media(%)',               # Narrow
    'other_narrow(%)'              # Narrow
]

day_analysis_default = {
    'day_type': 'N/A',
    'total_visits': 0,
    'average_visits_per_day': 0,
    'most_visited_url': 'N/A',
    'most_visisted_count': 0,
    'study(%)': 0,                    # Broad
    'entertainment(%)': 0,            # Broad
    'other_broad(%)': 0,              # Broad
    'coding(%)': 0,                   # Narrow
    'streaming(%)': 0,                # Narrow
    'medical(%)': 0,                  # Narrow
    'financial(%)': 0,                # Narrow
    'educational(%)': 0,              # Narrow
    'gaming(%)': 0,                   # Narrow
    'social_media(%)': 0,             # Narrow
    'news_media(%)': 0,               # Narrow
    'other_narrow(%)': 0              # Narrow
}

time_analysis_columns = [
    'time_category', 
    'total_visits', 
    'most_visited_url', 
    'most_visited_count', 
    'study(%)',                    # Broad
    'entertainment(%)',            # Broad
    'other_broad(%)',              # Broad
    'coding(%)',                   # Narrow
    'streaming(%)',                # Narrow
    'medical(%)',                  # Narrow
    'financial(%)',                # Narrow
    'educational(%)',              # Narrow
    'gaming(%)',                   # Narrow
    'social_media(%)',             # Narrow
    'news_media(%)',               # Narrow
    'other_narrow(%)'
]

time_analysis_default = {
    'time_category': 'N/A', 
    'total_visits': 0, 
    'most_visited_url': 'N/A', 
    'most_visited_count': 0, 
    'study(%)': 0,                    # Broad
    'entertainment(%)': 0,            # Broad
    'other_broad(%)': 0,              # Broad
    'coding(%)': 0,                   # Narrow
    'streaming(%)': 0,                # Narrow
    'medical(%)': 0,                  # Narrow
    'financial(%)': 0,                # Narrow
    'educational(%)': 0,              # Narrow
    'gaming(%)': 0,                   # Narrow
    'social_media(%)': 0,             # Narrow
    'news_media(%)': 0,               # Narrow
    'other_narrow(%)': 0
}

daily_columns = [
    'date', 
    'total_visits', 
    'most_visited_url', 
    'most_visited_count', 
'study(%)',                        # Broad
    'entertainment(%)',            # Broad
    'other_broad(%)',              # Broad
    'coding(%)',                   # Narrow
    'streaming(%)',                # Narrow
    'medical(%)',                  # Narrow
    'financial(%)',                # Narrow
    'educational(%)',              # Narrow
    'gaming(%)',                   # Narrow
    'social_media(%)',             # Narrow
    'news_media(%)',               # Narrow
    'other_narrow(%)'              # Narrow
]

daily_default = {
    'date': 'N/A', 
    'total_visits': -1, 
    'most_visited_url': 'N/A', 
    'most_visited_count': -1, 
    'study(%)': 0,                    # Broad
    'entertainment(%)': 0,            # Broad
    'other_broad(%)': 0,              # Broad
    'coding(%)': 0,                   # Narrow
    'streaming(%)': 0,                # Narrow
    'medical(%)': 0,                  # Narrow
    'financial(%)': 0,                # Narrow
    'educational(%)': 0,              # Narrow
    'gaming(%)': 0,                   # Narrow
    'social_media(%)': 0,             # Narrow
    'news_media(%)': 0,               # Narrow
    'other_narrow(%)': 0              # Narrow
    }

summary_columns = [
    'start_date',
    'end_date', 
    'total_visits', 
    'most_visited_url', 
    'most_visited_count', 
    'study(%)',                    # Broad
    'entertainment(%)',            # Broad
    'other_broad(%)',              # Broad
    'coding(%)',                   # Narrow
    'streaming(%)',                # Narrow
    'medical(%)',                  # Narrow
    'financial(%)',                # Narrow
    'educational(%)',              # Narrow
    'gaming(%)',                   # Narrow
    'social_media(%)',             # Narrow
    'news_media(%)',               # Narrow
    'other_narrow(%)'              # Narrow
]

summary_default = {
    'start_date': 'N/A', 
    'end_date': 'N/A',
    'total_visits': -1, 
    'most_visited_url': 'N/A', 
    'most_visited_count': -1, 
    'study(%)': 0,                    # Broad
    'entertainment(%)': 0,            # Broad
    'other_broad(%)': 0,              # Broad
    'coding(%)': 0,                   # Narrow
    'streaming(%)': 0,                # Narrow
    'medical(%)': 0,                  # Narrow
    'financial(%)': 0,                # Narrow
    'educational(%)': 0,              # Narrow
    'gaming(%)': 0,                   # Narrow
    'social_media(%)': 0,             # Narrow
    'news_media(%)': 0,               # Narrow
    'other_narrow(%)': 0              # Narrow
    }

ranking_columns = [
    'date',
    'domain',
    'counts'
]