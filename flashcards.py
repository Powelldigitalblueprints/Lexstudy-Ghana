"""Flashcard decks for LexStudy Ghana v0.3.1.

One deck per subject, seeded from the notes, cited briefs and
quiz content already in the app. Cards are study prompts, not
legal advice. Card ids are stable strings: <subject slug>-<n>.
"""

FLASHCARD_DECKS = {
    "legal-system-and-methods": {
        "subject": "Legal System and Methods",
        "cards": [
            {
                "id": "legal-system-and-methods-1",
                "front": "What are the four passes for reading a judgment?",
                "back": "First pass: read the headnote and the catchwords. Second pass: read the facts, issue, ratio and conclusion. Third pass: re-read the reasoning slowly and note each step. Fourth pass: write the rule in your own words and check it against the judgment.",
            },
            {
                "id": "legal-system-and-methods-2",
                "front": "What is the ratio decidendi of a case?",
                "back": "The rule of law the court decides on the facts before it — the part of the decision that binds later courts. It is the rule, not the facts and not the passing remarks.",
            },
            {
                "id": "legal-system-and-methods-3",
                "front": "What does stare decisis require?",
                "back": "Lower courts must follow the decisions of higher courts on the same point of law. A court follows a binding precedent; it may depart from its own earlier decisions only on the narrow grounds the law allows.",
            },
            {
                "id": "legal-system-and-methods-4",
                "front": "When you read a judgment, what must you separate?",
                "back": "The facts from the reasoning, and the rule from the background. Facts tell you what happened; the reasoning tells you why the court held as it did; the ratio tells you the rule for the next case.",
            },
            {
                "id": "legal-system-and-methods-5",
                "front": "Why note the dissenting opinions in a judgment?",
                "back": "A dissent is not the law, but it shows the other side of the argument and often becomes the majority view in a later case. Noting it shows you understood the debate, not just the result.",
            },
            {
                "id": "legal-system-and-methods-6",
                "front": "What are the five sources of law in Ghana under Article 11(1)?",
                "back": "(a) The Constitution; (b) enactments made by or under Parliament's authority; (c) Orders, Rules and Regulations made under a power conferred by the Constitution; (d) the existing law; (e) the common law.",
            },
            {
                "id": "legal-system-and-methods-7",
                "front": "Why is the Constitution listed first among the sources of law?",
                "back": "Because it is supreme. Under Article 1(2), any law inconsistent with the Constitution is void to the extent of the inconsistency — so Parliament legislates only within the Constitution's parameters.",
            },
            {
                "id": "legal-system-and-methods-8",
                "front": "What is an enactment? (Article 295)",
                "back": "An Act of Parliament, a Decree, a Law, a constitutional instrument or a statutory instrument, or any provision of one of those. In practice: statutes — the laws Parliament itself makes.",
            },
            {
                "id": "legal-system-and-methods-9",
                "front": "What is subsidiary legislation, and why does Parliament allow it?",
                "back": "Orders, Rules and Regulations made by a body other than Parliament under a power the Constitution or a statute confers. Parliament cannot sit constantly or legislate every technical detail, so it delegates — but the instrument must lie before Parliament for 21 sitting days (Article 11(7)).",
            },
            {
                "id": "legal-system-and-methods-10",
                "front": "Constitutional Instrument or Legislative Instrument — which draws its power from where?",
                "back": "A Constitutional Instrument draws its power from the Constitution; a Legislative Instrument draws its power from a statute. Both are delegated legislation.",
            },
            {
                "id": "legal-system-and-methods-11",
                "front": "What is 'the existing law'?",
                "back": "The written and unwritten laws of Ghana as they existed immediately before the 1992 Constitution came into force on 7 January 1993 (Article 11(4)) — including laws made before that date but coming into force on or after it.",
            },
            {
                "id": "legal-system-and-methods-12",
                "front": "What does Article 11(6) require when an existing law conflicts with the Constitution?",
                "back": "The existing law is construed with the modifications, adaptations, qualifications and exceptions necessary to bring it into conformity with the Constitution — the offending part is read down, the rest stands.",
            },
            {
                "id": "legal-system-and-methods-13",
                "front": "What is customary law under Article 11(3)?",
                "back": "Rules of law which by custom are applicable to particular communities in Ghana. It is local to the community it comes from — it does not apply throughout Ghana.",
            },
        ],
    },
    "constitutional-law": {
        "subject": "Constitutional Law",
        "cards": [
            {
                "id": "constitutional-law-1",
                "front": "What does article 1(2) of the 1992 Constitution say about laws that conflict with the Constitution?",
                "back": "Any law found to be inconsistent with any provision of the Constitution is, to the extent of the inconsistency, void.",
            },
            {
                "id": "constitutional-law-2",
                "front": "In Tuffour v Attorney-General [1980] GLR 637, how did the Supreme Court say a constitution must be interpreted?",
                "back": "As a living organism, capable of growth and development as the body politic of Ghana itself develops. The court looks to the Constitution itself first, not to foreign cases, when its language is clear.",
            },
            {
                "id": "constitutional-law-3",
                "front": "What did Tuffour v Attorney-General decide about who may bring a constitutional challenge?",
                "back": "A citizen has standing to seek a declaration that a law or act is inconsistent with the Constitution — the enforcement of the Constitution is open to the citizen, not only to the Attorney-General.",
            },
            {
                "id": "constitutional-law-4",
                "front": "What are the Directive Principles of State Policy in Chapter 6 of the 1992 Constitution?",
                "back": "A guide to the organs of state in applying and enforcing the Constitution. They are a statement of the purposes the state is to pursue, and they inform interpretation — the debate is about how far they can be enforced in court.",
            },
            {
                "id": "constitutional-law-5",
                "front": "In NPP v Inspector-General of Police [1993-94] 2 GLR 459, what happened to the police permit regime for assemblies?",
                "back": "The permit provisions of the Public Order Decree, 1972 were held inconsistent with the freedom of assembly in article 21(1)(d) and void. The decision shaped the Public Order Act, 1994, which uses notification rather than permission.",
            },
        ],
    },
    "criminal-law": {
        "subject": "Criminal Law",
        "cards": [
            {
                "id": "criminal-law-1",
                "front": "What two elements must the prosecution prove for murder under the Criminal Offences Act, 1960 (Act 29)?",
                "back": "The act that caused the death (actus reus) and the intention to cause death (mens rea). Act 29 defines murder by the intent; the jury must be satisfied on both.",
            },
            {
                "id": "criminal-law-2",
                "front": "In Sene v The Republic [1977] 1 GLR 434, why did the murder convictions fail?",
                "back": "The trial judge stressed who started the fight, but starting a fight does not show an intention to kill. Intention to cause death is distinct from intention to fight, and the judge also failed to deal with provocation.",
            },
            {
                "id": "criminal-law-3",
                "front": "In Akorful v The State [1963] 2 GLR 371, why was DPP v Smith rejected?",
                "back": "DPP v Smith's objective reasonable-man test is not the law of Ghana. Section 11 of Act 29 turns on the accused's own purpose or belief, so directing the jury on the objective test was a serious misdirection.",
            },
            {
                "id": "criminal-law-4",
                "front": "What does section 11(1) of Act 29 say about intention?",
                "back": "A person acts with intent when he intends to cause the event, or when he believes the event will probably be caused by his act — judged by what he actually intended or believed, not by what a reasonable stranger would have foreseen.",
            },
            {
                "id": "criminal-law-5",
                "front": "If a murder charge fails on intention, what may the court substitute?",
                "back": "Manslaughter, where the evidence supports an unlawful killing without the intention to cause death — as the Court of Appeal did in Sene v The Republic.",
            },
        ],
    },
    "law-of-contract": {
        "subject": "Law of Contract",
        "cards": [
            {
                "id": "law-of-contract-1",
                "front": "In NTHC Ltd v Antwi [2009] SCGLR 117, when is a statement an offer rather than an invitation to treat?",
                "back": "When it is definite and final, leaving no significant term open for further negotiation. The NTHC letter named the house, the price and the payment period, so it was an offer.",
            },
            {
                "id": "law-of-contract-2",
                "front": "In Fofie v Zanyo [1992] 2 GLR 475, why was there no contract?",
                "back": "Acceptance must be plain, unqualified, communicated to the offeror and within a reasonable time. A mere mental acceptance has no effect — and nothing showing acceptance was ever communicated, over ten years.",
            },
            {
                "id": "law-of-contract-3",
                "front": "Is a shop window display an offer or an invitation to treat?",
                "back": "An invitation to treat. The shop invites the customer to make an offer, which the shopkeeper may accept or refuse at the till.",
            },
            {
                "id": "law-of-contract-4",
                "front": "Must consideration be adequate to support a contract?",
                "back": "No. Consideration must be sufficient in law, but it need not be adequate — the courts do not weigh whether the bargain was a good one.",
            },
            {
                "id": "law-of-contract-5",
                "front": "What presumption applies to agreements between husband and wife?",
                "back": "Domestic agreements are presumed not to create legal relations, unless the context shows the parties intended to be legally bound. Commercial agreements carry the opposite presumption.",
            },
        ],
    },
    "law-of-tort": {
        "subject": "Law of Tort",
        "cards": [
            {
                "id": "law-of-tort-1",
                "front": "What are the four steps in a negligence claim?",
                "back": "Duty of care, breach of that duty, causation, and damage. The claimant must prove each one; failing on any one ends the claim.",
            },
            {
                "id": "law-of-tort-2",
                "front": "How is breach of duty judged in negligence?",
                "back": "By the standard of the reasonable person in the defendant's position. The question is whether the defendant fell below what a reasonable person would have done in the same circumstances.",
            },
            {
                "id": "law-of-tort-3",
                "front": "In Kotokoli v Moro Hausa [1967] GLR 298, to whom is a duty of care owed?",
                "back": "To persons who might reasonably be anticipated as likely to be injured by the conduct in question — not to the world at large. The pleaded negligence in the seating was not proved.",
            },
            {
                "id": "law-of-tort-4",
                "front": "In Asantekramo v Attorney-General [1975] 1 GLR 319, what did res ipsa loquitur do?",
                "back": "The facts — a healthy arm gangrenous after a transfusion — spoke for themselves and called for an explanation. The 'mystery' explanation did not displace the inference of negligence, and the State was held liable.",
            },
            {
                "id": "law-of-tort-5",
                "front": "What is the effect of contributory fault in a negligence claim?",
                "back": "The claimant's own fault in contributing to the harm reduces the damages awarded, rather than defeating the claim altogether.",
            },
        ],
    },
    "land-law": {
        "subject": "Land Law",
        "cards": [
            {
                "id": "land-law-1",
                "front": "In Manu v Ainoo [1976] 1 GLR 457, what interest does a customary tenant acquire?",
                "back": "Only the right to cultivate the land and share in the proceeds. The tenancy is created in respect of the share of proceeds only, not the land, so ownership remains with the landlord.",
            },
            {
                "id": "land-law-2",
                "front": "What is allodial title in Ghanaian land law?",
                "back": "The highest interest in land, held by a stool, skin, clan or family. It is the root from which all other interests in the land are derived.",
            },
            {
                "id": "land-law-3",
                "front": "How do abusa and abunu share tenancies divide the farm proceeds?",
                "back": "Under abusa the landlord takes one-third and the tenant two-thirds; under abunu the proceeds are shared equally, half and half.",
            },
            {
                "id": "land-law-4",
                "front": "Can a landlord unilaterally annul a customary tenancy?",
                "back": "No. Forfeiture is sparingly exercised: there must be the clearest indication for it, and the defaulter must have every opportunity to explain or mend their ways (Manu v Ainoo).",
            },
            {
                "id": "land-law-5",
                "front": "What is the first step in answering a Ghana land problem?",
                "back": "Identify the interest each party holds — allodial title, customary freehold, leasehold, tenancy or a mere licence — before deciding what any of them can do with the land.",
            },
        ],
    },
    "public-international-law": {
        "subject": "Public International Law",
        "cards": [
            {
                "id": "public-international-law-1",
                "front": "What are the main sources of international law under article 38 of the ICJ Statute?",
                "back": "Treaties, customary international law, general principles of law recognised by civilised nations, and — as subsidiary means — judicial decisions and the teachings of highly qualified publicists.",
            },
            {
                "id": "public-international-law-2",
                "front": "What two elements make up customary international law?",
                "back": "General state practice, and opinio juris — the belief that the practice is required by law. Practice without the sense of legal obligation is only usage.",
            },
            {
                "id": "public-international-law-3",
                "front": "Whom does a treaty bind?",
                "back": "The parties to it. A treaty does not create obligations for a third state without that state's consent — pacta tertiis nec nocent nec prosunt.",
            },
            {
                "id": "public-international-law-4",
                "front": "Does an international treaty automatically become part of Ghanaian domestic law?",
                "back": "No. Ghana follows the dualist approach: a treaty needs domestic legislation before it takes effect as domestic law. Do not assume direct effect.",
            },
            {
                "id": "public-international-law-5",
                "front": "What is the first step in answering a public international law problem?",
                "back": "Identify the source of the rule you rely on — treaty, custom or general principle — and then show why it binds the state in question.",
            },
        ],
    },
    "equity-and-trusts": {
        "subject": "Equity and Trusts",
        "cards": [
            {
                "id": "equity-and-trusts-1",
                "front": "What are the three certainties needed to create a trust?",
                "back": "Certainty of intention (imperative words), certainty of subject matter (definite property), and certainty of objects (identifiable beneficiaries) — restated in Cofie v Forson [1992] 1 GLR 312.",
            },
            {
                "id": "equity-and-trusts-2",
                "front": "In Cofie v Forson [1992] 1 GLR 312, why was an express trust created?",
                "back": "The statutory declaration used trust words without doubt, the property was definite, and the beneficiaries were named. Nothing was ambiguous about the intention, the property or the objects.",
            },
            {
                "id": "equity-and-trusts-3",
                "front": "What happens if any of the three certainties fails?",
                "back": "No trust is created. The property does not pass on trust, and the intended arrangement fails as a trust, whatever the settlor may have wished.",
            },
            {
                "id": "equity-and-trusts-4",
                "front": "Who holds legal title and who holds the equitable interest under a trust?",
                "back": "The trustee holds the legal title; the beneficiary holds the equitable interest. The trustee must administer the property for the beneficiary's benefit.",
            },
            {
                "id": "equity-and-trusts-5",
                "front": "How is the intention to create a trust judged?",
                "back": "Objectively, from the words used and the circumstances. The question is whether the words, fairly read, show an intention to impose a trust — not what the settlor privately hoped.",
            },
        ],
    },
}


def get_deck(slug):
    return FLASHCARD_DECKS.get(slug)


def all_cards():
    cards = []
    for slug, deck in FLASHCARD_DECKS.items():
        for card in deck["cards"]:
            cards.append({"deck_slug": slug, **card})
    return cards
