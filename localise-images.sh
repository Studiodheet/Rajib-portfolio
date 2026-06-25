#!/usr/bin/env bash
# Downloads every Squarespace CDN image referenced in ANY .html file
# in this folder, saves them to images/, and rewrites the HTML to use
# the local copies. Safe to run multiple times — existing files are kept.
#
# Run from the project folder:  bash localise-images.sh
set -e
mkdir -p images

# Collect all unique Squarespace URLs from every .html file in this folder
urls=$(grep -ohE 'https://images\.squarespace-cdn\.com/[^"]+' *.html 2>/dev/null | sort -u)

if [ -z "$urls" ]; then
  echo "No Squarespace CDN URLs found in any .html file. Nothing to do."
  exit 0
fi

echo "$urls" | while read -r url; do
  # Strip query string for cleaner filenames, then sanitise
  name=$(basename "${url%%\?*}" | sed 's/%20/-/g; s/+/-/g; s/[^A-Za-z0-9._-]//g')
  file="images/${name}"

  # Skip download if we already have the file
  if [ -f "$file" ]; then
    echo "Have: $file"
  else
    echo "Get:  $file"
    curl -sL "$url" -o "$file"
  fi

  # Rewrite every HTML file to point at the local copy.
  # macOS vs Linux sed have different -i syntax; this works on both.
  esc=$(printf '%s' "$url" | sed 's/[&/\]/\\&/g')
  for htmlfile in *.html; do
    if [ -f "$htmlfile" ]; then
      sed -i '' "s|$esc|$file|g" "$htmlfile" 2>/dev/null || sed -i "s|$esc|$file|g" "$htmlfile"
    fi
  done
done

echo ""
echo "Done. Review your pages, then:"
echo "  git add . && git commit -m 'Localise case study images' && git push"
