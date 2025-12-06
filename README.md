# SaaS MRR Performance Analysis (2024 Quarterly)

**Analyst:** Senior Data Analyst (deliverable created with LLM assistance)  
**Verification email:** 22f1000912@ds.study.iitm.ac.in

## Summary
This repository contains a compact data analysis of Monthly Recurring Revenue (MRR) growth for 2024 on a quarterly basis. The analysis processes the provided quarterly data, generates a visualization, and presents business findings and recommended actions.

### Data (MRR growth %)
- Q1 2024: 8.07
- Q2 2024: 8.69
- Q3 2024: 12.65
- Q4 2024: 13.04

**Average (2024 quarterly average, as required): 10.61**

**Industry target:** 15%

**Recommended solution:** **Expand into new market segments** — see Recommendations section.

---

## Key findings
1. The company’s Q1–Q2 growth is low (8.07 → 8.69), with a notable uplift starting Q3 and continuing Q4 (12.65 → 13.04).
2. Trajectory improved significantly in the second half of the year but still falls short of the industry target of 15%.
3. The computed average MRR growth for the four quarters is **10.61**, which is 4.39 percentage points below the industry target.
4. The recent upward trend demonstrates positive response to product/GT M changes but indicates insufficient reach or insufficient new market traction.

---

## Business implications
- Current growth rate (10.61) is below competitive benchmark (15%). If left unaddressed, this shortfall will compound into reduced ARR opportunity and slower scale.
- The improvement in Q3–Q4 suggests product-market-fit progress or better execution; however, incremental changes alone will likely not be enough to reach 15%.
- Management should prioritize structural growth levers: new market segments, targeted go-to-market, pricing experiments, and sales/partner enablement.

---

## Specific recommendations (how to reach 15%)
**Primary recommendation (strategic): Expand into new market segments**
- Identify 2–3 high-potential verticals adjacent to current customers (e.g., SMBs in healthcare, legal, or education depending on product fit). Use intent signals and ICP lookalike modeling to prioritize.
- Build tailored GTM playbooks per segment: vertical landing pages, vertical-specific case studies, targeted lead magnets and content, and vertical-specific pricing packs.
- Pilot a direct outbound + partner approach for each segment for 3 months; measure conversion lift and CAC.

**Tactical and measurable actions**
1. **Segmented Trials:** Launch 90-day free trial campaigns per new segment with tailored onboarding flows. Objective: increase trial-to-paid conversion by 15% in target segment.
2. **Product Localization/Packaging:** Create one vertical-specific edition (feature-lite or add-on) to reduce churn and increase perceived fit.
3. **Pricing experiments:** Run A/B price tests (3-arm) with targeted segments to discover willingness-to-pay; track ARPA uplift.
4. **Partnerships & Channel:** Recruit 2 channel partners per segment (consultancies or system integrators) to extend reach.
5. **Sales Enablement:** Re-scope sales collateral for vertical messaging; train SDRs for vertical discovery questions.
6. **Retention/Upsell:** Improve expansion revenue by adding in-app prompts for add-ons and quarterly account reviews to increase net revenue retention.

**Metrics & targets**
- Short-term (3 months): +2–4 pp MRR growth in pilot segments; improve trial→paid conversion by 10–15%.
- Mid-term (6–12 months): reach company-level MRR growth ≥13.5, with explicit roadmap to 15 by 12 months if pilots scale.
- OKRs: Segment pipeline created (>$X ARR), CAC payback <12 months, conversion rate lift.

---

## Files in this PR
- `analysis/mrr_analysis.py` — data processing + plotting script
- `analysis_output/mrr_quarterly_2024.csv` — raw data CSV
- `analysis_output/mrr_trend.png` — chart visualizing quarterly growth vs. target

---

## LLM assistance / provenance
- The code and analysis were produced with LLM assistance. Commits and PR notes should include labels such as:
  - `chore: add baseline mrr analysis (Jules commit)`
  - `docs: add README with findings (Codex-assisted)`

This PR demonstrates explicit LLM involvement for auditability.

---

## How to run locally
```bash
# clone the repo
git clone git@github.com:<your-username>/<your-repo>.git
cd <your-repo>

# create a branch for analysis changes
git checkout -b feature/mrr-analysis-jules

# place the files under analysis/ and analysis_output/ (or run the script to generate outputs)
python3 analysis/mrr_analysis.py

# the chart will be available in analysis_output/mrr_trend.png
