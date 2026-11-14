"""Seed content for LexStudy Ghana v0.3.2.

Important: the case briefs in this file are PRACTICE briefs built on
hypothetical facts for teaching IRAC. They are not reports of real
judgments and must never be cited as cases. Real case briefs added
later must be checked against the authoritative judgment first.
"""

SUBJECTS = [
    {
        "slug": "legal-system-and-methods",
        "name": "Legal System and Methods",
        "level": "Foundation",
        "description": "How Ghanaian law is made, found and applied: sources of law, courts, and how to read a judgment.",
        "topics": ["Sources of law in Ghana", "The court hierarchy", "Reading a judgment", "Precedent and stare decisis", "Legal reasoning"],
        "notes": [
            {
                "title": "Start here: reading a judgment in four passes",
                "summary": "First pass: who are the parties and what was decided? Second: what facts mattered? Third: what rule did the court apply? Fourth: why did that rule decide this case?",
                "points": ["Separate the facts from the court's reasoning.", "Find the ratio decidendi, not just the outcome.", "Note any dissent or distinguishing facts for later revision."],
            },
            {
                "title": "Sources of law in Ghana: Article 11",
                "summary": "Article 11 of the 1992 Constitution lists the five sources of Ghanaian law, in order: the Constitution itself, Acts of Parliament, subsidiary legislation, the existing law, and the common law — which includes equity and customary law. If you can place a rule in one of those five boxes, you can say where it comes from and how strong it is.",
                "points": [
                    "The Constitution is supreme: any law inconsistent with it is void to the extent of the inconsistency (Article 1(2)). Parliament is therefore not supreme — it legislates only within the Constitution's parameters.",
                    "Enactments (Article 11(1)(b)) are Acts of Parliament and laws made under Parliament's authority. A Bill becomes an Act after Parliament approves it and the President assents; Article 106 sets out the procedure and Article 107 bars retrospective criminal law.",
                    "Subsidiary legislation (Article 11(1)(c)) is Orders, Rules and Regulations made by a person or authority under a power conferred by the Constitution — because Parliament cannot legislate for every technical detail itself. It must be laid before Parliament for 21 sitting days (Article 11(7)) before it matures into law.",
                    "A Constitutional Instrument draws its power from the Constitution; a Legislative Instrument draws its power from a statute. An Executive Instrument is not legislative in nature and is not subsidiary legislation.",
                    "The existing law (Article 11(4)–(6)) is the written and unwritten law in force immediately before the Constitution came into force on 7 January 1993. It survives, but it must be read with whatever modifications bring it into conformity with the Constitution.",
                    "The common law of Ghana (Article 11(2)) comprises the common law, the doctrines of equity, and customary law, including customary law as determined by the Superior Court of Judicature. Customary law (Article 11(3)) means rules of law which by custom apply to particular communities in Ghana — it is local, not national.",
                ],
            },
        ],
    },
    {
        "slug": "constitutional-law",
        "name": "Constitutional Law",
        "level": "Core",
        "description": "The 1992 Constitution, supremacy, fundamental rights, and the structure of government in Ghana.",
        "topics": ["Supremacy of the Constitution", "Fundamental human rights", "Separation of powers", "Judicial review", "Amendment"],
        "notes": [
            {
                "title": "Supremacy: why the Constitution comes first",
                "summary": "A law or action inconsistent with the Constitution is, to the extent of the inconsistency, void. That is the starting point for most constitutional problem questions.",
                "points": ["Identify the constitutional provision first, then the challenged law or act.", "Ask what inconsistency is actually alleged, not just that one exists.", "Remedies and standing still matter: who can bring the claim, and in which court?"],
            },
            {
                "title": "What is a constitution? Written, supreme and rigid",
                "summary": "A constitution is the fundamental law that creates government, defines its powers and limits them. Ghana's 1992 Constitution is a single written document, supreme over all other law, and changeable only by the special procedure in Chapter 25.",
                "points": [
                    "In the wider sense, a constitution means the rules that determine how governmental institutions are created and operate — every country has such rules, whether or not they sit in one document (Jennings, as presented in the source notes). In the narrower sense, the word describes a selection of those rules embodied in one document or a few closely related documents (Wheare, as presented in the source notes).",
                    "A constitution comes before government: government is the constitution's creation, not the other way round. On Paine's argument, as presented in the source notes, a government without a constitution is power without right.",
                    "Ghana's 1992 Constitution is a written constitution: the framework of government sits in a single document, which came into force on 7 January 1993 (as presented in the source notes). An unwritten constitution, like the United Kingdom's, is spread across statutes, conventions and other documents, with Parliament supreme.",
                    "The Constitution is supreme: \"This Constitution shall be the supreme law of Ghana and any other law found to be inconsistent with any provision of this Constitution shall, to the extent of the inconsistency, be void.\" (article 1(2)). Sovereignty resides in the people of Ghana, in whose name and for whose welfare the powers of government are exercised (article 1(1)).",
                    "The Constitution creates the three arms of government — the executive (Chapter 8), the legislature (Chapter 9) and the judiciary (Chapter 11) — and sets the limits of each. Their authority derives from the Constitution itself; in Tuffour's words, as quoted in the source notes, the Constitution is the fountain-head for the authority which each of the three arms of government possesses and exercises (Tuffour v Attorney-General [1980] GLR 637).",
                    "A constitution is an instrument of rights and limitations, not a catalogue of powers: it confers limited, regulated powers, and a body that exceeds them acts beyond its authority and may be challenged before the Supreme Court (articles 2 and 130).",
                    "Ghana's Constitution is written, unitary and republican (as presented in the source notes; article 4: Ghana is a unitary Republic). The President is Head of State, Head of Government and Commander-in-Chief of the Armed Forces (article 57(1)), and there is a single Parliament (article 93). It is rigid: it can be changed only by the special amendment procedure in Chapter 25 (articles 289-292), not by an ordinary Act — entrenched provisions require a referendum, and non-entrenched provisions require a two-thirds majority at the second and third readings (as presented in the source notes).",
                    "The Constitution embraces the doctrines of separation of powers, checks and balances, the rule of law, judicial review, fundamental human rights (Chapter 5), constitutionalism and supremacy (as presented in the source notes). Suspending, overthrowing or abrogating the Constitution by violent or unlawful means is high treason (article 3(3)).",
                ],
            },
            {
                "title": "The Directive Principles of State Policy: guides, and are they enforceable?",
                "summary": "Chapter 6 sets out the objectives that must guide everyone who applies the Constitution or makes policy. Whether a court can enforce those objectives directly has divided the Supreme Court. This note presents the three positions recorded in the source notes side by side, without settling the question.",
                "points": [
                    "\"The Directive Principles of State Policy contained in this Chapter shall guide all citizens, Parliament, the President, the Judiciary, the Council of State, the Cabinet, political parties and other bodies and persons in applying or interpreting this Constitution or any other law and in taking and implementing any policy decisions, for the establishment of a just and free society.\" (article 34(1)). The President must report to Parliament at least once a year on the steps taken to realise these objectives (article 34(2)).",
                    "Chapter 6 is organised article by article: article 35 political objectives; article 36 economic objectives; article 37 social objectives; article 38 educational objectives; article 39 cultural objectives; article 40 international relations; article 41 duties of a citizen — including the duty to uphold and defend the Constitution and the law (article 41(b)).",
                    "Two distinct questions must not be confused. First, can the Directive Principles be used as an aid to interpreting the Constitution and other laws? Second, can a court enforce them directly? The source notes record broad agreement on the first question and division on the second. Justiciable means appropriate for adjudication by a court (as presented in the source notes).",
                    "As an aid to interpretation: where two readings of a provision are possible, the court should prefer the reading consistent with the Directive Principles (as presented in the source notes). The notes record that in NPP v Inspector-General of Police the Court took the article 35 political objectives into account when construing the freedom of assembly in article 21(1)(d) — that point comes from the source notes, not from the verified brief, which records the permit-regime holding.",
                    "Position 1 — the whole Constitution is justiciable (31 December case, Adade JSC, as presented in the source notes): Chapter 6 included, because articles 1 and 2 make any inconsistent law or act void, and if any part of the Constitution were non-justiciable the Constitution itself would have to say so. Evidence for non-justiciability must come from inside the Constitution, not from outside it.",
                    "Position 2 — a mixed bag (CIBA case, 4-1, as presented in the source notes; the reported judgment has not been checked for this site): the Principles provide goals for legislative programmes and a guide for judicial interpretation, and are not of themselves legally enforceable. A principle is justiciable where it is also stated as a substantive right elsewhere in the Constitution (for example in Chapter 5); a principle found only in Chapter 6, such as the article 36 economic objectives, is a policy guideline and a standard for measuring government performance.",
                    "Position 3 — a presumption of justiciability (Ghana Lotto Operators Association v National Lottery Authority, as presented in the source notes; the reported judgment has not been checked for this site): Chapter 6 provisions are presumed enforceable unless the particular principle does not lend itself to enforcement by the courts. On this view article 36(2)(b) is justiciable, and legislation flagrantly at odds with the article 36 objectives may be struck down. The Court treated the Consultative Assembly's rejection of the Committee of Experts' proposal (Report, paragraph 95) that the Principles should not be enforceable as a pointer in favour of justiciability.",
                    "For study purposes, argue all three positions and say which facts of the problem favour each. Do not present any one of them as settled without checking the reported judgments: the source notes call the third position authoritative, and this note deliberately does not adopt that.",
                ],
            },
            {
                "title": "The Council of State: consultation is mandatory, advice is not binding",
                "summary": "The President must seek the Council of State's advice, or consult it, before performing many constitutional functions — but, on the position presented in the source notes, the advice does not bind him. The distinction between \"in consultation with\", \"on the advice of\" and \"acting in accordance with the advice of\" is the heart of the topic.",
                "points": [
                    "Article 89: there shall be a Council of State to counsel the President in the performance of his functions. Article 91(1): the Council considers and advises on appointments required to be made in accordance with its advice or in consultation with it. Article 91(2): the advice must be given not later than thirty days after receipt of the request. Article 91(3): the President, a Minister, Parliament or another authority \"shall not be required to act in accordance with any recommendation\" made by the Council under that clause.",
                    "Three phrasings, three strengths (as presented in the source notes). \"In consultation with\" — ask and consider: article 70(1) appointments (including the Auditor-General, the Commissioner for Human Rights and Administrative Justice and the District Assemblies Common Fund Administrator), the prerogative of mercy (article 72), diplomatic representation (article 74), the Chief Justice (article 144(1), with Parliament's approval), and the Governor of the Bank of Ghana (article 183(4), four-year terms). \"On the advice of\" — a stronger restraint: Electoral Commission appointments (article 70(2)), and Supreme Court Justices on the advice of the Judicial Council (article 144(2)). \"Acting in accordance with the advice of\" — the strongest wording: creation, alteration or merger of regions (article 5(2)), declaration of a state of emergency (article 31(1)), and suspension of the Chief Justice during removal proceedings (article 146(10)).",
                    "The notes' position: the duty to seek the advice or consultation is mandatory — an appointment or act made without it is not valid. But the advice itself is not binding on the President, whatever the phrasing. The notes record the Supreme Court holding this in Ghana Bar Association v Attorney-General and the Judicial Council (20 July 2016), as presented in the source notes; the reported judgment has not been checked for this site. Whether 'on the advice of' in article 70(2) binds the President has itself been debated; this note records the source notes' position without settling that debate. The reasoning recorded is that binding advice would mean the Council was effectively performing the President's functions while accountability stayed with the President, who is directly elected by the people.",
                    "The notes' further argument, presented as the notes author's position and not as a verified holding: the President cannot go outside the names recommended to him — a person appointed as a Justice must be among those recommended, even though the President need not appoint any particular recommended person.",
                    "Other instances where the Council's role arises: the President may refer a bill passed by Parliament to the Council of State for advice under article 90; assent to a bill must be signified within seven days unless the bill was referred under article 90 (article 106(7)); the Council may advise that a commission of inquiry is in the public interest (article 278(1)(b)); a bill to amend an entrenched provision must be referred by the Speaker to the Council of State for its advice before Parliament considers it, and the Council renders its advice within thirty days (article 290(2), as presented in the source notes); presidential staff are appointed in consultation with the Council (Presidential Office Act 1993 (Act 463), section 4(1)).",
                    "Composition (article 89, as presented in the source notes): a person who previously held office as Chief Justice, a person who previously held office as Chief of Defence Staff, a person who previously held office as Inspector-General of Police, the President of the National House of Chiefs, one representative from each region, and eleven other members appointed by the President. The Council elects a Chairman from among its members.",
                ],
            }
        ],
    },
    {
        "slug": "criminal-law",
        "name": "Criminal Law",
        "level": "Core",
        "description": "Offences, actus reus and mens rea, defences, and how Ghanaian criminal liability is built up element by element.",
        "topics": ["Actus reus and mens rea", "Causation", "Murder and manslaughter", "Defences", "Inchoate offences"],
        "notes": [
            {
                "title": "Build liability element by element",
                "summary": "Do not jump to a conclusion. Work through actus reus, mens rea, causation and any defence, in that order, and say what is missing if an element fails.",
                "points": ["State the offence and its elements before applying facts.", "Causation needs both factual and legal causation.", "A defence is not an afterthought: it can defeat liability even where the elements are present."],
            }
        ],
    },
    {
        "slug": "law-of-contract",
        "name": "Law of Contract",
        "level": "Core",
        "description": "Formation, terms, vitiating factors, discharge and remedies: the rules that make an agreement enforceable.",
        "topics": ["Offer and acceptance", "Consideration and intention", "Terms and interpretation", "Misrepresentation and mistake", "Breach and remedies"],
        "notes": [
            {
                "title": "Formation: offer, acceptance, consideration, intention",
                "summary": "Most formation questions are won or lost on small facts: was there a definite offer, an unqualified acceptance, communicated to the offeror, supported by consideration, with intention to create legal relations?",
                "points": ["An invitation to treat is not an offer.", "Acceptance must match the offer and be communicated.", "Consideration must be sufficient, even if it need not be adequate."],
            }
        ],
    },
    {
        "slug": "law-of-tort",
        "name": "Law of Tort",
        "level": "Core",
        "description": "Negligence, nuisance, defamation and other civil wrongs, and when a duty is owed to a particular claimant.",
        "topics": ["Duty of care", "Breach and standard of care", "Causation and remoteness", "Defences", "Nuisance and defamation"],
        "notes": [
            {
                "title": "Negligence in four steps",
                "summary": "Duty, breach, causation, damage. If any step fails, the claim fails, so structure your answer around the weakest step, not just the strongest.",
                "points": ["Duty depends on foreseeability, proximity and policy, not sympathy alone.", "Breach is judged by the reasonable person in the defendant's position.", "Remoteness limits recovery even where causation in fact is made out."],
            }
        ],
    },
    {
        "slug": "land-law",
        "name": "Land Law",
        "level": "Core",
        "description": "Interests in land in Ghana, customary land, title, and how competing claims are resolved.",
        "topics": ["Customary land tenure", "Interests and estates", "Title and registration", "Competing interests", "Mortgages and leases"],
        "notes": [
            {
                "title": "Start with the interest, not the dispute",
                "summary": "Ask first what interest each party claims, how it was created, and whether it binds the other party. The dispute usually answers itself once the interests are clear.",
                "points": ["Customary and statutory interests can coexist and conflict.", "Registration and notice affect priority, but do not replace the underlying interest.", "Always check who had capacity to grant the interest claimed."],
            }
        ],
    },
    {
        "slug": "public-international-law",
        "name": "Public International Law",
        "level": "Core",
        "description": "Sources of international law, state responsibility, jurisdiction, and how international law relates to domestic law.",
        "topics": ["Sources: treaties, custom, general principles", "Statehood and recognition", "Jurisdiction and immunity", "State responsibility", "International courts"],
        "notes": [
            {
                "title": "Sources first, then the rule",
                "summary": "International law problem questions usually turn on which source creates the obligation: a treaty binding the parties, a rule of customary law, or a general principle.",
                "points": ["A treaty binds its parties; custom needs practice plus opinio juris.", "Distinguish a binding obligation from a political commitment.", "Domestic effect depends on the receiving system, so do not assume direct application."],
            }
        ],
    },
    {
        "slug": "equity-and-trusts",
        "name": "Equity and Trusts",
        "level": "Core",
        "description": "Equitable principles, the creation of trusts, trustees' duties, and equitable remedies.",
        "topics": ["Creation of trusts", "Certainties", "Trustees' duties", "Breach of trust", "Equitable remedies"],
        "notes": [
            {
                "title": "The three certainties",
                "summary": "A trust needs certainty of intention, subject matter and objects. If any certainty fails, there is no trust, however sympathetic the facts.",
                "points": ["Intention is judged objectively from words and conduct.", "Subject matter must be identifiable property.", "Objects must be certain enough for the trust to be administered."],
            }
        ],
    },
]

