# Long-form SEO guides at /guides/<slug>/ (not linked from nav; reached via sitemap, llms.txt and search).
# Source markdown: _src/guides/md/*.md (front matter + limited markdown). exec'd by build.py.
import glob as _glob, re as _re, datetime as _dt

GUIDE_DIR = '_src/guides/md'
GUIDE_DATE = '2026-10-19'
GUIDE_CATS = ['Campaigns', 'Field', 'Media', 'Organizing', 'Weddings']

def _inline(s):
    s = E(s)
    s = _re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    def lk(m):
        t, u = m.group(1), m.group(2).replace('&amp;', '&')
        if u.startswith('/'):
            return f'<a href="{{pre}}{u.lstrip("/")}">{t}</a>'
        return f'<a href="{E(u)}" target="_blank" rel="noopener">{t}</a>'
    return _re.sub(r'\[([^\]]+)\]\(((?:[^()\s]|\([^()\s]*\))+)\)', lk, s)

def _plain(s):
    s = _re.sub(r'\[([^\]]+)\]\(((?:[^()\s]|\([^()\s]*\))+)\)', r'\1', s)
    return s.replace('**', '')

def _md(body):
    """Return (html, faq[(q,a)], toc[(id,h)]) for the limited markdown the writers use."""
    lines = body.strip('\n').split('\n')
    out, faq, toc = [], [], []
    i, in_faq, cur_q, cur_a = 0, False, None, []
    def flush_q():
        nonlocal cur_q, cur_a
        if cur_q:
            faq.append((cur_q, ' '.join(_plain(a) for a in cur_a)))
        cur_q, cur_a = None, []
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            i += 1; continue
        if ln.startswith('## '):
            flush_q()
            h = ln[3:].strip()
            in_faq = h.lower().startswith('frequently asked')
            hid = _re.sub(r'[^a-z0-9]+', '-', h.lower()).strip('-')[:60]
            toc.append((hid, h))
            out.append(f'<h2 id="{hid}">{_inline(h)}</h2>')
            i += 1; continue
        if ln.startswith('### '):
            h = ln[4:].strip()
            if in_faq:
                flush_q(); cur_q = _plain(h)
                # gather answer paragraphs until next heading
                j = i + 1; ans = []
                while j < len(lines) and not lines[j].startswith('#'):
                    if lines[j].strip(): ans.append(lines[j].strip())
                    j += 1
                cur_a = ans
                out.append('<details><summary>' + _inline(h) + '</summary>' + ''.join(f'<p>{_inline(a)}</p>' for a in ans) + '</details>')
                i = j; continue
            out.append(f'<h3>{_inline(h)}</h3>')
            i += 1; continue
        if ln.lstrip().startswith('|'):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')]); i += 1
            rows = [r for r in rows if not all(_re.fullmatch(r':?-{2,}:?', c or '--') for c in r)]
            if rows:
                th = ''.join(f'<th>{_inline(c)}</th>' for c in rows[0])
                tb = ''.join('<tr>' + ''.join(f'<td>{_inline(c)}</td>' for c in r) + '</tr>' for r in rows[1:])
                out.append(f'<div class="gtable"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>')
            continue
        if _re.match(r'^\s*- ', ln):
            items = []
            while i < len(lines) and _re.match(r'^\s*- ', lines[i]):
                items.append(lines[i].strip()[2:]); i += 1
            out.append('<ul>' + ''.join(f'<li>{_inline(x)}</li>' for x in items) + '</ul>'); continue
        if _re.match(r'^\s*\d+[.)] ', ln):
            items = []
            n0 = int(_re.match(r'^\s*(\d+)', ln).group(1))
            while i < len(lines) and _re.match(r'^\s*\d+[.)] ', lines[i]):
                items.append(_re.sub(r'^\s*\d+[.)] ', '', lines[i])); i += 1
            st = f' start="{n0}" style="counter-reset:gstep {n0 - 1}"' if n0 > 1 else ''
            out.append(f'<ol{st}>' + ''.join(f'<li>{_inline(x)}</li>' for x in items) + '</ol>'); continue
        para = [ln.strip()]; i += 1
        while i < len(lines) and lines[i].strip() and not _re.match(r'^(#|\s*- |\s*\d+[.)] |\s*\|)', lines[i]):
            para.append(lines[i].strip()); i += 1
        out.append(f'<p>{_inline(" ".join(para))}</p>')
    flush_q()
    return '\n'.join(out), faq, toc

def _load_guides():
    G = {}
    for f in sorted(_glob.glob(os.path.join(GUIDE_DIR, '*.md'))):
        raw = open(f).read()
        m = _re.match(r'^---\n(.*?)\n---\n(.*)$', raw, _re.S)
        if not m: continue
        meta = {}
        for ln in m.group(1).split('\n'):
            if ':' in ln:
                k, v = ln.split(':', 1); meta[k.strip()] = v.strip()
        meta['body'] = m.group(2)
        meta['words'] = len(_re.findall(r'\w+', _plain(m.group(2))))
        meta['related'] = [s.strip() for s in meta.get('related', '').split(',') if s.strip()]
        G[meta['slug']] = meta
    return G

GUIDES = _load_guides()

