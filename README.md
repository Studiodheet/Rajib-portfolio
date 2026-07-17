# Rajib Moazzam — Personal Portfolio

Static HTML/CSS. No build step. Same design system as the Studio Dheet site (white/black, mint #A4FCA7, Cormorant Garamond + Inter) but framed as a personal portfolio.

## Pages

- index.html — case studies listing (homepage)
- brightlocal.html
- evolution.html
- halal-screener.html
- nisba-brand.html
- styles.css — shared stylesheet

## Images

Local image paths match the existing Studio Dheet portfolio repo exactly. Copy the images folder over from your existing repo:

```
cp -R ~/portfolio/images ~/rajib-portfolio/images
```

Squarespace-hosted images (TaylorMade, Amex, TFG, ISS, Sky Bet, Halal Screener carousel) are referenced by absolute URL and need nothing.

## Deploy

```
cd ~
unzip -o ~/Downloads/rajib-portfolio.zip
cd rajib-portfolio
cp -R ~/portfolio/images ./images
git init
git add .
git commit -m "Personal portfolio v1"
```

Create a new empty repo on GitHub (e.g. Studiodheet/rajib-portfolio), then:

```
git remote add origin git@github.com:Studiodheet/rajib-portfolio.git
git branch -M main
git push -u origin main
```

Then in Vercel: Add New Project, import rajib-portfolio, framework preset "Other", deploy. Done.

## Before going live

1. Check the LinkedIn URL in the nav and footer (currently linkedin.com/in/rajibmoazzam) and swap in your actual profile URL.
2. Check the contact email (currently rajib@studiodheet.com). Swap for a personal address if you want the job-search version fully separate from the studio.
