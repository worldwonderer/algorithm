
# @Title: 有效电话号码 (Valid Phone Numbers)
# @Author: 18015528893
# @Date: 2021-02-01 22:37:00
# @Runtime: 8 ms
# @Memory: 3.1 MB

# Read from the file file.txt and output all valid phone numbers to stdout.
egrep '^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$' file.txt
