# ---------- CHURCHES (/churches/) ----------
# exec'd by build.py after _weddings.py (reuses W_CSS/W_JS, recolored gold/purple). Media in assets/church (Rod's Pixieset, Drive and
# Dropbox church shoots, max three photos per church) and assets/work (Morganne's church graphics). Facts only: no prices.
CH_WALL = [  # (file, alt, caption)
 ("fbc-1", "Packed sanctuary and brass section at the First Baptist Church, Capitol Hill Christmas concert", "First Baptist Church, Capitol Hill"),
 ("ac-2", "Choir in maroon robes worshipping at Allen Chapel AME", "Allen Chapel AME"),
 ("miller-1", "Bishop speaking at the pulpit beside gold 16 balloons", "16th Pastoral Anniversary"),
 ("nc-1", "Choir and pulpit at the Nashville City Missionary Baptist District Association gathering", "NCMBDA"),
 ("mtb-1", "Mount Bethlehem Baptist Church choir in blue shirts", "Mount Bethlehem Baptist Church"),
 ("imf-2", "Full sanctuary at an Interdenominational Ministers Fellowship service", "Interdenominational Ministers Fellowship"),
 ("dh-2", "Gospel artist leading worship with arms wide", "Sunday service with Deitrick Haddon"),
 ("fmb-1", "Wide view of Friendship Missionary Baptist Church sanctuary during a service", "Friendship Missionary Baptist Church"),
 ("js-1", "Youth filling the pews for an MLK Day service", "MLK Day youth service"),
 ("fbc-3", "Church member with hands raised in worship", "First Baptist Church, Capitol Hill"),
 ("jk-1", "Congregation clapping in purple pews", "Joy Kimbrough swearing-in"),
 ("fuzz-1", "Pastor with women of the church in royal blue", "Pastor anniversary"),
 ("ac-1", "Packed sanctuary at Allen Chapel AME", "Allen Chapel AME"),
 ("miller-2", "Church members dancing in the aisle", "16th Pastoral Anniversary"),
 ("nc-3", "Wide view of the sanctuary at Fairfield", "NCMBDA"),
 ("mtb-2", "Mount Bethlehem choir singing outdoors", "Mount Bethlehem Baptist Church"),
 ("imf-1", "Preacher at the pulpit with green paraments", "Interdenominational Ministers Fellowship"),
 ("dh-1", "Full congregation group photo after service", "Sunday service with Deitrick Haddon"),
 ("fmb-3", "Speaker at the Friendship pulpit", "Friendship Missionary Baptist Church"),
 ("fbc-2", "Balcony view of the First Baptist Church, Capitol Hill sanctuary on its 160th anniversary", "First Baptist Church, Capitol Hill"),
 ("js-3", "Minister at the pulpit with the youth choir behind him", "MLK Day youth service"),
 ("jk-2", "Speaker at the pulpit during the swearing-in", "Joy Kimbrough swearing-in"),
 ("ac-3", "Preacher at the Allen Chapel pulpit", "Allen Chapel AME"),
 ("miller-3", "Sanctuary decorated for a 16th pastoral anniversary", "16th Pastoral Anniversary"),
 ("fuzz-2", "Pastor in his robe with church leaders", "Pastor anniversary"),
 ("mtb-3", "Children at a Mount Bethlehem community day", "Mount Bethlehem Baptist Church"),
 ("nc-2", "Ushers collecting the offering", "NCMBDA"),
 ("imf-3", "Ministers seated in the pulpit", "Interdenominational Ministers Fellowship"),
 ("fmb-2", "Women of the church applauding", "Friendship Missionary Baptist Church"),
 ("dh-3", "Pastor preaching with the choir behind him", "Sunday service with Deitrick Haddon"),
 ("jk-3", "Congregation seated for the swearing-in", "Joy Kimbrough swearing-in"),
 ("js-2", "Youth gathered in a brick sanctuary", "MLK Day youth service"),
]
CH_SERVED = ['Cathedral of Praise', 'First Baptist Church, Capitol Hill', 'St. Andrew’s Presbyterian Church', 'Allen Chapel AME', 'Mount Bethlehem Baptist Church',
             'Friendship Missionary Baptist Church', 'COP Global Ministry', 'Nashville City Missionary Baptist District Association',
             'Interdenominational Ministers Fellowship', 'Church of God in Christ']
