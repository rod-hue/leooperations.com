# ---------- STATE PAGES + WHERE WE WORK HUB ----------
# exec'd by build.py after _landing.py. Each state page is a LANDING entry (same template), with its own
# sourced election calendar, field rules and Leo's verified work there. Facts researched Nov 1 2026; no prices.
STATE_INFO = {}   # slug -> dict(name, abbr, blurb, y2027, y2028, past) used by the hub

def state(slug, name, abbr, *, blurb, lead, calendar, rules, work, feats, faq, related, y2027, y2028, past, vid='v2-strategy', h=None, title=None, desc=None):
    STATE_INFO[slug] = dict(name=name, abbr=abbr, blurb=blurb, y2027=y2027, y2028=y2028, past=past)
    LANDING_NAMES[slug] = name
    LANDING[slug] = dict(
        vid=vid, eyebrow=f'{name} political consultant',
        h=h or f'{name} campaigns.|<span class=grad>Field, film and digital.</span>',
        title=title or f'{name} Political Consultant | Canvassing, Campaign Video & Digital | Leo Operations',
        desc=desc, lead=lead,
        prose=[(f'{name} elections in 2027 and 2028', calendar), (f'What field programs in {name} need to know', rules), (f'Our work in {name} and the region', work)],
        feats=feats, faq=faq, related=related,
        area=[{"@type": "State", "name": name}, {"@type": "Country", "name": "United States"}])

FEATS = [('Field and canvassing', 'Door-to-door persuasion, voter registration, GOTV and paid canvass teams, with daily reporting.'),
         ('Petition drives', 'Signature gathering for ballot measures, with validation and compliance built in.'),
         ('Campaign video', 'Launch videos, ads, endorsements and constituent outreach films, shot by our own crew.'),
         ('Campaign photography', 'Portraits, events and rallies, delivered fast for press and social.'),
         ('Digital and social', 'Websites, social media management and targeted digital ads.'),
         ('Strategy', 'Campaign plans, budgets and staffing from launch to election night.')]

ORDER = ['florida','georgia','north-carolina','texas','virginia','michigan','nevada','arizona','pennsylvania','illinois','mississippi','louisiana','kentucky']
def _ordered():
    return sorted(STATE_INFO.items(), key=lambda kv: ORDER.index(kv[0].replace('-political-consultant','')))

def states_hub():
    cards = ''.join(f'<a class="stcard" href="{{pre}}{k}/" data-r="{i%3}"><span class="mono">{E(v["abbr"])}</span><b>{E(v["name"])}</b><em>{E(v["blurb"])}</em></a>' for i, (k, v) in enumerate(_ordered()))
    rows = ''.join(f'<tr><td><a href="{{pre}}{k}/">{E(v["name"])}</a></td><td>{E(v["y2027"])}</td><td>{E(v["y2028"])}</td></tr>' for k, v in _ordered())
    past = ''.join(f'<li><b>{E(v["name"])}:</b> {E(v["past"])}</li>' for v in [v for _, v in _ordered()] if v['past'])
    css = '<style>.stgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px}.stcard{display:block;padding:22px;border:1px solid rgba(255,255,255,.12);border-radius:16px;text-decoration:none;color:inherit;transition:border-color .2s}.stcard:hover{border-color:var(--cyan)}.stcard .mono{color:var(--cyan);font-size:11px;letter-spacing:.14em}.stcard b{display:block;font-size:24px;margin:8px 0 6px}.stcard em{font-style:normal;color:var(--dim);font-size:15px;line-height:1.5}.sttab{width:100%;border-collapse:collapse;font-size:15px}.sttab th,.sttab td{text-align:left;padding:12px 10px;border-bottom:1px solid rgba(255,255,255,.1);vertical-align:top}.sttab th{font-family:var(--mono,monospace);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--dim)}.sttab a{color:var(--cyan)}@media(max-width:700px){.sttab{font-size:13.5px}.sttab th,.sttab td{padding:10px 6px}}</style>'
    def body(pre):
        return f'''{css}<section class="hero page-hero"><div class="hero-media">{vid("v2-strategy",pre,eager=True)}</div><div class="hero-inner"><span class="eyebrow mono">Where we work</span><h1 class="h-xl">{split("Nashville roots.|<span class=grad>National reach.</span>")}</h1><p class="lead">{E(HUB_LEAD)}</p></div></section>
<section class="sec wrap"><span class="eyebrow mono">States</span><h2 class="h-lg" style="margin:14px 0 30px">{split("Campaign help|<span class=grad>state by state.</span>")}</h2><div class="stgrid">{cards.replace("{pre}", pre)}<a class="stcard" href="{pre}south-carolina/"><span class="mono">SC</span><b>South Carolina</b><em>First in the 2028 Democratic primary. Officials we film and photograph, plus a 2026 U.S. Senate campaign.</em></a><a class="stcard" href="{pre}nashville-political-consulting/"><span class="mono">TN</span><b>Tennessee</b><em>Home base. Mayors, legislators, judges and the 2020 Bloomberg field program.</em></a></div></section>
<section class="sec wrap"><div class="two-col"><div class="prose"><h2>On-cycle and off-cycle</h2>{"".join(f"<p>{E(p)}</p>" for p in HUB_CYCLE)}<table class="sttab"><thead><tr><th>State</th><th>2027</th><th>2028</th></tr></thead><tbody>{rows.replace("{pre}", pre)}</tbody></table><h2>Where we have run programs</h2><ul>{past}</ul></div><aside class="sticky-card"><h3>Building a team?</h3><p>Tell us the state, the race and the timeline. We reply within one business day.</p>{mail("rod","leooperations.com","Email Leo Operations <span class=\"arr\">&rarr;</span>","btn primary","Inquiry%20from%20leooperations.com")}</aside></div></section>
{bigcta(pre)}'''
    page('where-we-work/', 'Where We Work | Political Field, Video and Digital Across the U.S. | Leo Operations', HUB_DESC, body,
         extra_ld=[{"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": SITE + '/' + k + '/', "name": v['name']} for i, (k, v) in enumerate(_ordered())]}])

