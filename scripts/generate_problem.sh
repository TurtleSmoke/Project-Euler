#!/bin/bash

# shellcheck disable=SC2001
problemNumber=$(echo "$1" | sed 's/^0*//')
content=$(curl -L https://projecteuler.net/problem="$problemNumber")
problemTitle=$(echo "$content" | tr -d '\r\n' | sed -E 's/.*<h2>([^<]*)<\/h2>.*/\1/g')

mkdir mdbook_src/problems/problem_"$1"
touch mdbook_src/problems/problem_"$1"/problem.md
touch mdbook_src/problems/problem_"$1"/solution1.md
touch mdbook_src/problems/problem_"$1"/solution.md

mkdir problems/problem_"$1"
touch problems/problem_"$1"/solution1.py

echo -e "# [""$problemTitle""](https://projecteuler.net/problem=""$problemNumber"")\n\n>" >> mdbook_src/problems/problem_"$1"/problem.md
echo -e "# Brute force" >> mdbook_src/problems/problem_"$1"/solution1.md
echo -e "# Solution\n---\n\n> \n\n---" >> mdbook_src/problems/problem_"$1"/solution.md

last_lines="$(tail -n 2 mdbook_src/SUMMARY.md)"

head -n -2 mdbook_src/SUMMARY.md > tmp && mv tmp mdbook_src/SUMMARY.md
{
  echo "    - [Problem ""$problemNumber"": ""$problemTitle""](problems/problem_""$1""/problem.md)"
  echo "        - [Brute force](problems/problem_""$1""/solution1.md)"
  echo "        - [Solution](problems/problem_""$1""/solution.md)"
  echo "$last_lines"
} >> mdbook_src/SUMMARY.md

problemFunction=$(echo "$problemTitle" | sed 's/[ -]/_/g' | tr '[:upper:]' '[:lower:]')

echo -e "def ""$problemFunction""():\n\nif __name__ == \"__main__\":\n    print(""$problemFunction""())" > problems/problem_"$1"/solution1.py
