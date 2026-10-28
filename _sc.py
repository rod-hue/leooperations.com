# ---------- SOUTH CAROLINA (/south-carolina/) ----------
# exec'd by build.py after _weddings.py (reuses W_CSS/W_JS, recolored). Media in assets/sc from Rod's Dec 2025 South Carolina shoot
# (Drive: Brandon Brown For US Senate, plus Elected Headshots / Elected Videos). Facts only: no prices, no outcomes we can't source.
# The official in the Orangeburg holiday greeting is not named in her video, so she stays unnamed until Rod confirms.
SC_WALL = [  # (file, alt, caption)
 ("hs-govan-1", "South Carolina State Rep. Jerry N. Govan Jr. in a navy jacket and SCDES cap", "Rep. Jerry N. Govan Jr."),
 ("hs-smart-1", "Fairfax Town Councilwoman Phyllis Smart smiling in an orange cardigan", "Councilwoman Phyllis Smart"),
 ("bb-1", "Brandon Brown in a navy suit and striped tie", "Brandon Brown"),
 ("hs-ob-2", "Orangeburg official in a magenta blazer against a brick wall", "Orangeburg"),
 ("bb-trio", "Brandon Brown with Councilwoman Phyllis Smart and an Orangeburg official", "Orangeburg County"),
 ("hs-govan-3", "Rep. Jerry Govan under a palmetto tree", "Rep. Jerry N. Govan Jr."),
 ("bb-reese", "Brandon Brown with former State Sen. Glenn Reese at his Spartanburg Krispy Kreme", "Sen. Glenn Reese"),
 ("hs-smart-2", "Councilwoman Phyllis Smart against a brick wall", "Councilwoman Phyllis Smart"),
 ("bb-5", "Brandon Brown with arms crossed beside an American flag", "Brandon Brown"),
 ("hs-govan-2", "Rep. Jerry Govan standing against a brick wall", "Rep. Jerry N. Govan Jr."),
 ("hs-ob-1", "Orangeburg official smiling in a magenta blazer", "Orangeburg"),
 ("bb-2", "Brandon Brown smiling in a navy suit", "Brandon Brown"),
]
SC_OFFICIALS = [
 ('Rep. Jerry N. Govan Jr.', 'South Carolina House, District 93', 'Headshots, a re-election film for House District 93 and an endorsement film.'),
 ('Glenn Reese', 'Former State Senator, District 11', 'An endorsement film shot at the Spartanburg Krispy Kreme his family has run since 1969.'),
 ('Phyllis Smart', 'Fairfax Town Council', 'Headshots and a holiday thank-you to the voters of Fairfax.'),
 ('Bishop Hayes T. Ganey Jr.', 'Faith Group for Action', 'A vertical endorsement interview for voters in Orangeburg County.'),
 ('Brandon Brown', 'Candidate, U.S. Senate, 2026', 'Digital, website, portraits, endorsement films and issue videos.'),
]
SC_GET = [
 ('Organize', 'Field that starts early.', ['Statewide and county field plans built around the January 22 primary calendar',
   'Door-to-door canvassing, phone banks and relational texting', 'Church, HBCU, union and community outreach led by local voices',
   'Volunteer recruitment and weekly field reporting']),
 ('Film', 'Local leaders, on camera.', ['Endorsement films with South Carolina elected officials and faith leaders',
   'Constituent outreach and holiday videos for officeholders', 'Vertical issue videos for Reels, TikTok and Shorts',
   'Event coverage for town halls, rallies and bus tours']),
 ('Reach', 'Digital that raises and turns out.', ['Campaign websites with donate, volunteer and voter-registration flows',
   'Digital ads, email and SMS for grassroots fundraising', 'Social media management and graphic design',
   'Professional headshots and campaign portraits']),
]
SC_MENU = ['Presidential primary field', 'Endorsement films', 'Constituent videos', 'Headshots', 'Campaign portraits', 'Campaign websites',
           'Digital ads', 'Grassroots fundraising', 'Email and SMS', 'Social media', 'Graphic design', 'Faith outreach', 'HBCU outreach',
           'Canvassing', 'Phone banking', 'Relational organizing', 'Event production', 'Drone', 'Advance and rally coverage', 'Surrogate content']
