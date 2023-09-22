# Introduction 
This project intends to be a PoC for a portfolio management product that takes the AI technology and infrastructure to financial Advisors so that they can leverage their domain knowledge as well as the AI for better Asset Management.

# Tech Stack
LangChain, Streamlit

# Getting Started
Motivation is to create a Portfolio Management Service integrated that can be leveraged by financial advisors to use AI for Asset Management without having the deep knowledge of AI/ML.

What the product offers -
Data -
a) Fundamental data of the stocks of various exchanges by time and volume for last two decades.

Data Cleaning and Engineering -
a) Capability to clean and normalize data for various recommendation models.
b) Adding more mathematical features like integral derivatives over the fundamental features.

Range of trained ML and AI Models -
a) They can train/reuse a combination of models like decision tree to get the top n stocks and their weightage to invest in for t period of time. b) The software can use the capabilities of chatGPT to eliminate few of the stocks from the selected stocks using sentiment analysis.

Strong Back testing Framework -
a) The product will offer a strong unbiased back testing framework to verify that the model that the user came up with is working as per expected.

Create Automated PPT of Recommended Stocks
a) Create the ppt explaining why the given n stocks were selected and their financial analysis.

Tracking the portfolio -
a) The tracking mechanism will actively do news and sentiment analysis and recommend re-balancing of the portfolio. The tracking mechanism can be customized as per user needs.

# Contribute
Feel free to create a branch in this repo and share it's link to folks to socialize. Since at any point
we should not be holding NDA'ed code in here should be safe to share this repo around and extend access(es) as needed.

A general branch naming convention we could use is poc/{author-alias}/{poc-title} or simple poc/{poc-title} since author is implicit from
git history.
