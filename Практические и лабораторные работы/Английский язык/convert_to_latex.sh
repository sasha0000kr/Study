#!/bin/bash
pandoc -r markdown-auto_identifiers -w latex $1.md -o $1.tex
echo "Complete!"