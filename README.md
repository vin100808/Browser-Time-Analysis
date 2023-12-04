# Comprehensive User Browser History Analysis

[toc]

## Introduction

**Purpose**:

This project aims to analyze an individual's browser history to gain insights into their online behavior, preferences, and time allocation. By delving into various aspects of the user's browsing data, the project seeks to understand patterns in internet usage, with a particular focus on distinguishing between different types of online activities, such as educational, entertainment, and professional use.



In this project, we try to answer the following questions:

- What does the user’s browser history reveal about their daily and overall online behavioral patterns? How are these patterns influenced by different factors like time of day or type of website?

- How can we categorize and quantify the user's internet usage into different purposes such as entertainment, education, or work-related activities? How do these categories vary over time?

- Can we determine the intentionality of a user's website visits based on their method of accessing the website (e.g., typing the URL directly vs. clicking a link)? How does this intentionality vary across different types of websites?

  

## Background

**Why This Project is Important:**

Understanding one's browsing patterns can significantly aid in personal productivity and time management. By analyzing which websites are most frequently visited and categorizing them into productivity-related or entertainment-related, individuals can gain insights into how they allocate their online time. This awareness can lead to better time management strategies and more conscious decisions about web usage.



Furthermore, the recent global shift towards remote education and work has further intensified the need to understand online behaviors. As more people rely on the internet for learning and professional activities, it becomes important to analyze how effectively these platforms are being used.



Lastly, according to TODO: data, the market trends shows a tremendous increasing in personal development books, that means people nowadays focuses more on personal development rather than reading a fictional book. Therefore, this project could be considered an actual tool for personal development.

## Data Sources

