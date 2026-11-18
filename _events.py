# ---------- HIDDEN EVENT-MEDIA LANDING PAGES (Nov 17 2026) ----------
# exec'd by build.py after _landing.py. Not linked from nav, footer or homepage (Rod's call):
# these pages live in sitemap.xml + llms.txt and cross-link to each other and to their guides.
# Research + keyword map: _src/events/KEYWORD_MAP.md. Venue facts: _src/events/mcc_facts.md.
PHONE, PHONE_TEL = '(773) 573-2135', '+17735732135'
MCC_PLACE = {"@type": "Place", "name": "Music City Center", "address": {"@type": "PostalAddress", "streetAddress": "201 Rep. John Lewis Way S", "addressLocality": "Nashville", "addressRegion": "TN", "postalCode": "37203", "addressCountry": "US"}}
NASH_AREA = [{"@type": "City", "name": "Nashville"}, {"@type": "City", "name": "Franklin"}, {"@type": "City", "name": "Brentwood"}, {"@type": "City", "name": "Murfreesboro"}, {"@type": "State", "name": "Tennessee"}]

MCC_FACTS = [
 ('Address', '201 Rep. John Lewis Way South, Nashville, TN 37203 (contractor deliveries: 700 Korean Veterans Blvd)', 'https://nashvillemcc.com/maps-and-parking'),
 ('Opened', 'May 20, 2013. LEED Gold, with a four-acre green roof', 'https://nashvillemcc.com/sustainability'),
 ('Size', '2.1 million sq ft total, 1.2 million sq ft of public space', 'https://nashvillemcc.com/assets/3049/mcc_planning_guide.pdf'),
 ('Exhibit halls', '353,143 sq ft in Halls A1, A2, B, C and D, up to 1,726 booths (10x10), 32 ft 6 in ceilings', 'https://nashvillemcc.com/assets/3049/mcc_planning_guide.pdf'),
 ('Karl F. Dean Grand Ballroom', '57,500 sq ft on Level 4, up to 7,453 theater style, stage 78 ft wide', 'https://nashvillemcc.com/assets/3049/mcc_planning_guide.pdf'),
 ('Davidson Ballroom', '18,000 sq ft on Level 1M', 'https://nashvillemcc.com/assets/3049/mcc_planning_guide.pdf'),
 ('Meeting rooms', '60 meeting rooms (90,000 sq ft) plus 3 board rooms, 145,000 sq ft of pre-function space', 'https://nashvillemcc.com/assets/3049/mcc_planning_guide.pdf'),
 ('Terraces', 'Level 1 terrace 19,000 sq ft; Level 3 terrace 7,000 sq ft', 'https://nashvillemcc.com/assets/3049/mcc_planning_guide.pdf'),
 ('Loading', '32 loading docks, 3 drive-in ramps, 3 freight elevators', 'https://nashvillemcc.com/assets/3049/mcc_planning_guide.pdf'),
 ('Parking', '1,800-space covered garage at 701 Demonbreun St', 'https://nashvillemcc.com/maps-and-parking'),
 ('Exclusive services', 'Electrical, internet and telecom, rigging (Convention Production Rigging), food and beverage, move-in security', 'https://nashvillemcc.com/assets/3049/mcc_planning_guide.pdf'),
 ('Audio-visual', 'Not exclusive; LMG is the in-house preferred provider', 'https://nashvillemcc.com/audio-visual'),
 ('Signage rule', 'Nothing taped or fastened to walls; anything attached to the building goes through MCC Rigging', 'https://nashvillemcc.com/assets/3049/mcc_planning_guide.pdf'),
]

EV_FILMS = [('twsra', 'big'), ('tsu', ''), ('aone', ''), ('soul', ''), ('privy', ''), ('mc3', 'wide'), ('jetcars', ''), ('sierra', ''), ('bane', ''), ('aclu', '')]
EV_DESIGN = [('d-homecoming-cover', 'Homecoming 2025 cover', 'Tennessee State University Alumni Relations'),
             ('c-5th-cover', 'Anniversary program cover', 'Cathedral of Praise'),
             ('d-jazz-brunch', 'Event key art', 'Vintagers Jazz Brunch, Tennessee State University'),
             ('d-reunion-mixer', 'Reunion Weekend poster series', 'Tennessee State University'),
             ('c-60th', 'Save the date', 'Cathedral of Praise 60th Church Anniversary'),
             ('d-dowdy-happyhour', 'Event series key art', 'Ronald J. Dowdy for Criminal Court Judge'),
             ('d-tsu-postcard', 'Admissions postcard', 'Tennessee State University'),
             ('c-5th-speakers', 'Anniversary program, speakers spread', 'Cathedral of Praise')]
EV_WED = [('k-2132', 'Kenyon and Alea during their portraits'), ('k-3316', 'Aisha and Mazen face to face in their portraits'), ('k-2825', 'Jolene shows off her ring with William'),
          ('k-4390', 'Couple kiss by the lake'), ('k-2163', 'Kenyon and Alea walking arm in arm by the lake'), ('k-674', 'Tekisha and Newman under the floral arch'),
          ('k-3361', 'Mazen carries Aisha across the lawn'), ('k-4669', 'Couple at sunset by the water')]
EV_HOLIDAY = [('k-4159', 'Couple smiling by the Christmas tree'), ('k-4165', 'Couple kiss by the Christmas tree'), ('k-4113', 'Couple at a church altar dressed for the holidays'),
              ('k-3778', 'Winter portrait, forehead kiss'), ('k-3776', 'Winter portrait'), ('k-4793', 'Sparkler send-off'), ('k-3643', 'Couple entering a winter reception'), ('k-4660', 'Couple outside the venue')]

