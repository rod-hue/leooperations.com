# ---------- CONTENT PARTNERSHIPS (/content-partnerships/) ----------
# exec'd by build.py after _weddings.py. Replaces apply.leooperations.com (Landingsite): same concept and structure,
# reworded for owners, executives, candidates and PACs. No prices: every term is quoted in a written proposal.
P_WALL = [  # (path under assets/, alt, caption)
 ("shot/beyonce", "Beyonce photographed by Leo Operations", "Photography"),
 ("work/megan-endorse", "Campaign endorsement graphic designed by Leo Operations", "Design"),
 ("shot/metgala", "The Met Gala photographed by Leo Operations", "Photography"),
 ("work/tsu-roar", "TSU homecoming social graphic", "Design"),
 ("shot/jayz", "JAY-Z photographed by Leo Operations", "Photography"),
 ("work/dowdy-billboard", "Judicial campaign billboard design", "Design"),
 ("shot/warnock", "Sen. Raphael Warnock photographed by Leo Operations", "Photography"),
 ("work/hbcu-cover", "HBCU Achiever Awards cover graphic", "Design"),
 ("shot/patti", "Patti LaBelle photographed by Leo Operations", "Photography"),
 ("work/maynard-postcard", "Campaign mail piece design", "Design"),
 ("shot/jeezy", "Jeezy photographed by Leo Operations", "Photography"),
 ("work/gentry-invite", "Event invitation design", "Design"),
]
P_FOR = [
 ('Founders and executives', 'Build the personal brand that opens doors: headshots, speaking clips, thought leadership video and a feed that looks like you mean it.'),
 ('Candidates and elected officials', 'Stay visible between elections with weekly photo, video and graphics from the team that already runs campaign media.'),
 ('PACs, nonprofits and advocacy groups', 'Tell the story behind the cause every month, from event coverage to short films your supporters share.'),
 ('Public figures, artists and athletes', 'Content that matches the stage you are on, shot by the photographers behind Beyonce, JAY-Z and the Met Gala.'),
 ('Brands and businesses', 'Real estate, hospitality, lifestyle and corporate teams that need a consistent visual presence on every platform.'),
 ('Launches and campaigns', 'A focused month of content for a product, a book, a tour, an announcement or a run for office.'),
]
P_GET = [
 ('Video', 'Stories that move people.', ['Short-form vertical video for Reels, TikTok and YouTube Shorts', 'Brand films and personal brand documentaries', 'Commercials for TV, streaming and social', 'Speaking, interview and event coverage']),
 ('Photography', 'Your brand at its best.', ['Personal brand and lifestyle shoots', 'Headshots and executive portraits', 'Product, real estate and event photography', 'A fresh, organized image library every month']),
 ('Design', 'One look everywhere.', ['Brand identity, logos and guidelines', 'Social media graphics for every platform', 'Websites, print and marketing materials', 'Ad creative for digital and connected TV']),
]
P_TERMS = [
 ('One month', 'The brand sprint.', ['A focused month of shoot days, edits and graphics', 'Built for a launch, a relaunch, a campaign push or a new personal brand', 'Leaves you with a full library of photos, short videos and designs']),
 ('Three months', 'The quarter.', ['Monthly shoot days and a steady content calendar', 'Enough time to build a recognizable look and real momentum', 'Monthly planning so every post has a purpose']),
 ('Six months', 'The build.', ['Full creative direction and campaign development', 'Increased content volume with priority turnaround', 'Travel and on-demand coverage when your schedule moves']),
]
P_STEPS = [
 ('Reach out', 'Email us your brand, your goals and the term you are considering. We reply within one business day.'),
 ('Strategy', 'A discovery call to align on your brand, audience and content direction, then a visual roadmap and written proposal.'),
 ('Production', 'We plan it, shoot it, design it and edit it. You show up for your shoot days. We handle the rest.'),
 ('Delivery', 'Finished content arrives on a set schedule every month, ready to post.'),
]
P_FIT = ['You want to be seen consistently, not once', 'Your brand, your race or your cause is ready to grow', 'You value quality and want one team that owns the look', 'You will commit time for shoot days and approvals']
P_NOT = ['You need a single logo or one quick photo', 'You are shopping only for the lowest price', 'You want content without a plan behind it']
P_FAQ = [
 ('What is a content partnership?', 'A monthly engagement where Leo Operations plans, shoots, designs and delivers your photo, video and graphics on a set schedule, so your brand shows up consistently across every platform.'),
 ('Can I book just one month?', 'Yes. A one-month brand sprint works well for a launch, a relaunch, a campaign push or building a personal brand from scratch. Three-month and six-month partnerships build lasting momentum.'),
 ('What do I receive each month?', 'A combination of shoot days for photo and video, edited short-form and long-form video, a photo library and graphic design assets. Your proposal spells out the volume for your term.'),
 ('Do you work with candidates and PACs?', 'Yes. Political media is where Leo Operations started. We produce content for candidates, elected officials, PACs and advocacy groups year-round, not only in campaign season.'),
 ('Do your fees include ad spend?', 'No. Advertising and platform costs are paid directly by the client. We offer ad strategy and management as an additional service.'),
 ('Do you travel?', 'Yes. Partnerships include travel within 100 miles of Nashville, and we travel nationwide for partners outside that range.'),
 ('How many partners do you take on?', 'A limited number at a time, so every partner gets our full attention and a consistent team.'),
 ('How do we get started?', 'Email us with your name and brand, your industry and location, the term you are considering, when you want to start and why now. We reply within one business day to schedule a discovery call.'),
]
P_TITLE = 'Personal Brand Content Creation: Monthly Photo, Video & Design | Leo Operations'
P_DESC = 'Monthly content partnerships for founders, executives, candidates, PACs and brands. Photo, video and design for one, three or six months from Leo Operations in Nashville.'
P_CSS = '''<style>
.pfor{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(12px,1.6vw,20px)}
.pfor>div{border:1px solid var(--line);border-radius:22px;padding:clamp(22px,2.6vw,34px);background:linear-gradient(160deg,rgba(79,208,255,.06),rgba(7,13,26,.4) 60%)}
.pfor h3{font-family:var(--display);font-size:clamp(19px,1.7vw,24px);letter-spacing:-.02em;margin-bottom:10px}.pfor p{color:var(--silver);font-size:15px}
.pterms>div:nth-child(2){border-color:rgba(79,208,255,.6);box-shadow:0 30px 90px -40px rgba(79,208,255,.6)}
.pfit{display:grid;grid-template-columns:1fr 1fr;gap:clamp(12px,1.6vw,20px)}
.pfit>div{border:1px solid var(--line);border-radius:22px;padding:clamp(24px,3vw,40px)}
.pfit h3{font-family:var(--display);font-size:24px;margin-bottom:18px}.pfit ul{list-style:none;display:grid;gap:12px}
.pfit li{padding-left:30px;position:relative;color:var(--silver)}.pfit li::before{position:absolute;left:0;font-weight:700}
.pfit .y li::before{content:"\\2713";color:var(--cyan)}.pfit .n li::before{content:"\\00d7";color:var(--faint)}
.pask{list-style:none;display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin:0 auto 34px;max-width:760px}
.pask li{font-family:var(--mono);font-size:12px;letter-spacing:.06em;padding:10px 16px;border-radius:999px;border:1px solid rgba(79,208,255,.3);background:rgba(3,6,12,.4)}
@media (max-width:900px){.pfor{grid-template-columns:1fr 1fr}.pfit{grid-template-columns:1fr}}
@media (max-width:620px){.pfor{grid-template-columns:1fr}}
</style>'''

