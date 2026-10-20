# ---------- TERMS (/terms/) ----------
# exec'd by build.py. Adapted from the Partnership Terms on apply.leooperations.com/policies (Landingsite), widened to every Leo service.
# No prices on the site: travel and add-on rates are quoted in each proposal.
TERMS_UPDATED = 'October 20, 2026'
TERMS = [
 ('Overview', ['These terms apply to every service from Leo Operations, LLC: campaign and field programs, media production, photography and videography, design, websites, social media, education services and weddings.',
   'Your signed agreement or proposal sets the scope, schedule and fees for your project. Where your signed agreement differs from these terms, your signed agreement controls. By engaging Leo Operations, clients agree to the terms below.']),
 ('1. Engagement and commitment', ['Work begins once your agreement is signed and the initial payment is received.',
   'Content partnerships run for the term in your agreement: one, three or six months. After the initial term, they continue month to month unless otherwise agreed.',
   'Leo Operations may decline projects that do not fit its service model.']),
 ('2. Payment terms', ['Services are billed as stated in your agreement. Monthly partnerships are billed monthly, in advance.',
   'Payment secures and holds your date or slot. Late payments may pause services or require rescheduling.',
   'We accept bank transfer (ACH or wire) and credit or debit card through our invoicing platform.',
   'All payments are non-refundable once work has begun.']),
 ('3. Billing structure', ['Leo Operations uses package-based pricing that delivers complete creative and strategic solutions rather than line-item services.',
   'Services are billed as flat rates based on the package or proposal you select. We do not provide itemized invoices or breakdowns of individual tasks, hours or deliverables.',
   'Our pricing reflects the full value of strategy, creative direction, production and execution as one service. This lets our team focus on outcomes and execution rather than tracking individual components.']),
 ('4. Scope of services', ['Each agreement defines its scope, which may include strategy, creative direction, graphic design, photography, videography, field operations, and content production and delivery.',
   'Requests outside the agreed scope may be declined or may require an additional fee.',
   'Leo Operations maintains discretion over creative execution to protect quality and consistency.']),
 ('5. Shoot days and production', ['Shoot days are scheduled in advance and coordinated with you.',
   'Delays caused by the client, such as late arrival or an unprepared location, may reduce usable production time.',
   'Additional shoot days beyond your package are billed separately. Weather, location access and other outside conditions may affect production timelines.']),
 ('6. Revisions', ['Each package includes a set number of revisions for minor adjustments.',
   'Major changes, shifts in direction or edits beyond scope may incur additional fees.']),
 ('7. Turnaround times', ['Deliverables follow the schedule in your agreement. Timelines may vary with project complexity and volume.']),
 ('8. Travel', ['Packages include travel within 100 miles of Nashville, Tennessee.',
   'Projects outside that range are billed per shooting day, with driving and air travel rates quoted in your proposal. Rates may be higher in major markets such as Los Angeles, New York and Miami.',
   'Travel fees cover logistics, crew time and production movement.']),
 ('9. Advertising and third-party costs', ['Paid media, advertising spend and third-party platform costs are not included in Leo Operations service fees.',
   'This includes social media advertising (Meta, TikTok, Google and others), connected TV placements (Hulu, Roku, YouTube TV and others), and influencer or platform distribution fees.',
   'Clients fund all media spend directly. Ad strategy and management are available as an additional service.']),
 ('10. Client responsibilities', ['To keep your project on schedule, clients are responsible for timely communication and approvals, access to locations, people and resources, brand assets when needed, and being ready on scheduled shoot days.',
   'Delays caused by a lack of client readiness may affect delivery timelines.']),
 ('11. Creative control', ['Leo Operations keeps creative direction over all deliverables to maintain quality and brand alignment.',
   'Client input is always considered, and final execution decisions are made in the best interest of the project.']),
 ('12. Cancellations and rescheduling', ['Rescheduling a shoot requires advance notice.',
   'Last-minute cancellations may result in the loss of scheduled production time, and repeated rescheduling may affect availability and delivery timelines.']),
 ('13. Availability and communication', ['Leo Operations operates during standard business hours. Responses typically arrive within 24 to 48 hours.']),
 ('14. Intellectual property and usage', ['Upon full payment, clients receive the right to use delivered content for business, campaign and marketing purposes.',
   'Leo Operations keeps the right to use content in its portfolio, marketing and promotion.',
   'Raw files and unused content are not included unless otherwise agreed in writing.']),
 ('15. Limitation of liability', ['Leo Operations is not liable for the performance of outside platforms, such as social media algorithms or ad delivery, or for indirect outcomes such as sales, conversions, enrollment or votes.',
   'Services are provided on the basis of professional expertise and execution.']),
 ('16. Termination', ['Either party may end a content partnership after its initial term with written notice.',
   'No refunds are issued for work already completed or in progress.']),
 ('Questions', ['Email Leo Operations with any question about these terms.']),
]

def terms_page():
    def body(pre):
        btn = mail('rod', 'leooperations.com', 'Email Leo Operations <span class="arr">&rarr;</span>', 'btn ghost', 'Question%20about%20terms')
        prose = ''.join(f'<h2>{E(h)}</h2>' + ''.join(f'<p>{E(p)}</p>' for p in ps) for h, ps in TERMS)
        return (f'<section class="wrap" style="padding-top:clamp(120px,16vh,170px)"><span class="eyebrow mono">Legal</span>'
                f'<h1 class="h-lg" style="margin:16px 0 12px">Terms of Service</h1><p class="mono" style="color:var(--dim);margin-bottom:30px">Updated {TERMS_UPDATED}</p><div class="prose">{prose}</div><p style="margin-top:26px">{btn}</p></section>')
    page('terms/', 'Terms of Service | Leo Operations', 'Payment, billing, scope, travel, usage and cancellation terms for Leo Operations campaign, media, education and wedding services.', body)