EVENTS = {
 # ---------------- Cluster 1: Music City Center + conventions ----------------
 'music-city-center-photographer': dict(
  vid='v2-media', eyebrow='Music City Center photographer & videographer', place=True, proof='films', cluster='mcc',
  h='Music City Center|photographer &amp; videographer. <span class=grad>One crew, every hall.</span>',
  title='Music City Center Photographer & Videographer | Leo Operations',
  desc='Photography, video, highlight reels, headshot booths, livestream, signage and printed programs for events at Music City Center in Nashville. One local crew. Call (773) 573-2135.',
  lead='Leo Operations is a Nashville photo, video and design studio built for big rooms. We cover conventions, conferences, trade shows, galas and award dinners at Music City Center: the photos, the recap film, the same-day social clips, the headshot lounge, the livestream, and the signage and programs your attendees hold in their hands.',
  sections=[
   ('Everything your event needs, from one team', [
    'Most events at Music City Center hire four or five vendors to tell one story: a photographer, a video company, a designer, a print shop and someone to run headshots. Every handoff costs time, and the event comes out looking like five different brands. We do all of it under one roof, with one producer who knows your run of show.',
    'That means the program cover, the step-and-repeat, the stage graphics and the recap film all share one look, and the person shooting your keynote already knows which sponsors need to be in frame.']),
   ('Built for a building this size', [
    'Music City Center is 2.1 million square feet at 201 Rep. John Lewis Way South, with 353,143 square feet of exhibit halls, the 57,500 square foot Karl F. Dean Grand Ballroom, the Davidson Ballroom and 60 meeting rooms. A general session upstairs, breakouts on two floors and an expo in Halls A through D can all run at the same hour. We staff to the schedule, not to a flat headcount: one shooter per room that matters, a floater for the hallways, and an editor cutting as the day goes.',
    'We plan around the building\'s rules before we arrive. Electrical, internet and rigging are exclusive services at Music City Center, so we order power drops, a hardwired line for any livestream and rigged banner points through your show management in advance, and we coordinate camera risers with your audio-visual company. Drones are not allowed indoors, so aerials stay outside. Nothing gets taped to a wall, nothing blocks an egress path, and the contractor paperwork your show requires is done before we badge in.']),
   ('Proof from the floor', [
    'We filmed the 2026 Tennessee Wine & Spirits Retailers Association trade show in Nashville: the expo floor, the exhibitor booths, the awards ceremony and the step-and-repeat, cut into a highlight reel the association uses to sell sponsorships and booths for next year. We filmed a HYROX race simulation in Nashville station by station in 120 fps slow motion, ahead of HYROX Nashville at Music City Center on December 9 to 13, 2026.',
    'Our founder has photographed more than 1,000 events, including the DC Chamber of Commerce 2026 Chamber\'s Choice Awards & Gala as an official media partner, the Congressional Black Caucus Foundation\'s Phoenix Awards Dinner, Tennessee State University Homecoming 2025 and DJ AOne\'s 40th at Madison Square Garden. Clients include the National Black Caucus of State Legislators, the Memphis Grizzlies, Tennessee State University and Meharry Medical College.']),
   ('Design and print, handled', [
    'Our design studio, led by Partner and Creative Director Morganne Norwood, builds the visual system for the whole event: printed programs and agendas, pamphlets and one-sheets, sponsor boards, directional signage, stage screens, step-and-repeat banners, name badges and the social graphics that promote it all. We have designed anniversary programs, a full university magazine, yearbooks, postcards, invitations and event key art.',
    'We prepare print-ready files to your printer\'s spec or coordinate production with a Nashville printer and delivery to the loading dock, so the boxes are at registration when doors open.']),
  ],
  feats=[('Event photography', 'Keynotes, panels, expo floor, networking, awards and the room itself.'), ('Video and highlight reels', 'A 60 to 90 second recap, sponsor cuts and full session recordings.'),
         ('Same-day social', 'Edited photos and vertical clips delivered during the event so your team can post live.'), ('Headshot lounge', 'A branded headshot booth for attendees, with images delivered to their inbox.'),
         ('Livestream', 'Multi-camera streams of keynotes and general sessions to YouTube, Vimeo, Zoom or your event app.'), ('Design and print', 'Programs, pamphlets, signage, sponsor boards, banners and badges.')],
  faq=[('Do you work at Music City Center?', 'Yes. Leo Operations is based in Nashville and covers conventions, conferences, trade shows and galas at Music City Center and the downtown convention hotels. We coordinate with your show management and the venue\'s in-house providers before load-in.'),
       ('Can one company handle photography, video and design for our convention?', 'Yes. That is how we prefer to work. One producer runs photo, video, headshots, livestream and the design of your printed and digital materials, so everything matches and nothing falls between vendors.'),
       ('How fast do we get photos and video?', 'We can deliver edited selects the same day for social and press, with the full gallery and the highlight reel after the event. We agree on exact turnaround in writing when you book.'),
       ('Do you provide a headshot booth for attendees?', 'Yes. We set up a branded headshot lounge with lighting, a backdrop and a check-in flow, and attendees receive their edited headshot by email.'),
       ('Can you livestream our general session?', 'Yes. We run multi-camera livestreams of keynotes and general sessions. Internet at Music City Center is supplied by the venue\'s exclusive provider, so we order a dedicated hardwired line through your show management in advance.'),
       ('Can you design and print our programs and signage?', 'Yes. Our design team builds programs, agendas, pamphlets, sponsor boards, directional signs and banners, and we either deliver print-ready files or manage printing and delivery to the venue.'),
       ('How much does a Music City Center photographer or videographer cost?', 'It depends on days, crew size, rooms covered and deliverables. Email or call with your dates, halls and session schedule and we will send a written quote within one business day.'),
       ('How do we book?', f'Email us or call {PHONE} with your event name, dates, the halls and ballrooms you have contracted and your expected attendance. We reply within one business day.')],
  related=['nashville-conference-photographer', 'nashville-convention-videographer', 'nashville-trade-show-photographer', 'nashville-event-graphics-printing', 'headshot-photographer', 'video-production-company'],
  guides=['music-city-center-event-media', 'conference-media-checklist', 'trade-show-booth-content', 'conference-headshot-booth', 'event-photographer-cost'],
 ),
 'nashville-conference-photographer': dict(
  vid='v2-photo', eyebrow='Conference photographer, Nashville', proof='photos', cluster='mcc',
  h='Nashville conference|photographer. <span class=grad>Every room, every name.</span>',
  title='Conference Photographer Nashville | Convention & Event Photography',
  desc='Conference and convention photography in Nashville: keynotes, breakouts, expo floors, awards and headshots. 1,000+ events photographed. Leo Operations, (773) 573-2135.',
  lead='Conferences live or die on proof: proof for sponsors, for next year\'s registrations and for the speakers you want back. Leo Operations photographs conferences and conventions across Nashville, from Music City Center to the downtown hotel ballrooms, and delivers images your team can use the same day.',
  sections=[
   ('What we photograph at a conference', [
    'Keynotes from three angles, panels with every speaker sharp, breakout rooms full of people taking notes, the expo floor with sponsor logos readable, networking receptions, award presentations, VIP and board photos, and the wide shots of the room that show how big the event really was. We work from your agenda and a written shot list, so the sponsor who paid for the lunch gets photographed at the lunch.']),
   ('Same-day images for social and press', [
    'We cull and edit as the day goes. Your communications team gets a first set of edited images during the event to post while people are still talking about it, and the full color-corrected gallery follows in a private online gallery, ready to download and share.']),
   ('Names, captions and sponsors', [
    'We shoot like a newsroom. Our founder publishes Washington DC Magazine and has photographed more than 1,000 events, so names get captured, honorees are photographed with the people who matter to them, and sponsor signage is in the frame on purpose.']),
   ('Photo, video and design together', [
    'The same team shoots 4K video, runs headshot lounges and designs programs and signage. Book one or all of it. Either way you get one producer and one invoice.']),
  ],
  feats=[('Keynotes and general sessions', 'Stage, screens and audience reaction.'), ('Breakouts and panels', 'Every speaker, every room on your list.'), ('Expo floor', 'Exhibitors, booths and sponsor branding.'),
         ('Awards and galas', 'Presentations, honorees and the red carpet.'), ('Headshots', 'A branded lounge for attendees and speakers.'), ('Fast delivery', 'Same-day selects plus a full online gallery.')],
  faq=[('How much does a conference photographer cost in Nashville?', 'It depends on hours, the number of rooms running at once and how fast you need images. Email your agenda and dates and we will quote it in writing within one business day.'),
       ('How many photographers do we need for a conference?', 'Plan one photographer for every room that must be covered at the same time, plus a floater on large expo floors. We build the crew from your agenda.'),
       ('Can we get photos during the event?', 'Yes. We deliver edited selects during the event for social media and press, then the full gallery afterward.'),
       ('Do you cover Music City Center and hotel conferences?', 'Yes. We cover conferences at Music City Center, the downtown convention hotels, Gaylord Opryland, universities and corporate campuses across Middle Tennessee.'),
       ('Can you also film the conference?', 'Yes. We shoot session recordings, a highlight reel and vertical clips with the same crew.'),
       ('How do we book?', f'Email us or call {PHONE} with your dates, venue and agenda.')],
  related=['music-city-center-photographer', 'nashville-convention-videographer', 'nashville-trade-show-photographer', 'headshot-photographer', 'nashville-photographer'],
  guides=['conference-media-checklist', 'music-city-center-event-media', 'conference-headshot-booth', 'event-photographer-cost'],
 ),
 'nashville-convention-videographer': dict(
  vid='v2-media', eyebrow='Convention & conference videographer, Nashville', proof='films', cluster='mcc',
  h='Convention videography|in Nashville. <span class=grad>Recap films that sell next year.</span>',
  title='Convention & Corporate Event Videographer Nashville | Leo Operations',
  desc='Convention, conference and corporate event videography in Nashville: highlight reels, session recordings, sponsor videos, livestream and same-day social clips. Call (773) 573-2135.',
  lead='A good recap film does three jobs: it thanks the people who came, it shows sponsors what they bought, and it sells next year\'s event. Leo Operations films conventions, conferences and corporate events in Nashville in 4K and cuts them for every place they will be watched.',
  sections=[
   ('What we deliver', [
    'A 60 to 90 second highlight reel cut to music, longer recap films, full session recordings for your on-demand library, short sponsor and exhibitor videos, speaker soundbites, and vertical clips sized for Instagram, TikTok and LinkedIn. We can also livestream keynotes and general sessions.']),
   ('How we shoot an event', [
    'We start with your run of show and mark the moments that sell: the opening walk-in, the keynote applause line, the expo floor at its busiest, the award, the reception. We shoot high frame rate for slow motion, capture clean audio from the house sound board, and pull establishing wides early, because the open of a recap film has to show the size of the room.',
    'For the 2026 Tennessee Wine & Spirits Retailers Association trade show, that meant elevated wides from the stage, the exhibitor booths, the awards ceremony and the step-and-repeat, cut into a reel built to sell sponsorships and booths for the next show.']),
   ('Built for Music City Center and downtown', [
    'We know how the big rooms run. At Music City Center, power, rigging and internet go through the venue\'s exclusive providers, so camera risers, power drops and stream bandwidth get ordered through your show management before load-in. We handle that paperwork with you.']),
   ('One crew for photo, video and design', [
    'Add photography, a headshot lounge, or the design of your programs and signage, and it is all produced by the same team with one look.']),
  ],
  feats=[('Highlight reels', '60 to 90 second recaps cut to music.'), ('Session recordings', 'Multi-camera keynotes and panels with board audio.'), ('Sponsor videos', 'Short cuts sponsors can post and renew on.'),
         ('Testimonials', 'Attendee and speaker soundbites captured on site.'), ('Livestream', 'Keynotes and general sessions streamed live.'), ('Vertical social', 'Clips for Instagram, TikTok and LinkedIn during the event.')],
  faq=[('How much does it cost to hire a videographer for an event?', 'Event video is priced by crew size, hours on site and editing. A single camera for a half day and a multi-camera crew with a same-day edit are very different jobs. Send your agenda and we will quote it in writing within one business day.'),
       ('What is an event videographer?', 'An event videographer films live events such as conventions, conferences, galas and award shows, and edits the footage into recap films, session recordings and social clips.'),
       ('How long does a conference highlight video take?', 'We can deliver a same-day or next-day social cut during the event, with the full highlight reel after. We set the turnaround in writing when you book.'),
       ('Can you record every session?', 'Yes. We staff one camera operator per room that needs recording and capture audio from the house sound system.'),
       ('Do you livestream events?', 'Yes. We stream keynotes and general sessions to YouTube, Vimeo, Zoom or your event platform, with a dedicated hardwired line ordered through the venue.'),
       ('How do we book?', f'Email us or call {PHONE} with your dates, venue and agenda.')],
  related=['music-city-center-photographer', 'nashville-conference-photographer', 'nashville-trade-show-photographer', 'nashville-videographer', 'video-production-company'],
  guides=['music-city-center-event-media', 'conference-media-checklist', 'trade-show-booth-content', 'videographer-cost'],
 ),
 'nashville-trade-show-photographer': dict(
  vid='v2-media', eyebrow='Trade show photographer & booth video, Nashville', proof='films', cluster='mcc',
  h='Trade show photographer|in Nashville. <span class=grad>Booths, buyers, brands.</span>',
  title='Trade Show Photographer Nashville | Booth Photos & Video',
  desc='Trade show photography and video in Nashville for associations and exhibitors: expo floor coverage, booth photos and videos, product content and sponsor recaps. Call (773) 573-2135.',
  lead='We filmed the 2026 Tennessee Wine & Spirits Retailers Association trade show in Nashville, and the exhibitors were the point: Empress 1908, Dulce Vida, Penelope, Larceny, Patron, DoorDash, Uber Eats and dozens more, all on camera. Leo Operations photographs and films trade shows for the associations that run them and the brands that exhibit at them.',
  sections=[
   ('For show organizers', [
    'Your recap is your sales deck for next year. We cover the expo floor at peak traffic, every sponsor activation, the awards and the networking events, and we cut a highlight reel and sponsor-specific clips that make renewals easy. The TWSRA reel ends on a direct ask: sponsor, exhibit, attend.']),
   ('For exhibitors', [
    'Book us for your booth alone. We photograph your booth clean before doors open, then busy with buyers, capture product shots on the stand, record short interviews with your team and customers, and deliver vertical clips you can post during the show while buyers are still on the floor.']),
   ('How we work a show floor', [
    'Expo halls are dark, loud and crowded. We shoot fast cinema cameras at high frame rates for slow motion, pull elevated wides when the venue allows, and grade so products and faces read correctly even under warehouse lighting. We follow the show\'s exhibitor-appointed contractor rules and badge in like any other contractor.']),
   ('Design for the booth', [
    'Our design studio builds booth graphics, one-sheets, pamphlets, product cards and social promotion for the show, so the photos and the booth look like the same brand.']),
  ],
  feats=[('Expo floor coverage', 'Traffic, booths and activations at peak hours.'), ('Booth photos', 'Clean and busy versions of your stand.'), ('Booth video', 'Interviews, demos and product B-roll.'),
         ('Sponsor recaps', 'Clips each sponsor can post and renew on.'), ('Awards and receptions', 'Stage, honorees and the room.'), ('Booth design', 'Graphics, one-sheets and pamphlets.')],
  faq=[('Do you photograph trade shows at Music City Center?', 'Yes. We cover trade shows and expos at Music City Center and other Nashville venues, for organizers and for individual exhibitors.'),
       ('Can we book you for just our booth?', 'Yes. Exhibitors book us for booth photos, product shots, interviews and social clips during the show.'),
       ('Do you follow exhibitor-appointed contractor rules?', 'Yes. We register through the show as an exhibitor-appointed contractor when required, follow the show\'s badge and move-in rules, and coordinate with the general contractor.'),
       ('Can you post content during the show?', 'Yes. We deliver edited photos and vertical clips during the show so your team can post while buyers are on the floor.'),
       ('What trade shows have you covered?', 'Recent work includes the 2026 Tennessee Wine & Spirits Retailers Association trade show in Nashville: the expo floor, exhibitor booths, awards ceremony and step-and-repeat.'),
       ('How do we book?', f'Email us or call {PHONE} with the show name, dates and your booth number or the areas you need covered.')],
  related=['music-city-center-photographer', 'nashville-convention-videographer', 'nashville-conference-photographer', 'nashville-event-graphics-printing'],
  guides=['trade-show-booth-content', 'music-city-center-event-media', 'conference-media-checklist'],
 ),
 'nashville-event-graphics-printing': dict(
  vid='v2-social', eyebrow='Event graphics, signage & printed programs, Nashville', proof='design', cluster='mcc',
  h='Event graphics|&amp; printed programs. <span class=grad>Designed in Nashville.</span>',
  title='Event Graphics, Signage & Program Printing Nashville | Leo Operations',
  desc='Event design in Nashville: printed programs, pamphlets, agendas, signage, sponsor boards, step-and-repeat banners, badges and social graphics, designed and produced. Call (773) 573-2135.',
  lead='Your attendees judge an event by what they hold and what they walk past: the program, the badge, the sign that tells them where Hall C is. Leo Operations designs the full visual system for conferences, galas, conventions and church events, then prepares it for print or manages the printing and delivery for you.',
  sections=[
   ('What we design', [
    'Printed programs and agendas, pamphlets and tri-folds, one-sheets, sponsor boards and logo walls, directional and room signage, step-and-repeat banners, stage screen graphics, name badges and lanyards, tickets and invitations, save-the-dates, and the social graphics that promote the event before, during and after.']),
   ('Work you can see', [
    'Our design studio is led by Partner and Creative Director Morganne Norwood. Recent pieces include anniversary programs and a 60th anniversary save-the-date for Cathedral of Praise in Nashville, a Homecoming 2025 campaign and a full magazine for Tennessee State University, a yearbook for Invictus Nashville, reunion posters, admissions postcards and event key art for galas and brunches.']),
   ('Design to delivery', [
    'We build files to your printer\'s exact spec, with bleed, safe zones and the right color profile, or we coordinate production with a Nashville printer and get the boxes to your venue\'s loading dock on time. For Music City Center events, we schedule delivery with your general contractor so signage is in place at load-in.']),
   ('One look for the whole event', [
    'Because the same team photographs and films events, your program, signage, stage screens and recap video share one brand, and the photos show your signage the way it was meant to look.']),
  ],
  feats=[('Programs and agendas', 'Printed and digital, with speaker bios and sponsor pages.'), ('Pamphlets and one-sheets', 'Tri-folds, flyers and handouts.'), ('Signage', 'Directional, room and registration signs.'),
         ('Sponsor recognition', 'Logo walls, sponsor boards and stage loops.'), ('Banners and step-and-repeats', 'Photo walls and stage backdrops.'), ('Badges and invitations', 'Badges, tickets, invitations and save-the-dates.')],
  faq=[('Do you print event programs and signage?', 'We design them and either deliver print-ready files or manage the printing with a Nashville printer and delivery to your venue.'),
       ('Can you design a conference program with sponsor pages?', 'Yes. We lay out agendas, speaker bios, maps, sponsor pages and ads, and we can produce a matching digital version for your event app or website.'),
       ('Can you design our step-and-repeat banner?', 'Yes. We design step-and-repeats and logo walls sized for your venue, and we photograph your guests in front of them if you book coverage.'),
       ('How early should we start event design?', 'Start six to eight weeks before the event for programs and signage, earlier if sponsors need to approve their placements. Rush timelines are possible when content is final.'),
       ('Do you design for church events?', 'Yes. We design anniversary programs, save-the-dates, service graphics and visitor cards for churches in Nashville.'),
       ('How do we start?', f'Email us or call {PHONE} with the event, the date, what pieces you need and your quantities.')],
  related=['music-city-center-photographer', 'nashville-trade-show-photographer', 'social-media-design', 'churches'],
  guides=['conference-media-checklist', 'music-city-center-event-media', 'professional-social-media-graphics'],
 ),

 # ---------------- Cluster 2: weddings, proposals, engagements ----------------
 'nashville-wedding-videographer': dict(
  vid='w-hero', eyebrow='Nashville wedding videographer', proof='wedfilm', cluster='wed', cat='Weddings',
  h='Nashville wedding|videographer. <span class=grad>Films you will rewatch.</span>',
  title='Nashville Wedding Videographer | Cinematic Wedding Films | Leo Operations',
  desc='Nashville wedding videography in 4K: a 5 to 7 minute highlight film, drone when weather allows, two camera professionals and up to eight hours of coverage. Leo Operations.',
  lead='Leo Operations films weddings across Nashville and Middle Tennessee in 4K. Your highlight film runs five to seven minutes, color graded, with enhanced audio and licensed music, and it arrives within 14 business days.',
  sections=[
   ('What your wedding film includes', [
    'Coverage up to eight consecutive hours, from getting ready through the send-off. Two camera professionals, with a third added when your timeline needs it. Drone exteriors when the weather allows. A five to seven minute highlight film with color grading, audio enhancement and licensed music, delivered within 14 business days.']),
   ('Photo and film from one team', [
    'Book video alone or add photography from the same coordinated team. On combined bookings the two camera professionals are one photographer and one videographer who plan together, so nobody walks through the other\'s shot during the vows. Edited photos arrive within three business days.']),
   ('A planning call, a shot list, a timeline', [
    'Before the day, we sit down with you (and whoever is helping plan) and build a written shot list and timeline: the family combinations, the cultural moments, the speeches, the songs. On the day, nothing important depends on someone remembering.']),
   ('Every tradition, filmed with care', [
    'We have filmed Somali, Nigerian, Muslim and Christian weddings, church ceremonies and lakeside vows. We learn the order of your traditions before the day so we are in the right spot for each one. We are based in Nashville, film across Brentwood, Franklin and Murfreesboro, and travel for weddings in other states.']),
  ],
  feats=[('4K cinema cameras', 'Clean, cinematic images in every light.'), ('Two camera professionals', 'A third when the timeline calls for it.'), ('Up to 8 hours', 'Getting ready through the send-off.'),
         ('Highlight film', '5 to 7 minutes, graded, licensed music.'), ('Drone', 'Exterior aerials, weather permitting.'), ('Fast delivery', 'Film within 14 business days.')],
  faq=[('How much is a wedding videographer in Nashville?', 'Wedding film is priced by hours, crew and deliverables. Send your date, venue and guest count and we will send a written quote. For national market ranges, see our wedding videographer cost guide.'),
       ('How long is the highlight film?', 'Five to seven minutes, color graded, with enhanced audio and licensed music.'),
       ('When will we get our wedding film?', 'Your highlight film is delivered within 14 business days. If you also book photography, edited photos arrive within three business days.'),
       ('Do you use a drone?', 'Yes, for exterior footage when the weather and the venue allow it.'),
       ('Can we book photography and video together?', 'Yes. One coordinated team covers both, which keeps the day calmer and the coverage complete.'),
       ('Do you film weddings outside Nashville?', 'Yes. We film across Middle Tennessee and travel to other states.'),
       ('How do we check availability?', f'Email us or call {PHONE} with your date, venue and guest count.')],
  related=['weddings', 'nashville-proposal-photographer', 'nashville-videographer', 'nashville-photographer'],
  guides=['wedding-videographer-cost', 'wedding-videography-styles', 'wedding-photographer-and-videographer', 'nashville-engagement-photo-locations'],
 ),
 'nashville-proposal-photographer': dict(
  vid='w-hero', eyebrow='Nashville proposal photographer', proof='wedding', cluster='wed', cat='Weddings',
  h='Nashville proposal|photographer. <span class=grad>Hidden until the yes.</span>',
  title='Proposal Photographer Nashville | Surprise Proposal Photos & Video',
  desc='Surprise proposal photography and video in Nashville: we scout the spot, stay hidden, catch the question and the yes, then shoot a mini engagement session. Call (773) 573-2135.',
  lead='You get one chance at the moment. Leo Operations plans Nashville surprise proposals with you, hides in plain sight, captures the question, the reaction and the yes, and follows it with a short engagement session while you are both still glowing.',
  sections=[
   ('How a surprise proposal shoot works', [
    'We start with a call: where you want to ask, when, and what your partner would notice. We pick a spot with a clean background and a place for us to stand that does not give it away, agree on a signal, and time it to the best light. On the day we are already in position, looking like tourists, when you walk up.',
    'After the yes, we step out and shoot 20 to 30 minutes of portraits on location, so you leave with the moment and the photos you will put on the save-the-date.']),
   ('Where to propose in Nashville', [
    'Our guide to the best places to propose in Nashville covers the spots that photograph well and the practical details: crowds, parking, permits and timing. Popular choices include the John Seigenthaler Pedestrian Bridge with the skyline behind you, the Parthenon in Centennial Park, Love Circle at sunset, the stone steps in Percy Warner Park, Cheekwood\'s gardens and a downtown rooftop.']),
   ('Photo, video or both', [
    'Add a videographer and you get the whole thing with sound: the question, the gasp, the call to Mom. We shoot 4K video and can deliver a short film you can share the same week.']),
   ('Then the wedding', [
    'Many couples who start with a proposal shoot come back for engagement photos and the wedding. We film and photograph weddings across Middle Tennessee with a written shot list and timeline.']),
  ],
  feats=[('Location scouting', 'A spot with good light and a place to hide.'), ('Hidden coverage', 'Long lenses, no tip-offs.'), ('The question and the yes', 'Every second, in sequence.'),
         ('Mini engagement session', 'Portraits right after, on location.'), ('Proposal video', 'The whole moment, with sound.'), ('Private gallery', 'Edited photos online, ready to share.')],
  faq=[('How much does it cost to hire a photographer for a proposal?', 'It depends on the location, how long we need to be in position and whether you add video or a longer session. Send your date and spot and we will quote it in writing.'),
       ('How far in advance should I book a proposal photographer?', 'Two to four weeks is comfortable, and more around holidays and Valentine\'s Day. If the date is close, call us; short notice is often possible.'),
       ('How will my partner not see you?', 'We pick a position with natural cover, dress to blend in, use long lenses, and agree on a signal so you know we are ready before you kneel.'),
       ('What if it rains?', 'We plan a covered backup spot and stay in touch the day of, so you can move the plan without tipping off your partner.'),
       ('Do you need a permit to photograph a proposal in a Nashville park?', 'Some Metro and state parks require a photography permit for professional shoots. We check the rules for your spot and handle any permit we need.'),
       ('Can you film the proposal too?', 'Yes. Add video and we capture the full moment in 4K with sound.')],
  related=['nashville-wedding-videographer', 'weddings', 'nashville-family-photographer', 'nashville-photographer'],
  guides=['best-places-to-propose-in-nashville', 'nashville-engagement-photo-locations', 'engagement-photos', 'when-to-book-wedding-photographer'],
 ),

 # ---------------- Cluster 3: Christmas, holiday, family ----------------
 'nashville-christmas-photos': dict(
  vid='v2-photo', eyebrow='Christmas & holiday photos, Nashville', proof='holiday', cluster='hol', cat='Family',
  h='Christmas photos|in Nashville. <span class=grad>Card-ready by December.</span>',
  title='Christmas Photos Nashville | Holiday Photo Sessions | Leo Operations',
  desc='Christmas and holiday photo sessions in Nashville for families, couples and teams, plus office holiday party photography. Book early for card season. Call (773) 573-2135.',
  lead='Holiday photo season in Nashville runs from the week after Thanksgiving to Christmas Eve, and the good dates go first. Leo Operations photographs families, couples, kids and whole teams for Christmas cards, plus office holiday parties and church Christmas programs.',
  sections=[
   ('Holiday sessions for families and couples', [
    'Pick a spot that means something, under the lights downtown, at home by your own tree, or somewhere green in one of the city\'s parks, and we will make the photo that goes on the card and the one that goes on the wall. We guide the posing so the kids are not stiff and the adults are not squinting, and we shoot enough variety that you get the formal shot, the candid one and the silly one.']),
   ('Office holiday parties and church Christmas events', [
    'We are event photographers first: more than 1,000 events photographed. Book us for the company holiday party, a client appreciation night, a Christmas gala or a church Christmas program, and we cover the room, the toasts, the awards and the people. Add a step-and-repeat or a holiday photo backdrop and every guest leaves with a portrait.']),
   ('Corporate team photos for the holidays', [
    'Need a team photo for the year-end card or a refresh of everyone\'s headshot before January? We run on-site headshot and team sessions at your office with lighting and a backdrop.']),
   ('Plan around the card deadline', [
    'If your photos are for printed cards, book by early December. Our guide to the best Christmas photo spots in Nashville lists this season\'s lights, dates and photo rules, and our family Christmas photo guide covers outfits, timing and what to do when a toddler melts down.']),
  ],
  feats=[('Family Christmas sessions', 'Downtown lights, parks or at home.'), ('Couples and engagement', 'Holiday portraits and save-the-dates.'), ('Christmas card photos', 'Horizontal and vertical crops for any card.'),
         ('Office holiday parties', 'Toasts, awards, candids and the room.'), ('Holiday backdrop booth', 'A portrait for every guest.'), ('Team photos', 'Year-end team shots and headshots.')],
  faq=[('When should I book Christmas photos in Nashville?', 'Book in November for the best dates. Most families want photos in late November or the first two weeks of December so cards can print and mail before Christmas.'),
       ('Where are the best places for Christmas photos in Nashville?', 'Downtown under the holiday lights, Centennial Park and the Parthenon, the Gulch, Franklin\'s Main Street and your own living room by the tree all photograph beautifully. Some ticketed light shows limit professional photography, so check our Christmas photo spots guide before you plan around one.'),
       ('Do you photograph office holiday parties?', 'Yes. We cover holiday parties, galas and client events, and we can add a holiday backdrop so every guest gets a portrait.'),
       ('Can you photograph us at home with our tree?', 'Yes. In-home sessions are some of our favorites. We bring lighting that keeps the tree lights glowing and faces bright.'),
       ('How do we book a holiday session?', f'Email us or call {PHONE} with the number of people, the location you have in mind and two or three dates that work.')],
  related=['nashville-family-photographer', 'nashville-photographer', 'headshot-photographer', 'nashville-proposal-photographer'],
  guides=['best-christmas-photo-spots-nashville', 'family-christmas-photos', 'event-photographer-cost'],
 ),
 'nashville-family-photographer': dict(
  vid='v2-photo', eyebrow='Family photographer, Nashville', proof='holiday', cluster='hol', cat='Family',
  h='Nashville family|photographer. <span class=grad>Everyone in the frame.</span>',
  title='Family Photographer Nashville | Family Portraits & Reunions',
  desc='Family photography in Nashville: family portraits, extended family and reunion photos, milestone birthdays, anniversaries and holiday sessions. Leo Operations, (773) 573-2135.',
  lead='Somebody always ends up behind the camera instead of in the picture. Leo Operations photographs Nashville families so everyone is in the frame: portraits in the park, the whole extended family at the reunion, the 40th birthday, the 50th anniversary and the Christmas card.',
  sections=[
   ('Family sessions', [
    'An hour, a place you love, and a photographer who knows how to get a three-year-old and a grandfather to look at the camera at the same time. We guide the poses, keep it moving and photograph the in-between moments, which are usually the best ones.']),
   ('Reunions, anniversaries and milestone birthdays', [
    'Big family events are where our event experience pays off. We have photographed more than 1,000 events, including DJ AOne\'s 40th birthday at Madison Square Garden. At a reunion or anniversary we work from a list of family groupings so every branch of the family gets its photo, then cover the speeches, the food and the dance floor.']),
   ('Every family, every skin tone', [
    'We light and grade for every shade of skin, not just the brightest one in the frame, and we photograph families of every faith and tradition. Leo Operations is Black-owned and based in Nashville.']),
   ('Holiday and card season', [
    'From late November through mid December, family sessions turn into Christmas card sessions. See our Christmas photos page and our guide to the best Christmas photo spots in Nashville.']),
  ],
  feats=[('Family portraits', 'Parks, downtown or at home.'), ('Extended family', 'Grandparents, cousins and everyone.'), ('Reunions', 'Group photos by family branch, plus the party.'),
         ('Milestones', 'Birthdays, anniversaries and graduations.'), ('Holiday cards', 'Christmas and holiday sessions.'), ('Online gallery', 'A private gallery to download and print.')],
  faq=[('What is the average cost for a family photoshoot?', 'It depends on session length, the number of people and the location. Send your family size, location and dates and we will quote it in writing. Our event photographer cost guide covers market rates.'),
       ('What are the best places for family photos in Nashville?', 'Centennial Park, the Shelby Street pedestrian bridge, Cheekwood, the Percy Warner Park steps, Radnor Lake and your own home are all strong choices. Some parks and gardens require a permit or fee for professional photography, which we arrange.'),
       ('Do you photograph family reunions?', 'Yes. We work from a list of family groupings so every branch gets its portrait, and we cover the full event.'),
       ('What should our family wear?', 'Coordinate, do not match. Pick two or three colors and let each person wear them differently. Avoid big logos and tiny busy patterns.'),
       ('How do we book?', f'Email us or call {PHONE} with your family size, a location idea and a few dates.')],
  related=['nashville-christmas-photos', 'nashville-photographer', 'nashville-proposal-photographer', 'headshot-photographer'],
  guides=['family-christmas-photos', 'best-christmas-photo-spots-nashville', 'nashville-engagement-photo-locations'],
 ),
}
EVENT_NAMES = {'music-city-center-photographer': 'Music City Center Photographer & Videographer', 'nashville-conference-photographer': 'Nashville Conference Photographer',
               'nashville-convention-videographer': 'Convention & Event Videographer', 'nashville-trade-show-photographer': 'Trade Show Photographer',
               'nashville-event-graphics-printing': 'Event Graphics & Printed Programs', 'nashville-wedding-videographer': 'Nashville Wedding Videographer',
               'nashville-proposal-photographer': 'Nashville Proposal Photographer', 'nashville-christmas-photos': 'Christmas Photos in Nashville',
               'nashville-family-photographer': 'Nashville Family Photographer'}
