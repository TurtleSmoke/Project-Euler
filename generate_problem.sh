problemNumber=$(echo "$1" | sed 's/^0*//')
content=$(curl -L https://projecteuler.net/problem="$problemNumber")
problemTitle=$(echo "$content" | tr -d '\r\n' | sed -E 's/.*<h2>([^<]*)<\/h2>.*/\1/g')

mkdir mdbook_src/problems/problem_"$1"
touch mdbook_src/problems/problem_"$1"/problem.md
touch mdbook_src/problems/problem_"$1"/solution1.md
touch mdbook_src/problems/problem_"$1"/solution.md

mkdir problems/problem_"$1"
touch problems/problem_"$1"/solution1.py

echo -e "# ["$problemTitle"](https://projecteuler.net/problem=$problemNumber)\n\n>" >> mdbook_src/problems/problem_"$1"/problem.md
echo -e "# Brute force" >> mdbook_src/problems/problem_"$1"/solution1.md
echo -e "# Solution\n---\n\n> \n\n---" >> mdbook_src/problems/problem_"$1"/solution.md

echo "    - [Problem "$problemNumber": "$problemTitle"](problems/problem_"$1"/problem.md)" >> mdbook_src/SUMMARY.md
echo "        - [Brute force](problems/problem_"$1"/solution1.md)" >> mdbook_src/SUMMARY.md
echo "        - [Solution](problems/problem_"$1"/solution.md)" >> mdbook_src/SUMMARY.md

echo -e "\n\nif __name__ == \"__main__\":\n    print()" > problems/problem_"$1"/solution1.py
