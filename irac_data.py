"""IRAC practice scenarios for LexStudy Ghana v0.3.3.

Scenarios are hypothetical unless stated otherwise. Model answers are
teaching models, not court judgments. Students write their own IRAC,
then compare it with the model and the self-check list.
"""

SCENARIOS = {
    "constitutional-supremacy": {
        "title": "A statute that restricts a constitutional right",
        "subject": "Constitutional Law",
        "kind": "HYPOTHETICAL",
        "facts": "Hypothetical: Parliament passes a statute that restricts a right protected by the 1992 Constitution. A citizen challenges the statute as inconsistent with the Constitution.",
        "model_issue": "Is the statute, to the extent of any inconsistency, void under article 1(2) of the 1992 Constitution?",
        "model_rule": "The Constitution is supreme. A law inconsistent with it is void to the extent of the inconsistency. Parliament must legislate within the powers the Constitution confers (see NPP v Attorney-General [1993-94] 2 GLR 35).",
        "model_application": "Identify the constitutional provision first, then the exact section of the statute said to conflict with it. Ask whether the statute can be read consistently with the Constitution. A general complaint is not enough: the conflict must be pinpointed section by section.",
        "model_conclusion": "If a real, irreconcilable conflict is proved, the inconsistent part fails. If the statute can be reconciled with the Constitution, it stands.",
        "checklist": ["Did you name the constitutional provision?", "Did you pinpoint the exact conflicting section?", "Did you test whether a consistent reading is possible?", "Did you limit the conclusion to the extent of the inconsistency?"],
    },
    "contract-display": {
        "title": "Offer or invitation to treat?",
        "subject": "Law of Contract",
        "kind": "HYPOTHETICAL",
        "facts": "Hypothetical: A shop displays goods in a window with a price tag. A customer says they accept the price and demands the goods. The shop refuses to sell.",
        "model_issue": "Was the display an offer that the customer accepted, or an invitation to treat?",
        "model_rule": "A display of goods is generally an invitation to treat, not an offer. The customer makes the offer; the shop may accept or refuse it.",
        "model_application": "Apply the general rule, then test exceptions: did anything in the display amount to a definite promise to sell to anyone who accepted? On these bare facts, no. The customer's statement was the offer.",
        "model_conclusion": "No contract was formed by the display alone. The shop was entitled to refuse the customer's offer.",
        "checklist": ["Did you say who made the offer first?", "Did you apply the invitation-to-treat rule?", "Did you test for an exception on these facts?", "Did you state the result for this customer, not for shops in general?"],
    },
    "tort-driver": {
        "title": "Duty, breach and causation on the road",
        "subject": "Law of Tort",
        "kind": "HYPOTHETICAL",
        "facts": "Hypothetical: A driver, rushing to an appointment, fails to keep a proper lookout and collides with a pedestrian who was crossing lawfully.",
        "model_issue": "Is the driver liable in negligence to the pedestrian?",
        "model_rule": "Negligence requires duty, breach, causation and damage. A road user owes a duty of care to other road users.",
        "model_application": "Duty is straightforward. Breach turns on the reasonable driver, not on how urgent the appointment was. Causation asks whether, but for the failure to keep lookout, the collision would have been avoided, and whether the harm was reasonably foreseeable.",
        "model_conclusion": "On these facts, duty, breach and causation are made out, subject to any contributory fault by the pedestrian, which would reduce rather than defeat the claim.",
        "checklist": ["Did you work duty, breach, causation and damage in order?", "Did you judge breach by the reasonable driver, not by urgency?", "Did you address factual and legal causation?", "Did you consider contributory fault separately?"],
    },
    "habeas-corpus-detention": {
        "title": "A detention with no charge and no court order",
        "subject": "Constitutional Law",
        "kind": "HYPOTHETICAL",
        "facts": "Hypothetical: Ama Serwaa is arrested by the police on a Monday morning and held at a police station. By Friday she has not been charged, has not been brought before any court, and no one has shown her family any court order authorising the detention. Her brother, Kwame Serwaa, who has not been allowed to see her, applies to the High Court for a writ of habeas corpus under the Habeas Corpus Act 1964 (Act 244), supported by an affidavit stating the facts of the detention, the place of detention, and that no lawful justification has been shown. The police oppose the application, saying Kwame has no authority from Ama to act for her.",
        "model_issue": "Should the High Court issue a writ of habeas corpus requiring Ama to be brought before the court so the lawfulness of her detention can be tested — and can Kwame, who has not seen Ama, bring the application?",
        "model_rule": "Habeas corpus challenges the validity of a person's detention, whether in public or private custody. The right to apply exists at common law and is confirmed and regulated by the Habeas Corpus Act 1964 (Act 244). Under section 1(2), the detained person, a person entitled to custody of the detainee, or a person acting on the detainee's behalf may apply. The application is usually made ex parte under Order 56 of the High Court (Civil Procedure) Rules, 2004 (C.I. 47), supported by an affidavit stating the facts of the detention, who detains the person, the place of detention, and the grounds for saying the detention is unlawful. The writ is granted where there is a detention or restraint of liberty and no justification in law for it.",
        "model_application": "First, there is a detention: five days in police custody. Second, no justification in law has been shown — no charge, no court appearance, no order produced. Third, Kwame applies as a person acting on Ama's behalf under section 1(2), and the affidavit covers the facts, the place and the grounds. The objection is authority: Kwame has no express authority from Ama. On the slides' account of Republic v Director of Prisons; Ex parte Oduro [1979] GLR 354 — as presented in the source slides; the reported judgment has not been checked for this site — a person acting on the detainee's behalf must show authority from the detainee or prove that obtaining instructions was prevented. Here access to Ama was denied, which is the very circumstance the slides say excuses the lack of authority. The police must therefore justify the detention; the court tests lawfulness, it does not retry any underlying allegation.",
        "model_conclusion": "On these hypothetical facts, the writ should issue: the detention is unexplained, and Kwame's application is properly before the court because access to Ama was denied. If the police then produce lawful authority for the detention, the writ is discharged; if they cannot, Ama must be released.",
        "checklist": ["Identify the detention and who holds the detainee.", "State the Act 244 / Order 56 route and what the affidavit must contain.", "Deal with the applicant's standing under section 1(2) — including the authority point and the denied-access excuse.", "Put the burden on the detainer to justify the detention.", "Conclude with the two outcomes: lawful authority produced, or release."],
    },
    "suspended-student": {
        "title": "The suspended student: fair hearing, bias and a 'final' clause",
        "subject": "Legal System and Methods",
        "kind": "HYPOTHETICAL",
        "facts": "Efua Mensah is a final-year student at a public university in Ghana. After an examination, the university's disciplinary committee suspends her for two semesters for alleged examination malpractice. Efua receives no notice of the charge, is not shown the evidence against her, and is given no hearing and no opportunity to respond. The committee is chaired by Dr Owusu, who had told colleagues before the hearing that Efua 'definitely cheated' and should be made an example of. The university's regulations provide that decisions of the disciplinary committee 'shall be final and shall not be questioned in any court'. Efua applies to the High Court for an order quashing the suspension. The facts are invented; no real person or institution is referred to.",
        "model_issue": "Whether the High Court can quash the suspension: (1) whether the committee's procedure breached natural justice; (2) whether the chairman's prior statements disqualified him for bias; (3) whether the 'final' clause bars the High Court from intervening; and (4) what remedy is available and within what time.",
        "model_rule": "Article 23 of the Constitution requires administrative bodies and officials to act fairly and reasonably and gives persons aggrieved by their acts the right to seek redress before a court or tribunal. Natural justice has two rules: audi alteram partem (hear the other side) and nemo judex in causa sua (no one may be a judge in their own cause). The bias test is real likelihood of bias: actual bias need not be proved, but mere suspicion is not enough. The High Court has supervisory jurisdiction over lower adjudicating bodies (article 141), defined by article 161 as including jurisdiction to issue orders in the nature of certiorari, which quashes a decision already made. An application for judicial review is made under Order 55 of the High Court (Civil Procedure) Rules 2004 (C.I. 47) and must be made not later than six months from the date of the event giving grounds for it.",
        "model_application": "First, the committee is an amenable body: a disciplinary committee of a public university exercises a public function, and Efua, directly affected by the suspension, has standing. Second, audi alteram partem was breached: Efua had no notice of the charge, no sight of the adverse evidence, and no opportunity to respond. Proper notice is a condition precedent to a valid decision, and a decision taken without a fair hearing is a nullity. Third, nemo judex was breached: the chairman's statement before the hearing that Efua 'definitely cheated' goes beyond mere suspicion and gives rise to a real likelihood of bias in the eyes of a reasonable person; he should not have sat. Fourth, the 'final' clause does not bar the court: a clause saying a decision is final cannot oust the High Court's supervisory jurisdiction. Fifth, the remedy is certiorari under Order 55, applied for within six months of the suspension. The court reviews the fairness and legality of the process, not whether Efua cheated: if the suspension is quashed, the university may re-hear the matter fairly, before an unbiased panel, with proper notice and a chance to respond.",
        "model_conclusion": "The suspension is likely to be quashed for breach of both rules of natural justice, and the 'final' clause does not prevent the High Court from intervening. Efua must apply under Order 55 within six months of the suspension.",
        "checklist": ["Identify the two rules of natural justice and the constitutional footing in article 23.", "Apply audi alteram partem to the facts: no notice, no evidence, no opportunity to respond.", "Apply the real likelihood of bias test to the chairman's prior statements.", "Deal with the 'final' clause: it cannot oust the High Court's supervisory jurisdiction.", "Name the remedy (certiorari) and the Order 55 six-month time limit, and note that the court reviews the process, not the merits."],
    },
}


def get_scenario(slug):
    return SCENARIOS.get(slug)
