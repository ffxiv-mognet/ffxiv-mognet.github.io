{% assign q = site.quests | where:"questId", {{include.questId}} | first %}
{{q.content | markdownify}}
