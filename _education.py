# ---------- EDUCATION (/education/) ----------
# exec'd by build.py after _weddings.py (reuses W_CSS/W_JS look, recolored). Media in assets/education (Leo films + Pixieset + Rod's school shoots).
# Replaces education.leooperations.com (Landingsite). Facts only: no prices, no invented stats or testimonials.
E_WALL = [  # (file, alt, caption)
 ("meharry-match26-6", "Meharry Medical College Match Day residency map", "Meharry Medical College"),
 ("fd-7", "Student working with Montessori materials on the first day of school", "First day of school"),
 ("tsu26-17", "Tennessee State University students at homecoming", "Tennessee State University"),
 ("hs-17", "High school student learning pipefitting at a trades training center", "Career exploration day"),
 ("invictus-grad-0", "Invictus Nashville student recognition ceremony", "Invictus Nashville"),
 ("mg-36", "Music City Construction Careers graduates holding their certificates", "MC3 graduation"),
 ("meharry-awards26-21", "Meharry students at the Honors and Awards Program", "Meharry Medical College"),
 ("fd-2", "Young students gathered for circle time", "First day of school"),
 ("hs-10", "Student testing equipment during a career exploration day", "Career exploration day"),
 ("invictus-grad-27", "Invictus student smiling during the recognition ceremony", "Invictus Nashville"),
 ("tsu26-18", "Tennessee State University students at the homecoming parade", "Tennessee State University"),
 ("meharry-match26-41", "Meharry medical student on Match Day", "Meharry Medical College"),
 ("mt-27", "Pre-apprenticeship students reviewing training materials", "Music City Construction Careers"),
 ("fd-36", "Students lining up in their classroom", "First day of school"),
 ("hs-21", "High school students on a trades center visit", "Career exploration day"),
 ("invictus-grad-24", "Invictus students walking in their ceremony", "Invictus Nashville"),
 ("mg-26", "MC3 graduate receiving a certificate", "MC3 graduation"),
 ("meharry-match25-11", "Meharry students at Match Day 2025", "Meharry Medical College"),
 ("fd-12", "Students in a Montessori classroom", "First day of school"),
 ("hs-38", "Student practicing with a torch at a trades training center", "Career exploration day"),
 ("meharry-awards26-20", "Meharry students and faculty at the awards program", "Meharry Medical College"),
 ("hs-27", "Student cutting copper pipe during a career exploration day", "Career exploration day"),
 ("fd-26", "Teacher reading with students on the first day", "First day of school"),
 ("mt-25", "MC3 students in a training session", "Music City Construction Careers"),
]
E_PARTNERS = ['Purpose Prep', 'RePublic High School', 'Rocketship United Academy', 'Smithson Craighead Academy', 'LEAD Prep Southeast',
              'Liberty Collegiate Academy', 'Nashville Prep', 'Invictus Nashville', 'Tennessee State University', 'Fisk University',
              'Meharry Medical College', 'Music City Construction Careers', 'Tennessee Higher Education Initiative']
E_GET = [
 ('Recruit', 'Enrollment that runs all year.', ['A year-round recruitment plan built around your district’s school choice calendar',
   'Neighborhood canvassing, phone and text outreach to prospective families', 'Info sessions, open houses and school tours that families actually attend',
   'Weekly tracking of every family from first inquiry to the first day of school']),
 ('Engage', 'Families who become advocates.', ['Family engagement and parent ambassador programs', 'Parent advocacy training and community organizing',
   'Staff training on recruitment, follow-up and family communication', 'Coalitions with churches, employers and neighborhood groups']),
 ('Tell', 'Your school, on camera.', ['Photography for campuses, classrooms, graduations and events', 'Recruitment films, student voice videos and short-form social',
   'Websites, social media management and graphic design', 'Messaging, talking points and strategic communications']),
]
E_MENU = ['Student recruitment', 'Enrollment strategy', 'Door-to-door canvassing', 'Phone and text outreach', 'Open houses and tours', 'Family engagement',
          'Parent ambassadors', 'Parent advocacy training', 'Staff training', 'Community organizing', 'Coalition building', 'Strategic communications',
          'Crisis communications', 'Messaging', 'Photography', 'Videography', 'Drone', 'Social media', 'Websites', 'Graphic design',
          'Annual reports', 'Event production', 'Digital advertising', 'Advocacy and public affairs', 'School board campaigns']
