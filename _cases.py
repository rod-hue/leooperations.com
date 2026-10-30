# ---------- EXTENDED CASE STUDIES ----------
# exec'd by build.py; portfolio_pages() swaps in these sections for the listed slugs. Client facts come from the client's own
# site (linked) or data/portfolio_facts.json; Leo's role comes from Rod (Oct 29 2026). No prices.
JM = 'https://jerrymaynard.com/'
CASE_TITLE = {'jerry-l-maynard-ii': 'Pastor Jerry L. Maynard II'}
CASE_LEAD = {'jerry-l-maynard-ii': [
    'Pastor Jerry L. Maynard II leads Cathedral of Praise in Nashville, runs The Maynard Group and served eight years as an at-large member of the Metro Council. Leo Operations has worked with him since his 2022 campaign and remains a partner across his church, business and community work.',
]}

def _jm_extra(pre):
    def film(key, eyebrow, title):
        P = pre + 'assets/church/'
        return (f'<div class="wfilm" data-r="0"><video preload="none" playsinline poster="{P}{key}.jpg" data-hd="{P}{key}-hd.mp4" data-sd="{P}{key}-sd.mp4"></video>'
                f'<div class="ov"><span class="pb" aria-hidden="true"></span><span class="mono" style="color:var(--cyan)">{eyebrow}</span><b>{title}</b></div></div>')
    did = [
        ('Website', 'We designed and built jerrymaynard.com, his personal site covering his work as a pastor, entrepreneur and civic leader, with his resume, news, community projects and a contact page.'),
        ('Campaign', 'We worked with his 2022 campaign for Tennessee Senate District 19.'),
        ('Church photo and film', 'We photograph and film at Cathedral of Praise, including the church’s 60th anniversary recap, his 5th pastoral anniversary, a new member film and weekly vertical sermon clips.'),
        ('Design', 'Our design team produced the 5th pastoral anniversary program, the 60th anniversary save the date, service graphics, visitor cards and a welcome bookmark.'),
        ('Ongoing partnership', 'After the 2022 election we stayed on as a partner for his business and community work, handling media, design and digital as new projects come up.'),
    ]
    bio = [
        ('Pastor', 'Pastor of Cathedral of Praise, a multicampus church in North Nashville that began in 1966 and, according to his site, has more than 3,000 active members and has given more than $150,000 in scholarships over 20 years.'),
        ('Entrepreneur', 'Founder and president of The Maynard Group, a Nashville government relations and consulting firm he started in 2007, and a co-founder of The Nashville Voice.'),
        ('Civic leader', 'Elected to the Metro Council at-large in 2007 and re-elected in 2011, serving until 2015. Earlier he was the first African American deputy chairman of the Tennessee Democratic Party.'),
        ('Community', 'His site credits him with work to support Nashville General Hospital, the National Museum of African American Music and the Jefferson Street “Gateway to Heritage” project, and with a scholarship fund for Tennessee State University students.'),
    ]
    graphics = [('c-5th-cover', 'Pastoral anniversary program'), ('c-60th', '60th anniversary save the date'), ('c-sunday', 'Sunday service graphic'), ('c-thankyou', 'Visitor postcard')]
    did_h = ''.join(f'<div data-r="{i%3}"><b>{E(a)}</b><span>{E(b)}</span></div>' for i, (a, b) in enumerate(did))
    bio_h = ''.join(f'<h3>{E(a)}</h3><p>{E(b)}</p>' for a, b in bio)
    gfx = ''.join(f'<figure style="margin:0;border-radius:14px;overflow:hidden"><a href="{pre}assets/work/{k}.jpg" data-img="{pre}assets/work/{k}.jpg" aria-label="View {E(t)} full size"><img src="{pre}assets/work/{k}.jpg" alt="{E(t)} for Cathedral of Praise, designed by Leo Operations" loading="lazy" style="width:100%;height:auto;display:block"></a><figcaption class="mono" style="font-size:10px;color:var(--dim);margin-top:8px;letter-spacing:.1em;text-transform:uppercase">{E(t)}</figcaption></figure>' for k, t in graphics)
    return f'''<section class="sec wrap"><span class="eyebrow mono">What we do together</span><h2 class="h-lg" style="margin:14px 0 30px">{split("A partner since|<span class=grad>2022.</span>")}</h2><div class="feat">{did_h}</div></section>
<section class="sec wrap"><div class="sec-head"><div><span class="eyebrow mono">Website</span><h2 class="h-lg" style="margin-top:14px">{split("jerrymaynard.com|<span class=grad>built by Leo.</span>")}</h2></div><a class="btn ghost" href="{JM}" target="_blank" rel="noopener">Visit the site <span class="arr">&rarr;</span></a></div>
<div style="display:grid;grid-template-columns:minmax(0,8fr) minmax(0,3fr);gap:clamp(14px,2vw,26px);align-items:end"><figure style="margin:0;border-radius:18px;overflow:hidden;border:1px solid rgba(255,255,255,.12)">{img("assets/clients/jm-site-desktop.jpg", "jerrymaynard.com homepage designed by Leo Operations", pre)}</figure><figure style="margin:0;border-radius:18px;overflow:hidden;border:1px solid rgba(255,255,255,.12)">{img("assets/clients/jm-site-mobile.jpg", "jerrymaynard.com on a phone", pre)}</figure></div></section>
<section class="sec wrap" id="films"><div class="sec-head"><div><span class="eyebrow mono">Cathedral of Praise</span><h2 class="h-lg" style="margin-top:14px">{split("Films from|<span class=grad>his church.</span>")}</h2></div><a class="btn ghost" href="{pre}churches/">All church work <span class="arr">&rarr;</span></a></div>
<div class="wfilms">{film("ch-60th", "60th church anniversary", "Sixty years of praise")}{film("ch-newmember", "New member film", "Welcome to the family")}</div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:14px" class="jmv">{film("ch-cop5", "5th pastoral anniversary", "Anniversary reel")}{film("ch-sermon1", "Sermon clip", "Christianity vs. hypocrisy")}{film("ch-sermon3", "Sermon clip", "Do you act like Christ?")}{film("ch-sermon4", "Sermon clip", "The church must awaken")}</div>
<style>.jmv .wfilm{{aspect-ratio:9/16}}.jmv .wfilm .ov b{{font-size:clamp(15px,1.3vw,20px)}}@media(max-width:700px){{.jmv{{grid-template-columns:1fr 1fr!important}}}}</style></section>
<section class="sec wrap"><span class="eyebrow mono">Design</span><h2 class="h-lg" style="margin:14px 0 30px">{split("Programs and|<span class=grad>service graphics.</span>")}</h2><div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px;align-items:start">{gfx}</div></section>
<section class="sec wrap"><div class="two-col"><div class="prose"><h2>About Pastor Maynard</h2>{bio_h}<p style="color:var(--dim);font-size:14px">Source: <a href="{JM}" target="_blank" rel="noopener" style="color:var(--dim)">jerrymaynard.com</a></p></div><aside class="sticky-card"><h3>Work like this</h3><p><a href="{pre}churches/" style="color:var(--cyan)">Church photo, film and web &rarr;</a></p><p><a href="{pre}services/website-design/" style="color:var(--cyan)">Website design &rarr;</a></p><p><a href="{pre}political-video-production/" style="color:var(--cyan)">Campaign video &rarr;</a></p><p><a href="{pre}social-media-design/" style="color:var(--cyan)">Social media and design &rarr;</a></p></aside></div></section>'''

CASE_EXTRA = {'jerry-l-maynard-ii': _jm_extra}
CASE_DESC = {'jerry-l-maynard-ii': 'Leo Operations built jerrymaynard.com and photographs, films and designs for Pastor Jerry L. Maynard II and Cathedral of Praise, a partner since his 2022 campaign.'}
