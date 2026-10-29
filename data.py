"""Seed content for LexStudy Ghana v0.1.

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
            }
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
        "features": ["Everything in Free", "Quizzes and IRAC practice (coming in v0.2)", "Saved notes and revision progress (coming in v0.2)"],
        "cta": "Payments not yet connected",
    },
    {
        "name": "Annual",
        "price": "Price to be confirmed",
        "period": "per year",
        "features": ["Everything in Monthly", "Full revision tools (coming in v0.2)", "Best value for a full academic year"],
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