_EV_OTHER = {'headshot-photographer': 'Headshot Photographer', 'video-production-company': 'Video Production Company', 'nashville-photographer': 'Nashville Event Photographer',
             'nashville-videographer': 'Nashville Videographer', 'social-media-design': 'Social Media & Design', 'churches': 'Church Media', 'weddings': 'Wedding Photo & Film'}

def _ev_proof(kind, pre):
    if kind == 'films':
        F = {f[1]: f for f in FILMS}
        sel = [F[s][:4] + (c,) for s, c in EV_FILMS if s in F]
        return '<div class="films">' + ''.join(f'<div class="film {c}" ' + (f'data-video="{pre}{y[6:]}"' if y.startswith("video:") else f'data-yt="{y}"') + f' data-c="Play" data-r="{i%4}">{img("assets/films/"+s+".jpg","",pre)}<video muted loop playsinline preload="none" poster="{pre}assets/films/{s}.jpg" data-src="{pre}assets/films/{s}.mp4"></video><span class="play"></span><div class="cap"><span class="mono">{E(k)}</span><b>{E(t)}</b></div></div>' for i, (y, s, t, k, c) in enumerate(sel)) + '</div>'
    if kind == 'photos':
        return shot_strip(pre)
    if kind == 'design':
        figs = ''.join(f'<figure data-r="{i%3}" class="evd">{img("assets/work/"+k+".jpg", t+", "+by, pre)}<figcaption><b>{E(t)}</b><span>{E(by)}</span></figcaption></figure>' for i, (k, t, by) in enumerate(EV_DESIGN))
        return f'<div class="evgrid">{figs}</div>'
    if kind in ('wedding', 'holiday', 'wedfilm'):
        L = EV_HOLIDAY if kind == 'holiday' else EV_WED
        figs = ''.join(f'<figure data-r="{i%3}" class="evp">{img("assets/weddings/"+k+".jpg", a+", photographed by Leo Operations", pre)}</figure>' for i, (k, a) in enumerate(L))
        reel = (f'<div class="films" style="margin-bottom:18px"><div class="film wide" data-video="{pre}assets/weddings/w-reel-hd.mp4" data-c="Play" style="margin-bottom:18px">{img("assets/weddings/w-reel.jpg","Leo Operations wedding highlight reel",pre)}<span class="play"></span><div class="cap"><span class="mono">Wedding films</span><b>Our 60-second wedding reel</b></div></div></div>' if kind == 'wedfilm' else '')
        return f'{reel}<div class="evgrid">{figs}</div>'
    return clients_grid(pre, 8)