HUB_LEAD = 'Leo Operations is a Black-owned campaign, media and marketing firm based in Nashville. Our team has run field and petition programs in a dozen states and films and photographs candidates wherever the race is.'
HUB_DESC = 'Where Leo Operations works: political field, petition drives, campaign video and digital in Florida, Georgia, North Carolina, Texas, Virginia, Michigan, Nevada, Arizona, Illinois, Pennsylvania, Mississippi, Louisiana, Kentucky, South Carolina and Tennessee.'
HUB_CYCLE = ['Campaign work never really stops. Off-cycle years like 2027 bring governor\'s races in Kentucky, Louisiana and Mississippi, the entire Virginia and New Jersey legislatures, and mayor\'s races in Chicago, Philadelphia, Jacksonville, Nashville and other big cities. On-cycle years like 2028 bring the presidential primaries, 34 U.S. Senate races and all 435 House seats.',
             'The teams that win start hiring early. Here is what is on the ballot in the states we work in.']

# ---------- NATIONAL SERVICE PAGES ----------
# Facts from Rodriquez Wright II's resume (data/team_rodriquez-wright-ii.json) and the existing site.
LANDING.update({
 'political-field-consulting-firm': dict(
  vid='v2-field', eyebrow='Political field consulting firm',
  h='Field programs|that move <span class=grad>real votes.</span>',
  title='Political Field Consulting Firm | Canvassing, GOTV & Voter Registration Nationwide | Leo Operations',
  desc='Leo Operations is a Black-owned political field consulting firm: canvassing, voter registration, petition drives and GOTV, with programs run in Tennessee, Nevada, Illinois, Florida, Arizona, Virginia and more.',
  lead='Field is where campaigns are won or lost. Our founder has built and run field programs since 2012, from a presidential campaign\'s Tennessee operation to coordinated canvasses in Las Vegas and Chicago.',
  prose=[
   ('Programs our team has run', 'Tennessee State Organizing Director for Michael Bloomberg\'s 2020 presidential campaign, a program that made 228,000 voter calls. Tennessee State Project Director for BlackPAC in 2018. Project director for 2016 coordinated canvass programs in Las Vegas and Chicago, regional GOTV for the 2016 New Hampshire primary, and field director for Kansas City\'s 2017 bond and streetcar campaigns. Since 2019, Leo Operations has run field consulting for clients including SEIU Virginia in 2023.'),
   ('How we build a field program', 'We start from the vote goal and work backward: universe, contact targets, staffing and a week-by-week calendar. Turf is cut from VAN and MiniVAN data, canvassers are trained on the script and the tools, and every shift ends with numbers and quality checks. You see the same dashboard we do.'),
   ('On-cycle and off-cycle', 'Off-cycle years are when municipal races, special elections, ballot measures and organizing programs need experienced vendors who are not already booked. On-cycle years bring presidential, Senate and House coordinated campaigns that need to scale fast. We staff both, and we plan early so your program launches on time.'),
  ],
  feats=[('Canvassing','Persuasion, ID and turnout doors at scale.'),('Voter registration','Campuses, churches, neighborhoods and events, run to state rules.'),('Petition drives','Signature gathering with validation and compliance.'),('GOTV','Chase universes, early-vote pushes and Election Day operations.'),('Phone and text','Voter contact programs that back up the doors.'),('Staffing','Field directors, organizers and canvass leads, recruited and trained.')],
  faq=[('Do you work outside Tennessee?','Yes. Our team has run field and petition programs in Tennessee, South Carolina, Nevada, Illinois, Florida, Arizona, Montana, Massachusetts, Missouri, New Hampshire, California and Virginia.'),
       ('Who hires a political field consulting firm?','Candidates, party committees, independent expenditure campaigns, unions, ballot measure committees and civic organizations running voter registration or turnout programs.'),
       ('Can you scale up quickly?','Yes. Tell us the vote goal, universe and timeline, and we will scope staffing and a launch date within a few days.'),
       ('Do you follow state voter registration and petition laws?','Yes. Rules differ a lot by state, from registration-drive registration requirements to petition circulator rules, and we build compliance into training and quality control.')],
  related=['canvassing-company/','signature-gathering-company/','where-we-work/','black-political-consultant/'],
  area=[{"@type":"Country","name":"United States"}]),
 'signature-gathering-company': dict(
  vid='v2-field', eyebrow='Petition and signature gathering',
  h='Petition drives.|<span class=grad>Signatures that count.</span>',
  title='Signature Gathering Company | Ballot Measure Petition Drives | Leo Operations',
  desc='Leo Operations runs petition drives and signature gathering for ballot measures and candidate petitions, led by a director of statewide drives in Florida, Arizona, Montana, Massachusetts and Chicago.',
  lead='A ballot measure lives or dies on valid signatures. Our founder has directed petition drives for statewide and countywide ballot measures across the country.',
  prose=[
   ('Drives our team has run', 'Project director for the 2018 All for Transportation petition drive in Hillsborough County, Florida; the 2018 Invest in Ed petition drive in Arizona; the Montanans for Research and Cures (I-181) drive; and the Massachusetts fair hospital pricing petition. Field director for The Black Institute\'s 2019 #KeepStarz petition drive in Chicago.'),
   ('Valid signatures, not just signatures', 'Raw counts mean nothing if signatures fail review. We train circulators on the state\'s rules, check every sheet for completeness, run internal validation against the voter file and track the validity rate by circulator and location, so problems are caught in days, not at the filing deadline.'),
   ('Know the rules before you start', 'Petition law varies widely: who may circulate, how circulators are paid, deadlines, signature distribution requirements and how signatures are verified. Several states changed their rules recently. We build the plan around the current law in your state.'),
  ],
  feats=[('Drive planning','Signature goal, validity cushion, timeline and budget.'),('Circulator teams','Recruiting, training and daily management.'),('Validation','Internal checks against the voter file.'),('Compliance','State circulator and filing rules built in.'),('Reporting','Daily counts by team, site and validity rate.'),('Campaign media','Photo, video and digital for the campaign behind the measure.')],
  faq=[('How many extra signatures should a petition drive collect?','Most drives plan a cushion above the legal minimum because some signatures are always rejected. The right cushion depends on the state\'s review process and your validity rate, which we track daily.'),
       ('Can you run a drive outside Tennessee?','Yes. Our team has run drives in Florida, Arizona, Montana, Massachusetts and Illinois.'),
       ('Do you handle candidate petitions too?','Yes. Many states and cities require nominating petitions, and the same validation discipline applies.'),
       ('What does a petition drive cost?','It depends on the signature goal, deadline and state rules. Our ballot measure signature gathering guide explains the cost drivers, and we will scope your drive for free.')],
  related=['political-field-consulting-firm/','canvassing-company/','where-we-work/','field-strategies/'],
  area=[{"@type":"Country","name":"United States"}]),
 'campaign-videographer': dict(
  vid='v2-media', eyebrow='Campaign videographer',
  h='Campaign video.|<span class=grad>Shot by people who run campaigns.</span>',
  title='Campaign Videographer | Political Video Crew for Ads & Endorsements | Leo Operations',
  desc='Hire a campaign videographer who understands politics: launch videos, ads, endorsements and constituent outreach films for candidates and elected officials, from Leo Operations.',
  lead='Our crew films for candidates and elected officials from Tennessee to South Carolina. We know the rules, the deadlines and the message, because we run campaigns too.',
  prose=[
   ('What we film', 'Launch videos, biography films, TV and streaming ads, endorsement videos, constituent outreach and holiday messages for elected officials, event coverage and vertical clips for social media. Recent work includes endorsement and outreach films for South Carolina legislators, an endorsement from Rep. Jasmine Crockett and campaign ads for Nashville council candidates.'),
   ('Why a political crew matters', 'Campaign video runs on deadlines that do not move, and it has to be right the first time: the disclaimer, the message discipline, the B-roll that shows the candidate with real voters. Our founder has managed campaigns since 2015, so the crew knows what a campaign needs before you ask.'),
   ('Built for every screen', 'We deliver the 30-second spot, the 15-second cut, the vertical reel and the captioned social version from the same shoot, so one day of filming feeds your TV, streaming and social plans.'),
  ],
  feats=[('Launch videos','The story of why you are running.'),('Ads','TV, streaming and digital spots in every length.'),('Endorsements','Leaders and voters on camera.'),('Constituent outreach','Updates and messages for elected officials.'),('Event coverage','Rallies, town halls and election nights.'),('Social cuts','Vertical, captioned and ready to post.')],
  faq=[('Do you travel for campaign shoots?','Yes. We are based in Nashville and travel for campaigns, including recent work in South Carolina.'),
       ('Can you deliver ads for TV and streaming?','Yes. We deliver broadcast-ready files and the shorter cuts streaming and social platforms need.'),
       ('Do you also do campaign photography?','Yes. We shoot portraits and events on the same day as video when the schedule allows.'),
       ('How much does campaign video cost?','It depends on the number of shoot days, locations and deliverables. Our campaign video production cost guide breaks it down.')],
  related=['political-video-production/','political-photographer/','south-carolina/','where-we-work/'],
  area=[{"@type":"Country","name":"United States"}]),
 'political-photographer': dict(
  vid='v2-media', eyebrow='Political photographer',
  h='Political photography.|<span class=grad>Portraits that win trust.</span>',
  title='Political Photographer | Campaign Portraits & Event Photography | Leo Operations',
  desc='Political photographer for campaign portraits, headshots, rallies, swearing-ins and legislative events. Leo Operations photographs candidates, elected officials and organizations nationwide.',
  lead='We photograph candidates, elected officials and the organizations around them: campaign portraits, swearing-ins, rallies, galas and legislative days, delivered fast for press and social.',
  prose=[
   ('Who we have photographed', 'Nashville Mayor Freddie O\'Connell, Tennessee legislators including Sens. Raumesh Akbari, London Lamar and Charlane Oliver and Reps. Justin Jones and Gloria Johnson, South Carolina legislators, a U.S. Senate candidate in South Carolina, and organizations including the National Black Caucus of State Legislators. Our founder has also photographed Sen. Raphael Warnock, Sen. Cory Booker and Rev. Al Sharpton.'),
   ('Campaign portraits that work', 'A campaign portrait has to read at thumbnail size on a phone, hold up on a mailer and look like the candidate on their best day. We shoot a range of looks in one session (formal, outdoor, with voters) so your website, mail, ads and press kit all match.'),
   ('Fast turnaround', 'Event and rally photos are delivered quickly so your team can post while the moment is still news. Portrait sessions come back retouched and sized for print, web and social.'),
  ],
  feats=[('Campaign portraits','Formal, outdoor and lifestyle looks in one session.'),('Headshots','Official photos for elected officials and staff.'),('Rallies and events','Launches, town halls and election nights.'),('Swearing-ins','Ceremonies and first days in office.'),('Legislative days','Advocacy days at the capitol.'),('Galas and conferences','Organizations and caucuses.')],
  faq=[('Do you travel for political photography?','Yes. We are based in Nashville and travel for campaigns and organizations.'),
       ('How fast are event photos delivered?','We can deliver a first selection the same day or next morning for social media, with the full gallery to follow.'),
       ('Can you shoot video at the same event?','Yes. We can staff photo and video together so you get both from one booking.'),
       ('Do you photograph elected officials\' official portraits?','Yes. We shoot official portraits and headshots for elected officials and their staff.')],
  related=['headshot-photographer/','campaign-videographer/','nashville-photographer/','where-we-work/'],
  area=[{"@type":"Country","name":"United States"}]),
})
LANDING_NAMES.update({'political-field-consulting-firm':'Political Field Consulting','signature-gathering-company':'Signature Gathering','campaign-videographer':'Campaign Videographer','political-photographer':'Political Photographer','where-we-work/':'Where We Work','where-we-work':'Where We Work'})