SC_FAQ = [
 ('Why does South Carolina matter in 2028?', 'South Carolina holds the first Democratic presidential primary of the 2028 cycle on January 22, 2028, under the calendar the Democratic National Committee approved on August 15, 2026. It is the first chance for candidates to show they can win Black voters and working families in the South.'),
 ('Has Leo Operations worked in South Carolina?', 'Yes. We ran digital and built the website for Brandon Brown’s 2026 U.S. Senate campaign, and we filmed and photographed South Carolina legislators, local officials and faith leaders, including Rep. Jerry N. Govan Jr., former State Sen. Glenn Reese, Fairfax Councilwoman Phyllis Smart and Bishop Hayes T. Ganey Jr.'),
 ('Do you have presidential campaign experience?', 'Yes. Founder Rodriquez Wright II was Tennessee state organizing director for Mike Bloomberg’s 2020 presidential campaign. Leo Operations has since worked for more than 40 campaigns, officials and causes, with organizing and ballot work in 25 states and more than 650,000 doors knocked.'),
 ('Do you work with elected officials who are not on the ballot?', 'Yes. We produce headshots, constituent outreach videos, holiday messages and social content for legislators, council members and other officeholders year round.'),
 ('Can you film endorsements for a presidential campaign?', 'Yes. We plan, shoot and edit endorsement films with local leaders in the places voters know them, then cut them for social, email and digital ads with captions and campaign branding.'),
 ('How do we get started?', 'Email us about your campaign, your timeline and what you need in South Carolina. We start with a strategy session and follow up with a written proposal.'),
]
SC_TITLE = 'South Carolina Political Consulting, Endorsement Films & 2028 Primary Field | Leo Operations'
SC_DESC = 'South Carolina votes first in the 2028 Democratic presidential primary. Leo Operations has filmed and photographed SC elected officials and ran digital and web for a 2026 U.S. Senate campaign.'

SC_CSS = W_CSS.replace('.wed', '.scp').replace('#e8cf9e', '#ffb15c').replace('#c79b52', '#ff7a1a').replace('#fff4dc', '#fff0e0').replace('232,207,158', '255,177,92').replace('#140d02', '#1a0b00') + '''<style>
.scp .wfilm.wide{aspect-ratio:256/135}.scp .wfilm.wide video{object-fit:cover}
.scp .wfilms .wfilm .pb,.scv .wfilm .pb{top:18px;left:auto;right:18px;margin:0;width:64px;height:64px}.scp .wfilms .wfilm .pb::before,.scv .wfilm .pb::before{border-width:11px 0 11px 17px;margin-left:5px}
.scv{display:grid;grid-template-columns:repeat(2,minmax(0,380px));gap:clamp(12px,1.6vw,20px);margin-top:clamp(14px,2vw,26px)}
.scv .wfilm{aspect-ratio:9/16}.scv .wfilm .ov b{font-size:clamp(20px,1.8vw,28px)}
.scoff{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:clamp(12px,1.6vw,20px)}
.scoff>div{border:1px solid rgba(255,177,92,.2);border-radius:20px;padding:24px 24px 26px;background:linear-gradient(160deg,rgba(255,177,92,.06),rgba(7,13,26,.4) 60%)}
.scoff b{font-family:var(--display);font-size:22px;letter-spacing:-.02em;display:block}.scoff span{font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--gold);display:block;margin:8px 0 12px}.scoff p{color:var(--silver);margin:0}
.scbb{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(24px,4vw,64px);align-items:start}
.scbb figure{margin:0;border-radius:18px;overflow:hidden;border:1px solid rgba(255,177,92,.2)}.scbb figure img{width:100%;height:auto;display:block}
.scbb figcaption{padding:12px 16px;background:var(--bg2);font-family:var(--mono);font-size:11px;color:var(--dim)}
.scbb .q{font-family:var(--display);font-weight:600;font-size:clamp(22px,2.4vw,34px);line-height:1.15;letter-spacing:-.02em;margin:18px 0 24px}
.scbb .q em{font-family:"Instrument Serif",Georgia,serif;font-weight:400;color:var(--gold)}
.scbb ul{list-style:none;display:grid;gap:12px;margin:0 0 26px;padding:0}.scbb li{padding-left:26px;position:relative;color:var(--silver)}.scbb li::before{content:"";position:absolute;left:0;top:.62em;width:12px;height:1px;background:var(--gold)}
.scdate{display:flex;flex-wrap:wrap;gap:10px}.scdate span{font-family:var(--mono);font-size:13px;letter-spacing:.04em;padding:12px 18px;border-radius:999px;border:1px solid rgba(255,177,92,.28)}.scdate span b{color:var(--gold);font-weight:500;margin-right:8px}
@media (max-width:900px){.scp .wfilm.wide,.scp .wfilm.wreel.wide{aspect-ratio:256/135}.scbb{grid-template-columns:1fr}}
@media (max-width:520px){.scv{grid-template-columns:1fr 1fr;gap:10px}.scv .wfilm .ov p{display:none}}
</style>'''