CH_DESIGN = [('c-60th', '60th anniversary save the date'), ('c-5th-cover', 'Pastoral anniversary program'), ('c-sunday', 'Sunday service graphic'),
             ('c-revival-aug', 'Revival Sunday flyer'), ('c-welcome-visitors', 'Welcome visitors slide'), ('c-thankyou', 'Visitor postcard'),
             ('c-midweek', 'Midweek Bible study'), ('c-citywide-oct', 'Citywide revival flyer'), ('c-5th-legacy', 'Program spread'),
             ('c-couples', 'Couples workshop'), ('c-welcome-home', 'Welcome home card'), ('c-empower', 'Empowerment Tuesday'),
             ('c-wawya', 'We Are Where You Are'), ('c-transition', 'Service transition slide'), ('c-bookmark', 'Welcome bookmark')]
CH_GET = [
 ('Capture', 'Every Sunday worth sharing.', ['Photography for worship, anniversaries, revivals, baptisms and community days',
   'Sermon clips cut for Reels, TikTok and Shorts every week', 'Anniversary recaps, new member films and ministry videos',
   'Pastor and leadership portraits']),
 ('Connect', 'A church people can find.', ['Modern church websites with service times, sermons, events and online giving',
   'Social media management, posting and engagement', 'Google Business Profile and search so visitors find you first',
   'Email and text updates for members']),
 ('Design', 'A look that matches the ministry.', ['Service graphics, flyers and event campaigns', 'Anniversary programs, bookmarks and visitor cards',
   'Worship slides and service transitions', 'Church branding and logo refreshes']),
]
CH_MENU = ['Sunday photography', 'Anniversary coverage', 'Sermon clips', 'Recap films', 'New member videos', 'Pastor portraits', 'Church websites',
           'Online giving pages', 'Sermon archives', 'Social media management', 'Service graphics', 'Event flyers', 'Anniversary programs',
           'Visitor cards', 'Worship slides', 'Church branding', 'Drone', 'Google Business Profile', 'Email and text', 'Interview series']
CH_STEPS = [
 ('Visit', 'We worship with you, meet your leaders and see what your ministry already does well.'),
 ('Plan', 'A monthly plan for photos, video, posts and web updates built around your church calendar.'),
 ('Create', 'Photo, film, graphics and web pages produced by one team in one consistent look.'),
 ('Share', 'Posts, clips and updates go out every week so members and visitors always see something new.'),
]
CH_FAQ = [
 ('What does Leo Operations do for churches?', 'Photography, video, sermon clips, websites, social media and graphic design for churches and ministries. One team handles your Sunday coverage, your anniversary film, your website and your weekly posts.'),
 ('Which churches have you worked with?', 'Cathedral of Praise, First Baptist Church Capitol Hill, St. Andrew’s Presbyterian, Allen Chapel AME, Mount Bethlehem Baptist, Friendship Missionary Baptist, the Nashville City Missionary Baptist District Association and the Interdenominational Ministers Fellowship, among others.'),
 ('Can you build our church website?', 'Yes. We build modern church sites with service times, sermons, events, ministries, plan-your-visit pages and online giving, like the new site we built for St. Andrew’s Presbyterian Church in North Nashville.'),
 ('Can you turn our sermons into social clips?', 'Yes. We cut short vertical clips with captions from each sermon so your message reaches people who were not in the room on Sunday.'),
 ('Do you cover pastoral and church anniversaries?', 'Yes. We photograph and film anniversaries, revivals and special services, design the programs and save the dates, and deliver recap films your members will share.'),
 ('Where do you work?', 'Leo Operations is based in Nashville and works with churches across Tennessee, the South and the Midwest. Our photo, film and design team travels to you.'),
 ('How do we get started?', 'Email us about your church, your ministries and what you need. We start with a conversation and follow up with a written proposal.'),
]
CH_TITLE = 'Church Photography, Video, Websites & Social Media | Leo Operations'
CH_DESC = 'Photography, sermon clips, recap films, church websites, social media and design for churches in Nashville, the South and the Midwest.'