# ---------- STATES (B + C research, Nov 1 2026) ----------
REL = ['political-field-consulting-firm/', 'campaign-videographer/', 'signature-gathering-company/', 'where-we-work/']

state('virginia-political-consultant', 'Virginia', 'VA',
  blurb='Every General Assembly seat is up in 2027, and Virginia votes Feb 29 in the 2028 Democratic calendar.',
  desc='Political consultant for Virginia campaigns: canvassing, voter contact, campaign video and digital for the 2027 General Assembly and the 2028 presidential primary. SEIU Virginia field consultant.',
  lead='Virginia votes every year. In 2027 all 140 General Assembly seats are on the ballot, and in 2028 Virginia moves into the Democratic early window. Leo Operations has already run field consulting in Virginia for SEIU Virginia.',
  calendar='All 40 state Senate seats and all 100 House of Delegates seats are on the ballot on November 2, 2027, according to Ballotpedia. That makes 2027 one of the biggest off-cycle field years in the country. In 2028 Virginia is the sixth state in the Democratic early window, set for February 29 under the calendar the DNC approved in August 2026. State law still sets the first Tuesday in March, and Virginia leaders have said they will move the date in the 2027 legislative session.',
  rules='Virginia has no citizen-initiated ballot measures, so field programs here are about candidates and voter contact: persuasion canvassing, registration and turnout. With elections every year, voter files and volunteer lists stay warm, and the best programs start recruiting early before the vendor market books up. Northern Virginia sits in the Washington, D.C. media market, one of the most expensive in the country, which makes doors, digital and streaming video especially valuable there.',
  work='Leo Operations was a field consultant for SEIU Virginia in 2023. SEIU reported spending more than $1.4 million on its 2023 Virginia program, the year Democrats won control of the House of Delegates and kept their Senate majority. Our founder also publishes Washington DC Magazine and covers politics across the D.C. region.',
  feats=FEATS,
  faq=[('Is the Virginia General Assembly up in 2027?','Yes. All 40 Senate seats and all 100 House of Delegates seats are on the November 2, 2027 ballot.'),
       ('When is Virginia\'s 2028 presidential primary?','The DNC calendar places Virginia on February 29, 2028. State law currently sets the first Tuesday in March, so the date depends on a 2027 bill.'),
       ('Have you worked in Virginia before?','Yes. We were a field consultant for SEIU Virginia during its 2023 program.')],
  related=REL, y2027='All 140 General Assembly seats (Nov 2)', y2028='Democratic primary Feb 29 (pending state law)',
  past='Field consulting for SEIU Virginia, 2023.')