def sc_page():
    def body(pre):
        P = pre + 'assets/sc/'
        marq_items = ['South Carolina', 'First in the nation', 'Endorsement films', 'Headshots', 'Digital &amp; web', 'Field'] * 2
        marq = ''.join(f'<span class="{"o" if i % 2 else ""}">{w}</span><i>&#9670;</i>' for i, w in enumerate(marq_items))
        def film(key, eyebrow, title, desc, cls='wide'):
            return (f'<div class="wfilm {cls}" data-r="0"><video preload="none" playsinline poster="{P}{key}.jpg" data-hd="{P}{key}-hd.mp4" data-sd="{P}{key}-sd.mp4"></video>'
                    f'<div class="ov"><span class="pb" aria-hidden="true"></span><span class="mono" style="color:var(--gold)">{eyebrow}</span><b>{title}</b><p>{desc}</p></div></div>')
        lead = film('sc-govan-hd93', 'Rep. Jerry N. Govan Jr. &middot; House District 93 &middot; sound on', 'Look at what we&rsquo;ve done.', 'A re-election film for Rep. Govan: food for families after SNAP cuts, a 400-job facility between Orangeburg and Calhoun counties, and water and sewer for small towns.', 'wreel wide')
        endorse = ('<div class="wfilms" style="margin-top:clamp(14px,2vw,26px)">'
                   + film('sc-govan', 'Endorsement &middot; Rep. Jerry N. Govan Jr.', 'It takes a lot of us.', 'Rep. Govan asks for the $5 and $10 grassroots gifts that keep big money from running the race.')
                   + film('sc-reese', 'Endorsement &middot; former State Sen. Glenn Reese', 'He is the real deal.', 'Glenn Reese, who served Spartanburg in the State Senate from 1991 to 2021, at his family&rsquo;s Krispy Kreme.')
                   + film('sc-smart', 'Constituent outreach &middot; Fairfax Town Council', 'Thank you, Fairfax.', 'Councilwoman Phyllis Smart thanks the voters who elected her and wishes the town a happy holiday season.')
                   + film('sc-orangeburg', 'Constituent outreach &middot; Orangeburg', 'Happy holidays, Orangeburg.', 'A holiday greeting to the city and county of Orangeburg, cut short for social.')
                   + '</div>')
        verts = ('<div class="scv">'
                 + film('sc-ganey', 'Faith Group for Action &middot; vertical', 'Bishop Hayes T. Ganey Jr.', 'A faith leader asks Orangeburg County to register and vote.', '')
                 + film('sc-bb-musc', 'Issue video &middot; MUSC Orangeburg', 'Rural hospitals.', 'Brandon Brown on keeping rural hospitals open and medicine within reach.', '')
                 + '</div>')
        wall = ''.join(f'<figure data-r="{i%3}">{img("assets/sc/"+f+".jpg", alt, pre)}<figcaption class="mono">{c}</figcaption></figure>' for i, (f, alt, c) in enumerate(SC_WALL))
        offs = ''.join(f'<div data-r="{i%3}"><b>{E(n)}</b><span>{E(r)}</span><p>{E(w)}</p></div>' for i, (n, r, w) in enumerate(SC_OFFICIALS))
        get = ''.join(f'<div data-r="{i}"><span class="mono" style="color:var(--gold)">0{i+1}</span><h3>{E(h)}</h3><span class="t">{E(t)}</span><ul>{"".join(f"<li>{E(x)}</li>" for x in pts)}</ul></div>' for i, (h, t, pts) in enumerate(SC_GET))
        menu = ''.join(f'<span data-r="{i%3}">{E(m)}</span>' for i, m in enumerate(SC_MENU))
        faq = ''.join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in SC_FAQ)
        subj = 'South%20Carolina%20campaign%20inquiry'
        return f'''{SC_CSS}<div class="wed scp">
<section class="hero whero"><div class="hero-media"><video id="schv" muted loop playsinline autoplay preload="auto" poster="{P}sc-hero.jpg" data-q="{P}sc-hero"></video><script>(function(){{var v=document.getElementById("schv"),w=innerWidth*Math.min(2,devicePixelRatio||1);v.src=v.dataset.q+(w>=1000?"-hd":"-sd")+".mp4";var p=v.play();if(p)p.catch(function(){{}})}})()</script></div>
<div class="wtop mono"><span>Leo Operations / South Carolina</span><span>2028 Democratic primary</span></div>
<div class="hero-inner"><span class="eyebrow mono">First in the nation</span><h1 style="margin-top:18px">{split("South Carolina|<span class=serif>votes first.</span>")}</h1>
<p class="lead">The 2028 Democratic presidential race starts in South Carolina on January 22, 2028. We already work there, with legislators, local officials, faith leaders and a U.S. Senate campaign.</p>
<div class="hero-ctas">{mail("rod","leooperations.com","Plan your South Carolina program <span class=\"arr\">&rarr;</span>","btn primary",subj)}<a class="btn ghost" href="#films">Watch the films <span class="arr">&rarr;</span></a></div></div></section>
<div class="marq wmarq" aria-hidden="true"><div class="t">{marq}{marq}</div></div>
<section class="wman"><span class="eyebrow mono" style="margin-bottom:30px">01 / Why now</span><p>Presidential campaigns win South Carolina through <em>people voters already trust:</em> their state representative, their council member, their bishop. We have filmed and photographed those leaders in Orangeburg, Fairfax and Spartanburg, and we know how to put them on camera.</p></section>
<section class="sec wrap"><span class="eyebrow mono">02 / The calendar</span><h2 class="h-lg" style="margin:14px 0 30px">{split("The first five|<span class=serif>Democratic contests of 2028.</span>")}</h2><div class="scdate"><span><b>Jan 22</b>South Carolina</span><span><b>Feb 1</b>Nevada</span><span><b>Feb 8</b>New Hampshire</span><span><b>Feb 15</b>New Mexico</span><span><b>Feb 22</b>Michigan</span></div><p style="color:var(--dim);margin-top:22px;max-width:70ch">Approved by the Democratic National Committee on August 15, 2026.</p></section>
<section class="sec wrap" id="films"><div class="sec-head"><div><span class="eyebrow mono">03 / Films</span><h2 class="h-lg" style="margin-top:14px">{split("Elected officials,|<span class=serif>talking to voters.</span>")}</h2></div><p>Constituent outreach videos, endorsement films and vertical issue videos we produced in South Carolina. Press play with the sound on.</p></div>{lead}{endorse}{verts}</section>
<section class="sec wrap" id="officials"><span class="eyebrow mono">04 / Who we have worked with</span><h2 class="h-lg" style="margin:14px 0 34px">{split("Leaders across|<span class=serif>South Carolina.</span>")}</h2><div class="scoff">{offs}</div></section>
<section class="sec wrap" id="photos"><div class="sec-head"><div><span class="eyebrow mono">05 / Headshots</span><h2 class="h-lg" style="margin-top:14px">{split("Portraits for|<span class=serif>public servants.</span>")}</h2></div><p>Professional headshots and campaign portraits shot on location, in front of the schools, offices and palmettos of the communities these leaders serve.</p></div><div class="wwall">{wall}</div></section>
<section class="sec wrap" id="brandon-brown"><span class="eyebrow mono">06 / Case study</span><h2 class="h-lg" style="margin:14px 0 34px">{split("Brandon Brown|<span class=serif>for U.S. Senate.</span>")}</h2>
<div class="scbb"><figure data-r="0"><a href="https://brandonpbrown.com/" target="_blank" rel="noopener">{img("assets/sc/bb-site.jpg", "Homepage of brandonpbrown.com, the Brandon Brown for U.S. Senate website built by Leo Operations", pre)}</a><figcaption>brandonpbrown.com, built by Leo Operations</figcaption></figure>
<div data-r="1"><p class="q">A grassroots Senate campaign needs a site that raises money and <em>a feed that makes people care.</em></p><ul><li>Built brandonpbrown.com: donate, volunteer, meet-and-greet and voter information</li><li>Ran the campaign&rsquo;s digital program</li><li>Filmed endorsement videos with Rep. Jerry Govan, former Sen. Glenn Reese and Bishop Hayes T. Ganey Jr.</li><li>Shot campaign portraits and vertical issue videos across the state</li></ul>
<p><a class="btn ghost" href="https://brandonpbrown.com/" target="_blank" rel="noopener">Visit the site <span class="arr">&rarr;</span></a></p></div></div></section>
<section class="sec wrap"><span class="eyebrow mono">07 / What we build</span><h2 class="h-lg" style="margin:14px 0 34px">{split("Organize. Film.|<span class=serif>Reach.</span>")}</h2><div class="wget">{get}</div><p style="color:var(--dim);margin-top:26px;max-width:72ch">Founder Rodriquez Wright II was Tennessee state organizing director for Mike Bloomberg&rsquo;s 2020 presidential campaign. Since then Leo Operations has worked for more than 40 campaigns, officials and causes, with organizing and ballot work in 25 states and more than 650,000 doors knocked.</p></section>
<section class="sec wrap"><div class="sec-head"><div><span class="eyebrow mono">08 / Every service</span><h2 class="h-lg" style="margin-top:14px">{split("One team for|<span class=serif>the first primary.</span>")}</h2></div><p>Field, film, photo and digital from one firm, so every endorsement, door and ad tells the same story.</p></div><div class="wmom">{menu}</div></section>
<section class="sec wrap"><span class="eyebrow mono">09 / FAQ</span><h2 class="h-lg" style="margin:14px 0 30px">South Carolina questions, <span class="serif">answered.</span></h2><div class="faq">{faq}</div></section>
<section class="wcta" id="start"><video muted loop playsinline preload="none" poster="{P}sc-hero.jpg" data-q="{P}sc-hero"></video><span class="eyebrow mono">Campaigns, officials and causes</span><h2 style="margin-top:20px">Win the state <span class="serif">that votes first.</span></h2><p>Tell us about your campaign and what you need in South Carolina. We will set up a strategy session and send a written proposal.</p>{mail("rod","leooperations.com","Plan your South Carolina program <span class=\"arr\">&rarr;</span>","btn primary",subj)}</section>
<div class="marq wmarq rev" aria-hidden="true"><div class="t">{marq}{marq}</div></div>
</div>{W_JS}'''
    url = SITE + '/south-carolina/'
    vids = [('sc-govan-hd93', 'Rep. Jerry N. Govan Jr. for House District 93', 'Re-election film for South Carolina State Rep. Jerry N. Govan Jr., House District 93.', 'PT1M35S'),
            ('sc-govan', 'Rep. Jerry Govan endorses Brandon Brown', 'Endorsement film with South Carolina State Rep. Jerry N. Govan Jr.', 'PT48S'),
            ('sc-reese', 'Former State Sen. Glenn Reese endorses Brandon Brown', 'Endorsement film with former South Carolina State Sen. Glenn Reese in Spartanburg.', 'PT31S'),
            ('sc-smart', 'Councilwoman Phyllis Smart holiday message', 'Holiday thank-you from Fairfax Town Councilwoman Phyllis Smart.', 'PT15S'),
            ('sc-ganey', 'Bishop Hayes T. Ganey Jr. endorses Brandon Brown', 'Vertical endorsement interview with Bishop Hayes T. Ganey Jr. of Faith Group for Action.', 'PT1M22S'),
            ('sc-bb-musc', 'Brandon Brown at MUSC Orangeburg', 'Brandon Brown on rural hospitals at MUSC Health Orangeburg.', 'PT47S')]
    ld = [
      {"@context": "https://schema.org", "@type": "Service", "@id": url + "#service", "name": "South Carolina Political Consulting, Endorsement Films and Field",
       "serviceType": ["Political consulting", "Field organizing", "Endorsement videos", "Constituent outreach videos", "Political headshots", "Campaign websites", "Digital advertising"],
       "provider": {"@id": SITE + "/#organization"}, "areaServed": {"@type": "State", "name": "South Carolina"}, "url": url, "image": SITE + "/assets/sc/sc-hero.jpg", "description": SC_DESC},
      {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in SC_FAQ]},
      {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "South Carolina", "item": url}]},
    ] + [{"@context": "https://schema.org", "@type": "VideoObject", "name": n, "description": d, "thumbnailUrl": SITE + f"/assets/sc/{k}.jpg",
          "contentUrl": SITE + f"/assets/sc/{k}-hd.mp4", "uploadDate": "2026-10-28T12:00:00-05:00", "duration": t} for k, n, d, t in vids]
    page('south-carolina/', SC_TITLE, SC_DESC, body, og='assets/sc/sc-hero.jpg', extra_ld=ld)
