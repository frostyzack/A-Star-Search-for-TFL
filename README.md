# A Star Search for TFL
## **A Star search algorithm implemented on an adjacency list (TFL London Underground Map)**
---
### *Abstract notes on the use of A Star Search variables in this project*

#### G Score for each node is the **time taken** to go from one node to the next node, this is obtained from [TFL Unified API](https://api.tfl.gov.uk/swagger/ui/index.html "TFL Unified API"), for this example an authorisation token is not required.

#### H (Heuristic) Score for each node is the Eucledian product of a node and its next neighbour's cartesian co-ordinates (X,Y), this is obtained from [Openstreetmaps](https://wiki.openstreetmap.org/wiki/List_of_London_Underground_stations "List of Underground Stations") and [github.com/jamesstonehill](https://github.com/jamesstonehill/london-underground-stations-with-ics-codes/blob/master/stations.csv), this also includes TFL Station ICS codes which are needed for each API request.

#### F Score is the sum of the G and H scores, read more about the A Star Search [here](https://brilliant.org/wiki/a-star-search/ "Brilliant.com explanation").

---
### Limitations and considerations.
- This is an unfinished school project.
- Heuristic function used is not the best nor most efficient method for node cost calculation.
- Adjacency list is incomplete and does not include all stations (I cant be arsed).
- The way I made the adjacency list is very inefficient, instead of writing 300+ object instansiations, I could've read them in a for loop to generate the objects from an external file, you might want to do this for optimisation purposes.
- No GUI


Thank you, please consider buying my onlyfans x
