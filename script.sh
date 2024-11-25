#!/bin/bash

echo "# test_two" >> README.md
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/HazemHussien1/test_two.git
git push -u origin main