state('michigan-political-consultant', 'Michigan', 'MI',
  blurb='Fifth in the 2028 Democratic calendar, a top ad-spending state and an active ballot-measure state.',
  desc='Political consultant for Michigan campaigns and ballot measures: canvassing, petition drives, campaign video and digital for the 2028 cycle, when Michigan votes Feb 22 in the Democratic calendar.',
  lead='Michigan is a presidential battleground, an early 2028 Democratic state and one of the most active ballot-measure states in the country. Leo Operations brings field, petition and media experience to Michigan campaigns.',
  calendar='Michigan holds its presidential primary on the fourth Tuesday in February under state law, which falls on February 22, 2028, the same date the DNC assigned it in the early window. Michigan was also projected by AdImpact to be one of the top states for political ad spending in the 2026 cycle. Detroit, the state\'s largest media market, elected its mayor in 2025.',
  rules='Michigan voters can put both constitutional amendments and new laws on the ballot by petition. For the 2026 cycle, a constitutional amendment needed 446,198 valid signatures and a statutory initiative 356,958, based on the last governor\'s race, according to Ballotpedia. Those numbers will reset after 2026. The state Senate passed a ban on paying circulators by the signature in November 2025, so check its status before you budget a drive.',
  work='Our founder has directed statewide petition drives in Arizona, Montana and Massachusetts, a countywide drive in Florida and a citywide drive in Chicago, and he ran 2016 coordinated canvass programs in Las Vegas and Chicago. Leo Operations brings that petition and field experience, plus our own film and photo crew, to Michigan campaigns.',
  feats=FEATS,
  faq=[('When is Michigan\'s 2028 presidential primary?','February 22, 2028, the fourth Tuesday in February under state law and the date in the DNC early window.'),
       ('How many signatures does a Michigan ballot initiative need?','For the 2026 cycle, 446,198 for a constitutional amendment and 356,958 for a statutory initiative. The thresholds reset after each governor\'s race.'),
       ('Can you run a petition drive in Michigan?','Yes. We plan, staff and validate petition drives, and we build each plan around the current state rules.')],
  related=REL, y2027='Local and special elections', y2028='Presidential primary Feb 22; ballot measures',
  past='')