E_FUNNEL = ['Awareness', 'Inquiry', 'School tour', 'Open house', 'Application', 'Lottery offer', 'Acceptance', 'Registration', 'First day', 'Retention']
E_STEPS = [
 ('Discover', 'We study your enrollment history, waitlists, conversion at each stage, neighborhoods and how families see your school today.'),
 ('Plan', 'A recruitment and communications plan with monthly targets, weekly benchmarks and a calendar matched to your enrollment cycle.'),
 ('Create', 'Photo, film, messaging, materials and web content built around the plan, not in isolation.'),
 ('Launch', 'Organizers in neighborhoods, events on the calendar and campaigns live across every channel your families use.'),
 ('Measure', 'A weekly scorecard that shows where families enter, where they stall and what to do next.'),
]
E_JL = [
 ('Metro Nashville Board of Education', 'Won the 2020 District 4 special election in a four-way race with 9,660 votes and served Donelson, Hermitage and Old Hickory families through 2022.'),
 ('Public Advocate Fellowship', 'Co-founded the fellowship that trains parents to advocate for their children’s schools. Its work helped launch Memphis Lift and Nashville Propel.'),
 ('Strategy Redefined', 'Ran a Nashville education consulting firm that helped launch Memphis Lift.'),
 ('Tennessee Charter School Center', 'Served as director of community engagement.'),
 ('Parent organizing', 'Organizing specialist and Nashville coach at Organizer Zero, and director of The Surge Team, the grassroots organizing arm of Memphis Lift.'),
 ('Tennessee State University', 'TSU graduate and Pahara Institute fellow.'),
]
E_FAQ = [
 ('What kinds of schools does Leo Operations work with?', 'Public charter schools, traditional public schools and districts, private and independent schools, colleges and universities, medical and graduate programs, early learning programs, career and trades training programs, and education nonprofits.'),
 ('How do you help a school grow enrollment?', 'We build a year-round recruitment plan, put organizers in the neighborhoods your families live in, run info sessions, tours and open houses, and track every family weekly from first inquiry to the first day. Leaders always know where families are coming from and where they are being lost.'),
 ('Who leads the education work?', 'John Little, a former member of the Metro Nashville Board of Education and a co-founder of the Public Advocate Fellowship, leads recruitment, family engagement and training. Founder Rodriquez Wright II leads strategy, photography and film.'),
 ('Do you photograph and film school events?', 'Yes. We cover graduations, recognition ceremonies, Match Day, homecoming, first days of school, campus tours and classroom life, and we produce recruitment films, student voice videos and short-form social content.'),
 ('Do you train school staff?', 'Yes. We coach teams on recruitment best practices, family follow-up, enrollment tracking and communication standards so the work keeps going after our engagement ends.'),
 ('Where do you work?', 'We are based in Nashville and work with schools across Tennessee. Our photo, film and training teams travel nationwide.'),
 ('How do we get started?', 'Email us about your school, your enrollment goals and your timeline. We start with a strategy session and follow up with a written proposal.'),
]
E_TITLE = 'School Enrollment, Recruitment & Education Marketing | Leo Operations'
E_DESC = 'Student recruitment, family engagement, staff training and photo and film for schools and colleges. Led by former Metro Nashville school board member John Little.'

