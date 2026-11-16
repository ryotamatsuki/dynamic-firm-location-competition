# Dynamic Competition for Firms under Industrial Land Constraints

**Working research, not a publication or certified novelty claim.** 2026-11-16.
Stage 0: GO TO AUDIT. Stage 1: GO TO NOVELTY GATE within selected equilibrium. Stage 2: CONDITIONAL GO; novelty unresolved. TDF v5.1 STANDARD identified this branch as PROMISING, not pre-screen-certified.

## Research question
Can an expansion in available industrial land distort the allocation of firms in sequential subsidy competition even when the extra capacity is unused? This is a theoretical question, not a claim about actual policies or outcomes in Ehime.

## Frozen benchmark
Two municipalities A and B. Current firm X gives local gross benefits a and b, respectively; future firm Y arrives with probability p and has equal local benefit v. Let z=pv, d=b-a, b>a>z>=0. Firm location profits are identical across regions (normalized to zero), transfers are costless, additional capacity has zero cost. Capacity starts (1,1) or (1,2). Each firm consumes one slot; the eligible high bidder wins and pays its competitor's subsidy bid, or zero when alone. Fixed participation and automatic allocation; tie break fixed ex ante. Second-stage weakly dominant value bidding is selected at every history. First-stage continuation-adjusted willingness to pay is then weakly dominant in the induced game.

| state | X in A | X in B |
|---|---|---|
| baseline | continuation (0,z) | (z,0) |
| expanded | (0,z) | (0,0) |

Bids: baseline (a-z,b-z), expansion (a,b-z). When 0<d<z<a, X switches B to A, Y goes to B if present, so B's second slot is unused on path.

| regime | A | B | firms | aggregate |
|---|---:|---:|---:|---:|
| baseline | z | z+d | a-z | b+z |
| expanded, reversal | z-d | z | b-z | a+z |
| expanded, no reversal | 0 | d | a+z | b+z |

Thus under the selected continuation and first-stage bidding, reversal changes payoffs by (-d,-d,+d,-d). No reversal changes payoffs by (-z,-z,+2z,0). At d=z the tie rule determines allocation and welfare. Example a=8,b=10,v=5,p=0.6: (3,5,5,13) to (1,3,7,11).

## Equilibrium limitation
Not all SPNE yield this result. With the selected second-stage continuation, expanded first-stage bids (A=0,B=9) are also a Nash equilibrium for the example: X remains in B and aggregate welfare is 13. Disjoint mixed supports A={0,1}, B={9,10} also work. No full mixed-strategy equilibrium characterization is claimed. P4 (optimal capacity/publication/subsidy policy) remains unproved.

## Literature threats and scope
- Reiß & Schöndube (2010), Economic Theory 43, 99–141, https://doi.org/10.1007/s00199-008-0428-7, section 5.2 and Proposition 7: asymmetric capacity and sequential procurement.
- Budde & Minner (2015), IJPE 170, 652–662: capacity choice followed by project auctioning; capacity expansion can lower profits.
- Jayet & Paty (2006): industrial land supply and tax competition.
- Slattery (2025): bidding for firms.
- Jehiel & Moldovanu (2006): allocation externalities in auctions.
- Hendricks & Wiseman (2022): endogenous outside options in sequential auctions.

The payoff loss from capacity expansion alone is not claimed as novel. The surviving candidate is the unused marginal capacity / aggregate allocation loss and its policy implications. Whole-game prior-art mapping remains incomplete. No empirical validation, independent review, or exhaustive citation search has been performed.

## Related branch
A possible issue in Proposition 7(a) of Reiß & Schöndube motivated a distinct correction investigation: https://github.com/ryotamatsuki/reiss-schondube-sequential-auction-correction . The complete-information location model above is not the same as their Bayesian model. Do not transfer results across them without proof.

## Next-stage contract
Freeze this benchmark until novelty audit is resolved. Compare full games and results, not contextual labels. Separate subsequent mechanisms (endogenous capacity, first-price negotiations, firm heterogeneity, asymmetric future benefits) from the frozen benchmark. No posting of an article or claim of certified novelty at this stage.

AI-assisted derivation, source audit and numerical checks; author verification and external independent review pending.