state('nevada-political-consultant', 'Nevada', 'NV',
  blurb='Second in the 2028 Democratic calendar on Feb 1, with a U.S. Senate race and the Las Vegas market.',
  desc='Political consultant for Nevada campaigns: canvassing, voter registration, campaign video and digital for the 2028 cycle, when Nevada votes second on Feb 1. Our founder ran 2016 canvass programs in Las Vegas.',
  lead='Nevada votes second in the 2028 Democratic calendar and has a U.S. Senate seat on the 2028 ballot. Our founder ran coordinated canvass programs in Las Vegas in 2016.',
  calendar='Nevada law sets the presidential primary on the first Tuesday in February for all major parties, which is February 1, 2028, the same date the DNC assigned it as the second early state. Nevada\'s Class 3 U.S. Senate seat is also on the November 7, 2028 ballot. That combination means campaigns will be building Nevada teams through 2027.',
  rules='Voter registration drives in Nevada do not require training, but completed applications must be turned in within 10 days, and paying people per registration is illegal, according to the Fair Elections Center. For ballot measures, Nevada requires signatures from each of its four petition districts, equal to 10% of that district\'s vote in the last general election. Las Vegas is the state\'s largest media market.',
  work='Our founder was project director for 2016 coordinated canvass programs in Las Vegas, run through Revolution Field Strategies. Leo Operations now pairs that field experience with our own campaign video and photo crew.',
  feats=FEATS,
  faq=[('When is Nevada\'s 2028 presidential primary?','February 1, 2028, the first Tuesday in February under state law and second in the DNC calendar.'),
       ('Is there a U.S. Senate race in Nevada in 2028?','Yes. Nevada\'s Class 3 Senate seat is on the November 7, 2028 ballot.'),
       ('Have you worked in Nevada?','Yes. Our founder ran 2016 coordinated canvass programs in Las Vegas.')],
  related=REL, y2027='Campaign build-out for the early primary', y2028='Primary Feb 1; U.S. Senate',
  past='Coordinated canvass programs in Las Vegas, 2016.')

state('arizona-political-consultant', 'Arizona', 'AZ',
  blurb='U.S. Senate race in 2028, Tucson elections in 2027 and one of the busiest ballot-measure states.',
  desc='Political consultant for Arizona campaigns and ballot measures: petition drives, canvassing, campaign video and digital. Our founder directed the 2018 Invest in Ed petition drive.',
  lead='Arizona is a presidential battleground with a U.S. Senate race in 2028 and a long tradition of citizen ballot measures. Our founder directed Arizona\'s 2018 Invest in Ed petition drive.',
  calendar='Tucson elects its mayor and council in 2027. In 2028, Arizona\'s Class 3 U.S. Senate seat is on the November ballot, and the presidential preference election defaults to the Tuesday after March 15 under state law, which would be March 21, 2028, unless the date is changed. Phoenix is the state\'s largest media market and one of the largest in the country.',
  rules='Arizona voters can make laws and amend the constitution by petition. The current thresholds on the Secretary of State\'s site are 255,949 valid signatures for a statutory initiative and 383,923 for a constitutional amendment, and they reset after each governor\'s race. Arizona bans paying circulators by the signature, a rule the Arizona Supreme Court upheld in 2023, and paid and out-of-state circulators must register with the Secretary of State. Voter registration drives do not require notification or training.',
  work='Our founder was project director for the 2018 Invest in Ed petition drive in Arizona, a statewide education-funding initiative. Leo Operations brings that petition experience, plus field, video and photo, to Arizona campaigns.',
  feats=FEATS,
  faq=[('Can you run a petition drive in Arizona?','Yes. Our founder directed Arizona\'s 2018 Invest in Ed petition drive, and we build every drive around Arizona\'s circulator registration and pay rules.'),
       ('How many signatures does an Arizona initiative need?','Currently 255,949 for a statutory initiative and 383,923 for a constitutional amendment, per the Secretary of State. The thresholds reset after each governor\'s race.'),
       ('Is there a U.S. Senate race in Arizona in 2028?','Yes. Arizona\'s Class 3 Senate seat is on the November 7, 2028 ballot.')],
  related=REL, y2027='Tucson mayor and council', y2028='U.S. Senate; ballot measures',
  past='Invest in Ed petition drive, 2018.')

state('illinois-political-consultant', 'Illinois', 'IL',
  blurb='Chicago elects a mayor on Feb 23, 2027, and Illinois has a U.S. Senate race in 2028.',
  desc='Political consultant for Illinois and Chicago campaigns: canvassing, petition drives, campaign video and digital for the 2027 Chicago municipal election and 2028. Our founder ran field programs in Chicago.',
  lead='Chicago\'s 2027 municipal election is one of the biggest off-cycle races in the country. Our founder has run field and petition programs in Chicago, and Leo Operations has worked in southern Illinois.',
  calendar='Chicago\'s mayoral election is February 23, 2027, with a runoff on April 6, 2027 if no candidate wins a majority. In 2028, Illinois holds its presidential primary on March 21, according to Axios, and Sen. Tammy Duckworth\'s Class 3 seat is on the November ballot.',
  rules='Chicago municipal campaigns run on a short winter calendar, so nominating petitions, field hiring and voter contact all have to be planned in the fall before the election. Chicago is the third-largest media market in the country, which makes targeted field, mail and digital the most efficient way for many campaigns to reach voters.',
  work='Our founder was project director for a 2016 coordinated canvass program in Chicago and field director for The Black Institute\'s 2019 #KeepStarz petition drive in Chicago. Leo Operations has also worked with Marie Franklin\'s campaign for mayor of East St. Louis.',
  feats=FEATS,
  faq=[('When is the 2027 Chicago mayoral election?','February 23, 2027, with a runoff on April 6, 2027 if no candidate wins a majority.'),
       ('Have you worked in Chicago?','Yes. Our founder ran a 2016 coordinated canvass in Chicago and the 2019 #KeepStarz petition drive.'),
       ('Is there a U.S. Senate race in Illinois in 2028?','Yes. Illinois\'s Class 3 Senate seat is on the November 7, 2028 ballot.')],
  related=REL, y2027='Chicago mayor (Feb 23, runoff Apr 6)', y2028='Primary Mar 21; U.S. Senate',
  past='Chicago canvass (2016) and #KeepStarz petition drive (2019); East St. Louis mayoral campaign.')

