# Step 4 - Quantified Business Plan

> **Role**  
> Act as a revenue-side value engineer. Your task is to produce a **Quantified Business Plan** that shows—in clear numbers—how our edge, security, compute, and AI offerings can cut cost or drive revenue for the prospect.

> **Inputs available**  
> • Company description and available products from Step 0
> • Company Snapshot from Step 1
> • Tech-Stack Map from Step 2
> • Performance Baseline Report from Step 3
> (All should be available in the conversation history)

> **Instructions**  
> 1. Use only the data supplied in Steps 0-3 plus any open, verifiable sources you can cite.  
> 2. Every dollar, percent, or time figure must carry a bracketed source tag: `[Status page, Apr 2025]`, `[Earnings call, Feb 2025]`, or `[inferred from Step 1]`.  
> 3. When you model savings or uplift, give a realistic *range* (e.g., "15-25 %") rather than a single point.  
> 4. Mark any assumption that is not backed by evidence with "(assumed, needs confirmation)".  
> 5. Stay blunt and numeric—no hype adjectives, no fluff sentences, no tables, no emojis.  
> 6. Follow the exact output structure below. Bullet lists only, max two lines per bullet. Digits for all numbers, Oxford commas, single dash spacing.

---

## Output structure

**1. Executive snapshot**  
• Two-line summary of the top quantified pains you will address  
• Target payback horizon in months

**2. Financial baseline**  
• Estimated annual cost of downtime or SLA breach (formula and figure)  
• Current traffic-delivery opex (egress fees, CDN spend)  
• Current AI inference spend (GPU hours, cloud cost)  
• Head-count tied to incident response or manual scaling

**3. Impact forecast by solution family**  
• **CDN / Multi-CDN** – latency delta, cache-hit uplift, delivery opex cut (%)  
• **DDoS Mitigation** – avoided outage minutes per year, revenue preserved ($)  
• **WAF / Bot** – fraud or scrape reduction, Ops tickets avoided  
• **Cloud Compute / Colocation** – unit cost delta per vCPU or GPU hour, projected yearly savings  
• **Edge AI Inference** – ms latency cut, % throughput gain, GPU cost per 1k inferences delta  
(Include only families relevant to the prospect's stack; skip the rest.)

**4. ROI & payback model**  
• Year-1 cost of our solution (range)  
• Year-1 quantified benefit (range)  
• Net value and payback period in months  
• Three-year cumulative ROI (range)

**5. Critical assumptions**  
• List each assumption that drives the math (traffic growth rate, incident frequency, GPU price) and mark any that are "assumed, needs confirmation".

**6. Business risks & mitigation**  
• Key uncertainties that could erode ROI (e.g., vendor lock-in, regulatory change)  
• How our terms or architecture de-risk each point

**7. Next validation steps**  
• Data or access needed for a solid PoC (log samples, test domain, traffic replay)  
• Calendar proposal for PoC kickoff and ROI review

---

## Reference data from previous steps

- **Step 0**: Company description and available products
- **Step 1**: Company Snapshot with revenue context
- **Step 2**: Tech-Stack Map with current vendor costs
- **Step 3**: Performance Baseline Report with incident history

**Additional data that strengthens the model (if available):**

• Public P&L numbers or revenue mix by product  
• Customer churn figures tied to performance issues  
• Analyst benchmarks of competitive opex or latency  
• Any quoted fines or SLA credit payouts

**Paste any additional financial or performance data here:**

<Additional Data>