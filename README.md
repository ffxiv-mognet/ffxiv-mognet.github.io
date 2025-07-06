

## NOTES


#### searching for a quest's rowId by name
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

#### generate a quest list starting from the ending quest
```
% ./scripts/xiv-quest-scraper.py questList 66031 --count 7 --partQuestNo 2 

```

#### initialize a quest file
```
% ./scripts/xiv-quest-scraper.py dumpQuest 65958 > _collections/_quests/65958.md 
```

#### copy output to X11 clipboard
```
echo hello world | xclip -selection clipboard
```


#### find all referenced quest rowIds
```
grep -r rowId guide | cut -d':' -f3 | sort | uniq
```

#### dump quests that are referenced but not exist yet
```
for rowId in `grep -r rowId guide | cut -d':' -f3 | sort | uniq`; do
  if [ \! -e _collections/_quests/$rowId.md ]; then
    echo generating _collections/_quests/$rowId.md
    ./scripts/xiv-quest-scraper.py dumpQuest $rowId > _collections/_quests/$rowId.md 
  else
    echo skipping _collections/_quests/$rowId.md
  fi
done
```
