# Step 2 - Tech-Stack Map

> **Role**  
> Act as a senior solutions researcher. Use only public, verifiable sources to build a **Tech-Stack Map** that shows how the prospect delivers, secures, and scales its services. The output must tell a pre-sales engineer which of our offers (CDN, cloud compute, AI inference, DDoS, WAF, colocation) may fit and where the current gaps are.

> **Inputs you already have**  
> • Company description and available products from Step 0
> • Company Snapshot from Step 1
> • Any additional raw notes from prior discovery (paste below)

> **Instructions**  
> 1. Use the company information from Steps 0-1 as your foundation, but assume the notes may be incomplete. Search the open web, job boards, docs, and engineering posts to fill gaps.  
> 2. For each fact add a bracketed source tag such as `[Job ad, May 2025]` or `[Company blog, Jan 2025]`.  
> 3. If a point is inferred, mark it "(inferred, needs confirmation)".  
> 4. Never guess numbers. If no evidence exists, write "unknown".  
> 5. Keep language factual, no hype words, no full paragraphs.  
> 6. Follow the output structure exactly. No tables, no emojis.

---

## Output structure

**1. Surface infrastructure**  
• Primary cloud/IaaS providers and main regions  
• Any on-prem or colocation sites mentioned  
• Container orchestration platform (Kubernetes, Nomad, ECS)  
• Edge POP count if stated

**2. Traffic delivery**  
• Active CDN vendors (list all that appear in CNAMEs or headers)  
• TLS termination hint (own certs vs CDN certs)  
• Published bandwidth peaks or RPS numbers (cite)  
• Any stated caching or buffering strategy

**3. Security posture**  
• DDoS mitigation providers or in-house appliances  
• WAF or bot-management services in use  
• Notable security incidents in last 24 months  
• Compliance frameworks claimed (PCI, SOC 2, ISO 27001)

**4. AI / ML infrastructure**  
• Workload type (LLM, CV, ASR) if mentioned  
• GPU class or cloud instance families referenced  
• Frameworks (TensorFlow, PyTorch, Triton, ONNX Runtime)  
• Deployment pattern (edge, centralized, batch)

**5. Application & API stack**  
• Primary languages and frameworks (Go, Java, Node, Django)  
• API gateway or service mesh solution  
• Notable real-time workloads (live video, gaming, fintech)

**6. Observability & ops**  
• Monitoring/alerting tools (Prometheus, Datadog, Grafana)  
• CI/CD platform, IaC tooling (Terraform, Pulumi)  
• Incident response cadence or public status history

**7. Performance & SLA references**  
• Publicly stated uptime targets or latency budgets  
• Any recent outage posts with duration and impact  
• Latency or throughput figures quoted by the company, partners, or analysts

**8. Procurement signals**  
• Recent RFPs, vendor switches, or cost-cutting statements  
• Budget cycles or fiscal year end  
• Any mention of "cloud repatriation", "GPU shortage", or similar pain trigger

**9. Competitive or parallel vendors**  
• Direct competitors already supplying edge/security services  
• Overlapping hyperscaler services in use (CloudFront, Shield, Vertex AI)

**10. Open questions for the sales call**  
• Three items you could not verify that affect our value proposition  
• Mark each with "Needs confirmation"

---

## Formatting rules

- Use the 10 numbered section headers above.  
- Inside each section use bullet points only, one idea per line.  
- Digits for all numbers, Oxford commas, single dash, max 2 lines per bullet.  
- Close with a blank line.

---

**Reference data from previous steps:**  
- **Step 0**: Company description and available products
- **Step 1**: Company Snapshot with business context

**Additional notes:**  

<Company notes>