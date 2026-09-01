#!/usr/bin/env python3

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CSS to insert after hydration-badge
cigarettes_css = """.cigarettes-modern{background:rgba(30,41,59,.95);border:1px solid rgba(71,84,103,.6);border-radius:16px;padding:24px;box-shadow:0 10px 25px rgba(0,0,0,.3)}.cigarettes-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px}.cigarettes-header h2{font-size:1.4rem;font-weight:600;color:var(--ink);display:flex;align-items:center;gap:12px}.cigarettes-badge{padding:6px 16px;border-radius:9999px;background:rgba(64,224,208,.1);border:1px solid rgba(64,224,208,.3);color:rgba(64,224,208,.8);font-size:.75rem;font-weight:600}.cigarettes-display{text-align:center;margin-bottom:24px}.cigarettes-count{font-size:3.5rem;font-weight:900;color:var(--lime);line-height:1}.cigarettes-progress{margin-bottom:24px}.cigarettes-progress-bar{height:24px;background:rgba(26,40,65,.8);border-radius:8px;overflow:hidden;display:flex;border:1px solid rgba(71,84,103,.4)}.progress-segment{display:flex;align-items:center;justify-content:center;font-size:.65rem;font-weight:700;color:#000}.progress-segment.great{background:var(--lime);flex:1}.progress-segment.keep{background:rgba(158,171,193,.3);flex:2}.progress-segment.goal{background:var(--orange);flex:.5}.cigarettes-progress-labels{display:flex;justify-content:space-between;margin-top:8px;gap:8px;font-size:.7rem;color:var(--muted);font-weight:600}.cigarettes-actions{display:flex;gap:12px}.cigarettes-btn{min-height:44px;border:1px solid transparent;border-radius:8px;font-weight:700;flex:1;cursor:pointer;transition:all .2s}.cigarettes-btn-secondary{background:transparent;border-color:var(--line);color:var(--ink)}.cigarettes-btn-primary{background:var(--lime);color:#193100}.cigarettes-btn:active{transform:scale(.98)}.cigarettes-icon{width:24px;height:24px;display:grid;place-items:center;color:var(--orange);font-size:1.2rem}"""

search_text = ".hydration-badge{padding:6px 16px;border-radius:9999px;background:rgba(96,165,250,.1);border:1px solid rgba(96,165,250,.3);color:rgba(96,165,250,.8);font-size:.75rem;font-weight:600}"

if search_text in content:
    # Insert after hydration-badge
    new_content = content.replace(search_text, search_text + cigarettes_css)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✓ Successfully added cigarettes CSS classes")
else:
    print("✗ Could not find hydration-badge CSS")