def _guide_cta(cat, pre):
    if cat == 'Weddings':
        return (f'<h3>Planning a wedding?</h3><p>Send your date, venue and guest count. We will tell you what coverage your day actually needs.</p>'
                f'{mail("rod","leooperations.com","Check our availability <span class=\"arr\">&rarr;</span>","btn primary","Wedding%20inquiry%20from%20leooperations.com")}'
                f'<p style="margin-top:18px"><a href="{pre}weddings/" style="color:var(--cyan)">See our wedding photo and film work</a></p>')
    return (f'<h3>Planning a program?</h3><p>Tell us the race, the timeline and the budget. We will tell you honestly what it takes to win it.</p>'
            f'{mail("rod","leooperations.com","Talk to Leo Operations <span class=\"arr\">&rarr;</span>","btn primary","Inquiry%20from%20leooperations.com%20guides")}'
            f'<p style="margin-top:18px"><a href="{pre}clients/" style="color:var(--cyan)">See who we have worked with</a></p>')

def guide_page(slug):
    g = GUIDES[slug]
    html, faq, toc = _md(g['body'])
    url = SITE + '/guides/' + slug + '/'
    mins = max(1, round(g['words'] / 230))
    author = {"@type": "Person", "name": "Rodriquez Wright II", "alternateName": "Rod Wright", "url": SITE + "/team/rodriquez-wright-ii/", "jobTitle": "Founder and CEO, Leo Operations"}
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": g['h1'][:110], "description": g['description'], "author": author,
           "publisher": {"@id": SITE + "/#organization"}, "datePublished": GUIDE_DATE, "dateModified": GUIDE_DATE,
           "mainEntityOfPage": url, "articleSection": g.get('category', ''), "keywords": g.get('keywords', ''), "wordCount": g['words'],
           "image": SHARE + ('/assets/weddings/w-og.jpg' if g.get('category') == 'Weddings' else '/assets/img/og.jpg')},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
              {"@type": "ListItem", "position": 2, "name": "Guides", "item": SITE + "/guides/"},
              {"@type": "ListItem", "position": 3, "name": g['h1'], "item": url}]}]
    if faq:
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})
    rel = [r for r in g['related'] if r in GUIDES and r != slug][:4]
    if len(rel) < 3:
        rel += [k for k, v in GUIDES.items() if v.get('category') == g.get('category') and k != slug and k not in rel][:3 - len(rel)]
    tocl = ''.join(f'<li><a href="#{i}">{E(h)}</a></li>' for i, h in toc)
    og = 'assets/weddings/w-og.jpg' if g.get('category') == 'Weddings' else 'assets/img/og.jpg'
    def body(pre):
        relc = ''.join(f'<a class="gcard" href="{pre}guides/{r}/"><span class="eyebrow mono">{E(GUIDES[r].get("category",""))}</span><b>{E(GUIDES[r]["h1"])}</b><span>{E(GUIDES[r].get("dek",""))}</span></a>' for r in rel)
        return f'''<article class="guide">
<header class="ghero wrap"><nav class="crumbs mono"><a href="{pre}">Home</a> / <a href="{pre}guides/">Guides</a> / <span>{E(g.get("category",""))}</span></nav>
<h1 class="h-lg">{E(g["h1"])}</h1><p class="lead">{E(g.get("dek",""))}</p>
<p class="byline mono">By <a href="{pre}team/rodriquez-wright-ii/">Rodriquez Wright II</a>, Leo Operations &middot; Updated October 2026 &middot; {mins} min read</p></header>
<section class="sec wrap" style="padding-top:10px"><div class="two-col"><div class="prose gprose">{html.replace("{pre}", pre)}</div>
<aside class="sticky-card">{_guide_cta(g.get("category"), pre)}<div class="gtoc"><span class="eyebrow mono">In this guide</span><ol>{tocl}</ol></div></aside></div></section>
<section class="sec wrap"><span class="eyebrow mono">Keep reading</span><div class="grel">{relc}</div></section></article>
{bigcta(pre)}'''
    page('guides/' + slug + '/', g['title'] + ' | Leo Operations', g['description'], body, og=og, extra_ld=ld)

def guides_hub():
    def body(pre):
        secs = ''
        for c in GUIDE_CATS:
            items = [(k, v) for k, v in GUIDES.items() if v.get('category') == c]
            if not items: continue
            cards = ''.join(f'<a class="gcard" href="{pre}guides/{k}/"><b>{E(v["h1"])}</b><span>{E(v.get("dek",""))}</span></a>' for k, v in items)
            secs += f'<section class="sec wrap"><span class="eyebrow mono">{E(c)}</span><div class="grel">{cards}</div></section>'
        return f'''<header class="ghero wrap"><nav class="crumbs mono"><a href="{pre}">Home</a> / <span>Guides</span></nav><h1 class="h-lg">Guides from Leo Operations</h1>
<p class="lead">Straight answers on running for office, field programs, political media, organizing events and wedding photography and film, from the team that does the work.</p></header>{secs}{bigcta(pre)}'''
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Leo Operations Guides", "url": SITE + "/guides/",
           "hasPart": [{"@type": "Article", "headline": v['h1'], "url": SITE + "/guides/" + k + "/"} for k, v in GUIDES.items()]}]
    page('guides/', 'Campaign, Field, Media and Wedding Guides | Leo Operations',
         'Detailed guides on campaign costs, voter registration, GOTV, political TV and digital ads, and wedding photography and videography from Leo Operations.', body, extra_ld=ld)