def partners_page():
    def body(pre):
        P = pre + 'assets/img/'
        marq_items = ['Personal brands', 'Founders', 'Candidates', 'PACs', 'Brand films', 'Short-form', 'Photography', 'Design'] * 2
        marq = ''.join(f'<span class="{"o" if i % 2 else ""}">{w}</span><i>&#9670;</i>' for i, w in enumerate(marq_items))
        forc = ''.join(f'<div data-r="{i%3}"><h3>{E(h)}</h3><p>{E(p)}</p></div>' for i, (h, p) in enumerate(P_FOR))
        def cards(rows): return ''.join(f'<div data-r="{i}"><span class="mono" style="color:var(--gold)">0{i+1}</span><h3>{E(h)}</h3><span class="t">{E(t)}</span><ul>{"".join(f"<li>{E(x)}</li>" for x in pts)}</ul></div>' for i, (h, t, pts) in enumerate(rows))
        wall = ''.join(f'<figure data-r="{i%3}">{img("assets/"+f+".jpg", alt, pre)}<figcaption class="mono">{c}</figcaption></figure>' for i, (f, alt, c) in enumerate(P_WALL))
        steps = ''.join(f'<div data-r="{i}"><b>0{i+1}</b><h3>{E(h)}</h3><p>{E(p)}</p></div>' for i, (h, p) in enumerate(P_STEPS))
        fit = ''.join(f'<li>{E(x)}</li>' for x in P_FIT); nofit = ''.join(f'<li>{E(x)}</li>' for x in P_NOT)
        faq = ''.join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in P_FAQ)
        ask = ''.join(f'<li>{x}</li>' for x in ['Name and brand', 'Industry and city', 'One, three or six months', 'When you want to start', 'Why now'])
        subj = 'Content%20partnership%20inquiry'
        cta = mail("rod", "leooperations.com", "Start a partnership <span class=\"arr\">&rarr;</span>", "btn primary", subj)
        return f'''{E_CSS}{P_CSS}<div class="wed edu">
<section class="hero whero"><div class="hero-media"><video id="phv" muted loop playsinline autoplay preload="auto" poster="{P}v2-media.jpg" data-q="{P}v2-media"></video><script>(function(){{var v=document.getElementById("phv"),w=innerWidth*Math.min(2,devicePixelRatio||1);v.src=v.dataset.q+(w>=2300?"-4k":w>=1000?"-hd":"-sd")+".mp4";var p=v.play();if(p)p.catch(function(){{}})}})()</script></div>
<div class="wtop mono"><span>Leo Operations / Content partnerships</span><span>Nashville &amp; nationwide</span></div>
<div class="hero-inner"><span class="eyebrow mono">Monthly photo, video &amp; design</span><h1 style="margin-top:18px">{split("Your brand.|<span class=serif>Handled every month.</span>")}</h1>
<p class="lead">Content partnerships for founders, executives, candidates, PACs and growing brands. We plan it, shoot it, design it and deliver it, for one month, three months or six.</p>
<div class="hero-ctas">{cta}<a class="btn ghost" href="#work">See the work <span class="arr">&rarr;</span></a></div></div></section>
<div class="marq wmarq" aria-hidden="true"><div class="t">{marq}{marq}</div></div>
<section class="wman"><span class="eyebrow mono" style="margin-bottom:30px">01 / Not a content vendor</span><p>Most brands post when they remember. Our partners show up every week with photos, films and graphics that look like they came from the same studio, <em>because they did.</em> One team owns your look from strategy to delivery.</p></section>
<section class="sec wrap"><span class="eyebrow mono">02 / Who it is for</span><h2 class="h-lg" style="margin:14px 0 34px">{split("Built for people|<span class=serif>who need to be seen.</span>")}</h2><div class="pfor">{forc}</div></section>
<section class="sec wrap"><span class="eyebrow mono">03 / What we create</span><h2 class="h-lg" style="margin:14px 0 34px">{split("Video. Photography.|<span class=serif>Design.</span>")}</h2><div class="wget">{cards(P_GET)}</div></section>
<section class="sec wrap" id="terms"><div class="sec-head"><div><span class="eyebrow mono">04 / Choose your term</span><h2 class="h-lg" style="margin-top:14px">{split("One month,|<span class=serif>three or six.</span>")}</h2></div><p>Every partnership is scoped in a written proposal built around your goals, your schedule and how much content you need.</p></div><div class="wget pterms">{cards(P_TERMS)}</div></section>
<section class="sec wrap" id="work"><div class="sec-head"><div><span class="eyebrow mono">05 / The work</span><h2 class="h-lg" style="margin-top:14px">{split("Films and photos|<span class=serif>people remember.</span>")}</h2></div><p>Brand films, event films and campaign ads from our YouTube channel, plus photography and design from our partners.</p></div>{films_html(pre)}<div class="wwall" style="margin-top:clamp(14px,2vw,26px)">{wall}</div></section>
<section class="sec wrap"><span class="eyebrow mono">06 / How it works</span><h2 class="h-lg" style="margin:14px 0 34px">{split("Four steps.|<span class=serif>Then it runs itself.</span>")}</h2><div class="wsteps" style="grid-template-columns:repeat(4,1fr)">{steps}</div></section>
<section class="sec wrap"><span class="eyebrow mono">07 / Is this right for you</span><h2 class="h-lg" style="margin:14px 0 34px">{split("We take on|<span class=serif>a limited number of partners.</span>")}</h2><div class="pfit"><div class="y" data-r="0"><h3>This is for you</h3><ul>{fit}</ul></div><div class="n" data-r="1"><h3>Not the right fit</h3><ul>{nofit}</ul></div></div></section>
<section class="sec wrap"><span class="eyebrow mono">08 / FAQ</span><h2 class="h-lg" style="margin:14px 0 30px">Partnership questions, <span class="serif">answered.</span></h2><div class="faq">{faq}</div><p style="color:var(--dim);margin-top:24px">Payment, scope, travel and usage are covered in our <a href="{pre}terms/" style="color:var(--cyan)">terms of service</a>.</p></section>
<section class="wcta" id="start"><video muted loop playsinline preload="none" poster="{P}v2-media.jpg" data-q="{P}v2-media"></video><span class="eyebrow mono">Limited partner spots each quarter</span><h2 style="margin-top:20px">Ready to <span class="serif">be seen?</span></h2><p>Send us a short note with the details below. We reply within one business day to set up your discovery call.</p><ul class="pask">{ask}</ul>{cta}</section>
<div class="marq wmarq rev" aria-hidden="true"><div class="t">{marq}{marq}</div></div>
</div>{W_JS}'''
    url = SITE + '/content-partnerships/'
    ld = [
      {"@context": "https://schema.org", "@type": "Service", "@id": url + "#service", "name": "Monthly Content Partnerships: Personal Brand Photo, Video and Design",
       "serviceType": ["Personal brand content creation", "Monthly content creation", "Brand photography", "Brand videography", "Social media content", "Graphic design"],
       "provider": {"@id": SITE + "/#organization"}, "areaServed": [{"@type": "City", "name": "Nashville"}, {"@type": "Country", "name": "United States"}],
       "url": url, "image": SITE + "/assets/img/v2-media.jpg", "description": P_DESC},
      {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in P_FAQ]},
      {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Content Partnerships", "item": url}]},
    ]
    page('content-partnerships/', P_TITLE, P_DESC, body, og='assets/img/v2-media.jpg', extra_ld=ld)
