# 192. Word Frequency
awk '{ for (i=1; i<=NF; i++) { count[$i]++ } } END { for (word in count) print word, count[word] }' words.txt | sort -k2,2nr

# 193. Valid Phone Numbers
grep -e "^[0-9]\{3\}\-[0-9]\{3\}\-[0-9]\{4\}$" -e "^([0-9]\{3\}) [0-9]\{3\}\-[0-9]\{4\}$" file.txt

# 194. Transpose File
awk '{for (i=1; i<=NF; i++) {if (NR==1) {arr[i]=$i} else {arr[i]=arr[i] " " $i}}} END {for (i=1; i<=NF; i++) {print arr[i]}}' file.txt

# 195. Tenth Line
awk 'NR==10' file.txt