# UX-CC-Trial

A live demo of a designer's end-to-end workflow:

```
Figma  →  Claude Code  →  localhost  →  git push  →  Vercel (auto-deploy)
```

## The workflow

1. **Design in Figma** — make a visual change (colour, layout, component)
2. **Open Claude Code** — share the Figma URL or screenshot; describe the change
3. **Claude edits the code** — `index.html` / `style.css` / `script.js` update live on localhost
4. **Review on localhost** — open `http://localhost:3001` to verify
5. **Commit & push** to the `design/` branch
6. **Vercel auto-deploys** a preview URL — share with stakeholders
7. **Merge to `main`** — goes live

## Running locally

```bash
# Python (no install needed)
python3 -m http.server 3001

# or with Node
npx serve -l 3001 .
```

Open http://localhost:3001

## Branch strategy

| Branch | Purpose |
|--------|---------|
| `main` | Production — deploys to live Vercel URL |
| `design/*` | Feature branches for design changes — get Vercel preview URLs |

## Stack

- Plain HTML · CSS · JS — no build step, no framework
- Deployed on Vercel via GitHub integration
- Designed in Figma, coded with Claude Code
