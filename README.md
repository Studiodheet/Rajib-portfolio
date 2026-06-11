# Rajib Moazzam - Portfolio

A static portfolio site. No build step, no dependencies. Edit the HTML, push, done.

## Files

- `index.html` - homepage (hero + project sections + outro)
- `about.html` - about page
- `styles.css` - all styling; colours and fonts are CSS variables at the top
- `images/` - drop logos and screenshots here (create the folder when needed)

## Editing

- Every project section in `index.html` is marked with a comment like
  `<!-- ============ PROJECT: WAGGLE ============ -->`.
  Duplicate a whole section to add a project; delete one to remove it.
- Replace any paragraph starting with "Placeholder:" with your real copy.
- To swap a text logo for an image: put the SVG/PNG in `images/`, then inside
  the `.logo` div use `<img src="images/logo.svg" alt="Name" height="32">`.
- Colours and fonts live in the `:root` block at the top of `styles.css`.

## Preview locally

From the project folder:

    python3 -m http.server 8000

Then open http://localhost:8000 in your browser.

## Deploy

Push to GitHub, import the repo in Vercel, framework preset "Other",
no build command, output directory left blank. Every `git push` redeploys.
