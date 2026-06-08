"""Generate SVG step illustrations for the process page."""
import os

OUT = os.path.dirname(__file__)

def browser(content, url="", title=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="520" viewBox="0 0 900 520">
  <defs>
    <clipPath id="frame"><rect width="900" height="520" rx="12"/></clipPath>
    <filter id="shadow"><feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="#000" flood-opacity="0.4"/></filter>
  </defs>
  <rect width="900" height="520" rx="12" fill="#1e1e2e" clip-path="url(#frame)"/>
  <!-- Chrome bar -->
  <rect width="900" height="44" fill="#2a2a3a"/>
  <!-- Traffic lights -->
  <circle cx="22" cy="22" r="6" fill="#ff5f57"/>
  <circle cx="42" cy="22" r="6" fill="#febc2e"/>
  <circle cx="62" cy="22" r="6" fill="#28c840"/>
  <!-- URL bar -->
  <rect x="100" y="10" width="700" height="24" rx="12" fill="#13131f"/>
  <text x="450" y="26" font-family="SF Mono, monospace" font-size="12" fill="#7a7a8a" text-anchor="middle">{url}</text>
  <!-- Content area -->
  {content}
</svg>'''

def terminal(lines, title="Terminal"):
    content_lines = ""
    y = 90
    for line in lines:
        color = "#28c840" if line.startswith("$") else ("#7c6ef7" if line.startswith("→") else ("#e8e8ed" if not line.startswith("#") else "#7a7a8a"))
        content_lines += f'<text x="32" y="{y}" font-family="SF Mono, monospace" font-size="13" fill="{color}">{line}</text>\n  '
        y += 22
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="520" viewBox="0 0 900 520">
  <rect width="900" height="520" rx="12" fill="#0d0d0f"/>
  <!-- Chrome -->
  <rect width="900" height="44" fill="#1a1a22"/>
  <circle cx="22" cy="22" r="6" fill="#ff5f57"/>
  <circle cx="42" cy="22" r="6" fill="#febc2e"/>
  <circle cx="62" cy="22" r="6" fill="#28c840"/>
  <text x="450" y="27" font-family="SF Pro, system-ui, sans-serif" font-size="13" fill="#7a7a8a" text-anchor="middle">{title}</text>
  <!-- Prompt line indicator -->
  <rect x="0" y="44" width="4" height="476" fill="#7c6ef7" opacity="0.5"/>
  {content_lines}
</svg>'''

# ── Step 1: GitHub PAT ──────────────────────────────────────────────────────
step1 = browser(url="github.com / Settings / Developer Settings / Personal access tokens", content='''
  <!-- Sidebar -->
  <rect x="0" y="44" width="220" height="476" fill="#161620"/>
  <text x="20" y="80" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a" font-weight="600">DEVELOPER SETTINGS</text>
  <rect x="0" y="88" width="220" height="1" fill="#2a2a3a"/>
  <rect x="0" y="89" width="4" height="36" fill="#7c6ef7"/>
  <rect x="0" y="89" width="220" height="36" fill="rgba(124,110,247,0.08)"/>
  <text x="20" y="113" font-family="SF Pro, system-ui" font-size="13" fill="#e8e8ed" font-weight="500">Personal access tokens</text>
  <text x="20" y="148" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">OAuth Apps</text>
  <text x="20" y="180" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">GitHub Apps</text>

  <!-- Main content -->
  <text x="260" y="90" font-family="SF Pro, system-ui" font-size="22" fill="#e8e8ed" font-weight="700">Personal access tokens (classic)</text>
  <text x="260" y="115" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">Tokens you have generated that can be used to access the GitHub API.</text>

  <!-- Generate button -->
  <rect x="680" y="70" width="190" height="34" rx="6" fill="#7c6ef7"/>
  <text x="775" y="91" font-family="SF Pro, system-ui" font-size="13" fill="#fff" font-weight="600" text-anchor="middle">Generate new token</text>

  <!-- Token list header -->
  <rect x="240" y="140" width="640" height="1" fill="#2a2a3a"/>
  <text x="260" y="175" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a" font-weight="600">TOKEN NAME</text>
  <text x="500" y="175" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a" font-weight="600">SCOPES</text>
  <text x="700" y="175" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a" font-weight="600">EXPIRES</text>
  <rect x="240" y="182" width="640" height="1" fill="#2a2a3a"/>

  <!-- Token row -->
  <rect x="240" y="183" width="640" height="50" fill="rgba(40,200,64,0.04)"/>
  <text x="260" y="214" font-family="SF Mono, monospace" font-size="13" fill="#e8e8ed">UX-CC-Trial</text>
  <rect x="490" y="200" width="60" height="20" rx="10" fill="rgba(40,200,64,0.15)"/>
  <text x="520" y="214" font-family="SF Pro, system-ui" font-size="11" fill="#28c840" text-anchor="middle">repo</text>
  <text x="700" y="214" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">No expiration</text>

  <!-- Callout box -->
  <rect x="240" y="260" width="640" height="80" rx="8" fill="rgba(124,110,247,0.08)" stroke="#7c6ef7" stroke-width="1" stroke-opacity="0.3"/>
  <text x="264" y="288" font-family="SF Pro, system-ui" font-size="13" fill="#7c6ef7" font-weight="600">💡 Use this token as your Git password</text>
  <text x="264" y="310" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">GitHub no longer accepts account passwords for Git operations.</text>
  <text x="264" y="328" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">Copy the token and paste it when prompted for a password in terminal.</text>
''')

# ── Step 2: Claude MCP Config ───────────────────────────────────────────────
step2 = browser(url="Claude Desktop → Settings → Developer → Edit Config", content='''
  <!-- Settings modal -->
  <rect x="60" y="60" width="780" height="430" rx="10" fill="#161620" stroke="#2a2a3a" stroke-width="1"/>
  <!-- Sidebar -->
  <rect x="60" y="60" width="180" height="430" rx="10 0 0 10" fill="#13131f"/>
  <text x="80" y="100" font-family="SF Pro, system-ui" font-size="12" fill="#7a7a8a" font-weight="600">SETTINGS</text>
  <text x="80" y="130" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">General</text>
  <text x="80" y="160" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">Appearance</text>
  <rect x="60" y="170" width="4" height="32" fill="#7c6ef7"/>
  <rect x="60" y="170" width="180" height="32" fill="rgba(124,110,247,0.1)"/>
  <text x="80" y="191" font-family="SF Pro, system-ui" font-size="13" fill="#e8e8ed" font-weight="500">Developer</text>
  <text x="80" y="220" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">Privacy</text>

  <!-- Content -->
  <text x="270" y="100" font-family="SF Pro, system-ui" font-size="18" fill="#e8e8ed" font-weight="700">Developer Settings</text>
  <rect x="255" y="115" width="570" height="1" fill="#2a2a3a"/>

  <text x="270" y="148" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">MCP Servers Configuration</text>
  <rect x="270" y="160" width="530" height="180" rx="8" fill="#0d0d0f" stroke="#2a2a3a" stroke-width="1"/>

  <!-- JSON content -->
  <text x="292" y="185" font-family="SF Mono, monospace" font-size="12" fill="#7a7a8a">{"{"}</text>
  <text x="292" y="205" font-family="SF Mono, monospace" font-size="12" fill="#7a7a8a">  "mcpServers"{"{"}</text>
  <text x="292" y="225" font-family="SF Mono, monospace" font-size="12" fill="#7a7a8a">    "figma": {"{"}</text>
  <text x="292" y="245" font-family="SF Mono, monospace" font-size="12" fill="#7a7a8a">      "command": </text>
  <text x="410" y="245" font-family="SF Mono, monospace" font-size="12" fill="#28c840">"npx"</text>
  <text x="292" y="265" font-family="SF Mono, monospace" font-size="12" fill="#7a7a8a">      "args": [</text>
  <text x="370" y="265" font-family="SF Mono, monospace" font-size="12" fill="#28c840">"-y", "figma-developer-mcp",</text>
  <text x="292" y="285" font-family="SF Mono, monospace" font-size="12" fill="#28c840">               "--figma-api-key=YOUR_KEY"</text>
  <text x="292" y="305" font-family="SF Mono, monospace" font-size="12" fill="#7a7a8a">      ]</text>
  <text x="292" y="325" font-family="SF Mono, monospace" font-size="12" fill="#7a7a8a">    {"}"},</text>

  <!-- Edit Config button -->
  <rect x="270" y="355" width="140" height="34" rx="6" fill="#2a2a3a"/>
  <text x="340" y="377" font-family="SF Pro, system-ui" font-size="13" fill="#e8e8ed" text-anchor="middle">Edit Config</text>

  <!-- Connected indicator -->
  <circle cx="448" cy="372" r="6" fill="#28c840"/>
  <text x="462" y="377" font-family="SF Pro, system-ui" font-size="13" fill="#28c840">Figma MCP connected</text>
''')

# ── Step 3: Terminal git clone ──────────────────────────────────────────────
step3 = terminal(title="Terminal — zsh", lines=[
    "# Navigate to your projects folder",
    "$ cd /Users/yourname/Explorations",
    "",
    "# Clone the repository from GitHub",
    "$ git clone https://github.com/akanksha-designs/UX-CC-Trial.git",
    "→ Cloning into 'UX-CC-Trial'...",
    "→ remote: Enumerating objects: 15, done.",
    "→ Receiving objects: 100% (15/15), 4.65 KiB | 2.33 MiB/s, done.",
    "",
    "# Move into the project folder",
    "$ cd UX-CC-Trial",
    "",
    "# Set your identity (first time only)",
    "$ git config user.name \"Your Name\"",
    "$ git config user.email \"you@example.com\"",
    "",
    "# Start local dev server",
    "$ python3 -m http.server 3001",
    "→ Serving HTTP on 0.0.0.0 port 3001 ...",
])

# ── Step 4: Branching ───────────────────────────────────────────────────────
step4 = terminal(title="Terminal — branching strategy", lines=[
    "# Always start from the latest main",
    "$ git checkout main",
    "→ Switched to branch 'main'",
    "",
    "$ git pull origin main",
    "→ Already up to date.",
    "",
    "# Create a new branch for your design change",
    "$ git checkout -b design/update-hero-colours",
    "→ Switched to a new branch 'design/update-hero-colours'",
    "",
    "# Confirm you're on the right branch",
    "$ git branch",
    "→   main",
    "→ * design/update-hero-colours   ← you are here",
    "",
    "# Now make changes — main stays untouched",
    "# Each branch → separate Vercel preview URL",
])

# ── Step 5: Vibe-coding in Claude ──────────────────────────────────────────
step5 = browser(url="Claude Code — UX-CC-Trial project", content='''
  <!-- Split layout -->
  <!-- Left: Claude chat -->
  <rect x="0" y="44" width="430" height="476" fill="#13131f"/>
  <text x="20" y="80" font-family="SF Pro, system-ui" font-size="14" fill="#e8e8ed" font-weight="600">Claude Code</text>
  <rect x="0" y="88" width="430" height="1" fill="#2a2a3a"/>

  <!-- User message -->
  <rect x="20" y="104" width="390" height="80" rx="8" fill="#1e1e2e"/>
  <text x="36" y="126" font-family="SF Pro, system-ui" font-size="12" fill="#7a7a8a" font-weight="600">YOU</text>
  <text x="36" y="146" font-family="SF Pro, system-ui" font-size="13" fill="#e8e8ed">Update the hero heading to use the</text>
  <text x="36" y="164" font-family="SF Pro, system-ui" font-size="13" fill="#e8e8ed">Primary/500 colour from this Figma</text>
  <text x="36" y="180" font-family="SF Mono, monospace" font-size="11" fill="#7c6ef7">figma.com/design/abc123/Brand-Tokens</text>

  <!-- Claude response -->
  <rect x="20" y="200" width="390" height="140" rx="8" fill="rgba(124,110,247,0.06)" stroke="#7c6ef7" stroke-width="1" stroke-opacity="0.2"/>
  <text x="36" y="222" font-family="SF Pro, system-ui" font-size="12" fill="#7c6ef7" font-weight="600">CLAUDE</text>
  <text x="36" y="244" font-family="SF Pro, system-ui" font-size="13" fill="#e8e8ed">I can see the Figma file. The Primary/500</text>
  <text x="36" y="262" font-family="SF Pro, system-ui" font-size="13" fill="#e8e8ed">token is <tspan font-family="SF Mono, monospace" fill="#28c840">#4f3fbf</tspan>. Updating style.css now...</text>
  <rect x="36" y="276" width="360" height="52" rx="6" fill="#0d0d0f"/>
  <text x="52" y="296" font-family="SF Mono, monospace" font-size="11" fill="#7a7a8a">.hero-heading em {"{"}</text>
  <text x="52" y="312" font-family="SF Mono, monospace" font-size="11" fill="#28c840">  color: var(--color-primary-500);</text>
  <text x="52" y="328" font-family="SF Mono, monospace" font-size="11" fill="#7a7a8a">{"}"}</text>

  <!-- File edited indicator -->
  <rect x="20" y="356" width="390" height="32" rx="6" fill="rgba(40,200,64,0.08)"/>
  <text x="36" y="377" font-family="SF Pro, system-ui" font-size="12" fill="#28c840">✓ Edited style.css · Live at localhost:3001</text>

  <!-- Divider -->
  <rect x="430" y="44" width="1" height="476" fill="#2a2a3a"/>

  <!-- Right: Figma frame preview -->
  <rect x="431" y="44" width="469" height="476" fill="#0f0f11"/>
  <text x="460" y="80" font-family="SF Pro, system-ui" font-size="14" fill="#e8e8ed" font-weight="600">Figma — Brand Tokens</text>
  <rect x="431" y="88" width="469" height="1" fill="#2a2a3a"/>

  <!-- Colour token grid -->
  <text x="455" y="118" font-family="SF Pro, system-ui" font-size="12" fill="#7a7a8a" font-weight="600">PRIMARY</text>
  <rect x="455" y="128" width="50" height="50" rx="6" fill="#1a1360"/>
  <text x="455" y="194" font-family="SF Mono, monospace" font-size="10" fill="#7a7a8a">100</text>
  <rect x="515" y="128" width="50" height="50" rx="6" fill="#2d229e"/>
  <text x="515" y="194" font-family="SF Mono, monospace" font-size="10" fill="#7a7a8a">200</text>
  <rect x="575" y="128" width="50" height="50" rx="6" fill="#3d2fc4"/>
  <text x="575" y="194" font-family="SF Mono, monospace" font-size="10" fill="#7a7a8a">300</text>
  <rect x="635" y="128" width="50" height="50" rx="6" fill="#4538d4"/>
  <text x="635" y="194" font-family="SF Mono, monospace" font-size="10" fill="#7a7a8a">400</text>
  <rect x="695" y="120" width="66" height="66" rx="8" fill="#4f3fbf" stroke="#7c6ef7" stroke-width="2"/>
  <text x="728" y="202" font-family="SF Mono, monospace" font-size="10" fill="#7c6ef7" text-anchor="middle" font-weight="700">500 ←</text>
  <rect x="771" y="128" width="50" height="50" rx="6" fill="#6b5fd4"/>
  <text x="771" y="194" font-family="SF Mono, monospace" font-size="10" fill="#7a7a8a">600</text>

  <text x="455" y="230" font-family="SF Mono, monospace" font-size="11" fill="#7c6ef7">#4f3fbf — Primary/500</text>
  <text x="455" y="248" font-family="SF Pro, system-ui" font-size="12" fill="#7a7a8a">Used for: headings, CTA highlights, accent text</text>
''')

# ── Step 6: Localhost review ────────────────────────────────────────────────
step6 = browser(url="localhost:3001", content='''
  <!-- Site chrome inside browser -->
  <!-- Nav -->
  <rect x="0" y="44" width="900" height="52" fill="rgba(15,15,17,0.95)"/>
  <rect x="0" y="95" width="900" height="1" fill="#2a2a3a"/>
  <text x="52" y="76" font-family="SF Pro, system-ui" font-size="16" fill="#7c6ef7" font-weight="700">AK</text>
  <text x="680" y="76" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">Work</text>
  <text x="740" y="76" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">About</text>
  <text x="800" y="76" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">Contact</text>

  <!-- Hero -->
  <rect x="0" y="96" width="900" height="300" fill="#0f0f11"/>
  <text x="52" y="150" font-family="SF Pro, system-ui" font-size="11" fill="#7c6ef7" font-weight="600" letter-spacing="2">UX DESIGNER · DESIGN SYSTEMS · AI WORKFLOWS</text>
  <text x="52" y="195" font-family="SF Pro, system-ui" font-size="38" fill="#e8e8ed" font-weight="700">Designing at the</text>
  <text x="52" y="238" font-family="SF Pro, system-ui" font-size="38" fill="#e8e8ed" font-weight="700">intersection of</text>
  <text x="52" y="281" font-family="SF Pro, system-ui" font-size="38" fill="#4f3fbf" font-weight="700" font-style="italic">clarity and complexity.</text>
  <rect x="52" y="310" width="120" height="36" rx="8" fill="#7c6ef7"/>
  <text x="112" y="333" font-family="SF Pro, system-ui" font-size="13" fill="#fff" text-anchor="middle" font-weight="600">View Work</text>

  <!-- Updated indicator -->
  <rect x="660" y="390" width="220" height="80" rx="8" fill="#13131f" stroke="#28c840" stroke-width="1"/>
  <circle cx="678" cy="415" r="5" fill="#28c840"/>
  <text x="692" y="419" font-family="SF Pro, system-ui" font-size="12" fill="#28c840" font-weight="600">Live preview updated</text>
  <text x="678" y="440" font-family="SF Pro, system-ui" font-size="12" fill="#7a7a8a">style.css — hero colour</text>
  <text x="678" y="458" font-family="SF Pro, system-ui" font-size="11" fill="#7a7a8a">Review before committing</text>
''')

# ── Step 7: Commit & PR ─────────────────────────────────────────────────────
step7 = terminal(title="Terminal — commit, push, open PR", lines=[
    "# Stage all changed files",
    "$ git add .",
    "",
    "# Commit with a clear message",
    '$ git commit -m "Update hero colour to Primary/500 from Figma tokens"',
    "→ [design/update-hero-colours 3f7a2c1] Update hero colour...",
    "→ 1 file changed, 2 insertions(+), 2 deletions(-)",
    "",
    "# Push the branch to GitHub",
    "$ git push -u origin design/update-hero-colours",
    "→ Branch set up to track remote branch.",
    "→ To https://github.com/akanksha-designs/UX-CC-Trial.git",
    "→  * [new branch]  design/update-hero-colours → design/update-hero-colours",
    "",
    "# Go to GitHub → you'll see: 'Compare & pull request'",
    "# Fill in: what changed, Figma link, before/after screenshots",
    "# Submit PR → Vercel posts a preview URL automatically",
])

# ── Step 8: PR with Vercel preview ─────────────────────────────────────────
step8 = browser(url="github.com/akanksha-designs/UX-CC-Trial/pull/1", content='''
  <!-- PR title -->
  <text x="30" y="80" font-family="SF Pro, system-ui" font-size="18" fill="#e8e8ed" font-weight="700">Update hero colour to Primary/500 from Figma tokens</text>
  <rect x="30" y="90" width="60" height="22" rx="11" fill="rgba(40,200,64,0.15)"/>
  <text x="60" y="105" font-family="SF Pro, system-ui" font-size="11" fill="#28c840" text-anchor="middle">Open</text>
  <text x="100" y="105" font-family="SF Pro, system-ui" font-size="12" fill="#7a7a8a">akanksha wants to merge 1 commit into main from design/update-hero-colours</text>

  <rect x="30" y="118" width="840" height="1" fill="#2a2a3a"/>

  <!-- Vercel bot comment -->
  <rect x="30" y="130" width="840" height="140" rx="8" fill="#13131f" stroke="#2a2a3a" stroke-width="1"/>
  <circle cx="58" cy="162" r="16" fill="#0d0d0f"/>
  <text x="58" y="167" font-family="SF Pro, system-ui" font-size="10" fill="#e8e8ed" text-anchor="middle">▲</text>
  <text x="86" y="158" font-family="SF Pro, system-ui" font-size="13" fill="#e8e8ed" font-weight="600">vercel[bot]</text>
  <text x="200" y="158" font-family="SF Pro, system-ui" font-size="12" fill="#7a7a8a">commented 1 minute ago</text>

  <text x="56" y="185" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">🔍 The latest updates on your projects. Learn more about Vercel for Git.</text>

  <rect x="56" y="198" width="790" height="1" fill="#2a2a3a"/>
  <text x="70" y="220" font-family="SF Pro, system-ui" font-size="12" fill="#7a7a8a" font-weight="600">NAME</text>
  <text x="400" y="220" font-family="SF Pro, system-ui" font-size="12" fill="#7a7a8a" font-weight="600">STATUS</text>
  <text x="560" y="220" font-family="SF Pro, system-ui" font-size="12" fill="#7a7a8a" font-weight="600">PREVIEW URL</text>
  <rect x="56" y="226" width="790" height="1" fill="#2a2a3a"/>

  <text x="70" y="250" font-family="SF Pro, system-ui" font-size="13" fill="#e8e8ed">UX-CC-Trial</text>
  <rect x="390" y="238" width="80" height="22" rx="11" fill="rgba(40,200,64,0.15)"/>
  <text x="430" y="253" font-family="SF Pro, system-ui" font-size="11" fill="#28c840" text-anchor="middle">✓ Ready</text>
  <text x="560" y="250" font-family="SF Mono, monospace" font-size="12" fill="#7c6ef7">ux-cc-trial-git-design-update.vercel.app</text>

  <!-- Approve & merge -->
  <rect x="30" y="285" width="840" height="80" rx="8" fill="#13131f" stroke="#28c840" stroke-width="1" stroke-opacity="0.4"/>
  <text x="50" y="318" font-family="SF Pro, system-ui" font-size="14" fill="#e8e8ed" font-weight="600">✓ Review approved · Ready to merge</text>
  <text x="50" y="342" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">1 approval · 0 requested changes · All checks passed</text>
  <rect x="650" y="298" width="200" height="36" rx="6" fill="#28c840"/>
  <text x="750" y="321" font-family="SF Pro, system-ui" font-size="13" fill="#000" text-anchor="middle" font-weight="700">Merge pull request</text>
''')

# ── Step 9: Live deployed site ──────────────────────────────────────────────
step9 = browser(url="ux-cc-trial.vercel.app", content='''
  <!-- Deployed site nav -->
  <rect x="0" y="44" width="900" height="52" fill="rgba(15,15,17,0.95)"/>
  <rect x="0" y="95" width="900" height="1" fill="#2a2a3a"/>
  <text x="52" y="76" font-family="SF Pro, system-ui" font-size="16" fill="#7c6ef7" font-weight="700">AK</text>
  <text x="680" y="76" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">Work</text>
  <text x="740" y="76" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">About</text>
  <text x="800" y="76" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">Contact</text>

  <!-- Hero -->
  <rect x="0" y="96" width="900" height="300" fill="#0f0f11"/>
  <text x="52" y="150" font-family="SF Pro, system-ui" font-size="11" fill="#7c6ef7" font-weight="600" letter-spacing="2">UX DESIGNER · DESIGN SYSTEMS · AI WORKFLOWS</text>
  <text x="52" y="195" font-family="SF Pro, system-ui" font-size="38" fill="#e8e8ed" font-weight="700">Designing at the</text>
  <text x="52" y="238" font-family="SF Pro, system-ui" font-size="38" fill="#e8e8ed" font-weight="700">intersection of</text>
  <text x="52" y="281" font-family="SF Pro, system-ui" font-size="38" fill="#4f3fbf" font-weight="700" font-style="italic">clarity and complexity.</text>
  <rect x="52" y="310" width="120" height="36" rx="8" fill="#7c6ef7"/>
  <text x="112" y="333" font-family="SF Pro, system-ui" font-size="13" fill="#fff" text-anchor="middle" font-weight="600">View Work</text>

  <!-- Deploy success banner -->
  <rect x="0" y="396" width="900" height="78" fill="#13131f"/>
  <rect x="0" y="396" width="900" height="1" fill="#2a2a3a"/>
  <rect x="0" y="396" width="4" height="78" fill="#28c840"/>
  <text x="28" y="425" font-family="SF Pro, system-ui" font-size="14" fill="#28c840" font-weight="600">✓ Production deployment complete</text>
  <text x="28" y="448" font-family="SF Pro, system-ui" font-size="13" fill="#7a7a8a">Deployed from design/update-hero-colours → main · 34 seconds ago</text>
  <text x="28" y="466" font-family="SF Mono, monospace" font-size="12" fill="#7c6ef7">ux-cc-trial.vercel.app  ·  commit 3f7a2c1</text>
''')

# Write all files
steps = [
    ("step1-github-pat.svg", step1),
    ("step2-mcp-config.svg", step2),
    ("step3-git-clone.svg", step3),
    ("step4-branching.svg", step4),
    ("step5-vibe-coding.svg", step5),
    ("step6-localhost.svg", step6),
    ("step7-commit-push.svg", step7),
    ("step8-pr-vercel.svg", step8),
    ("step9-deployed.svg", step9),
]

for filename, content in steps:
    path = os.path.join(OUT, filename)
    with open(path, "w") as f:
        f.write(content)
    print(f"✓ {filename}")

print("\nAll done.")
