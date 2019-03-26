#!/usr/bin/env bash

curl --request POST --url $(cat credentials.txt) --header 'content-type: application/json' --data "{
    \"content\": \"$(~/dev/block-out-menu/index.py)\"
}"