state('pennsylvania-political-consultant', 'Pennsylvania', 'PA',
  blurb='Philadelphia elects a mayor and full council in 2027, and Pennsylvania has a U.S. Senate race in 2028.',
  desc='Political consultant for Pennsylvania and Philadelphia campaigns: canvassing, campaign video and digital for the 2027 Philadelphia municipal election and the 2028 cycle.',
  lead='Pennsylvania is the largest presidential battleground, and Philadelphia votes for mayor and every City Council seat in 2027. Leo Operations brings field, film and digital to Pennsylvania campaigns.',
  calendar='Philadelphia\'s mayor and all City Council seats are on the November 2, 2027 ballot, after a spring primary. In 2028 Pennsylvania has a U.S. Senate race (the Class 3 seat now held by Sen. John Fetterman) and, under current law, a late-April presidential primary.',
  rules='Pennsylvania has no statewide citizen initiative process, so field programs focus on candidates, voter registration and turnout. In Philadelphia, the primary is usually decisive, which means early voter contact and strong ward-level relationships matter. Philadelphia is one of the largest and most expensive media markets in the country, so doors, mail and digital carry a lot of the persuasion load.',
  work='Our founder has run field programs for a presidential campaign, a national Black-led PAC and coordinated canvasses in Las Vegas and Chicago. Leo Operations pairs that experience with its own campaign video and photo crew for Pennsylvania campaigns.',
  feats=FEATS,
  faq=[('When is Philadelphia\'s next mayoral election?','November 2, 2027, after a spring primary. All City Council seats are on the same ballot.'),
       ('Is there a U.S. Senate race in Pennsylvania in 2028?','Yes. The Class 3 seat is on the November 7, 2028 ballot.'),
       ('Do you travel to Pennsylvania for campaign video?','Yes. Our crew travels for campaign shoots and events.')],
  related=REL, y2027='Philadelphia mayor and council (Nov 2)', y2028='Late-April primary; U.S. Senate',
  past='')

state('mississippi-political-consultant', 'Mississippi', 'MS',
  blurb='An open governor\'s race and statewide offices on the Nov 2, 2027 ballot.',
  desc='Political consultant for Mississippi campaigns: field, voter registration, campaign video and digital for the 2027 governor and statewide races. Black-owned firm from Nashville.',
  lead='Mississippi elects a new governor in 2027. Gov. Tate Reeves is term-limited, and several statewide offices will change hands. Leo Operations is a Black-owned firm based next door in Tennessee.',
  calendar='Mississippi\'s general election is November 2, 2027. The governor\'s seat is open because Gov. Tate Reeves is term-limited, and a WLOX report noted that five of the eight statewide offices will change hands. Party primaries come in August 2027. Mississippi does not have a U.S. Senate race in 2028.',
  rules='Mississippi has had no working citizen initiative process since a 2021 state Supreme Court ruling, and bills to restore it died in 2026. That puts the focus on candidates, voter registration and turnout. About a third of Mississippians are Black, among the highest shares of any state, and church, HBCU and community networks are central to field programs here.',
  work='Leo Operations has photographed and filmed for Planned Parenthood of Tennessee and North Mississippi, and for Memphis clients including the Memphis Grizzlies and Sen. Raumesh Akbari. Our team runs field, video and digital across the Mid-South from Nashville.',
  feats=FEATS,
  faq=[('When is the 2027 Mississippi governor\'s race?','The general election is November 2, 2027, with party primaries in August. The seat is open because Gov. Tate Reeves is term-limited.'),
       ('Does Mississippi have ballot initiatives?','Not currently. The process has been inactive since a 2021 state Supreme Court ruling.'),
       ('Do you work in Mississippi?','Yes. We are based in Nashville and work across the Mid-South, including photo and video for Planned Parenthood of Tennessee and North Mississippi.')],
  related=REL, y2027='Open governor + statewide (Nov 2)', y2028='Presidential and House races',
  past='Photo and video for Planned Parenthood of Tennessee and North Mississippi.')

state('louisiana-political-consultant', 'Louisiana', 'LA',
  blurb='Governor, statewide offices and the full legislature are on the 2027 ballot, plus a U.S. Senate race in 2028.',
  desc='Political consultant for Louisiana campaigns: field, campaign video and digital for the 2027 governor, statewide and legislative elections and the 2028 U.S. Senate race.',
  lead='Louisiana elects its governor, every statewide official and the entire legislature in 2027. Leo Operations brings field, film and digital to Louisiana campaigns from Nashville.',
  calendar='In 2027 Louisiana elects its governor, lieutenant governor, secretary of state, attorney general, treasurer, insurance and agriculture commissioners and the full legislature. The governor\'s race still uses Louisiana\'s open primary, where all candidates run on one ballot; the new closed party primaries that began in 2026 apply to Congress and some other offices. In 2028, Sen. John Kennedy\'s Class 3 seat is on the ballot.',
  rules='Two different primary systems now run side by side in Louisiana, so a campaign plan has to follow the right calendar for each office. About a third of Louisianans are Black, and the New Orleans and Baton Rouge areas are the largest population centers for statewide field programs. Louisiana\'s congressional map has also been in court after the Supreme Court\'s 2026 Louisiana v. Callais decision, which can change district lines.',
  work='Our founder has built field programs for a presidential campaign and a national Black-led PAC and run petition drives in five states. Leo Operations pairs that experience with its own film and photo crew for Louisiana campaigns.',
  feats=FEATS,
  faq=[('What is on the 2027 Louisiana ballot?','Governor, all statewide offices and the entire legislature.'),
       ('Does the governor\'s race use the new closed primaries?','No. The governor\'s race still uses the open primary. The closed party primaries apply to Congress and some other offices starting in 2026.'),
       ('Is there a U.S. Senate race in Louisiana in 2028?','Yes. The Class 3 seat held by Sen. John Kennedy is on the 2028 ballot.')],
  related=REL, y2027='Governor, statewide, full legislature', y2028='U.S. Senate',
  past='')

