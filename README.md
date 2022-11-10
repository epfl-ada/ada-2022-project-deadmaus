# Identifying Missing Links in Wikipedia

## Abstract
When the user clicks or restarts on a page, we can infer that the user expects a link to the target or at least something related to the target, but it is missing. By analyzing the categories of the pages with missing links, we can also gain insight into which categories of Wikipedia pages are underdeveloped. 

Alternatively, a graph of Wikipedia articles can be developed where the edge weights are representative of how deficient the interconnectedness is between two nodes. For example, the edge weight between two nodes can be the number of times the user back clicks or restarts on one node while the target is on the other node. Another possible method of inferring missing links could be identifying that in the pattern “A;B;<;C”, B is missing a link to C. Graphical analysis of this proposed graph should reveal insights into where Wikipedia should channel its efforts into developing its pages.

## Our questions to you:
How could we potentially expand on this idea? 
- Suggestions: What “expected” links were missing in the Wikipedia pages from 2011? Have they been fixed in 2022
Will this be enough on its own? For the entire data story.
What do you think would be interesting to learn from this analysis?
Do you have any suggestions on how we might infer missing links in alternative ways?
One proposed method to create such a pair: Find terminal node from unfinished path; Find a word with high categorical (sub/super) similarity with this word where an outgoing edge does not exist.
Follow-up: Has this link been created in the Wikipedia today