CASES = [
    {
        "slug": "sample-constitutional-brief",
        "title": "Practice brief: a constitutional supremacy question",
        "subject": "Constitutional Law",
        "kind": "PRACTICE BRIEF — hypothetical facts, not a real judgment",
        "facts": "Hypothetical: Parliament passes a statute that restricts a right protected by the Constitution. A citizen challenges the statute as inconsistent with the Constitution.",
        "issue": "Is the statute, to the extent of the inconsistency, void for inconsistency with the Constitution?",
        "rule": "The Constitution is supreme. A law inconsistent with it is void to the extent of the inconsistency.",
        "application": "Apply the constitutional provision to the statute section by section. A general complaint is not enough: identify the exact conflict, then consider whether the statute can be read consistently with the Constitution.",
        "conclusion": "If the conflict is real and cannot be reconciled, the inconsistent part fails. If it can be reconciled, the statute stands.",
        "principle": "Start from the constitutional text, then the challenged law — never the other way round.",
    },
    {
        "slug": "sample-contract-brief",
        "title": "Practice brief: offer or invitation to treat?",
        "subject": "Law of Contract",
        "kind": "PRACTICE BRIEF — hypothetical facts, not a real judgment",
        "facts": "Hypothetical: A shop displays goods in a window with a price tag. A customer says they accept the price and demands the goods. The shop refuses to sell.",
        "issue": "Was the display an offer that the customer accepted, or an invitation to treat?",
        "rule": "A display of goods is generally an invitation to treat, not an offer. The customer makes the offer; the shop may accept or refuse it.",
        "application": "Apply the general rule to these facts, then test the exceptions: did anything in the display amount to a definite promise to sell to anyone who accepted? On these bare facts, no.",
        "conclusion": "No contract was formed by the display alone. The customer's statement was an offer, which the shop was entitled to refuse.",
        "principle": "Formation questions turn on who made the offer — get that right first.",
    },
    {
        "slug": "sample-criminal-brief",
        "title": "Practice brief: actus reus without mens rea",
        "subject": "Criminal Law",
        "kind": "PRACTICE BRIEF — hypothetical facts, not a real judgment",
        "facts": "Hypothetical: A person causes harm while genuinely believing, on reasonable grounds, that the facts were different from what they were.",
        "issue": "Does liability follow from the harmful act alone, or must the required mental element also be proved?",
        "rule": "For most offences, both actus reus and mens rea must coincide. A genuine mistake of fact can negate mens rea where it removes the required mental element.",
        "application": "Identify the offence and its mental element first. Then ask whether, on the facts as the defendant believed them, that element is present. Do not assume intention from outcome alone.",
        "conclusion": "If mens rea is not proved, liability for that offence fails, even though harm occurred. A different offence with a lower mental element may still need to be considered.",
        "principle": "Harm alone is not guilt. Prove the mental element too.",
    },
    {
        "slug": "sample-tort-brief",
        "title": "Practice brief: duty, breach, causation",
        "subject": "Law of Tort",
        "kind": "PRACTICE BRIEF — hypothetical facts, not a real judgment",
        "facts": "Hypothetical: A driver, rushing to an appointment, fails to keep a proper lookout and collides with a pedestrian who was crossing lawfully.",
        "issue": "Is the driver liable in negligence to the pedestrian?",
        "rule": "Negligence requires duty, breach, causation and damage. A road user owes a duty of care to other road users.",
        "application": "Duty is straightforward here. Breach turns on the reasonable driver, not on how urgent the appointment was. Causation asks whether, but for the failure to keep lookout, the collision would have been avoided, and whether the harm was reasonably foreseeable.",
        "conclusion": "On these facts, duty, breach and causation are all made out, subject to any contributory fault by the pedestrian, which would reduce rather than defeat the claim.",
        "principle": "Structure negligence answers duty → breach → causation → damage, and spend time on the weakest link.",
    },
]

