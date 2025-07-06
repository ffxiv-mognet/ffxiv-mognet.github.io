

## NOTES


searching for a quest's rowId by name:
```
function findq { 
eval ./scripts/xiv-quest-scraper.py findQuest --name \"$@\" | jq -r '.[] | "\(.["#"]): \(.Name)"'; 
}
```
e.g.:
```
% findq beyond the great wall
67982: Beyond the Great Wall
```