**Data Origin**: The data for the project originates from personal browser history, which is collected using the Chrome extension [Export Chrome History](https://chromewebstore.google.com/detail/export-chrome-history/dihloblpkeiddiaojbagoecedbfpifdj). This extension allows users to extract their browsing history from Google Chrome and export it in various formats for analysis.



**Data Description**: The dataset includes the following fields, as captured by the Chrome extension:

- `order`: A sequential identifier for the browsing entries.

- `id`: A unique identifier for each entry, possibly correlating to an internal database ID used by Chrome.

- `date`: The date on which the website was visited.

- `time`: The time at which the website was accessed.

- `title`: The title of the webpage as it appears in the browser tab.

- `url`: The full URL of the visited webpage.

- `visitCount`: The number of times the webpage was visited.

- `typedCount`: The number of times the URL was typed directly into the browser's address bar.

- `transition`: How the browser navigated to the URL (e.g., link click, typed, bookmarked).

  

**Data Accessibility**: Currently, the data is not publicly available as it is personal and has been extracted using a private Chrome extension. The data includes potentially sensitive information and may require anonymization before being shared or used for collaborative purposes.



**Data Collection Range**: The extension allows for the extraction of data over variable time ranges, including a day, a week, a month, or three months, giving flexibility in the period of analysis.



**Disclaimer**: While the data is sourced from personal browsing history, if similar analysis is intended for broader use, it is crucial to ensure that proper permissions and privacy considerations are taken into account. Data should be anonymized and stripped of any personally identifiable information (PII) before being used in any public or shared context.



## Technologies and Tools Used

**Programming Languages:** 

- Python 



**Python Libraries:** 

- Pandas
- re
- os
- urllib.parse: urlparse
- collections: Counter



**Tools**:

- Python: Responsible for data preprocess and analysis
- Excel: Used to store processed and analyzed data
- Tableau: Used for data visualization



## Installation and Setup

**Steps to analyze:**

1. Fork this repository
2. Download Chrome Extension [Export Chrome History](https://chromewebstore.google.com/detail/export-chrome-history/dihloblpkeiddiaojbagoecedbfpifdj)

3. Used [Export Chrome History](https://chromewebstore.google.com/detail/export-chrome-history/dihloblpkeiddiaojbagoecedbfpifdj) to generate browser history of any length you wishes to analyze
4. Move the generated `history.csv` to `Comprehensive-User-Browser-History-Analysis/data/raw`
5. Run the `analysis.py` from `Comprehensive-User-Browser-History-Analysis/src`
6. Your analyzed data will be generated in `Comprehensive-User-Browser-History-Analysis/data/processed`



## File and Directory Structure

```
Project/
│
├── README.md                # Project overview and documentation
│
├── data/                    # Data used and generated by the project
│   ├── processed/           # Processed data ready for analysis
│   │   ├── daily_df.csv         # Daily browser history data
│   │   ├── daily_ranking_df.csv # Daily ranking of visited websites
│   │   ├── summary_df.csv       # Summary statistics of browser usage
│   │   ├── summary_ranking_df.csv # Ranking of sites based on summary stats
│   │		└── [Additional generated csv]
│   │
│   └── raw/                 # Original, unmodified data
│       └── history_month.csv    # Raw monthly browser history data
│
├── src/                     # Source code for the project
│   ├── analysis.py              # Main analysis scripts
│   ├── scoring_analysis.py      # Scripts for scoring website interactions
│   └── specifications.py        # Definitions and specifications for analysis
│
└── results/                 # Visualization and analysis results
    ├── browser_analysis.twb     # Tableau workbook for data visualization
    └── [Additional PNG files]   # Exported visualizations from Tableau```
```



## Analysis and Results

### Overall Analysis

#### 1. Top 20 Overall Most Visited Websites

![Top 20 Overall Visited Websites](results/1Top_20_Overall_Most_Visited_Websites.png)

The graph titled "Top 20 Overall Most Visited Websites" is a horizontal bar chart that displays the top 20 websites visited by the user, ranked by the total number of visits. Each bar represents a different domain and the length of the bar indicates the count of visits to that domain.

Graph Description:

- **Horizontal Bars**: Each bar corresponds to the total number of visits on a particular domain.
- **Ranking Sequence**: The Y-axis represents domain names, specifically the top 20 visited domains in the dataset.
- **Activity Volume**: The X-axis measures the volume of visits, providing a sense of the user's top 20 domain activity levels.

Key findings from the graph:

1. **Dominant Websites**: The website 'youtube.com' has the highest number of visits by a significant margin, suggesting it is the most frequented site for the user. This is followed by 'chat.openai.com' and 'google.com', which also have a high number of visits, indicating regular usage.
2. **Popular Domains**: Domains such as 'github.com' and 'docs.google.com' suggest that the user engages with sites related to programming, software development, and document collaboration.
3. **Variety of Interests**: The presence of a diverse range of domains including social media platforms ('tiktok.com'), professional networking ('linkedin.com'), and job-related sites ('career.huawei.com'), reflects the user's varied interests and activities online.
4. **Educational and Career-Oriented Usage**: Several domains like 'exam.nowcoder.com' and 'smith.queensu.ca' indicate the user's engagement with educational resources and career-oriented platforms.
5. **Consistency Across Visits**: The distribution of visits across these top domains shows a consistency in the user's browsing habits, with several sites visited over 50 times, indicating regular engagement rather than sporadic visits.

This chart provides a clear snapshot of the user's online behavior, identifying which websites are most integral to their daily internet usage.



#### 2. Overall Broad Categorization

<img src="results/3Overall_Broad_Categorization.png" alt="Overall Broad Categorization" style="zoom:50%;" />

The "Overall Broad Categorization" pie chart compiles the user's entire browsing history into three main categories—`Study(%)`, `Entertainment(%)`, and `Other Broad(%)`—depicting the cumulative time spent in each category.

Graph Description:

- **Proportional Representation**: The chart uses colored segments to represent the percentage of the user's total browsing activity that falls into each category.
- **Majority Share**: The `Study(%)` category forms the majority of the chart, indicating a significant focus on educational or work-related browsing.
- **Secondary Activities**: `Entertainment(%)` and `Other Broad(%)` make up smaller portions of the chart, illustrating the user's time spent on leisure and other miscellaneous activities.

Insights from the Graph:

1. **Study Dominance**: With `Study(%)` accounting for 58.55% of the browsing activity, it's clear that the user's primary online engagement is with educational or productivity-related content.
2. **Considerable Entertainment Usage**: The `Entertainment(%)` category, at 23.89%, reflects a substantial engagement with entertainment websites, which is significant but not predominant.
3. **Miscellaneous Interactions**: `Other Broad(%)` holds 17.56%, suggesting that the user also explores a variety of websites that don't fall strictly into the study or entertainment classifications.

Comparative Note with "Daily Broad Category Percentages":

- When compared to the "Daily Broad Category Percentages" graph, this pie chart provides a holistic view of the user's browsing behavior over an extended period, likely revealing more consistent long-term trends as opposed to the daily fluctuations seen in the bar graph.
- The daily chart may show certain days where one category spikes, due to specific events or activities, but the overall chart averages these out to present a general pattern of internet usage.
- The pie chart's aggregation of data across a broader timeframe smoothens out daily anomalies and presents a clear picture of the user's general browsing priorities.

This overall categorization helps in understanding the user's typical internet usage patterns, offering a snapshot of their priorities over the observed period. It complements the daily distribution chart by providing a macro-level perspective on the user's browsing habits.



#### 3. Overall Narrow Categorization

![Overall Narrow Categorization](results/5Overall_Narrow_Categorization.png)

The "Overall Narrow Categorization" bar chart provides a detailed breakdown of the user's internet browsing across specific categories within a set period. This visualization enables a more granular view of the user's online activities.

Graph Description:

- **Categories**: Each horizontal bar represents a distinct category, such as `Educational`, `Coding`, `Social Media`, and others, showing a more detailed classification of the user's browsing data.
- **Proportionality**: The length of each bar correlates to the percentage of total visits that fall within each category, giving a visual representation of how much time was spent in each area.
- **Major Category**: The `Other Narrow(%)` category comprises the majority of the user's browsing activity, suggesting that most of their web usage does not fall into the predefined categories but rather into a broad range of other activities.

Insights from the Graph:

1. **Focus on Education**: With `Educational(%)` constituting 10.34% of the browsing, it's clear that a significant portion of the user's internet use is dedicated to educational content.
2. **Interest in Coding**: The `Coding(%)` category has a notable representation at 7.22%, indicating that activities related to programming or development are a substantial part of the user's online time.
3. **Social Media Engagement**: `Social Media(%)` accounts for 2.51% of the browsing history, reflecting the user's moderate use of social media platforms compared to other activities.
4. **Limited Variety in Other Segments**: Several categories such as `Streaming`, `News Media`, `Medical`, `Gaming`, and `Financial` show no recorded activity, which could imply a lack of interest or a need for better categorization if the user did engage in these activities but they were not captured by the data.
5. **Dominance of 'Other Narrow' Activities**: The overwhelming majority of the user's browsing falls into the `Other Narrow(%)` category at 79.93%, which includes any activity not classified in the specified narrow categories. This indicates diverse internet usage that may require further categorization to fully understand the user's browsing preferences and behavior.



### Daily Analysis

#### 1. Daily Broad Category Percentages

![Daily Broad Category Percentages](results/2Daily_Broad_Category_Percentages.png)

The "Daily Broad Category Percentages" chart categorizes the user's browser history into three main categories: `Entertainment`, `Study`, and `Other Broad`. The stacked bar graph visually represents the proportional distribution of these categories across each day in the dataset.

Graph Description:

- **Stacked Segments**: The bars are segmented to reflect the proportionate engagement in Study, Entertainment, or Other Broad activities on each specific day.
- **Date Axis**: The X-axis lists consecutive dates, indicating the period over which the browsing data was collected.
- **Percentage Axis**: The Y-axis shows percentages, allowing for the visualization of the relative distribution of the browsing activity across the categories.
- **Color Coding**: Each category is assigned a distinct color to easily differentiate between the types of activities within a day's browsing.

From this visualization, several insights emerge:

1. **Study as a Priority**: A significant portion of each bar is often dedicated to the `Study(%)` category, suggesting that the user's primary use of the internet is for educational or productivity-related purposes.
2. **Daily Fluctuations**: There is noticeable daily fluctuation in the proportion of time spent on `Entertainment(%)` and `Other Broad(%)` categories, indicating variability in the user's day-to-day browsing activities.
3. **Consistent Other Activities**: The `Other Broad(%)` segment is present each day, which implies that the user consistently engages in a variety of other activities beyond just study and entertainment.
4. **Notable Peaks**: Certain days show pronounced peaks in one category over others. For example, some days may have a higher proportion of `Entertainment(%)` or `Other Broad(%)`, which may correspond to specific events or personal downtime.
5. **Low Entertainment Engagement**: Overall, the `Entertainment(%)` category occupies the smallest segment on most days, suggesting that the user spends less time on entertainment-related websites compared to other activities.
6. **Further Exploration**: A fun activity for everyone is to assess the days with 100% `Entertainment` or `Study` to discern any patterns or triggers that lead to exclusive browsing history of one category, such as deadlines, holidays or weekends.



#### 2. Number of Visits Per Day

![Number of Visits Per Day](results/4Number_of_Visits_Per_Day.png)

The chart "Number of Visits Per Day" illustrates a user's web browsing activity over a period, quantified by the number of site visits each day. The horizontal bars represent the total count of website visits per day, laid out on a calendar timeline.

Graph Description:

- **Horizontal Bars**: Each bar corresponds to the total number of visits on a particular day.
- **Activity Volume**: The X-axis measures the volume of visits, providing a sense of the user's daily internet activity levels.
- **Time Sequence**: The Y-axis represents time, specifically the days in November and early December 2023.

Insights from the Graph:

1. **Fluctuating Activity**: There's a noticeable fluctuation in daily browsing activity. Some days exhibit high numbers of site visits, while others show significantly fewer visits.
2. **Peaks of Activity**: Certain days, such as November 6, November 24, November 28, and November 29, have particularly high activity, which could correspond to specific personal or professional needs that required more extensive internet use.
3. **Periods of Low Activity**: There are also instances of minimal activity, for instance, on November 4, November 11, and November 19. These could represent days when the user was less active online or potentially did not have access to the internet.
4. **Trending Increase**: Towards the end of the month, there is a trend of increasing activity, peaking on November 29. This pattern might correlate with end-of-the-month routines or deadlines.
5. **Consistency**: Despite fluctuations, the user consistently engages with the internet on a daily basis, indicating that web browsing is a regular part of their daily routine.



### Time Category Analysis

#### 1. Total Visits Based On Time Category

<img src="results/6Total_Visits_Based_On_Time_Category.png" alt="Total Visits Based on Time Category" style="zoom:100%;" />

The "Total Visits Based On Time Category" bar chart displays the aggregate of the user's website visits segmented by different times of the day. This visualization allows for an analysis of the user's online activity patterns relative to the time of day.

Graph Description:

- **Categories**: Each horizontal bar represents a time category—Morning, Afternoon, Evening, and Before Dawn—offering insight into when the user is most active online.
- **Proportionality**: The length of each bar corresponds to the total number of visits within each time category, visually indicating the user's internet activity volume during different times of the day.
- **Major Category**: The Afternoon category shows the highest number of visits, suggesting that this is the period of peak activity for the user.

Insights from the Graph:

1. **Afternoon Activity**: With 990 visits, the Afternoon category sees the highest internet use, which could correspond to the user's personal schedule or work-related activity peaks.
2. **Evening Consistency**: The Evening period also sees substantial activity with 751 visits, indicating sustained internet use during these hours, possibly for relaxation or post-work activities.
3. **Morning Engagement**: The Morning category shows moderate activity with 520 visits, which may align with the start of the user's day or routine morning tasks.
4. **Before Dawn Usage**: There is a notable amount of activity (330 visits) categorized as Before Dawn, which might indicate late-night browsing or activities that occur in the very early hours of the day.
5. **Dominance of Daytime Activity**: The significant activity during the Afternoon and Evening hours in contrast to Morning and Before Dawn suggests the user's browsing aligns with typical daytime and early evening periods, which may reflect a standard workday or personal habit pattern.

This chart provides a clear depiction of the user's preferred browsing times, which could be valuable for targeting specific content delivery times or understanding the user's daily routine and lifestyle.



#### 2. Broad Categorization Based on Time Category

![Broad Categorization Based on Time Category](results/7Broad_Categorization_Based_on_Time_Category.png)

The "Broad Categorization Based on Time Category" chart is a stacked bar graph illustrating the distribution of the user's web browsing across three broad categories—`Study(%)`, `Other Broad(%)`, and `Entertainment(%)`—segmented by different times of the day: Morning, Afternoon, Evening, and Before Dawn.

Graph Description:

- **Categories**: Each horizontal bar is divided into segments that represent the proportion of the user's browsing activity within the categories of Study, Other Broad, and Entertainment for each time category.
- **Proportionality**: The length of each segment within the bars correlates to the percentage of total visits attributed to each category, providing a visual comparison of how the user's browsing preferences vary by the time of day.
- **Time of Day**: The bars are grouped by the time of day, indicating when the user is most active in each of the browsing categories.

Insights from the Graph:

1. **Study Focus**: A significant segment of the browsing activity across all times of day is dedicated to Study, which is especially pronounced during the Morning period.
2. **Afternoon Entertainment**: In the Afternoon, there is a visible increase in Entertainment-related browsing, suggesting this might be the user's preferred time for leisure activities online.
3. **Evening Diversification**: During the Evening, there's a more balanced distribution between Study and Other Broad activities, indicating the user's engagement in a variety of activities.
4. **Before Dawn**: The Before Dawn period shows a lower overall browsing activity, but it still includes a mix of Study and Other Broad, with Study being slightly more predominant.
5. **Overall Trends**: While Study is a constant throughout all times of the day, the user's engagement with Entertainment and Other Broad categories suggests a transition from work or study-oriented activities to more leisure and varied browsing as the day progresses.

This chart offers insights into the user's daily rhythm and preferences, showing how their focus shifts across different types of online content from morning to night.



#### 3. Narrow Categorization Based On Time Category

![Narrow Categorization Based On Time Category](results/8Narrow_Categorization_Based_On_Time_Category.png)

The "Narrow Categorization Based on Time Category" chart is a stacked bar graph that displays the user's website visits broken down into specific categories within narrower interests, distributed across different times of the day: Morning, Afternoon, Evening, and Before Dawn.

Graph Description:

- **Categories**: Each horizontal bar represents a time category, segmented into narrower interests like `Coding(%)`, `Educational(%)`, `Social Media(%)`, and others, providing a detailed insight into the user's specific browsing activities during these periods.
- **Proportionality**: The segments within each bar show the relative proportion of visits to websites within each narrow category, relative to the time of day.
- **Time of Day**: The bars are ordered by the time of day, highlighting when certain activities are more prevalent.

Insights from the Graph:

1. **Educational Focus**: There is a significant emphasis on `Educational(%)` content during the Morning and Afternoon, which could indicate dedicated times for learning or professional development.
2. **Evening Diversification**: In the Evening, while `Educational(%)` content still has a presence, there's also a noticeable portion of browsing in the `Other Narrow(%)` category, suggesting a variety of activities that may include reading news, online shopping, or other interests.
3. **Before Dawn Engagement**: During the Before Dawn period, `Other Narrow(%)` activities dominate, which may include a range of miscellaneous activities or late-night browsing habits.
4. **Social Media and Coding**: `Social Media(%)` and `Coding(%)` have consistent yet smaller segments throughout the day, with an uptick in social media in the Evening and Before Dawn hours.
5. **Low Activity in Other Interests**: Categories like `Financial(%)`, `Gaming(%)`, `Medical(%)`, `News Media(%)`, and `Streaming(%)` show little to no activity, which could indicate lesser interest or that these activities occur less frequently within the user's online routine.

This chart offers a detailed perspective on the user's daily internet use, showing not only the volume of activity but also how the user's focus shifts among various interests at different times of the day.



### Weekday V.S. Weekend Analysis

#### 1. Average Visits Per Day Based On Day Type

![Average Visits Per Day Based On Day Type](results/9Average_Visits_Per_Day_Based_On_Day_Type.png)

The chart titled "Average Visits Per Day Based On Day Type" is a horizontal bar graph that compares the average number of website visits per day between two categories: Weekday and Weekend.

Graph Description:

- **Categories**: There are two categories represented by horizontal bars: Weekday and Weekend.
- **Proportionality**: The length of each bar indicates the average number of visits per day for each category, providing a clear comparison of user activity between weekdays and weekends.
- **Measurements**: The Y-axis lists the day types, while the X-axis represents the average number of visits, quantified on the scale.

Insights from the Graph:

1. **Higher Weekday Activity**: The Weekday bar is significantly longer, indicating a much higher average number of visits per day compared to the Weekend. This suggests that the user is more active online during weekdays.
2. **Reduced Weekend Browsing**: The Weekend bar shows that on average, there are fewer visits, which might imply that the user spends less time online during the weekends or that their browsing habits change, possibly due to different weekend routines or leisure activities.
3. **Routine Implications**: The marked difference in averages could reflect the user's work or school schedule, which typically involves more consistent internet usage during the weekdays.
4. **Potential for Deeper Analysis**: The average figures invite a deeper analysis of why there might be such a discrepancy. Factors could include work-related use, study habits, or other scheduled weekly activities that do not occur on weekends.

This visualization is useful for understanding the user's browsing habits in the context of their weekly routine, highlighting the stark contrast in online engagement between weekdays and weekends.



#### 2. Broad Categorization Based On Day Type

![Broad Categorization Based On Day Type](results/10Broad_Categorization_Based_On_Day_Type.png)

The chart titled "Broad Categorization Based On Day Type" is a stacked bar graph that delineates the proportion of the user's web browsing activity across three broad categories—`Study(%)`, `Other Broad(%)`, and `Entertainment(%)`—differentiated by day type: Weekday and Weekend.

Graph Description:

- **Categories**: Each horizontal bar is segmented according to the percentage of the user's browsing activity within the categories of Study, Other Broad, and Entertainment, for each day type.
- **Proportionality**: The segments within each bar reflect the proportion of visits to websites within each category, illustrating the user's browsing preference pattern on weekdays versus weekends.
- **Day Type**: The bars are divided into two categories, Weekday and Weekend, indicating when the user engages in different types of online activities.

Insights from the Graph:

1. **Weekday Activities**: On weekdays, `Other Broad(%)` activities constitute the majority of the user's browsing activity, followed by `Study(%)` and then `Entertainment(%)`, which could be indicative of work or school-related internet usage being prioritized during the week.
2. **Weekend Preferences**: Over the weekend, while `Other Broad(%)` still remains the largest category, the proportion of `Entertainment(%)` increases compared to weekdays, suggesting that the user allocates more time for leisure activities during weekends.
3. **Decrease in Study Focus**: The `Study(%)` category shows a lower percentage on weekends, which aligns with typical behavior patterns where academic or professional work is reduced during these days.
4. **Consistency in `Other Broad` Category**: Despite the changes from weekdays to weekends, the `Other Broad(%)` category consistently constitutes a significant portion of the browsing activity, indicating a continuous engagement with a variety of websites.

This chart offers insights into the user's browsing behavior, demonstrating how their focus shifts from study and work-related content on weekdays to more entertainment-focused content during weekends, while consistently maintaining a variety of other activities.



#### 3. Narrow Categorization Based On Day Type

![Narrow Categorization Based On Day Type](results/11Narrow_Categorization_Based_On_Day_Type.png)

The "Narrow Categorization Based On Day Type" chart is a stacked bar graph that presents the user's web browsing activity categorized into specific interests or content types, further differentiated by day type: Weekday and Weekend.

Graph Description:

- **Categories**: Each horizontal bar is divided into segments that correspond to narrow categories such as `Coding(%)`, `Educational(%)`, `Social Media(%)`, and so on, providing a detailed view of the user's specific browsing activity.
- **Proportionality**: The width of each segment within the bars indicates the proportion of total visits that fall within each narrow category, enabling a visual comparison of how the user's browsing preferences differ between weekdays and weekends.
- **Day Type**: The bars are categorized by the day type, illustrating when the user engages in these specific types of online activities.

Insights from the Graph:

1. **Weekday Distribution**: On weekdays, the vast majority of the user's browsing activity falls within the `Other Narrow(%)` category, with a small segment of `Educational(%)` activity, suggesting focused internet use potentially related to work or study.
2. **Weekend Activities**: During the weekend, the `Other Narrow(%)` category still comprises most of the browsing activity, but there is also a small increase in `Educational(%)` content compared to weekdays.
3. **Educational Engagement**: The presence of `Educational(%)` content on both weekdays and weekends indicates a consistent engagement with learning or informational websites, regardless of the day type.
4. **Limited Diversification**: The absence of notable segments for `Social Media(%)`, `Streaming(%)`, and other specific activities suggests that these do not make up a large portion of the user's browsing, or these activities are less frequent within the observed timeframe.
5. **Dominance of 'Other Narrow' Activities**: Regardless of whether it's a weekday or weekend, `Other Narrow(%)` activities dominate the user's browsing, implying a diverse range of interests that are not classified within the more defined narrow categories.

This visualization highlights the user's browsing habits in relation to the types of content they access, offering insights into how their specific interests in online content may vary between regular weekdays and the weekend.



### Intention Scoring Of Website Domains

#### 1. Scoring Mechanism

**Intention Score Significance**: In the realm of web analytics, intention score is a crucial metric that provides insights into user behavior beyond mere visit counts. It reveals the quality of user engagement and the level of intent behind interactions with website domains. Understanding user intention is essential for several reasons:

- **User Experience Optimization**: Knowing which sites users actively seek out can inform decisions on user interface and experience improvements.
- **Content Strategy**: High intention interactions suggest strong user interest, guiding content creators and marketers on what to focus on.
- **Conversion Potential**: Users with a higher intention are more likely to convert, making them prime targets for marketing and sales strategies.
- **Personalization**: Analyzing intention can lead to better personalization of user experiences, recommendations, and advertisements.

### Implementation of Intention Score

The intention score was implemented with the goal of quantifying the degree of user engagement and interest in specific website domains. 

```python
def calculate_domain_score(transition_count, number_of_visits, max_visits):
    # Define relative weights for transition types
    weights = {
        'typed': 0.8,
        'auto_bookmark': 0.8,
        'form_submit': 0.4,
        'link': 0.6,
        'reload': 0.6,
        'auto_toplevel': 0.3,
        'generated': 0.3
    }
    
    # Calculate the weighted interaction score
    weighted_interaction_score = sum(transition_count.get(t, 0) * w for t, w in weights.items())
    
    # Normalize the weighted interaction score by the total possible score for this domain
    max_possible_score_for_domain = number_of_visits * max(weights.values())
    normalized_intent_score = weighted_interaction_score / max_possible_score_for_domain * 100
    
    return round(normalized_intent_score, 2)
```

Here's a breakdown of the process:

1. **Transition Weights**:
   - Different user actions, or 'transitions,' such as typing a URL directly (`typed`) or accessing a site via a bookmark (`auto_bookmark`), carry different implications for user intent. These actions are assigned weights that correspond to their perceived level of user intent, with higher weights indicating stronger intent.
2. **Weighted Interaction Score Calculation**:
   - For each domain, the algorithm calculates a `weighted_interaction_score` by multiplying the frequency of each transition type by its assigned weight and summing these products. This results in a score that reflects the combined weighted user interactions for the domain.
3. **Normalization**:
   - To compare domains fairly, the `weighted_interaction_score` is normalized. This is achieved by dividing it by the `max_possible_score_for_domain`, which is the product of the number of visits to the domain and the highest transition weight. The result is a normalized score representing the quality of user engagement per visit, which is then scaled to a percentage.
4. **Final Scoring**:
   - The final intention score is expressed as a percentage, with 100% representing the highest possible user engagement level per visit for a domain. The score is rounded to two decimal places for clarity and ease of interpretation.

By focusing on the types of user interactions with a website, the intention score effectively captures the qualitative aspects of user engagement. It allows for distinguishing between passive visits and those driven by active user interest and intent. 

Note: Number of Visits to a site **DOES NOT** reflect on the score!



#### 2. Top 20 Score Websites

![Top 20 Intention Scored Websites](results/12Top_20_Intention_Scored_Websites.png)

The "Top 20 Intention Scored Websites" bar chart presents a ranking of websites based on their intention scores, which reflect the inferred user interest and purpose in visiting each site. The scores are calculated using a custom algorithm that assigns weights to different types of user interactions, with higher weights indicating stronger user intent.

Graph Description:

- **Domains**: Each horizontal bar corresponds to a unique website domain.
- **Intention Score**: The length of each bar represents the intention score out of 100 for each domain, calculated based on user interaction data.
- **Scale**: The scores range from 0 to a little over 100, with the highest-scoring domains approaching the maximum.

Insights from the Graph:

1. **High Intention Sites**: The domains `zwfw.cscc.edu.cn` and `microsoft.com` are tied for the highest intention score at 87.50, suggesting that users exhibit a high level of deliberate interaction with these sites, such as typing the URL directly into the browser or using bookmarks.
2. **Strong Engagement**: Domains like `baidu.com` and `209.209.59.233` show high intention scores above 80, which implies that users are actively seeking out these sites, indicating strong engagement or relevance to the users' needs.

This graph underscores the value of assessing user engagement through intention scoring, offering a nuanced view of how users interact with websites, which can be more informative than simple visit counts. The intention score is a robust metric for understanding user behavior, providing actionable insights for website owners and marketers in optimizing their content and user engagement strategies. 



## Challenges and Learnings

Challenges and Solutions:

- **Data Integrity**: Initially, the data visualization process revealed the presence of ambiguous URLs that did not correspond to meaningful website visits, likely stemming from ad-related traffic or automated scripts. To address this, I implemented a data cleaning step to identify and remove these outliers, ensuring the integrity and relevance of the analyzed data.
- **Code Efficiency**: As the project evolved, I encountered issues with redundant code which made the scripts less efficient and harder to maintain. The solution was twofold: I abstracted common functionality into helper functions and centralized all specifications into a single file. This not only streamlined the codebase but also made it more readable and easier to update.
- **Data Management**: Managing the output of various analyses presented a challenge due to the diversity of categories such as time-based, overall, scoring, and ranking analyses. To organize this, I adopted a systematic approach by storing each analysis type in dedicated dataframes and then outputting these into well-structured CSV files. This separation facilitated more focused and efficient analysis within each category.

Learnings and Insights:

- **Dataset Creation**: When no suitable dataset was readily available online, I learned to generate my own by exporting browser history data. This process taught me valuable skills in dataset acquisition and preparation, which are crucial for any data-driven project.
- **Data Manipulation**: Throughout this project, I honed my abilities to manipulate and analyze data using pandas DataFrames. This experience deepened my understanding of data structures and the power of Python for data science tasks.
- **Data Visualization**: Using Tableau, I explored various types of graphs and learned to select the most effective visual representations for different data insights. This practice was instrumental in translating complex data into understandable and actionable visual information.
- **Adaptive Learning**: One of the most significant learnings from this project was the need to remain adaptive and open to new solutions when faced with unexpected issues. Whether it was refining the data cleaning process or restructuring the code for better efficiency, the project was a continuous learning journey.

Through overcoming these challenges and embracing the learning process, I have gained a comprehensive skill set in data analysis and visualization, which I believe will be invaluable for future projects and professional endeavors in the field of data science.



## Future Work

The current iteration of the project provides a robust foundation for analyzing browser history, yet it involves a multi-step process that could be streamlined for enhanced user experience. Potential developments to elevate the project include:

1. **Browser Extension Development**: Creating a Chrome Extension or a similar add-on for other browsers would significantly simplify the user experience. With such an integration, users could gain insights into their browsing habits with a single click, directly within their browser environment.
2. **Automation of Data Visualization**: The current procedure for visual analysis requires several steps: forking the repository, generating browser history data, executing the Python scripts, and finally, creating visualizations in Tableau with the resulting CSV files. Although this workflow is manageable, it presents opportunities for further simplification. Automating the data visualization process would make the tool more accessible and user-friendly, reducing the barrier to entry for those less familiar with data analysis tools and methods.

In pursuit of these enhancements, the project aims to evolve into a more seamless and automated solution, bringing sophisticated browsing habit analysis to a wider audience with minimal setup requirements. These improvements would not only refine the user journey but also broaden the applicability of the tool for everyday use, making data-driven personal productivity insights readily available for all users.



## Contact Information or Credits

**References**:

- Chrome Web Store - Export Chrome History Extension: [Export Chrome History](https://chromewebstore.google.com/detail/export-chrome-history/dihloblpkeiddiaojbagoecedbfpifdj)



## License 

- Specify the license under which the project is released, if applicable.