state('kentucky-political-consultant', 'Kentucky', 'KY',
  blurb='An open governor\'s race in 2027 (primary May 18) and a U.S. Senate race in 2028.',
  desc='Political consultant for Kentucky campaigns: field, campaign video and digital for the 2027 open governor\'s race and the 2028 U.S. Senate race. Based next door in Nashville.',
  lead='Kentucky picks a new governor in 2027. Gov. Andy Beshear is term-limited, and the attorney general, secretary of state and other statewide offices are on the same ballot. Leo Operations is based a short drive away in Nashville.',
  calendar='Kentucky\'s 2027 primary is May 18 and the general election is November 2, 2027. The governor\'s seat is open, and the attorney general, auditor, secretary of state, treasurer and agriculture commissioner are also on the ballot. In 2028, Sen. Rand Paul\'s Class 3 seat is up.',
  rules='Kentucky does not have citizen-initiated ballot measures, so field programs focus on candidates, registration and turnout. The May primary means statewide campaigns need staff, video and voter contact in place by early 2027. Louisville, Lexington, Cincinnati and Nashville media markets all reach parts of the state.',
  work='Leo Operations is based in Nashville, a short drive from southern Kentucky. Our founder has run field programs across Tennessee, including a presidential campaign\'s statewide operation in 2020.',
  feats=FEATS,
  faq=[('When is the 2027 Kentucky primary?','May 18, 2027. The general election is November 2, 2027.'),
       ('Is the Kentucky governor\'s seat open in 2027?','Yes. Gov. Andy Beshear is term-limited.'),
       ('Is there a U.S. Senate race in Kentucky in 2028?','Yes. The Class 3 seat held by Sen. Rand Paul is on the 2028 ballot.')],
  related=REL, y2027='Open governor (primary May 18, general Nov 2)', y2028='U.S. Senate',
  past='')

# ---------- STATES (A research, Nov 1 2026) ----------
state('florida-political-consultant', 'Florida', 'FL',
  blurb='Tampa and Jacksonville elect mayors in spring 2027, plus a 2028 U.S. Senate race and strict new field laws.',
  desc='Political consultant for Florida campaigns and ballot measures: petition drives, voter registration, canvassing, campaign video and digital. Our founder directed the 2018 All for Transportation petition drive in Hillsborough County.',
  lead='Florida has big-city mayoral races in 2027, a U.S. Senate race in 2028 and some of the strictest field laws in the country. Our founder directed the 2018 All for Transportation petition drive in Hillsborough County.',
  calendar='Tampa elects its mayor on March 2, 2027, with a runoff on April 27, and Jacksonville holds its first election on March 23, 2027, with a runoff on May 18. In 2028, Florida\'s presidential preference primary falls on March 21, the third Tuesday in March under state law, and Florida\'s Class 3 U.S. Senate seat is on the November ballot. Florida has five of the country\'s top 45 media markets: Tampa, Orlando, Miami, West Palm Beach and Jacksonville.',
  rules='Florida field programs run under tight rules. Third-party voter registration organizations must register with the state and deliver applications within 10 days, with fines of up to $5,000 per late application. A 2026 law requiring proof of citizenship to register takes effect January 1, 2027 and is being challenged in court. For ballot measures, the 2025 petition law (HB 1205) requires paid circulators to be registered, trained Florida residents and citizens, bans pay per signature and requires forms within 10 days. Constitutional amendments need 60% of the vote to pass. Compliance has to be built into every shift.',
  work='Our founder was project director for the 2018 All for Transportation petition drive in Hillsborough County, the Tampa-area transit initiative. Leo Operations brings that petition experience, plus field, film and photo, to Florida campaigns.',
  feats=FEATS,
  faq=[('Can you run a petition drive in Florida under the new law?','Yes. We build drives around HB 1205: registered and trained circulators, no pay per signature and 10-day form delivery. Our founder directed the 2018 All for Transportation drive in Hillsborough County.'),
       ('When are the 2027 Tampa and Jacksonville mayoral elections?','Tampa votes March 2, 2027 (runoff April 27). Jacksonville votes March 23, 2027 (runoff May 18).'),
       ('When is Florida\'s 2028 presidential primary?','March 21, 2028, the third Tuesday in March under Florida law.')],
  related=REL, y2027='Tampa (Mar 2) and Jacksonville (Mar 23) mayors', y2028='Primary Mar 21; U.S. Senate',
  past='All for Transportation petition drive, Hillsborough County, 2018.')

