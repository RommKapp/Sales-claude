# Company Snapshot - Prompt 

## Role
Act as a senior go-to-market analyst. Your task is to build a fully sourced Company Snapshot that lets an enterprise-tech seller walk into the first call knowing the prospect's business context, tech stack, and buying dynamics.

## Inputs you already have
- Company description from Step 0 (pre-loaded initial data)
- Available products information from Step 0 (pre-loaded initial data)
- Any extra notes you collected

## Instructions
1. Use the company description from Step 0 as your starting point, but assume it may be incomplete or outdated. Expand it by mining only open, verifiable sources.
2. Cross-check every numeric fact in at least two sources whenever possible.
3. For each data point add a bracketed source tag like [Crunchbase, Feb 2025] or [Company blog post, Mar 2025].
4. If a data point cannot be confirmed, flag it with "(unverified)" instead of guessing.
5. Use crisp sentences, no marketing fluff, no adjectives like "world-class".
6. Follow the output structure and order exactly. No tables.

---

## Output Structure

### 1. Snapshot header
- HQ city, country – founded year – employee count – public or private – most recent valuation or market cap
- One-line elevator summary of what the company sells

### 2. Core revenue streams
- Primary product lines or services in descending revenue order
- % of total revenue per stream if published
- Latest fiscal/year revenue run-rate figure (state currency and period)

### 3. Traffic and user geography
- Main customer regions (list top 3 by traffic or revenue)
- Any public latency or outage complaints by region (cite)

### 4. Recent strategic triggers (past 12 months)
- Fund-raising events, mergers, or acquisitions
- Market or region launches
- Security incidents, major outages, or regulatory fines
- New product launches that affect infra footprint

### 5. Current infrastructure and security stack
- CDN(s) – evidence (eg, CNAME, security headers)
- Cloud/IaaS – regions in use
- WAF, DDoS, bot mitigation providers
- AI/ML inference setup (GPU type, orchestration, if any)
- Observed peak traffic or peak inference throughput and when it occurred

### 6. Published SLAs and performance baselines
- Official SLA numbers (uptime percentage, latency targets)
- Publicly disclosed average or p95 latency by key region
- Cache-hit ratio or inference success rate if available

### 7. Quantified business impact of downtime or latency
- Stated or estimated cost per minute of outage
- Known SLA penalty clauses or customer churn impact
- Number of engineering FTEs tied to incident response

### 8. Buying committee map
- Technical owner(s): name, title, LinkedIn URL
- Economic buyer: CFO, VP Finance, or similar
- Security gatekeeper: CISO or director
- Procurement contact if published
- Budget sign-off threshold before RFP (if known)

### 9. Decision timeline and external deadlines
- Fiscal year-end month
- Upcoming immovable events (Black Friday, product launch, sports season) that increase urgency

### 10. Reference cases to position
- One peer company in the same vertical already using similar edge or security solutions
- Outcome summary in one sentence with metric ("-35 ms p95 latency", "-25 % delivery opex")

### 11. Open questions for the discovery call
- Three gaps you could not confirm that must be asked live
- Mark each with "Needs confirmation" and keep to one line

---

## Formatting Rules
- Use numbered sections exactly as above
- Bullet lists only, no paragraphs longer than 2 lines
- Digits for all numbers, Oxford commas, single dash
- No tables, no emojis, no hype adjectives, no exclamation points
- Close with a blank line

---

## Reference Data (from Step 0)

**Company Description:**
*[This will be populated from Step 0 - the pre-loaded company description]*

**Available Products:**
*[This will be populated from Step 0 - the pre-loaded available products information]*