CH_CSS = W_CSS.replace('.wed', '.chp').replace('#c79b52', '#8f5cff').replace('#140d02', '#0d0420') + '''<style>
.chp .wfilms .wfilm .pb,.chv .wfilm .pb{top:18px;left:auto;right:18px;margin:0;width:64px;height:64px}.chp .wfilms .wfilm .pb::before,.chv .wfilm .pb::before{border-width:11px 0 11px 17px;margin-left:5px}
.chv{display:grid;grid-template-columns:repeat(5,1fr);gap:clamp(10px,1.4vw,18px);margin-top:clamp(14px,2vw,26px)}
.chv .wfilm{aspect-ratio:9/16}.chv .wfilm .ov b{font-size:clamp(16px,1.4vw,22px)}.chv .wfilm .ov p{display:none}
.chserved{display:flex;flex-wrap:wrap;gap:10px 14px}.chserved span{font-family:var(--display);font-weight:600;font-size:clamp(16px,1.5vw,22px);padding:12px 22px;border-radius:999px;background:rgba(232,207,158,.06);border:1px solid rgba(232,207,158,.22)}
.chdes{columns:4 220px;column-gap:clamp(12px,1.6vw,20px)}.chdes .dp{break-inside:avoid;margin:0 0 clamp(12px,1.6vw,20px)}
.chdes .dp a{display:block;border-radius:14px;overflow:hidden;box-shadow:0 24px 60px rgba(0,0,0,.45)}.chdes .dp img{width:100%;height:auto;display:block}
.chdes figcaption{font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--dim);margin-top:8px}
.chweb{display:grid;grid-template-columns:minmax(0,8fr) minmax(0,3fr);gap:clamp(14px,2vw,26px);align-items:end}
.chweb figure{margin:0;border-radius:18px;overflow:hidden;border:1px solid rgba(232,207,158,.2);background:var(--bg2)}.chweb img{width:100%;height:auto;display:block}
.chweb figcaption{padding:12px 16px;font-family:var(--mono);font-size:11px;color:var(--dim)}
.chp .wsteps{grid-template-columns:repeat(4,1fr)}
@media (max-width:900px){.chv{grid-template-columns:repeat(3,1fr)}.chweb{grid-template-columns:1fr 1fr}.chp .wsteps{grid-template-columns:1fr 1fr}}
@media (max-width:520px){.chv{grid-template-columns:1fr 1fr}.chp .wsteps{grid-template-columns:1fr}}
</style>'''

