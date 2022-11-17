# Wikipedia Link Structure - Is it Developed in An Intuitive Way?

## Abstract
The purpose of this data analysis is to investigate the link structure of Wikipedia and analyse if it corresponds to how humans think Wikipedia is intuitive to use. From there, we are going to explore if Wikipedia, when developing the content of their pages, take this into consideration. This is going to be done in two main segmets of analysis. (1) Comparing the graph of the link structure of Wikipedia 2009 to a graph of how humans navigate the link structure of Wikipedia. The second graph is constructed from recorded games of Wikispeedia, a game where the task is to navigate from one page to another using only the links on each page respectively. (2) In the second part we compare the first graph from part one to a graph constructed of the same Wikipedia pages from 2022. Thus, we can compare the development of the pages over time. Depending ont the answer to part 1, we will analyse if the link structure has improved or decayed in relation to how humans navigate Wikipedia. The dataset represents a subset of all wikipedia pages. Pages representing the same subset is analysed for both time persiods.

## Research Questions
1. How well did the link structure of Wikipedia follow human intuition in 2009?
2. How has the Wikipedia link structure evolved between 2009 and 2022?

## Proposed additional datasets
In addition to the Wikispeedia dataset, we have scraped the same pages of Wikipedia as are represented in the links dataset of wikispeedia. We expect to find similar amount of links in the new dataset as in the old.

Processing the new version of the 4600 pages will include:
* Scraping the complete content of the pages with html tags
* Indetifying outgoing links of each page and creating a dataset with an origin column (representing the page of which the links are extracted) and a destination column (representing the links found on that page)
* Data size is expected to be similar to the dataset of 2009 which was ~3 MB


## Methods
To acomplish these goals, we intend to use the methods described below.

**Node2Vec**
Node2Vec is used to represent the graphs as vectors. When we have the graphs in vector embedding, we can more efficiently carry out...!
[Alt text](../../../../../../var/folders/ys/8zw_hvxx3fn29zqr94wz19gc0000gn/T/TemporaryItems/NSIRD_screencaptureui_XCyFtr/Screenshot%202022-11-17%20at%2020.01.18.png)


**PCA**



## Proposed timeline
A high level timeline follows below. 

**End of week 49**
Detailed investigation of the data
- All fundamental statistics and visualisations are developed.
- At this point, the investigation is at a point where we understand what parts are interesting to look further into. 

**End of week 50**
Data story in progress
- High level outline of descrition of data story.
- Plots and descriptive statistics fully prepared.

**End of week 51**
Datastory compleated 
- Write the full description of the story.
- Double check every task and make sure plots have all requiered attributs for effective visualisation. 

## Tasks of individual team members










