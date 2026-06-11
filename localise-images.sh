#!/usr/bin/env bash
# Downloads every Squarespace CDN image referenced in index.html into images/
# and rewrites index.html to use the local copies.
# Run once from the project folder:  bash localise-images.sh
set -e
mkdir -p images
i=0
grep -o 'https://images\.squarespace-cdn\.com/[^"]*' index.html | sort -u | while read -r url; do
  i=$((i+1))
  # Build a clean local filename from the original name
  name=$(basename "${url%%\?*}" | sed 's/%20/-/g; s/+/-/g; s/[^A-Za-z0-9._-]//g')
  file="images/${name}"
  echo "Downloading $file"
  curl -sL "$url" -o "$file"
  # Escape for sed and swap the URL for the local path
  esc=$(printf '%s' "$url" | sed 's/[&/\]/\\&/g')
  sed -i '' "s|$esc|$file|g" index.html 2>/dev/null || sed -i "s|$esc|$file|g" index.html
done
echo "Done. Review the site, then: git add . && git commit -m 'Localise images' && git push"
