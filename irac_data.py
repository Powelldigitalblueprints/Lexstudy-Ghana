"""IRAC practice scenarios for LexStudy Ghana v0.2.

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
}


def get_scenario(slug):
    return SCENARIOS.get(slug)