PLANS = [
    {
        "name": "Free",
        "price": "Free at launch",
        "period": "",
        "features": ["Browse subjects and study notes", "Practice case briefs", "Search the library"],
        "cta": "Browse free",
    },
    {
        "name": "Monthly",
        "price": "Price to be confirmed",
        "period": "per month",
        "features": ["Everything in Free", "Quizzes, IRAC practice, flashcards and timed mocks", "Saved bookmarks and revision progress"],
        "cta": "Payments not yet connected",
    },
    {
        "name": "Annual",
        "price": "Price to be confirmed",
        "period": "per year",
        "features": ["Everything in Monthly", "Full revision tools", "Best value for a full academic year"],
        "cta": "Payments not yet connected",
    },
]


def get_subject(slug):
    return next((s for s in SUBJECTS if s["slug"] == slug), None)


def get_case(slug):
    return next((c for c in CASES if c["slug"] == slug), None)


def search(query):
    q = query.strip().lower()
    if not q:
        return [], []
    subjects = [
        s for s in SUBJECTS
        if q in s["name"].lower() or q in s["description"].lower()
        or any(q in t.lower() for t in s["topics"])
        or any(q in n["title"].lower() or q in n["summary"].lower() for n in s["notes"])
    ]
    cases = [
        c for c in CASES
        if q in c["title"].lower() or q in c["subject"].lower()
        or q in c["issue"].lower() or q in c["principle"].lower()
    ]
    return subjects, cases
