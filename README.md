# FastNews
FastNews(http://52.10.183.132/) is a news article recommendation system that adapts to personalized needs by adaptively learning users' interests in reading articles.

The system consists of the following four components:

1. A crawler that scrapes the news webpages and extracts the important components. The components are sorted as titles, text, dates etc.
2. A parser system that extracts keywords with the help of NLP libraries (in order to reject most common words and such) that will represent the article content.
3. A recommendation system that queries readers' interested keywords in our database of up-to-date articles.
4. User interfaces. In this project, we have a django/Python based webserver and a Javascript based Chrome extension