def church_page():
    def body(pre):
        P = pre + 'assets/church/'
        marq_items = ['Churches', 'Sunday photography', 'Sermon clips', 'Church websites', 'Social media', 'Anniversaries'] * 2
        marq = ''.join(f'<span class="{"o" if i % 2 else ""}">{w}</span><i>&#9670;</i>' for i, w in enumerate(marq_items))
        def film(key, eyebrow, title, desc, cls=''):
            return (f'<div class="wfilm {cls}" data-r="0"><video preload="none" playsinline poster="{P}{key}.jpg" data-hd="{P}{key}-hd.mp4" data-sd="{P}{key}-sd.mp4"></video>'
                    f'<div class="ov"><span class="pb" aria-hidden="true"></span><span class="mono" style="color:var(--gold)">{eyebrow}</span><b>{title}</b><p>{desc}</p></div></div>')
        reel = film('ch-60th', 'Cathedral of Praise &middot; 60th anniversary recap &middot; sound on', 'Sixty years of praise.', 'A community day, a mass choir and a packed sanctuary, from the weekend Cathedral of Praise celebrated 60 years.', 'wreel')
        films = ('<div class="wfilms" style="margin-top:clamp(14px,2vw,26px)">'
                 + film('ch-newmember', 'Cathedral of Praise &middot; new member film', 'Welcome to the family.', 'The pastor welcomes new members and shares what the church believes, ready to play in the new members class and online.')
                 + film('ch-mic', 'Interview series &middot; Mic on the Floor', 'Members, on the record.', 'A church interview series that puts members and ministry leaders in front of the camera.')
                 + film('ch-webpromo', 'Website promo &middot; anniversary weekend', 'Launch the site in style.', 'A promo walking members through the anniversary weekend website: events, speakers and how to give.')
                 + film('ch-ministry', 'COP Global Ministry &middot; ministry film', 'A ministry beyond the walls.', 'An opener for the church’s global ministry, cut for services, events and social.')
                 + '</div>')
        verts = ('<div class="chv">'
                 + film('ch-cop5', '5th pastoral anniversary', 'Anniversary reel', '')
                 + film('ch-sermon1', 'Sermon clip', 'Christianity vs. hypocrisy', '')
                 + film('ch-sermon2', 'Sermon clip', 'Jesus was an immigrant', '')
                 + film('ch-sermon3', 'Sermon clip', 'Do you act like Christ?', '')
                 + film('ch-sermon4', 'Sermon clip', 'The church must awaken', '')
                 + '</div>')
        wall = ''.join(f'<figure data-r="{i%3}">{img("assets/church/"+f+".jpg", alt, pre)}<figcaption class="mono">{c}</figcaption></figure>' for i, (f, alt, c) in enumerate(CH_WALL))
        served = ''.join(f'<span data-r="{i%3}">{E(p)}</span>' for i, p in enumerate(CH_SERVED))
        des = ''.join(f'<figure class="dp"><a href="{pre}assets/work/{k}.jpg" data-img="{pre}assets/work/{k}.jpg" aria-label="View {E(t)} full size"><img src="{pre}assets/work/{k}.jpg" alt="{E(t)}, church graphic designed by Leo Operations" loading="lazy"></a><figcaption>{E(t)}</figcaption></figure>' for i, (k, t) in enumerate(CH_DESIGN))
        get = ''.join(f'<div data-r="{i}"><span class="mono" style="color:var(--gold)">0{i+1}</span><h3>{E(h)}</h3><span class="t">{E(t)}</span><ul>{"".join(f"<li>{E(x)}</li>" for x in pts)}</ul></div>' for i, (h, t, pts) in enumerate(CH_GET))
        menu = ''.join(f'<span data-r="{i%3}">{E(m)}</span>' for i, m in enumerate(CH_MENU))
        steps = ''.join(f'<div data-r="{i%4}"><b>0{i+1}</b><h3>{E(h)}</h3><p>{E(p)}</p></div>' for i, (h, p) in enumerate(CH_STEPS))
        faq = ''.join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in CH_FAQ)
        subj = 'Church%20media%20inquiry'
        return f'''{CH_CSS}<div class="wed chp">
<section class="hero whero"><div class="hero-media"><video id="chhv" muted loop playsinline autoplay preload="auto" poster="{P}ch-hero.jpg" data-q="{P}ch-hero"></video><script>(function(){{var v=document.getElementById("chhv"),w=innerWidth*Math.min(2,devicePixelRatio||1);v.src=v.dataset.q+(w>=1000?"-hd":"-sd")+".mp4";var p=v.play();if(p)p.catch(function(){{}})}})()</script></div>
<div class="wtop mono"><span>Leo Operations / Churches</span><span>The South &amp; the Midwest</span></div>
<div class="hero-inner"><span class="eyebrow mono">Church media</span><h1 style="margin-top:18px">{split("Tell the story|<span class=serif>of your church.</span>")}</h1>
<p class="lead">Photography, sermon clips, recap films, websites, social media and design for churches and ministries. One team, every Sunday.</p>
<div class="hero-ctas">{mail("rod","leooperations.com","Talk with our team <span class=\"arr\">&rarr;</span>","btn primary",subj)}<a class="btn ghost" href="#films">Watch the films <span class="arr">&rarr;</span></a></div></div></section>
<div class="marq wmarq" aria-hidden="true"><div class="t">{marq}{marq}</div></div>
<section class="wman"><span class="eyebrow mono" style="margin-bottom:30px">01 / Why it matters</span><p>Your next member will find your church <em>on a phone</em> before they ever walk through the door. They will check your website, scroll your page and watch a clip of your pastor. We make sure what they see looks like the church you really are.</p></section>
<section class="sec wrap" id="films"><div class="sec-head"><div><span class="eyebrow mono">02 / Films</span><h2 class="h-lg" style="margin-top:14px">{split("Moments your members|<span class=serif>will share.</span>")}</h2></div><p>Anniversary recaps, new member films, interview series and weekly sermon clips we produced for churches. Press play with the sound on.</p></div>{reel}{films}{verts}</section>
<section class="sec wrap"><span class="eyebrow mono">03 / Churches we have served</span><h2 class="h-lg" style="margin:14px 0 34px">{split("Pulpits, choirs|<span class=serif>and congregations.</span>")}</h2><div class="chserved">{served}</div></section>
<section class="sec wrap" id="photos"><div class="sec-head"><div><span class="eyebrow mono">04 / Photography</span><h2 class="h-lg" style="margin-top:14px">{split("Every pew.|<span class=serif>Every praise.</span>")}</h2></div><a class="btn ghost" href="https://rodwrightphotography.pixieset.com/" target="_blank" rel="noopener">Full galleries <span class="arr">&rarr;</span></a></div><div class="wwall">{wall}</div></section>
<section class="sec wrap" id="design"><div class="sec-head"><div><span class="eyebrow mono">05 / Design</span><h2 class="h-lg" style="margin-top:14px">{split("Graphics for|<span class=serif>every service.</span>")}</h2></div><p>Service graphics, revival flyers, anniversary programs, visitor cards and worship slides, designed in house by <a href="{pre}team/morganne-norwood/#portfolio" style="color:var(--gold)">Morganne Norwood</a>. Tap any piece to see it full size.</p></div><div class="chdes">{des}</div></section>
<section class="sec wrap" id="websites"><div class="sec-head"><div><span class="eyebrow mono">06 / Websites</span><h2 class="h-lg" style="margin-top:14px">{split("A front door|<span class=serif>that is always open.</span>")}</h2></div><p>We built a new website for St. Andrew&rsquo;s Presbyterian Church, a North Nashville congregation since 1898, with service times, weekly sermons and transcripts, events and a plan-your-visit page.</p></div>
<div class="chweb"><figure data-r="0">{img("assets/church/sa-desktop.jpg", "St. Andrew's Presbyterian Church website homepage built by Leo Operations", pre)}<figcaption>St. Andrew&rsquo;s Presbyterian Church &middot; desktop</figcaption></figure><figure data-r="1">{img("assets/church/sa-mobile.jpg", "St. Andrew's Presbyterian Church website on a phone", pre)}<figcaption>Mobile</figcaption></figure></div></section>
<section class="sec wrap"><span class="eyebrow mono">07 / What we build</span><h2 class="h-lg" style="margin:14px 0 34px">{split("Capture. Connect.|<span class=serif>Design.</span>")}</h2><div class="wget">{get}</div></section>
<section class="sec wrap"><div class="sec-head"><div><span class="eyebrow mono">08 / Every service</span><h2 class="h-lg" style="margin-top:14px">{split("Pick what|<span class=serif>your ministry needs.</span>")}</h2></div><p>Most churches start with a website and Sunday photography, then add sermon clips and social media.</p></div><div class="wmom">{menu}</div></section>
<section class="sec wrap"><span class="eyebrow mono">09 / How it works</span><h2 class="h-lg" style="margin:14px 0 34px">{split("Four steps.|<span class=serif>Every month.</span>")}</h2><div class="wsteps">{steps}</div></section>
<section class="sec wrap"><span class="eyebrow mono">10 / FAQ</span><h2 class="h-lg" style="margin:14px 0 30px">Church questions, <span class="serif">answered.</span></h2><div class="faq">{faq}</div></section>
<section class="wcta" id="start"><video muted loop playsinline preload="none" poster="{P}ch-hero.jpg" data-q="{P}ch-hero"></video><span class="eyebrow mono">Churches and ministries</span><h2 style="margin-top:20px">Let&rsquo;s fill <span class="serif">your pews.</span></h2><p>Tell us about your church and what you need. We will set up a conversation and send a written proposal.</p>{mail("rod","leooperations.com","Talk with our team <span class=\"arr\">&rarr;</span>","btn primary",subj)}</section>
<div class="marq wmarq rev" aria-hidden="true"><div class="t">{marq}{marq}</div></div>
</div>{W_JS}'''
    url = SITE + '/churches/'
    ld = [
      {"@context": "https://schema.org", "@type": "Service", "@id": url + "#service", "name": "Church Photography, Video, Websites and Social Media",
       "serviceType": ["Church photography", "Church videography", "Sermon clips", "Church website design", "Church social media management", "Church graphic design"],
       "provider": {"@id": SITE + "/#organization"}, "audience": {"@type": "Audience", "audienceType": "Churches and ministries"},
       "areaServed": [{"@type": "State", "name": "Tennessee"}, {"@type": "Country", "name": "United States"}], "url": url, "image": SITE + "/assets/church/ch-hero.jpg", "description": CH_DESC},
      {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in CH_FAQ]},
      {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Churches", "item": url}]},
      {"@context": "https://schema.org", "@type": "VideoObject", "name": "Cathedral of Praise 60th Anniversary Recap", "description": "Recap film of the Cathedral of Praise 60th church anniversary weekend in Nashville, produced by Leo Operations.",
       "thumbnailUrl": SITE + "/assets/church/ch-60th.jpg", "contentUrl": SITE + "/assets/church/ch-60th-hd.mp4", "uploadDate": "2026-10-28T12:00:00-05:00", "duration": "PT5M20S"},
    ]
    page('churches/', CH_TITLE, CH_DESC, body, og='assets/church/ch-hero.jpg', extra_ld=ld)
