# Comprehensive User Browser History Analysis

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

- List the software, programming languages, and tools used in the project (e.g., Python, R, Jupyter Notebook, Excel, specific libraries or frameworks).



## Installation and Setup

- Describe the source of your data.
- Include links or references to the data, if publicly available.



## How to Run the Project

- Detailed instructions on how to run your analysis.
- Include any necessary commands or scripts.



## File and Directory Structure

- Explain the structure of your project’s directories and files.
- Describe the purpose of key folders and files for easier navigation.



## Analysis and Results

- Summarize the findings or results of the data analysis.
- Include key insights, charts, or graphs if applicable.



## Challenges and Learnings

- Mention any challenges faced during the project and how you addressed them.
- Share any significant learnings or surprises from the project.



## Future Work

- Discuss potential extensions or future directions for the project.

  

## Contact Information or Credits

- Provide your contact information or acknowledge contributions from others.

**References**:

- Chrome Web Store - Export Chrome History Extension: [Export Chrome History](https://chromewebstore.google.com/detail/export-chrome-history/dihloblpkeiddiaojbagoecedbfpifdj)



## License 

- Specify the license under which the project is released, if applicable.