state('georgia-political-consultant', 'Georgia', 'GA',
  blurb='A 2028 U.S. Senate race, the Atlanta market and a third of voters who are Black.',
  desc='Political consultant for Georgia campaigns: canvassing, voter registration, campaign video and photography and digital for the 2028 U.S. Senate race and beyond. Black-owned firm from Nashville.',
  lead='Georgia is a presidential battleground with a U.S. Senate race in 2028, and about a third of Georgians are Black. Leo Operations is a Black-owned field, film and digital firm a few hours up I-24 in Nashville.',
  calendar='Sen. Raphael Warnock\'s Class 3 seat is on the November 7, 2028 ballot. Georgia\'s presidential primary date is set by the Secretary of State, so it is not fixed in law; Georgia applied for an early 2028 Democratic slot but was not selected. AdImpact projected about $700 million in Georgia political ad spending for the 2026 cycle, including about $196 million on the governor\'s race.',
  rules='Georgia voter registration drives must deliver completed applications within 10 days, or within 72 hours near the registration deadline, and paying anyone per registration is a crime, according to the Fair Elections Center. Georgia has no citizen-initiated ballot measures. Atlanta is the seventh-largest media market in the country, which makes it expensive to buy and makes doors, digital and streaming more important.',
  work='Our founder has photographed Sen. Raphael Warnock and has run field programs for a presidential campaign and a national Black-led PAC. Leo Operations films and photographs candidates and organizations across the South, including the Atlanta-rooted DJ AOne\'s 40th at Madison Square Garden.',
  feats=FEATS,
  faq=[('Is there a U.S. Senate race in Georgia in 2028?','Yes. The Class 3 seat held by Sen. Raphael Warnock is on the November 7, 2028 ballot.'),
       ('When is Georgia\'s 2028 presidential primary?','The Georgia Secretary of State sets the date. Georgia was not selected for the 2028 Democratic early window.'),
       ('What are the rules for voter registration drives in Georgia?','Completed applications must be delivered within 10 days, or 72 hours near the deadline, and paying per registration is a crime.')],
  related=REL, y2027='Campaign build-out for 2028', y2028='U.S. Senate; presidential primary (date set by SOS)',
  past='')

state('north-carolina-political-consultant', 'North Carolina', 'NC',
  blurb='Super Tuesday primary, a U.S. Senate race and a governor\'s race in 2028, plus an open Charlotte mayor\'s seat in 2027.',
  desc='Political consultant for North Carolina campaigns: canvassing, voter registration, campaign video and digital for the 2028 U.S. Senate and governor races and the 2027 Charlotte mayoral race.',
  lead='North Carolina votes on Super Tuesday in 2028 and has a U.S. Senate race and a governor\'s race on the same ballot. Leo Operations brings Black-owned field, film and digital to North Carolina campaigns.',
  calendar='North Carolina\'s primary falls on the Tuesday after the first Monday in March, which is March 7, 2028, Super Tuesday. Sen. Ted Budd\'s Class 3 seat and the governor\'s office are both on the November 2028 ballot. In 2027, Charlotte elects a new mayor: Mayor Vi Lyles resigned in 2026 and the interim mayor is not running. AdImpact projected about $510 million in North Carolina political ad spending for the 2026 cycle.',
  rules='North Carolina voter registration drives must get forms to the county within 5 business days and no later than 25 days before an election, may not keep or alter forms, and may not use quotas or pay per form, according to the State Board of Elections. North Carolina has no citizen-initiated ballot measures. Charlotte and Raleigh-Durham are the state\'s two largest media markets, both in the national top 25.',
  work='Our founder has built field programs for a presidential campaign\'s Tennessee operation and a national Black-led PAC, and has run canvass and petition programs in a dozen states. Leo Operations pairs that with its own film and photo crew for North Carolina campaigns.',
  feats=FEATS,
  faq=[('When is North Carolina\'s 2028 primary?','March 7, 2028, on Super Tuesday.'),
       ('What is on North Carolina\'s 2028 ballot?','President, U.S. Senate, governor and all congressional seats.'),
       ('Is the Charlotte mayor\'s seat open in 2027?','Yes. Mayor Vi Lyles resigned in 2026 and the interim mayor is not running.')],
  related=REL, y2027='Open Charlotte mayor', y2028='Super Tuesday Mar 7; U.S. Senate; governor',
  past='')

state('texas-political-consultant', 'Texas', 'TX',
  blurb='Houston and Dallas elect mayors in November 2027, and Texas votes on Super Tuesday in 2028.',
  desc='Political consultant for Texas campaigns: canvassing, voter registration, campaign video and digital for the 2027 Houston and Dallas mayoral races and the 2028 Super Tuesday primary.',
  lead='Texas has two of the five largest media markets in the country and big-city mayoral races in 2027. Leo Operations brings field, film and digital to Texas campaigns, and our crew has filmed an endorsement from Rep. Jasmine Crockett.',
  calendar='Houston elects its mayor on November 2, 2027, and Dallas, which moved its city elections to November of odd years, also elects its mayor in November 2027. Texas holds its presidential primary on March 7, 2028, Super Tuesday. AdImpact projected about $850 million in Texas political ad spending for the 2026 cycle, the most of any state.',
  rules='Voter registration in Texas runs through volunteer deputy registrars, who must be citizens, Texas residents and at least 18, complete county training and turn applications in within 5 days, according to the Secretary of State. Registering voters without an active appointment is a misdemeanor. Texas has no citizen-initiated statewide ballot measures. Dallas-Fort Worth and Houston are the fourth- and sixth-largest media markets in the country.',
  work='Our crew filmed an endorsement video from Rep. Jasmine Crockett of Texas, and our founder has run field programs for a presidential campaign and a national Black-led PAC and petition drives in five states.',
  feats=FEATS,
  faq=[('When are the 2027 Houston and Dallas mayoral elections?','November 2027. Houston votes November 2, 2027, and Dallas moved its city elections to November of odd years.'),
       ('How does voter registration work in Texas?','Through volunteer deputy registrars appointed by each county. They must complete training and turn in applications within 5 days.'),
       ('When is the Texas 2028 presidential primary?','March 7, 2028, on Super Tuesday.')],
  related=REL, y2027='Houston and Dallas mayors (Nov)', y2028='Super Tuesday Mar 7',
  past='')