EV_CSS = ('<style>.evgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}@media (max-width:860px){.evgrid{grid-template-columns:repeat(2,1fr)}}.evgrid figure{margin:0;border-radius:16px;overflow:hidden;position:relative;background:var(--bg2)}'
          '.evp{aspect-ratio:4/5}.evp img,.evd img{width:100%;height:100%;object-fit:cover;display:block}.evd{aspect-ratio:4/5}.evd figcaption{position:absolute;left:0;right:0;bottom:0;padding:14px;background:linear-gradient(transparent,rgba(3,6,12,.85));font-size:13px}'
          '.evd figcaption b{display:block;color:#fff}.evd figcaption span{color:var(--silver)}.evfacts{margin-top:8px}.evfacts table{min-width:0}.evfacts td:first-child{width:34%}.evcall{display:block;margin-top:14px;font-size:20px;color:#fff;font-weight:600}.evcall small{display:block;font-size:12px;color:var(--silver);font-weight:400}'
          '.evlinks{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;margin-top:18px}</style>')

def _ev_facts():
    rows = MCC_FACTS if 'MCC_FACTS' in globals() else []
    if not rows: return ''
    tr = ''.join(f'<tr><td>{E(a)}</td><td>{E(b)}</td></tr>' for a, b, _ in rows)
    src = ' &middot; '.join(sorted({f'<a href="{s}" rel="noopener" target="_blank" style="color:var(--cyan)">{E(s.split("/")[2].replace("www.",""))}</a>' for _, _, s in rows}))
    return (f'<section class="sec wrap"><span class="eyebrow mono">The venue</span><h2 class="h-lg" style="margin:14px 0 24px">{split("Music City Center,|<span class=grad>by the numbers.</span>")}</h2>'
            f'<div class="gtable evfacts"><table><thead><tr><th>Space</th><th>Detail</th></tr></thead><tbody>{tr}</tbody></table></div><p class="mono" style="font-size:11px;color:var(--silver)">Sources: {src}. Leo Operations is an independent vendor and is not affiliated with Music City Center.</p></section>')

