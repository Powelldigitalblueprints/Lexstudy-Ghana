"""Quiz bank for LexStudy Ghana v0.3.2.

Every question is tied to a principle already taught in the notes or
in a cited brief. Answers are indices into options. Explanations are
short, so a wrong answer still teaches.
"""

QUIZZES = {
    "constitutional-law": {
        "title": "Constitutional Law quiz",
        "subject": "Constitutional Law",
        "questions": [
            {
                "q": "Under article 1(2) of the 1992 Constitution, what happens to a law that is inconsistent with the Constitution?",
                "options": ["It is void to the extent of the inconsistency", "It is suspended for one year", "It applies until Parliament repeals it", "It applies only in Accra"],
                "answer": 0,
                "explanation": "Supremacy means inconsistency leads to voidness to the extent of that inconsistency, not to the whole law automatically.",
            },
            {
                "q": "In Tuffour v Attorney-General [1980] GLR 637, how did the Court say the Constitution should be interpreted?",
                "options": ["Narrowly and literally only", "As a living organism, broadly and liberally", "Only by its original 1979 wording", "By Parliament's later view of it"],
                "answer": 1,
                "explanation": "Sowah JSC's celebrated approach: a written constitution is a living organism, requiring a broad and liberal spirit, not a doctrinaire approach.",
            },
            {
                "q": "In the 31 December case, NPP v Attorney-General [1993-94] 2 GLR 35, what did the Court hold about Parliament's power to legislate?",
                "options": ["Parliament may legislate without constitutional limits", "Parliament must legislate within the powers the Constitution confers", "Parliament may not legislate on public holidays at all", "Only the President may limit legislation"],
                "answer": 1,
                "explanation": "Parliament has the right to legislate, but every such law must stay within the parameters of the Constitution.",
            },
            {
                "q": "According to Tuffour, who may invoke the Supreme Court to protect the constitutional order?",
                "options": ["Only a person personally affected", "Only a lawyer", "Any Ghanaian citizen, by citizenship alone", "Only Parliament"],
                "answer": 2,
                "explanation": "Citizenship alone was held sufficient to protect the constitutional order, without a separate personal interest.",
            },
            {
                "q": "In which chapter of the 1992 Constitution are the Directive Principles of State Policy found?",
                "options": ["Chapter 1", "Chapter 5", "Chapter 6", "Chapter 12"],
                "answer": 2,
                "explanation": "Chapter 6 contains the Directive Principles. Their justiciability has evolved in Supreme Court decisions — do not treat them as ordinary enforceable rights without checking the case law.",
            },
            {
                "q": "Article 34(1) says the Directive Principles of State Policy \"shall guide\" whom?",
                "options": ["Only Parliament and the President", "All citizens, Parliament, the President, the Judiciary, the Council of State, the Cabinet, political parties and other bodies and persons", "Only the courts", "Only political parties"],
                "answer": 1,
                "explanation": "Article 34(1) names them all: the Principles guide everyone who applies or interprets the Constitution or any other law, and everyone taking or implementing policy decisions, for the establishment of a just and free society.",
            },
            {
                "q": "Which article of the 1992 Constitution sets out the ECONOMIC objectives of the Directive Principles of State Policy?",
                "options": ["Article 35", "Article 36", "Article 41", "Article 34"],
                "answer": 1,
                "explanation": "Article 35 is political objectives, 36 economic, 37 social, 38 educational, 39 cultural, 40 international relations, 41 duties of a citizen. Article 34 is the guide clause itself.",
            },
            {
                "q": "Under article 91(2), how quickly must the Council of State give advice requested by the President?",
                "options": ["Within 7 days", "Within 14 days", "Not later than 30 days after receipt of the request", "Within 90 days"],
                "answer": 2,
                "explanation": "Article 91(2): the advice \"shall be given not later than thirty days after the receipt of the request from the President or other authority.\"",
            },
            {
                "q": "A constitution is described as \"rigid\" when…",
                "options": ["It can never be changed at all", "It can be changed only by a special procedure, not by an ordinary Act", "It is written in only one language", "It contains no bill of rights"],
                "answer": 1,
                "explanation": "Rigidity is about the amendment procedure. Ghana's Constitution can be changed only through the special procedure in Chapter 25 (articles 289-292) — entrenched provisions by referendum, others by a two-thirds majority at the second and third readings.",
            },
            {
                "q": "Under section 1(2) of the Habeas Corpus Act 1964 (Act 244), who may apply for the writ?",
                "options": ["Only the Attorney-General", "The detained person, a person entitled to custody of the detainee, or a person acting on the detainee's behalf", "Only a relative of the detainee", "Only the detainee personally"],
                "answer": 1,
                "explanation": "Section 1(2) names three classes of applicant: the detained person, a person entitled to custody (for example a parent), and any person acting on the detainee's behalf.",
            },
        ],
    },
    "law-of-contract": {
        "title": "Law of Contract quiz",
        "subject": "Law of Contract",
        "questions": [
            {
                "q": "A shop displays goods in a window with a price tag. In general, is that display an offer or an invitation to treat?",
                "options": ["An offer", "An invitation to treat", "A binding contract", "An acceptance"],
                "answer": 1,
                "explanation": "The display invites customers to make an offer. The shop may accept or refuse that offer.",
            },
            {
                "q": "For a valid acceptance, which of these is generally required?",
                "options": ["It must be in writing", "It must match the offer and be communicated to the offeror", "It must be sent by post", "It must be witnessed"],
                "answer": 1,
                "explanation": "Acceptance must be unqualified, match the offer, and be communicated to the offeror.",
            },
            {
                "q": "Consideration must be sufficient, but need not be:",
                "options": ["Adequate", "Present", "From the promisee", "Real"],
                "answer": 0,
                "explanation": "The classic rule: consideration must be sufficient in law, even if it is not adequate in value.",
            },
            {
                "q": "In a purely domestic or social agreement, what is the usual presumption about intention to create legal relations?",
                "options": ["Intention is presumed", "No intention is presumed", "Intention is irrelevant", "The court always enforces it"],
                "answer": 1,
                "explanation": "Social and domestic agreements are presumed not to be intended as legally binding, unless the facts rebut that presumption.",
            },
            {
                "q": "Which element is missing if there is an offer and acceptance, but no consideration and no intention?",
                "options": ["Formation is still complete", "Formation is incomplete — a contract needs all its elements", "Only damages are missing", "Only the price is missing"],
                "answer": 1,
                "explanation": "Formation needs offer, acceptance, consideration and intention together. Missing elements mean no contract on those facts.",
            },
        ],
    },
    "law-of-tort": {
        "title": "Law of Tort quiz",
        "subject": "Law of Tort",
        "questions": [
            {
                "q": "Negligence is usually structured in which order?",
                "options": ["Damage, duty, breach, causation", "Duty, breach, causation, damage", "Breach, duty, damage, causation", "Causation, duty, breach, damage"],
                "answer": 1,
                "explanation": "Duty, then breach, then causation, then damage. If any step fails, the claim fails.",
            },
            {
                "q": "Breach is judged by the standard of:",
                "options": ["The defendant's best intentions", "The reasonable person in the defendant's position", "The claimant's expectations", "The average expert in every case"],
                "answer": 1,
                "explanation": "The reasonable person in the defendant's position, taking account of relevant circumstances and any special skill.",
            },
            {
                "q": "If causation in fact is proved, what else can still limit recovery?",
                "options": ["Nothing", "Remoteness", "The defendant's wealth", "The claimant's age"],
                "answer": 1,
                "explanation": "Remoteness limits recovery to harm that was reasonably foreseeable, even where factual causation is made out.",
            },
            {
                "q": "What is the usual effect of contributory fault by the claimant in negligence?",
                "options": ["It always defeats the claim", "It reduces damages, rather than defeating the claim", "It increases damages", "It has no effect"],
                "answer": 1,
                "explanation": "Contributory fault usually reduces, rather than defeats, a negligence claim.",
            },
            {
                "q": "Duty of care depends on more than sympathy alone. Which factors are usually considered?",
                "options": ["Foreseeability, proximity and policy", "Wealth, age and location only", "The defendant's job title only", "Whether the claimant is a student"],
                "answer": 0,
                "explanation": "Foreseeability, proximity and policy considerations together shape whether a duty is owed to this claimant.",
            },
        ],
    },
    "legal-system-and-methods": {
        "title": "Legal System and Methods quiz",
        "subject": "Legal System and Methods",
        "questions": [
            {
                "q": "Article 11(1) of the 1992 Constitution lists how many sources of law in Ghana?",
                "options": ["Three", "Four", "Five", "Seven"],
                "answer": 2,
                "explanation": "Five: (a) the Constitution, (b) enactments made by or under Parliament's authority, (c) Orders, Rules and Regulations, (d) the existing law, and (e) the common law.",
            },
            {
                "q": "Under Article 11(7), subsidiary legislation must be laid before Parliament for how long before it matures into law?",
                "options": ["7 sitting days", "14 sitting days", "21 sitting days", "30 sitting days"],
                "answer": 2,
                "explanation": "21 sitting days. That scrutiny period is what turns a delegated instrument into law.",
            },
            {
                "q": "What is the difference between a Constitutional Instrument and a Legislative Instrument?",
                "options": ["A Constitutional Instrument comes from the President and a Legislative Instrument from Parliament", "A Constitutional Instrument draws its power from the Constitution; a Legislative Instrument draws its power from a statute", "A Legislative Instrument is supreme and a Constitutional Instrument is not", "There is no difference — the names are interchangeable"],
                "answer": 1,
                "explanation": "Both are delegated legislation, but the source of the power differs: Constitution for a C.I., statute for an L.I.",
            },
            {
                "q": "What counts as 'the existing law' under Article 11(4)?",
                "options": ["Only Acts passed after 7 January 1993", "The written and unwritten laws of Ghana as they existed immediately before the Constitution came into force", "Only customary law", "Only decisions of the Supreme Court"],
                "answer": 1,
                "explanation": "The law as it stood immediately before 7 January 1993 — including Acts, Decrees and statutory instruments made before that date.",
            },
            {
                "q": "Under Article 11(2), the common law of Ghana comprises which three things?",
                "options": ["The Constitution, Acts of Parliament and subsidiary legislation", "The common law, the doctrines of equity, and customary law", "Common law, civil law and religious law", "Statutes, case law and textbooks"],
                "answer": 1,
                "explanation": "Common law, equity and customary law — including customary law as determined by the Superior Court of Judicature.",
            },
        ],
    },
}


def get_quiz(slug):
    return QUIZZES.get(slug)
