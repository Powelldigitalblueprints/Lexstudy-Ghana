"""Quiz bank for LexStudy Ghana v0.2.

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
}


def get_quiz(slug):
    return QUIZZES.get(slug)