def event_page(slug):
    L = EVENTS[slug]
    prose = ''.join(f'<h2>{E(h)}</h2>' + ''.join(f'<p>{E(p)}</p>' for p in ps) for h, ps in L['sections'])
    feats = ''.join(f'<div data-r="{i%3}"><b>{E(a)}</b><span>{E(b)}</span></div>' for i, (a, b) in enumerate(L['feats']))
    faq = ''.join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in L['faq'])
    url = SITE + '/' + slug + '/'
    subj = 'Inquiry%20from%20leooperations.com%20' + slug
    # cross-links: sibling event pages first, then guides that exist
    def rel_html(pre):
        cards = ''
        for r in L['related']:
            nm = EVENT_NAMES.get(r) or _EV_OTHER.get(r) or LANDING_NAMES.get(r + '/') or LANDING_NAMES.get(r) or r
            cards += f'<a class="gcard" href="{pre}{r}/"><span class="eyebrow mono">Service</span><b>{E(nm)}</b></a>'
        for g in L.get('guides', []):
            if g in GUIDES:
                cards += f'<a class="gcard" href="{pre}guides/{g}/"><span class="eyebrow mono">Guide</span><b>{E(GUIDES[g]["h1"])}</b><span>{E(GUIDES[g].get("dek",""))}</span></a>'
        return f'<div class="evlinks">{cards}</div>'
    biz = {"@type": "ProfessionalService", "@id": SITE + "/#nashville", "name": "Leo Operations", "url": SITE + "/", "telephone": PHONE_TEL, "image": SITE + "/assets/img/og.jpg",
           "priceRange": "Quote on request", "address": {"@type": "PostalAddress", "addressLocality": "Nashville", "addressRegion": "TN", "addressCountry": "US"},
           "areaServed": NASH_AREA, "parentOrganization": {"@id": SITE + "/#organization"}}
    area = NASH_AREA + ([MCC_PLACE] if L.get('place') else [])
    ld = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in L['faq']]},
          dict({"@context": "https://schema.org"}, **biz),
          {"@context": "https://schema.org", "@type": "Service", "name": L['eyebrow'], "serviceType": L['eyebrow'], "provider": {"@id": SITE + "/#nashville"}, "areaServed": area, "url": url, "description": L['desc']},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": EVENT_NAMES[slug], "item": url}]}]
    hero_vid = L['vid']
    def body(pre):
        hv = (f'<video muted loop playsinline autoplay preload="auto" poster="{pre}assets/weddings/w-hero.jpg" src="{pre}assets/weddings/w-hero-hd.mp4"></video>' if hero_vid == 'w-hero' else vid(hero_vid, pre, eager=True))
        call = f'<a class="btn ghost" href="tel:{PHONE_TEL}">Call {PHONE}</a>'
        proof_h = {'films': 'See it|<span class=grad>in motion.</span>', 'photos': 'In the|<span class=grad>room.</span>', 'design': 'Designed by|<span class=grad>our studio.</span>',
                   'wedding': 'Couples we|<span class=grad>photographed.</span>', 'wedfilm': 'Our wedding|<span class=grad>films.</span>', 'holiday': 'Holiday|<span class=grad>portraits.</span>'}.get(L['proof'], 'Who we|<span class=grad>work with.</span>')
        return f'''{EV_CSS}<section class="hero page-hero"><div class="hero-media">{hv}</div><div class="hero-inner"><span class="eyebrow mono">{E(L["eyebrow"])}</span><h1 class="h-xl">{split(L["h"])}</h1><p class="lead">{E(L["lead"])}</p><div class="hero-ctas">{mail("rod","leooperations.com","Get a quote <span class=\"arr\">&rarr;</span>","btn primary",subj)}{call}</div></div></section>
{stats_html()}
<section class="sec wrap" id="more"><div class="two-col"><div class="prose">{prose}</div><aside class="sticky-card"><h3>Let&rsquo;s talk.</h3><p>Send your date, venue and what you need. We reply within one business day.</p>{mail("rod","leooperations.com","Email Leo Operations <span class=\"arr\">&rarr;</span>","btn primary",subj)}<a class="evcall" href="tel:{PHONE_TEL}"><small>Or call</small>{PHONE}</a></aside></div></section>
{_ev_facts() if L.get("place") else ""}
<section class="sec wrap"><span class="eyebrow mono">What we deliver</span><h2 class="h-lg" style="margin:14px 0 30px">{split("Everything|<span class=grad>you need.</span>")}</h2><div class="feat">{feats}</div></section>
<section class="sec wrap"><div class="sec-head"><div><span class="eyebrow mono">Proof</span><h2 class="h-lg" style="margin-top:14px">{split(proof_h)}</h2></div></div>{_ev_proof(L["proof"], pre)}</section>
<section class="sec wrap"><span class="eyebrow mono">FAQ</span><h2 class="h-lg" style="margin:14px 0 30px">Questions, answered.</h2><div class="faq">{faq}</div></section>
<section class="sec wrap"><span class="eyebrow mono">Keep reading</span>{rel_html(pre)}</section>
{bigcta(pre, h="Let&rsquo;s make it|<span class=grad>unforgettable.</span>", p="Tell us the date, the place and what you need. We will tell you how we would cover it.")}'''
    page(slug + '/', L['title'], L['desc'], body, og=('assets/weddings/w-og.jpg' if L.get('cat') == 'Weddings' else 'assets/img/og.jpg'), extra_ld=ld)
