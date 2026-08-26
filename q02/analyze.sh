#!/bin/bash
[ -f "$1" ] || { echo "File not found" >&2; exit 1; }
tail -n +2 "$1" | awk -F, '$4>=500{print $3}' | sort | uniq -c | sort -k1,1nr -k2,2 | head -2 | awk '{print $2}'
tail -n +2 "$1" | awk -F, '{s+=$5}END{printf "%.2f\n",s/NR}'
