
# @Title: 统计词频 (Word Frequency)
# @Author: 18015528893
# @Date: 2021-02-01 22:22:42
# @Runtime: 0 ms
# @Memory: 3.7 MB

# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | tr -s " " "\n" | sort -r | uniq -c | sort -r| awk '{print $2" "$1}'
