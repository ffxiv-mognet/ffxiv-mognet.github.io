#!/usr/bin/env bash 



curl -v $1 \
  -O \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'Referer: https://imgur.com/' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="133", "Not(A:Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0'