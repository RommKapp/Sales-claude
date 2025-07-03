# Step 3 - Performance Baseline Report

> **Role**  
> Act as a senior reliability analyst. Using only open, verifiable sources, compile a **Performance Baseline Report** that captures how the prospect's digital services behave today (availability, latency, throughput, scale, incident cadence). The goal is to arm pre-sales engineers with realistic performance starting points before they pitch CDN, cloud compute, AI inference, WAF, DDoS, or colocation upgrades.

> **Inputs you can supply**  
> • Company description and available products from Step 0
> • Company Snapshot from Step 1
> • Tech-Stack Map from Step 2
> • Any status-page URLs, public dashboards, or incident post-mortems you already know  
> • Nothing else—assume you cannot run active probes

> **Instructions**  
> 1. Use the analysis from Steps 0-2 as your foundation. Mine only public artifacts: status pages, SLA documents, investor decks, engineering blogs, third-party monitoring portals (e.g., Cloudflare Radar), and media reports.  
> 2. For every metric, attach a bracketed source tag: `[Status page, Apr 2025]`, `[Earnings call, Feb 2025]`.  
> 3. If a figure is approximate, prefix with "≈"; if unverified, note "unknown". Never fabricate numbers.  
> 4. Keep language factual, tight, and free of marketing adjectives.  
> 5. Follow the exact output structure below. No tables, no emojis.  
> 6. Bullet lists only, max two lines per bullet. Digits for all numbers, Oxford commas, single dash spacing.

---

## Output structure

**1. Services in scope**  
• List the public-facing services/apps covered (web, API, live video, inference endpoint) with brief purpose.

**2. Availability baseline**  
• Published uptime SLA (e.g., 99.95 %) and period covered  
• Actual uptime reported last 12 months (source)  
• Number and duration of incidents ≥ 15 min in last 12 months

**3. Latency baseline**  
• Any published average, p90, or p99 latency figures by region (ms)  
• Regions with repeated user complaints on social or status posts  
• Latency budget targets stated by the company, if any

**4. Throughput & capacity**  
• Peak traffic or RPS publicly quoted, with date  
• Average daily traffic where available  
• Stated or implied capacity headroom (e.g., "2× traffic buffer")

**5. Scalability & burst behaviour**  
• Autoscaling solution in use (Kubernetes HPA, AWS ASG, GCP MIG)  
• Largest recorded burst event (traffic, inference jobs, etc.) and scaling time  
• Any capacity-planning commentary from engineering blogs or talks

**6. Incident patterns**  
• Recurring root causes (DNS, SSL, database, DDoS) mentioned in post-mortems  
• Mean time to recovery (MTTR) if disclosed  
• Notable cascading failures affecting multiple regions

**7. Cost vs performance signals**  
• Public comments on cloud spend, egress fees, GPU shortages, or cost-cutting  
• Any metric tying performance targets to financial impact (e.g., checkout latency to conversion)

**8. Regulatory & SLA risk**  
• Regions where SLA misses triggered fines or customer credits  
• Compliance obligations that tighten performance windows (PCI, PSD2, GDPR)  
• Upcoming events that magnify risk (Black Friday, sports finals)

**9. Gaps & optimization opportunities**  
• Bullet each weak spot you see (e.g., "No multi-CDN failover", "Single cloud region for inference")  
• Link each gap to a product family we sell (CDN, DDoS, AI edge, etc.)

**10. Open questions for the prospect call**  
• Three to five unknowns that must be clarified live, each tagged "Needs confirmation"

---

## Reference data from previous steps

- **Step 0**: Company description and available products
- **Step 1**: Company Snapshot – gives revenue context for outage cost math  
- **Step 2**: Tech-Stack Map – reveals current vendors and scaling mechanisms  

**Additional material (if available):**

• Public status JSON or RSS feeds – provide raw uptime/incident counts  
• Investor presentations – sometimes list performance KPIs  
• Third-party benchmarks (Cedexis, ThousandEyes, Radar) – latency snapshots

**Paste any additional URLs or data here:**  

<Additional Data>