E_CSS = W_CSS.replace('.wed', '.edu').replace('#e8cf9e', '#4fd0ff').replace('#c79b52', '#2f8bff').replace('#fff4dc', '#dff6ff').replace('232,207,158', '79,208,255').replace('#140d02', '#03101e') + '''<style>
.edu .wfilms .wfilm .pb,.eshorts .wfilm .pb{top:18px;left:auto;right:18px;margin:0;width:64px;height:64px}.edu .wfilms .wfilm .pb::before,.eshorts .wfilm .pb::before{border-width:11px 0 11px 17px;margin-left:5px}
.eshorts{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(12px,1.6vw,20px);margin-top:clamp(14px,2vw,26px)}
.eshorts .wfilm{aspect-ratio:9/16}.eshorts .wfilm .ov b{font-size:clamp(18px,1.6vw,24px)}
.ejl{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:clamp(24px,4vw,64px);align-items:start}
.ejl figure{border-radius:22px;overflow:hidden;border:1px solid rgba(79,208,255,.2);position:sticky;top:110px}
.ejl figure img{width:100%;height:auto;display:block}
.ejl figcaption{padding:16px 20px;background:var(--bg2)}.ejl figcaption b{font-family:var(--display);font-size:20px;display:block}.ejl figcaption span{color:var(--dim);font-size:14px}
.ejl .q{font-family:var(--display);font-weight:600;font-size:clamp(22px,2.4vw,34px);line-height:1.15;letter-spacing:-.02em;margin:18px 0 30px}
.ejl .q em{font-family:"Instrument Serif",Georgia,serif;font-weight:400;color:var(--gold)}
.ejl dl{display:grid;gap:0;border-top:1px solid rgba(79,208,255,.2)}
.ejl dl>div{padding:20px 0;border-bottom:1px solid rgba(79,208,255,.12)}
.ejl dt{font-family:var(--display);font-size:18px;margin-bottom:6px}.ejl dd{color:var(--silver);margin:0}
.efun{display:flex;flex-wrap:wrap;gap:10px;counter-reset:fn}.efun span{font-family:var(--mono);font-size:13px;letter-spacing:.04em;padding:12px 18px;border-radius:999px;border:1px solid rgba(79,208,255,.28)}
.efun span::before{counter-increment:fn;content:counter(fn,decimal-leading-zero) "  ";color:var(--gold)}
.edu .wsteps{grid-template-columns:repeat(5,1fr)}
.epart{display:flex;flex-wrap:wrap;gap:10px 14px}.epart span{font-family:var(--display);font-weight:600;font-size:clamp(16px,1.5vw,22px);padding:12px 22px;border-radius:999px;background:rgba(79,208,255,.06);border:1px solid rgba(79,208,255,.22)}
@media (max-width:900px){.ejl{grid-template-columns:1fr}.ejl figure{position:static;max-width:420px}.edu .wsteps{grid-template-columns:1fr 1fr}.eshorts{grid-template-columns:1fr 1fr}}
@media (max-width:520px){.edu .wsteps{grid-template-columns:1fr}.eshorts{grid-template-columns:1fr}}
</style>'''

