
if [ -f README.md ]; then
    pandoc README.md -o README.org
    git add README.org
fi