def education_page():
    def body(pre):
        P = pre + 'assets/education/'
        marq_items = ['Student recruitment', 'Enrollment', 'Family engagement', 'Training', 'Photo &amp; film', 'Tennessee &amp; nationwide'] * 2
        marq = ''.join(f'<span class="{"o" if i % 2 else ""}">{w}</span><i>&#9670;</i>' for i, w in enumerate(marq_items))
        def film(key, eyebrow, title, desc, cls=''):
            return (f'<div class="wfilm {cls}" data-r="0"><video preload="none" playsinline poster="{P}{key}.jpg" data-hd="{P}{key}-hd.mp4" data-sd="{P}{key}-sd.mp4"></video>'
                    f'<div class="ov"><span class="pb" aria-hidden="true"></span><span class="mono" style="color:var(--gold)">{eyebrow}</span><b>{title}</b><p>{desc}</p></div></div>')
        def short(n, title):
            return (f'<div class="wfilm" data-r="{n%3}"><video preload="none" playsinline poster="{P}e-short{n}.jpg" data-hd="{P}e-short{n}.mp4" data-sd="{P}e-short{n}.mp4"></video>'
                    f'<div class="ov"><span class="pb" aria-hidden="true"></span><span class="mono" style="color:var(--gold)">Invictus Nashville &middot; social</span><b>{title}</b></div></div>')
        reel = film('e-reel', 'Highlight reel &middot; 60 seconds &middot; sound on', 'Schools families choose.', 'Classrooms, career training, homecoming and the students at the center of it, from films we produced.', 'wreel')
        films = (f'<div class="wfilms" style="margin-top:clamp(14px,2vw,26px)">'
                 + film('e-invictus', 'Invictus Nashville &middot; student voices', 'In their own words.', 'Invictus students tell families why they love their school and why they should come. A recruitment film in the voices families trust most.')
                 + film('e-mc3', 'Music City Construction Careers &middot; 4 min', 'Three weeks. One new career.', 'A pre-apprenticeship class, from the first day of training to graduation, told by the students who lived it.')
                 + '</div>')
        shorts = '<div class="eshorts">' + short(1, 'Why hands-on learning wins') + short(2, 'A Montessori experience families notice') + short(3, 'Educator, parent and Montessori approved') + '</div>'
        wall = ''.join(f'<figure data-r="{i%3}">{img("assets/education/"+f+".jpg", alt, pre)}<figcaption class="mono">{c}</figcaption></figure>' for i, (f, alt, c) in enumerate(E_WALL))
        partners = ''.join(f'<span data-r="{i%3}">{E(p)}</span>' for i, p in enumerate(E_PARTNERS))
        get = ''.join(f'<div data-r="{i}"><span class="mono" style="color:var(--gold)">0{i+1}</span><h3>{E(h)}</h3><span class="t">{E(t)}</span><ul>{"".join(f"<li>{E(x)}</li>" for x in pts)}</ul></div>' for i, (h, t, pts) in enumerate(E_GET))
        menu = ''.join(f'<span data-r="{i%3}">{E(m)}</span>' for i, m in enumerate(E_MENU))
        funnel = ''.join(f'<span>{E(s)}</span>' for s in E_FUNNEL)
        steps = ''.join(f'<div data-r="{i%4}"><b>0{i+1}</b><h3>{E(h)}</h3><p>{E(p)}</p></div>' for i, (h, p) in enumerate(E_STEPS))
        jl = ''.join(f'<div><dt>{E(h)}</dt><dd>{E(p)}</dd></div>' for h, p in E_JL)
        faq = ''.join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in E_FAQ)
        subj = 'Education%20services%20inquiry'
        return f'''{E_CSS}<div class="wed edu">
<section class="hero whero"><div class="hero-media"><video id="ehv" muted loop playsinline autoplay preload="auto" poster="{P}e-hero.jpg" data-q="{P}e-hero"></video><script>(function(){{var v=document.getElementById("ehv"),w=innerWidth*Math.min(2,devicePixelRatio||1);v.src=v.dataset.q+(w>=1000?"-hd":"-sd")+".mp4";var p=v.play();if(p)p.catch(function(){{}})}})()</script></div>
<div class="wtop mono"><span>Leo Operations / Education</span><span>Tennessee &amp; nationwide</span></div>
<div class="hero-inner"><span class="eyebrow mono">Education services</span><h1 style="margin-top:18px">{split("Schools families|<span class=serif>choose.</span>")}</h1>
<p class="lead">Student recruitment, family engagement, staff training and photo and film for schools, colleges and education programs. Led by former Metro Nashville school board member John Little and the Leo Operations media team.</p>
<div class="hero-ctas">{mail("rod","leooperations.com","Schedule a strategy session <span class=\"arr\">&rarr;</span>","btn primary",subj)}<a class="btn ghost" href="#films">Watch the reel <span class="arr">&rarr;</span></a></div></div></section>
<div class="marq wmarq" aria-hidden="true"><div class="t">{marq}{marq}</div></div>
<section class="wman"><span class="eyebrow mono" style="margin-bottom:30px">01 / Why Leo</span><p>Families choose a school based on what they see, what they hear and <em>who they trust.</em> We build all three: a recruitment plan that runs all year, organizers who talk with families face to face, and photo and film that show your school at its best.</p></section>
<section class="sec wrap" id="films"><div class="sec-head"><div><span class="eyebrow mono">02 / Films</span><h2 class="h-lg" style="margin-top:14px">{split("Stories that|<span class=serif>fill seats.</span>")}</h2></div><p>Recruitment films, student voices and short-form social we produced for schools and training programs. Press play with the sound on.</p></div>{reel}{films}{shorts}</section>
<section class="sec wrap"><span class="eyebrow mono">03 / Who we have worked with</span><h2 class="h-lg" style="margin:14px 0 34px">{split("Schools, colleges|<span class=serif>and programs.</span>")}</h2><div class="epart">{partners}</div></section>
<section class="sec wrap" id="photos"><div class="sec-head"><div><span class="eyebrow mono">04 / Photography</span><h2 class="h-lg" style="margin-top:14px">{split("Every student.|<span class=serif>Every milestone.</span>")}</h2></div><a class="btn ghost" href="https://rodwrightphotography.pixieset.com/" target="_blank" rel="noopener">Full galleries <span class="arr">&rarr;</span></a></div><div class="wwall">{wall}</div></section>
<section class="sec wrap" id="john-little"><span class="eyebrow mono">05 / Leadership</span><h2 class="h-lg" style="margin:14px 0 34px">{split("Led by someone who|<span class=serif>sat on the board.</span>")}</h2>
<div class="ejl"><figure data-r="0">{img("assets/team/john-little.jpg", "John Little, education lead at Leo Operations", pre)}<figcaption><b>John Little</b><span>Education lead, Leo Operations. Former Metro Nashville Board of Education member.</span></figcaption></figure>
<div data-r="1"><p class="q">John has recruited families, trained parents and governed a district. He knows how schools make decisions and what families need <em>before they say yes.</em></p><dl>{jl}</dl>
<p style="color:var(--dim);margin-top:24px">He ran for the board on one promise: every student should be college ready, career ready and community ready. At Leo Operations he leads recruitment, family engagement and training, alongside founder <a href="https://rodriquezwright.com/" style="color:var(--cyan)">Rodriquez Wright II</a>, who leads strategy, photography and film.</p>
<p style="margin-top:22px"><a class="btn ghost" href="{pre}team/john-little/">Full bio <span class="arr">&rarr;</span></a></p></div></div></section>
<section class="sec wrap"><span class="eyebrow mono">06 / What we build</span><h2 class="h-lg" style="margin:14px 0 34px">{split("Recruit. Engage.|<span class=serif>Tell your story.</span>")}</h2><div class="wget">{get}</div></section>
<section class="sec wrap"><div class="sec-head"><div><span class="eyebrow mono">07 / Every service</span><h2 class="h-lg" style="margin-top:14px">{split("Pick what|<span class=serif>your school needs.</span>")}</h2></div><p>One team for everything from your recruitment plan to your graduation photos. Most schools start with recruitment and add photo and film.</p></div><div class="wmom">{menu}</div></section>
<section class="sec wrap"><div class="sec-head"><div><span class="eyebrow mono">08 / The enrollment journey</span><h2 class="h-lg" style="margin-top:14px">{split("Ten steps.|<span class=serif>No family lost.</span>")}</h2></div><p>We map every step a family takes, set benchmarks for each one and review them weekly. Your leaders can answer four questions at any time: where are families entering, which outreach is working, where are we losing them, and what do we do this week.</p></div><div class="efun">{funnel}</div></section>
<section class="sec wrap"><span class="eyebrow mono">09 / How it works</span><h2 class="h-lg" style="margin:14px 0 34px">{split("Five steps.|<span class=serif>All year.</span>")}</h2><div class="wsteps">{steps}</div></section>
<section class="sec wrap"><span class="eyebrow mono">10 / FAQ</span><h2 class="h-lg" style="margin:14px 0 30px">School questions, <span class="serif">answered.</span></h2><div class="faq">{faq}</div></section>
<section class="wcta" id="start"><video muted loop playsinline preload="none" poster="{P}e-hero.jpg" data-q="{P}e-hero"></video><span class="eyebrow mono">Planning next enrollment season</span><h2 style="margin-top:20px">Let&rsquo;s fill <span class="serif">your seats.</span></h2><p>Tell us about your school, your enrollment goals and your timeline. We will set up a strategy session and send a written proposal.</p>{mail("rod","leooperations.com","Schedule a strategy session <span class=\"arr\">&rarr;</span>","btn primary",subj)}</section>
<div class="marq wmarq rev" aria-hidden="true"><div class="t">{marq}{marq}</div></div>
</div>{W_JS}'''
    url = SITE + '/education/'
    ld = [
      {"@context": "https://schema.org", "@type": "Service", "@id": url + "#service", "name": "Education Services: Student Recruitment, Family Engagement and School Media",
       "serviceType": ["Student recruitment", "School enrollment marketing", "Family engagement", "School photography", "School videography", "Staff training"],
       "provider": {"@id": SITE + "/#organization"}, "audience": {"@type": "Audience", "audienceType": "Schools, colleges and education organizations"},
       "areaServed": [{"@type": "State", "name": "Tennessee"}, {"@type": "Country", "name": "United States"}], "url": url, "image": SITE + "/assets/education/e-hero.jpg", "description": E_DESC},
      {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in E_FAQ]},
      {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Education", "item": url}]},
      {"@context": "https://schema.org", "@type": "VideoObject", "name": "Leo Operations Education Highlight Reel", "description": "One-minute highlight reel of school and training programs filmed by Leo Operations: classrooms, career training, homecoming and student voices.",
       "thumbnailUrl": SITE + "/assets/education/e-reel.jpg", "contentUrl": SITE + "/assets/education/e-reel-hd.mp4", "uploadDate": "2026-10-20T12:00:00-05:00", "duration": "PT59S"},
    ]
    page('education/', E_TITLE, E_DESC, body, og='assets/education/e-hero.jpg', extra_ld=ld)
