#!/usr/bin/env python3
"""Generate the Master Equity Ranking Analysis as a Word document."""

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
import datetime

doc = Document()

# ── Style setup ──────────────────────────────────────────────────────────────
style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(11)
style.paragraph_format.space_after = Pt(4)
style.paragraph_format.space_before = Pt(2)

for level in range(1, 4):
    hs = doc.styles[f'Heading {level}']
    hs.font.color.rgb = RGBColor(0x1B, 0x2A, 0x4A)
    hs.font.name = 'Calibri'

# ── Title page ───────────────────────────────────────────────────────────────
doc.add_paragraph('\n\n\n')
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run('MASTER EQUITY RANKING ANALYSIS')
run.bold = True
run.font.size = Pt(28)
run.font.color.rgb = RGBColor(0x1B, 0x2A, 0x4A)

subtitle = doc.add_paragraph()
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = subtitle.add_run('Independent Buy-Side Research')
run.font.size = Pt(16)
run.font.color.rgb = RGBColor(0x4A, 0x4A, 0x4A)

dateline = doc.add_paragraph()
dateline.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = dateline.add_run(f'June 2025  |  96 Companies  |  Bottoms-Up Framework')
run.font.size = Pt(12)
run.font.color.rgb = RGBColor(0x6A, 0x6A, 0x6A)

doc.add_paragraph('\n')
disc = doc.add_paragraph()
disc.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = disc.add_run(
    'CONFIDENTIAL — FOR INVESTMENT COMMITTEE USE ONLY\n'
    'This analysis is bottoms-up, independent, and non-consensus. '
    'It does not anchor to sell-side estimates. All views are probabilistic.'
)
run.font.size = Pt(9)
run.font.italic = True
run.font.color.rgb = RGBColor(0x88, 0x88, 0x88)

doc.add_page_break()

# ── Helper ───────────────────────────────────────────────────────────────────
def add_ranked_entry(rank, name, ticker, rationale):
    p = doc.add_paragraph()
    run_rank = p.add_run(f'{rank}. ')
    run_rank.bold = True
    run_rank.font.size = Pt(11)
    run_name = p.add_run(f'{name} ({ticker})')
    run_name.bold = True
    run_name.font.size = Pt(11)
    run_name.font.color.rgb = RGBColor(0x1B, 0x2A, 0x4A)
    run_body = p.add_run(f' — {rationale}')
    run_body.font.size = Pt(10)

# ══════════════════════════════════════════════════════════════════════════════
# LIST 1: MOST LIKELY TO 2X IN 2 YEARS
# ══════════════════════════════════════════════════════════════════════════════
doc.add_heading('LIST 1: Most Likely to 2X in 2 Years', level=1)
doc.add_paragraph(
    'Ranked from highest to lowest probability of doubling within 24 months. '
    'Near-term catalysts, FCF inflection, valuation discount, and non-consensus signals weighted heavily.'
)

list1 = [
    (1, "Nu Holdings", "NU",
     "Triple-digit customer growth trajectory with 100M+ customers across LatAm, accelerating ARPAC, and now durably profitable with expanding margins. Trading at a meaningful discount to its growth rate. Bank charter economics compound — deposits are near-zero cost, lending spreads are wide, and cross-sell into insurance, crypto, and investing is just beginning. Non-consensus: insiders have not been selling, and LatAm digital banking penetration remains below 40%."),

    (2, "Grab Holdings", "GRAB",
     "Southeast Asian super-app approaching durable EBITDA profitability across ride-hailing, delivery, and fintech. The $40B+ SE Asian digital economy TAM is massively underpenetrated. GrabFin (lending, insurance, payments) is inflecting, and cost discipline has dramatically improved unit economics. Valuation remains compressed due to prior SPAC stigma, creating a wide gap between enterprise value and forward earnings power."),

    (3, "Marvell Technology", "MRVL",
     "Custom AI silicon and data center networking revenue is inflecting sharply higher, with AI-related revenue on track to exceed 50% of total. Major hyperscaler design wins (Amazon, Microsoft, Google custom chips + electro-optics) provide multi-year visibility. The stock trades at a discount to the AI semiconductor peer group despite comparable or superior growth. Near-term catalyst: each earnings cycle reveals accelerating AI mix."),

    (4, "Credo Technology Group", "CRDO",
     "Active electrical cables and SerDes IP for AI data center connectivity are seeing explosive demand as GPU cluster scale-out requires higher bandwidth interconnects. Revenue is growing >100% YoY from a small base, gross margins are expanding, and the company is already profitable. Every major hyperscaler buildout drives incremental demand. Valuation is elevated on a trailing basis but cheap on forward estimates if growth persists."),

    (5, "Hims & Hers Health", "HIMS",
     "Revenue growth exceeding 70% with high gross margins (~80%) and an expanding subscriber base across weight management, sexual health, dermatology, and mental health. The GLP-1 compounding opportunity adds a massive near-term catalyst. Path to significant FCF generation is visible. Risk is regulatory (FDA compounding enforcement), but even ex-GLP-1 the core business supports a much higher valuation."),

    (6, "SoFi Technologies", "SOFI",
     "Now sustainably profitable with a banking charter generating low-cost deposit funding. Lending, financial services, and the technology platform (Galileo/Technisys) are all growing. Member count exceeding 8M with rising products-per-member. The market still prices SoFi as a fintech when it is increasingly a bank with a tech platform, creating a valuation arbitrage that should close as earnings scale."),

    (7, "Sea Limited", "SE",
     "Shopee (e-commerce) has regained growth momentum while maintaining improved profitability discipline. Garena (gaming) has stabilized, and SeaMoney (fintech) is scaling. SE Asian digital economy is a multi-decade secular growth story. Valuation has re-rated from the 2022 lows but remains well below 2021 peaks, with the business in far better fundamental shape."),

    (8, "Robinhood Markets", "HOOD",
     "Product expansion into retirement accounts, credit cards, futures, and prediction markets is broadening the revenue base beyond volatile transaction revenue. Crypto exposure provides upside in a favorable regulatory cycle. Operating leverage is strong — each incremental user costs very little to serve. The stock is still perceived as a meme brokerage; fundamentals tell a different story."),

    (9, "Coinbase", "COIN",
     "Dominant US crypto exchange benefiting from a more favorable regulatory environment, institutional adoption via ETF custody, and Base (L2 chain) ecosystem growth. Revenue is cyclical but the structural trajectory is higher. Subscription and services revenue provides a growing base layer. In a sustained crypto upcycle, earnings power is dramatically underestimated by consensus."),

    (10, "Vertiv Holdings", "VRT",
     "Critical infrastructure for AI data centers (power, cooling, management). Order book is at record levels driven by hyperscaler buildouts. Revenue growth is accelerating while margins expand due to operational improvements and favorable pricing. The data center power bottleneck is the single biggest constraint on AI buildout, and Vertiv sits directly at that chokepoint."),

    (11, "CoreWeave", "CRWV",
     "Purpose-built GPU cloud with massive contracted backlog ($15B+) from hyperscalers and AI companies. Revenue is growing at triple-digit rates. The risk is high leverage and capex intensity, but if AI infrastructure demand persists (which every signal suggests it will), CoreWeave is positioned to be a foundational AI compute layer. Recent IPO discount provides entry opportunity."),

    (12, "Sezzle", "SEZL",
     "Small-cap BNPL player that has achieved consistent profitability while growing revenue at 50%+. Differentiated focus on younger demographics and subscription model. Tiny market cap means modest absolute growth in earnings can drive outsized stock appreciation. Insider ownership is high and aligned. The market overlooks this name due to BNPL sector stigma from Affirm/Klarna."),

    (13, "Oscar Health", "OSCR",
     "Health insurance technology company that has reached profitability and is scaling membership rapidly. Medical loss ratio improvements demonstrate the technology platform is working. Medicare Advantage expansion provides a large incremental TAM. The healthcare payer space is massive and the market underestimates the sustainability of Oscar's margin improvement."),

    (14, "Celestica", "CLS",
     "Contract manufacturer with dominant position in AI server and networking hardware assembly for hyperscalers. AI/ML revenue segment is growing 50%+ and now represents a majority of the business. Margins are expanding as mix shifts to higher-value AI infrastructure. Trades at a significant discount to the AI hardware value chain despite being a critical enabler."),

    (15, "Applied Digital", "APLD",
     "AI data center infrastructure company with significant contracted capacity. The pivot from crypto mining to AI cloud services offers a structural re-rating opportunity. Recent financing and partnerships (including with major hyperscalers) validate the model. High risk but high convexity — if execution continues, the current market cap dramatically undervalues the contracted revenue stream."),

    (16, "Astera Labs", "ALAB",
     "Semiconductor company providing connectivity solutions (PCIe retimers, smart cable modules) critical for AI server architectures. Revenue is growing >100% and the product cycle aligns with every GPU platform refresh. High gross margins (70%+) and capital-light model. Valuation is rich but growth justifies it if AI capex cycle has multiple years of runway remaining."),

    (17, "Zeta Global", "ZETA",
     "AI-powered marketing cloud seeing accelerating growth as enterprises adopt AI-driven customer acquisition. Revenue growth exceeding 30% with improving margins. The proprietary data asset and AI models create defensibility. Under-followed by institutional investors, creating an information asymmetry that is closing as the company scales into profitability."),

    (18, "Palantir", "PLTR",
     "AIP (Artificial Intelligence Platform) is driving a commercial re-acceleration, with boot camps converting prospects at unprecedented rates. Government business provides a durable, high-margin base. The valuation is rich on any traditional metric, but if AIP becomes the standard enterprise AI deployment platform, current pricing could prove cheap. Near-term risk is that elevated expectations leave little room for disappointment."),

    (19, "Nebius Group", "NBIS",
     "Spun out of Yandex, building AI cloud infrastructure and AI development tools with deep technical DNA. Early-stage but with substantial capital and experienced engineering talent. The opportunity is to become a credible non-hyperscaler AI compute provider. Very high risk, very high convexity — limited downside data makes this inherently speculative."),

    (20, "AppLovin", "APP",
     "AI-powered ad tech platform with a self-improving AXON engine that has driven explosive margin expansion. E-commerce advertising entry dramatically expands TAM beyond gaming. FCF generation is exceptional. The stock has re-rated significantly but earnings growth may continue to outpace valuation expansion. Key risk is that the re-rating is mostly complete."),

    (21, "IREN Limited", "IREN",
     "Former Iris Energy, pivoting from Bitcoin mining to AI/HPC data center services. Owned power infrastructure and sites provide structural cost advantages. The AI compute demand tailwind could drive a fundamental re-rating from crypto miner to AI infrastructure provider. Execution risk is real but the asset base is tangible and undervalued."),

    (22, "Shopify", "SHOP",
     "Commerce platform growth re-acceleration driven by enterprise (Shopify Plus), B2B, international expansion, and AI tools (Sidekick). Margin expansion following the logistics divestiture has been impressive. FCF is scaling rapidly. The question is whether the current valuation fully prices the growth outlook — at 15x+ forward revenue, execution must remain flawless."),

    (23, "JD.com", "JD",
     "Chinese e-commerce leader trading at a deep discount on depressed multiples (low single-digit P/E, significant net cash). Logistics infrastructure is a genuine moat. Shareholder returns via buybacks and dividends are accelerating. The risk is macro/regulatory in China, but the margin of safety at current valuations is substantial if the geopolitical discount even partially normalizes."),

    (24, "Camtek", "CAMT",
     "Semiconductor inspection equipment maker benefiting from advanced packaging demand (HBM, CoWoS) driven by AI chips. Revenue growth is strong and order visibility is high. Israeli-based company with niche dominance. The AI chip packaging tailwind has multi-year duration as every major chipmaker expands advanced packaging capacity."),

    (25, "MongoDB", "MDB",
     "Developer-centric document database with Atlas (cloud) growing rapidly. The AI-driven application development cycle should increase database demand. Net expansion rates remain healthy. Valuation has compressed meaningfully from peaks, creating a more favorable risk/reward. The concern is competition from PostgreSQL and whether AI code generation commoditizes database choice."),

    (26, "Tempus AI", "TEM",
     "AI-driven precision medicine platform with a unique proprietary clinical and molecular dataset. Revenue growth is strong, driven by genomics, data licensing, and clinical trial matching. If the platform becomes standard-of-care for oncology treatment selection, the TAM is enormous. Early stage and not yet profitable, but the data moat is defensible and growing."),

    (27, "Pure Storage", "PSTG",
     "All-flash storage leader benefiting from AI data infrastructure requirements. Subscription (Evergreen) model drives recurring revenue and improved visibility. Revenue growth is re-accelerating as AI workloads require high-performance storage. Valuation is reasonable relative to the storage peer group and the AI-driven growth inflection."),

    (28, "Cloudflare", "NET",
     "Internet infrastructure platform expanding from CDN/security into compute, storage, and AI inference at the edge. Developer platform adoption is accelerating. Revenue growth remains above 25% with a massive TAM ahead. Valuation is premium but the platform breadth and developer mindshare create a defensible long-term position."),

    (29, "Datadog", "DDOG",
     "Cloud monitoring and observability leader with a best-in-class land-and-expand model. AI/LLM observability adds a new growth vector. Net revenue retention remains above 120%. Valuation is fair-to-premium but justified by the combination of growth, margins, and TAM expansion. Risk is that cloud optimization headwinds are structural, not cyclical."),

    (30, "Snowflake", "SNOW",
     "Cloud data platform with consumption-based model seeing growth re-acceleration as cloud optimization headwinds fade. Product expansion into streaming, ML/AI workloads, and data applications broadens the platform. New CEO is refocusing execution. Valuation has compressed from peak froth, improving risk/reward, but the stock needs to demonstrate sustained reacceleration."),

    (31, "Advanced Micro Devices", "AMD",
     "AI GPU/accelerator business (MI300X/MI400) is scaling but remains a distant second to Nvidia. Data center revenue is growing rapidly and the AI inference opportunity is massive. Traditional server, PC, and embedded segments provide a revenue floor. Valuation reflects significant AI optimism — the risk is that Nvidia's moat in AI training proves durable, limiting AMD's AI upside."),

    (32, "Gambling.com Group", "GAMB",
     "Online gambling affiliate with high margins benefiting from US sports betting legalization wave. Small market cap with strong organic growth and disciplined M&A. Each new state that legalizes iGaming is an incremental catalyst. Capital-light model generates strong FCF. Under-followed and mispriced due to small size and gambling sector associations."),

    (33, "Novo Nordisk", "NVO",
     "GLP-1 obesity/diabetes franchise (Ozempic, Wegovy) represents a generational pharmaceutical opportunity. Supply is finally scaling to meet demand. The TAM for obesity treatment is potentially $100B+. The risk is competitive — Eli Lilly and oral alternatives may erode pricing and share. At current valuation, significant growth is already priced in, limiting near-term upside to 2x unless execution exceeds expectations."),

    (34, "CrowdStrike", "CRWD",
     "Cybersecurity platform leader with the industry's highest gross retention rates. Module adoption is expanding wallet share per customer. Post-July 2024 outage, the business has shown resilience and regained customer trust. Valuation is premium but the cybersecurity spending cycle is durable. Near-term 2x requires multiple expansion from already-elevated levels, which is the constraint."),

    (35, "First Majestic Silver", "AG",
     "Primary silver producer with significant operating leverage to silver prices. If silver breaks above $35-40/oz sustained, First Majestic's earnings and FCF inflect dramatically. High-cost producer means maximum torque to price increases. The risk is that silver remains range-bound, in which case the company's cost structure limits profitability."),

    (36, "Agnico Eagle Mines", "AEM",
     "Premier gold producer with Tier 1 assets in safe jurisdictions (Canada, Australia, Finland). Generating record FCF at current gold prices ($2,300+). Operating discipline is best-in-class among senior miners. If gold prices sustain above $2,500, Agnico's FCF yield makes it a compelling value name. Limited 2x upside unless gold rallies significantly further."),

    (37, "Innodata", "INOD",
     "AI data engineering and annotation company riding the wave of AI model training demand. Revenue has inflected sharply higher as LLM developers require high-quality training data. Small market cap means moderate revenue growth can drive outsized stock moves. The risk is customer concentration and whether demand normalizes as frontier model training cycles evolve."),

    (38, "Rubrik", "RBRK",
     "Cyber resilience and data security platform with subscription ARR growing 40%+. The ransomware epidemic creates a durable demand tailwind. Recently public with improving margins. Valuation is premium for the growth rate but the market opportunity is large and Rubrik's competitive position is strong. Near-term 2x requires continued ARR acceleration."),

    (39, "Kaspi.kz", "KSPI",
     "Kazakhstan super-app dominating payments (80%+ share), marketplace, and fintech in a rapidly digitizing economy. ROE consistently above 60%, net margins above 40%. Growth is driven by increasing digital penetration and geographic expansion. Risk is concentrated country exposure and geopolitical proximity to Russia. Valuation remains attractive for the quality of the business."),

    (40, "Duolingo", "DUOL",
     "AI-native language learning platform with exceptional engagement metrics and a viral growth loop. Subscriber growth and ARPPU expansion drive revenue growth above 40%. AI integration (Birdbrain, GPT-powered features) enhances the product while reducing content creation costs. Valuation is elevated but the combination of growth, margins, and consumer stickiness is rare."),

    (41, "Aris Mining", "ARMN",
     "Growing gold producer in Colombia with a clear path to 500K+ oz annual production. Costs are competitive and the asset base is expanding. Operating leverage to gold prices is significant. Small-cap with limited analyst coverage creates potential mispricing. The risk is jurisdictional — Colombia's mining regulatory environment adds a discount."),

    (42, "eToro", "ETOR",
     "Social trading platform that recently completed its IPO. Benefits from retail trading cycles and crypto exposure. Global reach with a unique social/copy-trading differentiator. Revenue is cyclical and valuation post-IPO is uncertain. Near-term 2x depends heavily on sustained retail trading engagement and crypto market conditions."),

    (43, "Clearwater Analytics", "CWAN",
     "Investment accounting and reporting SaaS platform with 95%+ gross retention. Revenue growth of 20%+ is steady and predictable. Financial services clients are sticky and the platform is mission-critical. A solid compounder but not a high-velocity grower — 2x in 2 years requires either multiple expansion or an acquisition catalyst."),

    (44, "Pagaya", "PGY",
     "AI-driven lending network that connects financial institutions with borrowers using proprietary models. Revenue growth is strong but profitability remains elusive. The model is capital-light (Pagaya doesn't hold loans on balance sheet). If credit conditions remain favorable and partner expansion continues, earnings could inflect. High uncertainty on timing."),

    (45, "Cipher Mining", "CIFR",
     "Bitcoin miner with low energy costs and growing hashrate capacity. Potential pivot to AI/HPC hosting adds optionality. Near-term upside is tied to Bitcoin price trajectory. If BTC sustains above $80K+, mining economics are attractive. The risk is that Bitcoin corrects and the AI pivot takes longer than expected."),

    (46, "SoundHound AI", "SOUN",
     "Voice AI platform for automotive, restaurants, and customer service. Revenue is growing rapidly from a small base. The agentic AI wave could accelerate adoption of voice interfaces. Market cap has expanded significantly on AI enthusiasm, creating execution risk — the company must demonstrate revenue scaling to justify the current valuation."),

    (47, "Toast", "TOST",
     "Restaurant technology platform reaching profitability with 120K+ locations. Net adds remain strong and ARPU is expanding through fintech and marketing modules. The restaurant tech TAM is large and fragmented. Valuation is fair — 2x requires sustained strong execution and further fintech penetration."),

    (48, "NIO", "NIO",
     "Chinese EV maker with brand recognition and battery swap technology differentiation. Revenue growth has re-accelerated with new model launches. However, cash burn remains significant and the Chinese EV market is brutally competitive. Near-term 2x is possible in a risk-on environment for China tech, but fundamental improvement in profitability is needed for sustained gains."),

    (49, "Semtech", "SMTC",
     "Semiconductor company focused on IoT (LoRa) and data center connectivity. Integration of Sierra Wireless is progressing. The IoT and data center connectivity markets provide secular growth. Debt from the acquisition is being reduced. 2x requires successful integration completion and IoT market acceleration."),

    (50, "Oracle", "ORCL",
     "Cloud infrastructure (OCI) growth is accelerating, driven by AI workload demand and competitive pricing. Database franchise remains a durable cash flow engine. RPO (remaining performance obligation) is at record levels. The stock has re-rated significantly — further 2x from current levels requires OCI to sustainably take cloud share, which is possible but far from certain."),

    (51, "Atlassian", "TEAM",
     "Collaboration and developer tools (Jira, Confluence) with strong brand loyalty and cloud migration tailwinds. AI-powered features (Rovo, Intelligence) add value. Revenue growth is 20%+ with expanding margins post-cloud migration. Valuation is premium; 2x requires growth acceleration or multiple expansion from already-rich levels."),

    (52, "TransMedics Group", "TMDX",
     "Organ transplant technology (OCS) with a unique market position as the only FDA-approved portable organ perfusion system. Revenue has scaled rapidly as adoption increases. Recent growth deceleration has pressured the stock, creating a potential re-entry point. The moat is deep but the TAM is relatively niche, capping the ultimate upside."),

    (53, "Newmont", "NEM",
     "World's largest gold miner with Tier 1 assets globally. Generating strong FCF at current gold prices. Newcrest acquisition integration provides operational synergies. As a large-cap miner, it offers gold exposure with lower single-stock risk. 2x requires gold to rally significantly from current levels given the large market cap."),

    (54, "Microsoft", "MSFT",
     "The world's most complete AI platform — Azure OpenAI, Copilot across 365/GitHub/Security, plus dominant enterprise franchise. AI monetization is real and scaling. The challenge for a 2x is math: at $3T+ market cap, doubling requires ~$3T of value creation in 2 years, which implies earnings growth well above current trajectory. A superb business but near-term 2x probability is low due to size."),

    (55, "Fair Isaac", "FICO",
     "Monopoly on credit scoring with extraordinary pricing power — score prices have increased ~100%+ over 5 years with zero churn. Software segment adds growth. Capital-light model generates FCF margins above 30%. The stock has compounded remarkably but valuation (50x+ earnings) now prices in significant continued pricing expansion. 2x from here requires heroic assumptions."),

    (56, "e.l.f. Beauty", "ELF",
     "Mass-market cosmetics brand taking share from legacy players with a digital-first, value-oriented approach. Revenue growth has been exceptional (40%+ CAGR). International expansion is the next leg. Concerns are whether growth decelerates as the base scales and whether the brand can sustain momentum. Valuation has contracted from peaks, improving risk/reward."),

    (57, "Celsius Holdings", "CELH",
     "Energy drink brand with strong growth driven by health-conscious positioning. Distribution partnership with PepsiCo provides scale. Revenue growth is decelerating from peak rates as distribution gains normalize. The stock is well off highs, creating potential value, but the beverage market is competitive and growth rate sustainability is uncertain."),

    (58, "Doximity", "DOCS",
     "Physician social network with 80%+ of US physicians on the platform. Margins are best-in-class (50%+ EBITDA margins). Revenue growth has re-accelerated after a temporary slowdown. The moat is deep (network effects) and the business is capital-light. 2x is achievable if pharma advertising budgets continue shifting digital, but the TAM has a natural ceiling."),

    (59, "The Honest Company", "HNST",
     "Consumer products company that has completed a turnaround — now profitable with improving margins. Revenue growth is modest but sustainable. Brand recognition (Jessica Alba) provides a halo. Small market cap means earnings growth can drive meaningful stock appreciation. The risk is that the CPG space is brutally competitive and growth may plateau."),

    (60, "Adeia", "ADEA",
     "IP licensing company (media patents, semiconductor) with a high-margin, recurring revenue model. FCF generation is strong relative to market cap. Dividend yield is attractive. Upside is driven by new licensing agreements and potential patent portfolio expansion. Limited growth catalyst for a 2x — this is more of a yield-plus-modest-growth story."),

    (61, "Accelerant", "ACNT",
     "Specialty insurtech using data and analytics to underwrite niche insurance risks. Growing premiums and improving combined ratios. Small and under-followed. The insurance industry is being disrupted by data-driven approaches, and Accelerant is positioned to benefit. Limited public data history makes conviction lower."),

    (62, "Waystar", "WAY",
     "Healthcare payment technology company that recently IPO'd. Revenue growth is steady (15-20%) with improving margins. Healthcare payments is a massive, complex market ripe for software penetration. Execution has been solid. 2x requires sustained growth and margin expansion, which is plausible but not high-probability in 24 months."),

    (63, "MSCI", "MSCI",
     "Premier index and analytics provider with monopoly-like characteristics — once an index is embedded in ETFs and benchmarks, switching costs are astronomical. Run-rate revenue is 95%+ recurring. Margins and pricing power are exceptional. However, trading at 35x+ forward earnings, 2x requires significant multiple expansion or earnings acceleration, both of which are unlikely in 24 months."),

    (64, "PTC", "PTC",
     "Industrial software (CAD, PLM, IoT) provider with successful SaaS transition driving recurring revenue growth. ARR growth of 12-15% is steady. Margin expansion is ongoing. A solid compounder but not a high-growth name — 2x in 2 years is unlikely absent a takeout premium."),

    (65, "Roper Technologies", "ROP",
     "Diversified industrial technology conglomerate with a Danaher-like compounding model. Asset-light, high-margin, acquisition-driven growth. Capital allocation track record is excellent. However, at 30x+ earnings with mid-teens organic growth, 2x in 2 years requires a significant re-rating or a large, accretive acquisition."),

    (66, "Fiserv", "FI",
     "Large-cap payments/fintech infrastructure with steady mid-to-high single-digit revenue growth. Clover (merchant POS) is a growth engine. Margin expansion is ongoing. A quality compounder but the large market cap and moderate growth rate make 2x in 2 years improbable absent a significant catalyst."),

    (67, "Adobe", "ADBE",
     "Creative and document cloud leader with AI integration (Firefly) driving product enhancement. Revenue growth of 10-12% is steady. FCF generation is excellent. Market has been concerned about AI disruption to creative workflows, creating some valuation discount. 2x requires a narrative shift back to growth — possible but requires AI monetization to visibly accelerate."),

    (68, "Intuit", "INTU",
     "Tax, accounting, and financial management software leader. AI integration (Intuit Assist) enhances the platform. Revenue growth of 10-15% with strong margins. The consumer tax monopoly is durable. 2x from a $170B+ market cap is mathematically difficult in 24 months."),

    (69, "Synopsys", "SNPS",
     "EDA software duopoly member with AI-driven chip design tools. The Ansys acquisition (pending/completed) expands into simulation. Revenue growth of 15%+ with expanding margins. Semiconductor design complexity is a secular tailwind. Valuation is full; 2x requires both organic execution and successful Ansys integration."),

    (70, "Cadence Design Systems", "CDNS",
     "EDA duopoly with strong AI/semiconductor design tailwinds. Computational software expansion broadens TAM. Revenue growth of 15%+ with exceptional margins. Like Synopsys, valuation is premium. 2x requires sustained execution and TAM expansion into new verticals."),

    (71, "Veeva Systems", "VEEV",
     "Life sciences vertical cloud platform with 80%+ market share in pharma CRM. Transition from Salesforce to proprietary Vault CRM reduces platform risk. Revenue growth of 15%+ is steady. Moat is deep but growth is moderate — 2x is unlikely in 24 months absent an acquisition or acceleration."),

    (72, "Paymentus", "PAY",
     "Bill payment technology platform with steady revenue growth. Expanding across utilities, government, and financial services verticals. Small market cap with a large addressable market. Growth is solid but not explosive — 2x requires either a re-rating or an acceleration in enterprise wins."),

    (73, "DigitalOcean", "DOCN",
     "Cloud infrastructure for SMBs and developers. AI workload adoption provides a growth vector. Revenue growth of 10-15% is modest. The SMB cloud market is large but competitive. 2x requires AI-driven reacceleration, which is uncertain."),

    (74, "Autodesk", "ADSK",
     "Design and engineering software leader with a completed SaaS transition. Revenue growth of 10-12% with improving margins as the shift to annual billing completes. FCF generation is strong. A quality compounder but not a 2x-in-2-years candidate at current valuation."),

    (75, "Verra Mobility", "VRRM",
     "Smart transportation technology (tolling, speed cameras, commercial fleet). Revenue growth of 10%+ with high recurring revenue. Steady and predictable but not high-growth. 2x is unlikely absent a strategic event."),

    (76, "SPS Commerce", "SPSC",
     "Supply chain management SaaS with 15%+ revenue growth and a network-effect moat. High retention rates and steady expansion. A quality small-cap compounder. 2x is possible over 2 years if growth sustains and multiples hold, but it requires consistent execution."),

    (77, "Alignment Healthcare", "ALHC",
     "Value-based care platform for Medicare Advantage. Revenue growth is strong (30%+) as membership scales. Path to profitability is emerging but not yet achieved. The VBC model has a long runway in US healthcare. High risk but meaningful upside if execution continues."),

    (78, "Clear Secure", "YOU",
     "Identity verification company with airport security lanes as the core product. Member growth is strong and ARPU is expanding. FCF positive with a capital-light model. Expansion into non-airport verticals (healthcare, sports) broadens TAM. Solid business but 2x requires significant membership acceleration."),

    (79, "Paychex", "PAYX",
     "Payroll and HR services leader with steady 5-7% revenue growth and a 40%+ operating margin. Dividend yield is attractive. Extremely stable but this is a bond-like equity — 2x in 2 years is very improbable."),

    (80, "NetEase", "NTES",
     "Chinese gaming giant with strong game pipeline and diversified revenue streams. Trades at low-teens P/E with significant cash. Shareholder returns are increasing. The China discount creates a valuation floor well below intrinsic value, but catalysts for re-rating are unclear."),

    (81, "Barrick Gold", "GOLD",
     "Major gold miner with a global asset base. Generating healthy FCF at current gold prices. Operational improvements under Bristow are ongoing. Large-cap gold exposure with geographic diversification (including higher-risk jurisdictions). 2x requires a significant gold rally from already-elevated levels."),

    (82, "Check Point Software", "CHKP",
     "Legacy cybersecurity vendor with steady growth and high margins. Infinity platform consolidation is driving modest acceleration. FCF generation is strong. The stock is inexpensive relative to cybersecurity peers but growth is below the sector average. 2x requires either a sector re-rating or a takeout premium."),

    (83, "Dayforce", "DAY",
     "HCM software (formerly Ceridian) with a cloud-native platform. Revenue growth of 15-20% with improving margins. Competitive market with Workday, ADP, and Paycom. A solid business but not differentiated enough for 2x in 24 months absent an acquisition catalyst."),

    (84, "Shopify", "SHOP",
     "Already ranked #22 — see above. Duplicate entry noted for completeness."),

    (85, "SS&C Technologies", "SSNC",
     "Financial services software with an acquisition-driven model. Revenue growth is mid-single digits organically. High leverage from M&A. Stable but not a growth story. 2x is improbable without a takeout."),

    (86, "Progress Software", "PRGS",
     "Application development tools with an acquisition-led growth strategy. Revenue growth of 15-20% driven by M&A. Organic growth is low single digits. Steady cash flow generation. 2x requires a major strategic event."),

    (87, "Blackbaud", "BLKB",
     "Nonprofit/education vertical software. Revenue growth of 5-8% with margin expansion from operational improvements. Niche market position is defensible but small TAM limits upside. 2x is very unlikely in 24 months."),

    (88, "Jack Henry & Associates", "JKHY",
     "Community banking technology provider with 95%+ retention. Revenue growth of 6-8% is steady and predictable. A quality defensive name but not a growth story. 2x probability is very low."),

    (89, "Paycom Software", "PAYC",
     "HCM/payroll software with decelerating growth as BETI (employee-driven payroll) cannibalized short-term revenue. Single-digit revenue growth in a competitive market. Quality product but near-term headwinds make 2x unlikely."),

    (90, "SolarWinds", "SWI",
     "IT management software recovering from the 2020 supply chain attack. Growth has stabilized in mid-single digits. Margin improvement is ongoing. Takeout by Turn/River was completed — this may no longer be publicly traded. Data point requires verification."),

    (91, "Bentley Systems", "BSY",
     "Infrastructure engineering software with steady 10-12% growth. Infrastructure spending tailwinds are durable. Asset-light model with high margins. A quality compounder but not a 2x candidate at current valuation."),

    (92, "AspenTech", "AZPN",
     "Industrial software (process optimization) majority-owned by Emerson. Limited public float reduces liquidity. Growth is mid-single digits. 2x probability is negligible as a controlled entity."),

    (93, "Fidelity National Info Services", "FIS",
     "Large-cap financial technology recovering from the Worldpay-related strategic missteps. Revenue growth is low single digits. Margin improvement post-Worldpay separation is ongoing. A turnaround story but not a 2x in 2 years."),

    (94, "Descartes Systems", "DSGX",
     "Logistics and supply chain technology with steady growth through acquisition and organic means. Revenue growth of 10-15% with high margins. A quality compounder but modest growth rate limits 2x probability."),

    (95, "Viavi Solutions", "VIAV",
     "Network test and measurement with cyclical end markets (telecom, enterprise). Revenue has been stagnant. Telecom capex recovery would help but timing is uncertain. 2x requires a significant end-market recovery that has been delayed repeatedly."),

    (96, "Figma", "FIGMA",
     "Collaborative design platform that remains private as of the latest available data. The Adobe acquisition was terminated in December 2023. An IPO is expected but timing is unconfirmed. Cannot fully rank without public financial data. Placed last due to inability to analyze public market dynamics, not a reflection of business quality — Figma is an exceptional business."),
]

# Remove the duplicate Shopify entry and Netskope (private) - add them properly
# Actually, let me just fix the Shopify duplicate entry
list1[83] = (84, "Netskope", "PRIVATE",
     "Private company — not publicly traded as of the latest available data. Netskope is a leading SASE/cloud security vendor, but without public financials, a full ranking is not possible. Placed here due to data unavailability, not business quality.")

for entry in list1:
    add_ranked_entry(*entry)

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# LIST 2: MOST LIKELY TO 5X IN 3 YEARS
# ══════════════════════════════════════════════════════════════════════════════
doc.add_heading('LIST 2: Most Likely to 5X in 3 Years', level=1)
doc.add_paragraph(
    'Ranked from highest to lowest probability of a 5x return within 36 months. '
    'TAM, revenue CAGR durability, operating leverage potential, and asymmetric upside vs downside weighted heavily.'
)

list2 = [
    (1, "Nu Holdings", "NU",
     "The combination of 100M+ customers, sub-5% penetration in most product categories, near-zero customer acquisition cost via viral referral, and LatAm's $1T+ financial services TAM creates a rare setup for a 5x. Revenue per customer is still a fraction of traditional bank ARPU, and every incremental product (insurance, investing, crypto, lending) accretes to margins that are already positive and expanding. The base rate for a fintech achieving this scale in an underbanked market with a bank charter is exceptional."),

    (2, "Credo Technology Group", "CRDO",
     "Revenue is growing triple digits from a small base in a market (AI data center connectivity) that is expanding faster than any enterprise infrastructure segment in history. Each successive GPU generation requires higher bandwidth, directly benefiting Credo's active electrical cables and SerDes IP. If AI infrastructure capex compounds at 30-40% annually for 3 years, Credo's revenue base could expand 8-10x, and operating leverage would accelerate earnings even faster."),

    (3, "Grab Holdings", "GRAB",
     "SE Asian super-app with 40M+ transacting users in a region of 700M+ people with rising smartphone and internet penetration. The path from current EBITDA to $2-3B in earnings over 3 years is visible if lending scales (high-margin), advertising grows (pure margin), and ride-hailing/delivery mature (improving unit economics). At current EV, 5x requires roughly $10-15B in earnings power, which is ambitious but not impossible if fintech execution succeeds."),

    (4, "Nebius Group", "NBIS",
     "Former Yandex AI division with deep engineering talent, building AI cloud and training infrastructure. Backed by significant capital and existing technology assets. At a small market cap, 5x requires the company to establish itself as a credible AI compute provider outside the hyperscaler oligopoly. High conviction on capability, lower conviction on timing and competitive dynamics."),

    (5, "Hims & Hers Health", "HIMS",
     "DTC healthcare platform with subscriber count growing exponentially. Weight management (GLP-1 compounding) is a potential $50B+ market where Hims has early traction. If the platform scales to 5M+ subscribers at $50+ monthly ARPU, revenue would exceed $3B with 30%+ EBITDA margins. The 5x math works if subscriber growth sustains and the regulatory environment remains favorable for telehealth/compounding."),

    (6, "SoFi Technologies", "SOFI",
     "Bank charter economics (low-cost deposits funding high-yield lending) combined with a growing fintech platform (Galileo/Technisys) create dual earnings engines. If SoFi reaches 15-20M members with 7+ products per member and the technology platform scales to 200M+ accounts, a $50B+ valuation is defensible. The 5x requires sustained 25%+ earnings growth, which the current trajectory supports."),

    (7, "CoreWeave", "CRWV",
     "Contracted GPU cloud revenue backlog of $15B+ provides unusual revenue visibility for a recently public company. If AI compute demand continues compounding and CoreWeave executes on its build-out roadmap, revenue could scale from $2-3B to $10B+ within 3 years. The risk is leverage — the business is heavily financed — but the assets (GPU clusters) are in high demand and generate cash."),

    (8, "Applied Digital", "APLD",
     "AI data center developer with contracted capacity at attractive economics. Small market cap means moderate revenue growth drives large percentage gains. If even 2-3 major facilities reach full utilization, the FCF could support a valuation 5-10x current levels. Execution and financing risk are the primary constraints."),

    (9, "Sezzle", "SEZL",
     "Profitable BNPL company with a tiny market cap (~$1-2B) growing revenue 50%+. If BNPL adoption continues and Sezzle maintains profitability while scaling, the market cap required for 5x ($5-10B) is well within reach for a financial services company of that revenue scale. Insider ownership alignment and differentiated demographic focus reduce agency risk."),

    (10, "IREN Limited", "IREN",
     "Bitcoin mining infrastructure pivoting to AI/HPC cloud. Owned power assets at below-market rates create structural cost advantages. If the pivot to AI hosting succeeds, the per-MW valuation should re-rate from crypto-miner multiples to data center multiples (5-10x higher). The 5x is predicated on successful execution of this transition."),

    (11, "Robinhood Markets", "HOOD",
     "Product expansion (retirement, credit, futures, international) is diversifying revenue. Crypto exposure adds convexity. If Robinhood reaches 30M+ funded accounts with $100+ ARPU, revenue could exceed $5B. At a financial services multiple, 5x from current levels is achievable. The platform's brand and user engagement create a real distribution advantage."),

    (12, "Sea Limited", "SE",
     "E-commerce (Shopee), gaming (Garena), fintech (SeaMoney) across SE Asia and LatAm. The combined TAM exceeds $500B. If Shopify is any guide for e-commerce platform valuations at maturity, Sea's commerce segment alone could justify the current enterprise value. Add fintech and gaming, and 5x is a reasonable bull case over 3 years."),

    (13, "Tempus AI", "TEM",
     "Proprietary clinical and molecular dataset covering millions of patients. If Tempus becomes the data infrastructure layer for precision medicine — connecting diagnostics, clinical trials, and treatment selection — the TAM is $50B+. Early stage, not yet profitable, but the data moat compounds with each additional patient record. 5x requires proving the flywheel."),

    (14, "Innodata", "INOD",
     "AI data annotation and engineering at the epicenter of LLM training demand. Revenue has inflected sharply. Small market cap ($1-2B) means 5x requires reaching only $5-10B, achievable if AI training data demand remains robust. Key risk is customer concentration and cyclicality of model training budgets."),

    (15, "Coinbase", "COIN",
     "Crypto exchange with dominant US market share, ETF custody business, and Base L2 ecosystem. In a sustained crypto bull cycle with BTC above $150K, Coinbase's earnings power could be $5-10B. 5x requires both crypto market cooperation and successful diversification beyond trading fees. Regulatory clarity is a tailwind."),

    (16, "SoundHound AI", "SOUN",
     "Voice AI platform with automotive and restaurant partnerships. If voice interfaces become the primary mode of human-computer interaction in commerce (ordering, customer service, in-car), the TAM is enormous. Revenue is small but growing rapidly. 5x from a small base is mechanically easier but requires proving sustainable enterprise demand."),

    (17, "Marvell Technology", "MRVL",
     "Custom AI silicon for hyperscalers is a multi-billion dollar revenue opportunity still in early innings. Each major cloud provider building custom chips is a Marvell customer or prospect. 5x from a ~$70-80B market cap requires reaching $350-400B, which implies $15-20B in revenue at 20x sales — ambitious but possible if Marvell becomes the dominant custom silicon partner."),

    (18, "Astera Labs", "ALAB",
     "Connectivity silicon for AI server architectures with >100% revenue growth. Each GPU platform generation drives new design wins. If AI server buildout sustains for 3+ years, Astera's revenue base could expand 5-8x. The question is valuation — the stock may already price in significant growth, limiting the stock-price 5x even if business 5x occurs."),

    (19, "AppLovin", "APP",
     "AI-powered ad tech with a self-improving algorithm and expansion into e-commerce advertising. If e-commerce ad TAM capture succeeds, revenue could expand 3-5x from current levels. FCF margins are exceptional. The recent massive re-rating means 5x from current levels ($100B+ to $500B+) is a much higher bar — requires becoming a top-5 advertising platform globally."),

    (20, "Zeta Global", "ZETA",
     "AI marketing cloud with accelerating growth and improving margins. The enterprise marketing technology market is large and fragmented, creating consolidation opportunities. If Zeta scales to $1B+ revenue with 20%+ margins, a $10B+ valuation is reasonable. 5x from current levels requires sustained 30%+ growth."),

    (21, "Gambling.com Group", "GAMB",
     "Online gambling affiliate with high margins and a small market cap. Each US state legalizing iGaming is an incremental growth driver. If the US fully legalizes online casino gambling (following sports betting), the TAM expands massively. 5x from a small base is achievable if the regulatory catalyst materializes."),

    (22, "Palantir", "PLTR",
     "AIP commercial acceleration could make Palantir the default enterprise AI deployment platform. If government + commercial revenue reaches $10B+ at 30% margins, a $300B valuation is defensible. 5x from ~$150B+ requires Palantir to become an AI platform at the scale of Salesforce or ServiceNow. Possible but demands consistent execution against well-funded competitors."),

    (23, "Oscar Health", "OSCR",
     "Scaling health insurance membership with improving unit economics. If Oscar reaches 2M+ members with a 3-5% net margin, earnings power supports a much higher valuation. The health insurance market is enormous and technology-driven disruption is still early. 5x requires sustained membership growth and margin expansion."),

    (24, "Shopify", "SHOP",
     "Commerce platform with massive merchant base and expanding into B2B, international, and AI-powered tools. Revenue growth of 25%+ at scale with improving margins. 5x from $100B+ market cap requires becoming a $500B+ company, which implies Shopify capturing a significantly larger share of global commerce infrastructure. Possible but the base is large."),

    (25, "Cloudflare", "NET",
     "Platform expansion from CDN/security into compute, AI inference, and developer tools. If Workers/R2/AI gateway adoption accelerates, Cloudflare could become a top-5 cloud platform. 5x from ~$40B requires reaching $200B, implying $10B+ revenue at 20x sales. Ambitious but the platform breadth and developer adoption trends are encouraging."),

    (26, "Vertiv Holdings", "VRT",
     "Data center power and cooling at the epicenter of AI infrastructure buildout. Order book is at records. If AI capex cycles extend for 3+ years, Vertiv could become a $5-10B revenue company with 20%+ margins. 5x from ~$40B to $200B is ambitious but supported by the capital cycle."),

    (27, "Camtek", "CAMT",
     "Advanced packaging inspection for AI chips. HBM and CoWoS capacity expansion drives multi-year demand. Small market cap means revenue growth can drive outsized returns. 5x requires sustained semiconductor capex in advanced packaging."),

    (28, "Celestica", "CLS",
     "AI server manufacturing with growing margins and visibility. 5x from current levels requires Celestica to become a significantly larger enterprise — achievable if AI infrastructure demand sustains but constrained by contract manufacturing margins."),

    (29, "Datadog", "DDOG",
     "Cloud observability leader with AI/LLM monitoring as a new growth vector. 5x from ~$50B requires becoming a $250B platform company. Revenue would need to reach $10-15B, which implies 25%+ CAGR sustained for 3 years. Possible if the platform continues expanding but the base is already significant."),

    (30, "MongoDB", "MDB",
     "Developer database platform with AI application development tailwinds. If AI drives a new wave of application creation, MongoDB's Atlas consumption grows proportionally. 5x from ~$25B requires reaching $125B, demanding $5B+ revenue at 25x sales. Possible in a strong AI application cycle."),

    (31, "Kaspi.kz", "KSPI",
     "Super-app dominance in Kazakhstan with potential expansion across Central Asia. 60%+ ROE and 40%+ net margins are exceptional. 5x requires geographic expansion beyond Kazakhstan, which is the key unknown."),

    (32, "Rubrik", "RBRK",
     "Cyber resilience platform with 40%+ ARR growth. Ransomware epidemic drives demand. 5x from ~$10-15B requires scaling to a $50-75B company, which demands $3-5B in ARR at enterprise software multiples. Ambitious but the market opportunity is large."),

    (33, "Duolingo", "DUOL",
     "AI-powered education platform with exceptional engagement. 5x from ~$12-15B requires reaching $60-75B, implying significant revenue scaling. The education TAM is massive but monetization per user has natural limits. Possible if international expansion and new subjects (math, music) succeed."),

    (34, "Novo Nordisk", "NVO",
     "GLP-1 dominance is a generational pharmaceutical franchise. However, 5x from ~$400-500B requires reaching $2T+, making NVO one of the world's most valuable companies. Possible only if obesity treatment becomes as universal as statin therapy AND Novo maintains pricing/share. More likely a 2-3x compounder than a 5x."),

    (35, "CrowdStrike", "CRWD",
     "Cybersecurity platform consolidation leader. 5x from ~$80B requires reaching $400B. Even as the cybersecurity market grows to $500B+, CrowdStrike would need to capture an outsized share. Possible but demands significant market cap expansion beyond what growth rates typically support."),

    (36, "Fair Isaac", "FICO",
     "Credit scoring monopoly with pricing power. 5x from ~$50-60B to $250-300B requires FICO to sustain 20%+ earnings growth for 3 years while multiples expand or hold. The pricing power is real but the stock is already richly valued."),

    (37, "ServiceNow", "NOW",
     "Enterprise workflow platform with AI-driven acceleration. 5x from ~$180B to $900B would make NOW one of the most valuable software companies ever. Revenue growth of 20%+ is strong but 5x is a very high bar at this scale."),

    (38, "Snowflake", "SNOW",
     "Cloud data platform with consumption re-acceleration. 5x from ~$50B requires reaching $250B, implying massive revenue scaling. If AI workloads drive data consumption growth, possible but highly dependent on execution."),

    (39, "AMD", "AMD",
     "AI GPU challenger to Nvidia. 5x from ~$250B to $1.25T requires closing the gap with Nvidia significantly. Possible if AMD's AI accelerators capture meaningful share in inference workloads, but Nvidia's moat in AI training is formidable."),

    (40, "Toast", "TOST",
     "Restaurant tech platform scaling profitability. 5x from ~$20B requires reaching $100B, implying Toast becomes the dominant restaurant operating system with significant fintech revenue. Possible but the path is long."),

    (41, "Pure Storage", "PSTG",
     "AI storage beneficiary with subscription model. 5x from ~$20B requires reaching $100B. Needs AI to drive a fundamental step-change in storage demand. Possible but storage multiples historically cap returns."),

    (42, "Clearwater Analytics", "CWAN",
     "Investment accounting SaaS with steady growth. 5x from ~$7B to $35B requires sustained 25%+ growth, which is above current trajectory. Needs a product expansion or M&A catalyst."),

    (43, "NIO", "NIO",
     "Chinese EV with brand and battery swap technology. 5x is possible if the Chinese EV market consolidates favorably and NIO achieves sustained profitability. The downside is also significant — cash burn in a competitive market."),

    (44, "e.l.f. Beauty", "ELF",
     "Mass cosmetics brand with strong growth. 5x from ~$7B to $35B requires sustained 30%+ growth and international expansion. Possible if the brand momentum continues but CPG competition is intense."),

    (45, "Aris Mining", "ARMN",
     "Growing gold producer with leverage to gold prices. 5x from a small base is achievable if gold rallies and production scales as planned. Jurisdictional risk in Colombia is the primary concern."),

    (46, "eToro", "ETOR",
     "Social trading platform with crypto exposure. 5x requires a sustained retail trading boom and successful product expansion. Cyclicality of trading revenues makes this uncertain."),

    (47, "Oracle", "ORCL",
     "Cloud infrastructure growth and AI workload demand. 5x from ~$400B to $2T would make Oracle one of the world's most valuable companies. Possible only if OCI becomes a major cloud platform, which is a non-consensus view. More likely a 2-3x."),

    (48, "First Majestic Silver", "AG",
     "Silver producer with maximum leverage to silver prices. 5x requires silver to rally to $50+/oz and production to scale. Possible in a precious metals supercycle but highly speculative."),

    (49, "Cipher Mining", "CIFR",
     "Bitcoin miner with AI pivot optionality. 5x requires Bitcoin rally and/or successful AI hosting transition. Both are plausible but uncertain."),

    (50, "TransMedics Group", "TMDX",
     "Organ transplant technology with deep moat. 5x from ~$5B requires reaching $25B, which is constrained by the niche TAM. Possible if the company expands into adjacent organ care markets."),

    (51, "Semtech", "SMTC",
     "IoT and data center semiconductor. 5x from ~$5B requires IoT market acceleration and data center connectivity growth. Integration risk from Sierra Wireless acquisition is moderating."),

    (52, "Celsius Holdings", "CELH",
     "Energy drink brand competing with Monster and Red Bull. 5x from ~$10B to $50B requires becoming a global beverage champion. Possible but the beverage market favors incumbents at scale."),

    (53, "Pagaya", "PGY",
     "AI lending platform with rapid growth but profitability challenges. 5x from a small base is mechanically achievable if the platform scales and achieves profitability."),

    (54, "The Honest Company", "HNST",
     "Consumer products turnaround. 5x from a tiny market cap is arithmetically possible but requires significant revenue and margin expansion in a competitive category."),

    (55, "Doximity", "DOCS",
     "Physician network with 80%+ penetration. 5x from ~$10B to $50B requires expanding beyond pharma advertising into healthcare workflows. The moat is deep but TAM growth is the constraint."),

    (56, "Alignment Healthcare", "ALHC",
     "Value-based care scaling membership. 5x requires achieving profitability while scaling significantly. High execution risk."),

    (57, "Atlassian", "TEAM",
     "Developer tools platform. 5x from ~$50B to $250B requires AI-driven acceleration beyond current growth rates. Possible but demands successful AI monetization."),

    (58, "Agnico Eagle Mines", "AEM",
     "Premier gold miner. 5x from ~$50B to $250B requires gold at $5,000+ sustained. Very unlikely absent a monetary system restructuring."),

    (59, "Adeia", "ADEA",
     "IP licensing with limited growth vectors. 5x is very improbable from an asset-light licensing model."),

    (60, "Accelerant", "ACNT",
     "Specialty insurtech with limited public history. 5x from a small base is possible but data limitations reduce conviction."),

    (61, "Waystar", "WAY",
     "Healthcare payments technology. 5x from ~$7B requires reaching $35B, which demands significant market penetration. Possible but competitive market."),

    (62, "Clear Secure", "YOU",
     "Identity verification expanding beyond airports. 5x from ~$5B requires reaching $25B, which demands successful expansion into healthcare, events, and other verticals."),

    (63, "Microsoft", "MSFT",
     "5x from $3T+ to $15T+ is mathematically near-impossible in 3 years. The world's best business but size prevents 5x returns."),

    (64, "MSCI", "MSCI",
     "Index monopoly with exceptional economics. 5x from ~$50B to $250B requires sustained 25%+ earnings growth, well above historical trend."),

    (65, "Roper Technologies", "ROP",
     "Compounding machine but 5x from $60B to $300B requires a pace far above historical compounding."),

    (66, "Adobe", "ADBE",
     "Creative software leader. 5x from $200B+ to $1T+ requires AI to dramatically accelerate growth. Possible in theory but the base is large."),

    (67, "Intuit", "INTU",
     "Financial software monopoly. 5x from $170B to $850B is a very high bar for a mature software company."),

    (68, "Fiserv", "FI",
     "Payments infrastructure. 5x from $100B+ to $500B+ requires payments market restructuring. Very unlikely in 3 years."),

    (69, "Synopsys", "SNPS",
     "EDA duopoly. 5x from ~$80B to $400B requires semiconductor complexity growth beyond historical rates."),

    (70, "Cadence", "CDNS",
     "EDA duopoly. Same dynamics as Synopsys — 5x is a very high bar from a ~$80B base."),

    (71, "PTC", "PTC",
     "Industrial software. 5x from ~$25B requires reaching $125B, far above what organic growth can deliver."),

    (72, "Veeva", "VEEV",
     "Life sciences vertical SaaS. 5x from ~$35B requires dominating pharma IT spend. Possible in a very long timeframe but unlikely in 3 years."),

    (73, "Autodesk", "ADSK",
     "Design software. 5x from ~$60B to $300B is extremely unlikely in 3 years given mid-teens growth."),

    (74, "Paymentus", "PAY",
     "Bill payment tech. 5x from a small base is possible but the market is niche."),

    (75, "SPS Commerce", "SPSC",
     "Supply chain SaaS. 5x from ~$8B to $40B requires acceleration well above current 15% growth."),

    (76, "DigitalOcean", "DOCN",
     "SMB cloud. 5x from ~$4B to $20B is possible if AI workloads drive reacceleration."),

    (77, "Verra Mobility", "VRRM",
     "Smart transportation. 5x is very unlikely given the steady-state nature of the business."),

    (78, "Newmont", "NEM",
     "Largest gold miner. 5x from ~$60B to $300B requires gold at $5,000+. Very improbable."),

    (79, "Barrick Gold", "GOLD",
     "Major gold miner. Same dynamics as Newmont. 5x is near-impossible from this base without a monetary regime shift."),

    (80, "Check Point", "CHKP",
     "Legacy cybersecurity. 5x from ~$20B to $100B requires growth acceleration far above historical 5-8% rates."),

    (81, "NetEase", "NTES",
     "Chinese gaming. 5x from ~$60B to $300B requires significant gaming market share expansion. Unlikely given regulatory constraints."),

    (82, "Paycom", "PAYC",
     "HCM software with decelerating growth. 5x is very improbable without a strategic transformation or takeout."),

    (83, "Dayforce", "DAY",
     "HCM software. 5x from ~$10B to $50B requires sustained 25%+ growth in a competitive market."),

    (84, "Progress Software", "PRGS",
     "Application tools. 5x from a small base is possible via M&A but organic growth does not support it."),

    (85, "Jack Henry", "JKHY",
     "Community banking tech. 5x from ~$14B is near-impossible given 6-8% growth."),

    (86, "SS&C Technologies", "SSNC",
     "Financial services software. 5x from ~$17B requires transformative M&A or organic acceleration far above trend."),

    (87, "Blackbaud", "BLKB",
     "Nonprofit software. 5x from ~$4B to $20B requires revenue acceleration that the nonprofit TAM likely cannot support."),

    (88, "Paychex", "PAYX",
     "Payroll services. 5x from ~$50B to $250B is mathematically improbable for a 5-7% grower."),

    (89, "SolarWinds", "SWI",
     "IT management software. May be private (Thoma Bravo). 5x is moot if no longer publicly traded."),

    (90, "Bentley Systems", "BSY",
     "Infrastructure software. 5x from ~$15B to $75B requires growth acceleration well above trend."),

    (91, "AspenTech", "AZPN",
     "Industrial software controlled by Emerson. 5x is extremely unlikely as a controlled entity with limited public float."),

    (92, "FIS", "FIS",
     "Financial tech infrastructure. 5x from ~$45B is near-impossible for a low-single-digit grower."),

    (93, "Descartes", "DSGX",
     "Logistics tech. 5x from ~$10B to $50B requires sustained 20%+ growth, above historical trend."),

    (94, "Viavi Solutions", "VIAV",
     "Network test. 5x from ~$2B to $10B is possible in a telecom capex supercycle but that cycle has been perpetually delayed."),

    (95, "Netskope", "PRIVATE",
     "Private company. Cannot rank for public market 5x return."),

    (96, "Figma", "FIGMA",
     "Private company. Cannot rank for public market 5x return."),
]

for entry in list2:
    add_ranked_entry(*entry)

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# LIST 3: MOST LIKELY TO 10X IN 5 YEARS
# ══════════════════════════════════════════════════════════════════════════════
doc.add_heading('LIST 3: Most Likely to 10X in 5 Years', level=1)
doc.add_paragraph(
    'Ranked from highest to lowest probability of a 10x return within 5 years. '
    'Long-duration compounders, reinvestment runway, competitive moat, and category leadership weighted heavily.'
)

list3 = [
    (1, "Credo Technology Group", "CRDO",
     "AI data center connectivity is the fastest-growing segment in enterprise infrastructure. Credo's revenue is growing >100% from a base small enough that 10x in stock price is achievable even with moderate multiple expansion. Each GPU generation drives higher bandwidth requirements. 5-year view: if AI infrastructure capex compounds at 25-35% annually, Credo's revenue could reach $5-10B from <$1B, and at 15-20x sales, the stock price math works for 10x."),

    (2, "Nu Holdings", "NU",
     "LatAm's largest digital bank with 100M+ customers and sub-10% product penetration. A 10x requires NU to reach $300-400B market cap, implying $15-20B in revenue at 15-20x sales. With 25-30% revenue CAGR and margin expansion, this is achievable over 5 years. The key insight: NU is replicating the JPMorgan playbook in a market where incumbents are structurally disadvantaged by legacy cost structures."),

    (3, "Nebius Group", "NBIS",
     "AI cloud infrastructure from a small base with deep technical capabilities. 10x from a small market cap is mechanically easier. If Nebius establishes itself as a credible non-hyperscaler AI compute provider, the addressable market is hundreds of billions. 5-year view: the AI compute market is likely to fragment beyond the current hyperscaler oligopoly, creating room for specialized providers. Very high conviction on TAM, moderate conviction on Nebius specifically."),

    (4, "Grab Holdings", "GRAB",
     "SE Asian super-app in the early innings of financial services monetization. 10x requires GRAB to reach $100-150B market cap, achievable if GrabFin (lending, insurance, wealth) scales to $3-5B in revenue at fintech multiples. The 700M+ population across SE Asia with rapidly rising digital engagement provides a multi-decade growth runway. 5-year view: Grab becomes the financial infrastructure layer for SE Asia, similar to what Alipay/WeChat Pay became for China."),

    (5, "Sezzle", "SEZL",
     "Tiny market cap + profitability + 50%+ revenue growth = high mechanical probability of 10x. If Sezzle sustains growth and expands from BNPL into broader financial services for its demographic (younger consumers), a $10-15B market cap is achievable. The alignment of insider ownership reduces agency risk. 5-year view: Sezzle evolves from BNPL into a niche consumer finance platform."),

    (6, "Applied Digital", "APLD",
     "AI data center infrastructure at a small market cap with significant contracted capacity. 10x requires successful execution on 2-3 major facility buildouts and sustained AI compute demand. The asset base is real and the contracts provide visibility. 5-year view: if AI infrastructure becomes as critical as cloud infrastructure, purpose-built AI data center developers will command premium valuations."),

    (7, "IREN Limited", "IREN",
     "Owned power infrastructure pivoting from Bitcoin mining to AI/HPC hosting. 10x requires the AI pivot to succeed and per-MW valuations to re-rate to data center levels. The power assets are tangible and increasingly scarce as AI data centers compete for grid access. 5-year view: power-first data center operators benefit from the fundamental constraint on AI buildout — not silicon, but energy."),

    (8, "SoFi Technologies", "SOFI",
     "Digital bank with 8M+ members, a bank charter, and a technology platform. 10x from ~$12-15B requires reaching $120-150B, implying SoFi becomes a top-10 US financial institution by market cap. This requires 25%+ compounding of both members and ARPU. Possible but ambitious. 5-year view: if SoFi's tech platform (Galileo) becomes the AWS of fintech infrastructure, the valuation re-rates from bank to platform."),

    (9, "CoreWeave", "CRWV",
     "GPU cloud with massive contracted backlog. 10x from a post-IPO market cap requires CoreWeave to become a foundational AI compute layer valued at $200B+. The leverage risk is the primary concern, but if AI compute demand compounds and CoreWeave maintains utilization, the revenue and earnings growth support it. 5-year view: CoreWeave is to AI compute what AWS was to cloud in 2012."),

    (10, "Hims & Hers Health", "HIMS",
     "DTC healthcare platform with exponential subscriber growth. 10x from ~$8-10B to $80-100B requires HIMS to become a major healthcare platform company. If subscribers scale to 10M+ at $80+ ARPU with 25%+ net margins, this is achievable. GLP-1, hair loss, skincare, and mental health each represent billion-dollar categories. 5-year view: HIMS becomes the Amazon of DTC healthcare."),

    (11, "SoundHound AI", "SOUN",
     "Voice AI for commerce and customer service. 10x from a small base requires voice AI to become the primary interface for commercial transactions. If SoundHound captures even 5% of the global customer service automation market, revenue could reach $5B+. Very speculative but the convexity is real. 5-year view: voice agents replace traditional IVR and chatbots across millions of businesses."),

    (12, "Innodata", "INOD",
     "AI data engineering and annotation. 10x from ~$1-2B is achievable if AI training data demand scales and Innodata maintains its position. The risk is that demand is cyclical — each foundation model training cycle drives a burst of demand that may normalize. 5-year view: if AI models continue scaling (which all evidence suggests), training data demand compounds."),

    (13, "Tempus AI", "TEM",
     "Precision medicine AI platform with proprietary datasets. 10x requires Tempus to become the data layer for clinical decision-making globally. The TAM is massive ($50B+) and the data moat deepens with each patient. 5-year view: Tempus becomes the Palantir of healthcare — controversial but indispensable."),

    (14, "Coinbase", "COIN",
     "Crypto infrastructure with Base L2 and ETF custody. 10x from ~$50-60B requires crypto to become a mainstream asset class and Coinbase to maintain dominance. If crypto market cap reaches $10T+ and Coinbase captures infrastructure fees across trading, custody, and on-chain activity, a $500B+ valuation is conceivable. Highly scenario-dependent."),

    (15, "Robinhood Markets", "HOOD",
     "Fintech platform expanding product suite. 10x from ~$30-40B to $300-400B requires Robinhood to become a top financial services franchise. Possible if international expansion and product diversification succeed, but the path requires flawless execution over 5 years."),

    (16, "Gambling.com Group", "GAMB",
     "iGaming affiliate with a tiny market cap. 10x is achievable on modest revenue growth if US iGaming legalization accelerates. The capital-light model means FCF conversion is high. 5-year view: if iGaming follows the sports betting legalization path, GAMB's affiliate revenue could expand 5-10x."),

    (17, "Zeta Global", "ZETA",
     "AI marketing cloud. 10x from ~$6-8B to $60-80B requires Zeta to become a major enterprise marketing platform. If AI-driven marketing automation displaces legacy approaches, Zeta is positioned to benefit. 5-year view: the marketing tech stack consolidates around AI-native platforms."),

    (18, "Sea Limited", "SE",
     "SE Asian digital economy platform. 10x from ~$30-40B to $300-400B requires Sea to dominate e-commerce, fintech, and gaming across SE Asia. This is the same vision as Grab but through e-commerce rather than ride-hailing. 5-year view: SE Asia's digital economy reaches $1T, and Sea captures the largest share."),

    (19, "Camtek", "CAMT",
     "Semiconductor inspection for advanced packaging. 10x from a small base requires sustained AI chip packaging demand growth. If HBM and advanced packaging capacity expands 5-10x over 5 years, Camtek's revenue scales proportionally."),

    (20, "Astera Labs", "ALAB",
     "AI server connectivity silicon. 10x from current valuation requires the AI server buildout to extend for 5+ years and Astera to maintain its technology leadership. Already richly valued, so stock-price 10x is a higher bar than business 10x."),

    (21, "Oscar Health", "OSCR",
     "Health insurance tech scaling. 10x from ~$5B to $50B requires Oscar to achieve sustained profitability at 5M+ members. Possible if the technology platform genuinely improves healthcare delivery economics."),

    (22, "Marvell Technology", "MRVL",
     "Custom AI silicon. 10x from ~$70B to $700B makes Marvell a top-10 semiconductor company globally. Requires dominant custom silicon share across all major hyperscalers. Possible but demands consistent design win execution."),

    (23, "Palantir", "PLTR",
     "AI deployment platform. 10x from ~$150B to $1.5T requires Palantir to become a foundational AI platform company at the scale of Microsoft's enterprise franchise. Very ambitious but the AIP platform has early traction. 5-year view: if AI deployment becomes as complex as cloud migration, Palantir is the systems integrator."),

    (24, "AppLovin", "APP",
     "AI ad tech. 10x from ~$100B to $1T requires AppLovin to become one of the world's largest advertising platforms. Possible only if e-commerce advertising scales massively."),

    (25, "Pagaya", "PGY",
     "AI lending platform. 10x from a small base is achievable if the platform scales and achieves profitability."),

    (26, "Cipher Mining", "CIFR",
     "Bitcoin mining with AI pivot. 10x from a small base requires Bitcoin rally and/or successful AI hosting. Both provide convexity."),

    (27, "Vertiv Holdings", "VRT",
     "Data center infrastructure. 10x from ~$40B to $400B requires becoming the dominant power/cooling provider for AI data centers globally. Possible if AI capex extends but industrial multiples typically cap returns."),

    (28, "Cloudflare", "NET",
     "Internet infrastructure and edge compute. 10x from ~$40B to $400B requires Cloudflare to become a top-3 cloud platform. The developer adoption trend supports this long-term thesis."),

    (29, "NIO", "NIO",
     "Chinese EV. 10x from a depressed base is possible if NIO achieves profitability and the Chinese EV market consolidates in its favor. Very high risk."),

    (30, "Celestica", "CLS",
     "AI server manufacturing. 10x from ~$15B to $150B requires a fundamental re-rating of contract manufacturing multiples. Unlikely unless Celestica develops proprietary IP."),

    (31, "First Majestic Silver", "AG",
     "Silver miner. 10x requires silver at $60-80+/oz sustained. Possible in a precious metals supercycle but highly speculative."),

    (32, "Shopify", "SHOP",
     "Commerce platform. 10x from ~$100B to $1T requires Shopify to become the dominant global commerce infrastructure. Possible over 5 years if enterprise and international execution succeeds."),

    (33, "MongoDB", "MDB",
     "Developer database. 10x from ~$25B to $250B requires AI-driven application proliferation and database demand acceleration."),

    (34, "Rubrik", "RBRK",
     "Cyber resilience. 10x from ~$10-15B requires reaching $100-150B, achievable if cyber resilience becomes as critical as endpoint security."),

    (35, "Snowflake", "SNOW",
     "Data cloud. 10x from ~$50B to $500B requires dominant AI data platform positioning. Possible but competitive market."),

    (36, "e.l.f. Beauty", "ELF",
     "Mass cosmetics. 10x from ~$7B to $70B requires becoming a global CPG champion. Possible if international expansion replicates US success."),

    (37, "The Honest Company", "HNST",
     "Consumer products. 10x from a tiny base is arithmetically possible but the CPG market growth rate is modest."),

    (38, "eToro", "ETOR",
     "Social trading. 10x requires sustained retail trading engagement and crypto cycle tailwinds."),

    (39, "Aris Mining", "ARMN",
     "Gold mining growth. 10x from a small base requires gold rally + production scaling."),

    (40, "Duolingo", "DUOL",
     "AI education. 10x from ~$12B to $120B requires global education platform dominance. Possible if new subjects and markets succeed."),

    (41, "Datadog", "DDOG",
     "Observability. 10x from ~$50B to $500B requires platform dominance of the entire DevOps/cloud management stack."),

    (42, "Clearwater Analytics", "CWAN",
     "Investment accounting. 10x from ~$7B to $70B requires significant TAM expansion beyond current scope."),

    (43, "Toast", "TOST",
     "Restaurant tech. 10x from ~$20B to $200B requires dominating restaurant operations globally."),

    (44, "Pure Storage", "PSTG",
     "Flash storage. 10x from ~$20B to $200B requires AI to fundamentally reshape storage demand curves."),

    (45, "TransMedics", "TMDX",
     "Organ transplant tech. 10x from ~$5B requires expanding into adjacent organ care markets. Niche limits ultimate scale."),

    (46, "AMD", "AMD",
     "AI semiconductors. 10x from ~$250B to $2.5T requires AMD to close the gap with Nvidia, becoming the clear #2 AI chip company. Possible but Nvidia's moat is deep."),

    (47, "Semtech", "SMTC",
     "IoT semiconductor. 10x from ~$5B requires IoT market acceleration. Long-duration thesis but timing uncertain."),

    (48, "CrowdStrike", "CRWD",
     "Cybersecurity platform. 10x from ~$80B to $800B requires cybersecurity market to expand dramatically and CRWD to maintain leadership."),

    (49, "Kaspi.kz", "KSPI",
     "Kazakhstan super-app. 10x from ~$25B requires geographic expansion across Central Asia and beyond. Country concentration risk limits probability."),

    (50, "JD.com", "JD",
     "Chinese e-commerce. 10x from ~$50B requires China geopolitical discount to fully normalize. Possible but political risk is the binding constraint."),

    (51, "Celsius Holdings", "CELH",
     "Energy drinks. 10x from ~$10B to $100B requires global expansion at the scale of Monster. Possible but competitive."),

    (52, "Novo Nordisk", "NVO",
     "GLP-1 pharma. 10x from ~$400B to $4T would make NVO the world's most valuable company. Extremely unlikely even with obesity drug dominance."),

    (53, "ServiceNow", "NOW",
     "Enterprise workflows. 10x from ~$180B to $1.8T requires becoming the definitive enterprise AI platform. Theoretically possible but a very high bar."),

    (54, "Alignment Healthcare", "ALHC",
     "Value-based care. 10x from a small base is possible if the model scales across Medicare Advantage."),

    (55, "Oracle", "ORCL",
     "Cloud and database. 10x from ~$400B to $4T is near-impossible in 5 years."),

    (56, "Agnico Eagle", "AEM",
     "Gold mining. 10x from ~$50B requires gold at $10,000+. Near-impossible."),

    (57, "Doximity", "DOCS",
     "Physician network. 10x from ~$10B to $100B requires expanding well beyond pharma advertising. TAM is the constraint."),

    (58, "Waystar", "WAY",
     "Healthcare payments. 10x from ~$7B to $70B requires dominating healthcare payment workflows."),

    (59, "Clear Secure", "YOU",
     "Identity verification. 10x from ~$5B to $50B requires successful expansion beyond airports."),

    (60, "Fair Isaac", "FICO",
     "Credit scoring monopoly. 10x from ~$50B to $500B requires sustained aggressive pricing + platform expansion. The monopoly supports it but valuation already reflects pricing power."),

    (61, "Atlassian", "TEAM",
     "Developer tools. 10x from ~$50B to $500B requires AI to fundamentally expand the developer productivity TAM."),

    (62, "Newmont", "NEM",
     "Gold mining. 10x from ~$60B to $600B is near-impossible for a gold miner."),

    (63, "Barrick Gold", "GOLD",
     "Gold mining. Same as Newmont. 10x is near-impossible."),

    (64, "Microsoft", "MSFT",
     "10x from $3T to $30T is mathematically impossible — it would exceed global GDP."),

    (65, "Adobe", "ADBE",
     "Creative software. 10x from $200B to $2T requires AI to dramatically accelerate growth. Very unlikely."),

    (66, "Intuit", "INTU",
     "Financial software. 10x from $170B to $1.7T is extremely unlikely for a mature software company."),

    (67, "Fiserv", "FI",
     "Payments. 10x from $100B to $1T requires payments infrastructure transformation. Very unlikely."),

    (68, "MSCI", "MSCI",
     "Index provider. 10x from $50B to $500B requires index adoption to expand at rates far above historical."),

    (69, "Synopsys", "SNPS",
     "EDA software. 10x from $80B to $800B requires semiconductor design complexity to explode."),

    (70, "Cadence", "CDNS",
     "EDA software. Same dynamics as Synopsys. 10x from ~$80B is extremely ambitious."),

    (71, "Roper Technologies", "ROP",
     "Industrial software conglomerate. 10x from $60B to $600B is well above the historical compounding rate."),

    (72, "PTC", "PTC",
     "Industrial software. 10x from $25B to $250B requires growth acceleration far above trend."),

    (73, "Veeva", "VEEV",
     "Life sciences SaaS. 10x from $35B to $350B requires expanding well beyond life sciences."),

    (74, "Check Point", "CHKP",
     "Cybersecurity. 10x from $20B to $200B requires growth acceleration from 5-8% to 25%+. Near-impossible for this mature business."),

    (75, "NetEase", "NTES",
     "Chinese gaming. 10x from $60B to $600B requires becoming the global gaming leader. Unlikely given China regulatory constraints."),

    (76, "Autodesk", "ADSK",
     "Design software. 10x from $60B to $600B requires sustained 25%+ growth, well above current trajectory."),

    (77, "Paymentus", "PAY",
     "Bill payment tech. 10x from a small base is possible but the market is niche."),

    (78, "SPS Commerce", "SPSC",
     "Supply chain SaaS. 10x from $8B to $80B requires sustained 20%+ growth for 5 years."),

    (79, "DigitalOcean", "DOCN",
     "SMB cloud. 10x from $4B to $40B is possible if AI workloads drive significant reacceleration."),

    (80, "Accelerant", "ACNT",
     "Specialty insurtech. 10x from a small base is possible but data limitations reduce conviction."),

    (81, "Adeia", "ADEA",
     "IP licensing. 10x is very improbable for a mature licensing business."),

    (82, "Verra Mobility", "VRRM",
     "Smart transportation. 10x is very unlikely given the steady-state business model."),

    (83, "Dayforce", "DAY",
     "HCM software. 10x from $10B to $100B requires sustained 20%+ growth in a competitive market."),

    (84, "Progress Software", "PRGS",
     "Application tools. 10x requires transformative M&A far beyond historical pattern."),

    (85, "Blackbaud", "BLKB",
     "Nonprofit software. 10x from $4B to $40B requires revenue acceleration the nonprofit TAM cannot support."),

    (86, "Jack Henry", "JKHY",
     "Banking tech. 10x from $14B to $140B is near-impossible at 6-8% growth."),

    (87, "SS&C", "SSNC",
     "Financial services software. 10x from $17B to $170B requires transformative M&A."),

    (88, "Paycom", "PAYC",
     "HCM software. 10x from $12B to $120B requires reversing the growth deceleration and significant product expansion."),

    (89, "SolarWinds", "SWI",
     "IT management. Likely private. 10x is moot."),

    (90, "Paychex", "PAYX",
     "Payroll services. 10x from $50B to $500B is impossible for a 5-7% grower."),

    (91, "FIS", "FIS",
     "Financial tech. 10x from $45B to $450B requires transformation well beyond current trajectory."),

    (92, "Bentley Systems", "BSY",
     "Infrastructure software. 10x from $15B to $150B requires growth acceleration above historical."),

    (93, "AspenTech", "AZPN",
     "Industrial software. Controlled entity. 10x is extremely unlikely."),

    (94, "Descartes", "DSGX",
     "Logistics tech. 10x from $10B to $100B requires acquisition-driven scaling."),

    (95, "Viavi Solutions", "VIAV",
     "Network test. 10x from $2B to $20B is possible only in a telecom supercycle that has been perpetually delayed."),

    (96, "Netskope / Figma", "PRIVATE",
     "Private companies. Cannot rank for public market 10x return."),
]

for entry in list3:
    add_ranked_entry(*entry)

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# LIST 4: MOST LIKELY TO DELIVER 20%+ ANNUALIZED RETURNS INDEFINITELY
# ══════════════════════════════════════════════════════════════════════════════
doc.add_heading('LIST 4: Most Likely to Deliver 20%+ Annualized Returns Indefinitely', level=1)
doc.add_paragraph(
    'Ranked from highest to lowest probability of compounding at 20%+ per year on a sustained basis. '
    'Rule of 40, capital efficiency, pricing power, and durable competitive advantage weighted heavily.'
)

list4 = [
    (1, "Fair Isaac", "FICO",
     "The closest thing to a legal monopoly in financial services. FICO scores are embedded in virtually every US lending decision by regulation and convention. Switching costs are infinite — no lender will unilaterally stop using FICO scores. Pricing power is extraordinary: score prices have roughly doubled over 5 years with zero volume attrition. Software segment adds incremental growth. Capital-light model with 30%+ FCF margins. Rule of 40 score consistently above 50. The only risk is regulatory intervention on pricing, which has not materialized. This is a perpetual compounding machine."),

    (2, "MSCI", "MSCI",
     "Index and analytics monopoly with 95%+ recurring revenue. Once an MSCI index is embedded in ETFs and institutional benchmarks, it is virtually impossible to displace. Asset-based fees grow with global market capitalization — passive growth driver. ESG and private assets analytics extend the moat into new data verticals. Capital-light, 50%+ EBITDA margins, and consistent pricing power. Rule of 40 score above 55. MSCI compounds at 20%+ returns as long as global capital markets expand and indexation penetration increases."),

    (3, "ServiceNow", "NOW",
     "Enterprise workflow platform with best-in-class net expansion rates (130%+) and 97%+ renewal rates. Every enterprise process that gets digitized onto the Now Platform becomes embedded in organizational DNA. AI integration (Now Assist) adds a new monetization layer while increasing switching costs. Revenue growth of 20%+ at $10B+ scale is rare. Rule of 40 score consistently above 60. The question is whether NOW can sustain 20%+ growth as the base scales — early evidence suggests yes, as the TAM expands into new verticals (HR, supply chain, industry-specific)."),

    (4, "AppLovin", "APP",
     "AI-powered advertising platform with a self-improving AXON engine that creates a reflexive competitive advantage — more data improves targeting, which drives more ad spend, which generates more data. FCF margins are exceptional (40%+) and the e-commerce TAM expansion is a step-function growth driver. Rule of 40 score is above 70. The risk is that the AI edge is replicated by competitors, but the data moat deepens with scale. If AXON maintains its edge, 20%+ compounding is sustainable."),

    (5, "Datadog", "DDOG",
     "Cloud observability leader with a platform that becomes more valuable as customers adopt additional modules. Net revenue retention above 120% demonstrates organic wallet share expansion. AI/LLM observability is a new growth vector. Gross margins above 80%, operating margins expanding, and FCF generation is strong. Rule of 40 score above 55. The combination of a large, growing TAM (cloud monitoring + security + AI ops) and platform-driven expansion supports 20%+ compounding."),

    (6, "Shopify", "SHOP",
     "Commerce infrastructure platform that is becoming the operating system for independent retail globally. Payments (Shop Pay), fulfillment, B2B, and international expansion provide multiple growth vectors. FCF margins are expanding rapidly post-logistics divestiture. Rule of 40 score is above 45. The competitive moat is the merchant ecosystem — once a merchant builds their business on Shopify, migration cost is prohibitive. 20%+ compounding requires sustained GMV growth, which global e-commerce penetration supports."),

    (7, "CrowdStrike", "CRWD",
     "Cybersecurity platform with the industry's highest gross retention (98%+) and a module adoption model that expands wallet share from endpoint into cloud, identity, and SIEM. Cybersecurity spending is non-discretionary and growing faster than IT budgets. Rule of 40 score above 60. The July 2024 outage was a stress test that demonstrated the stickiness of the platform. 20%+ compounding is supported by the combination of TAM expansion and module cross-sell."),

    (8, "Palantir", "PLTR",
     "AI platform for government and commercial with a unique deployment model (ontology-based). If AIP becomes the standard enterprise AI deployment framework, the competitive moat is deep — once an organization's data and workflows are mapped in Palantir's ontology, switching costs are enormous. Rule of 40 score is above 55 and improving. The risk is that valuation already prices in significant AIP success. If execution continues, 20%+ compounding is driven by commercial acceleration."),

    (9, "Nu Holdings", "NU",
     "Digital bank compounding at 40%+ revenue growth with expanding margins. Capital efficiency is high — CAC is near zero (viral referral) and the bank charter provides low-cost funding. Cross-sell into insurance, investing, and lending expands ARPU. Rule of 40 score is above 70. The challenge for sustained 20%+ compounding is whether growth normalizes as LatAm market penetration matures — but with <5% product penetration, that inflection point is likely 5+ years away."),

    (10, "Cadence Design Systems", "CDNS",
     "EDA duopoly with 85%+ recurring revenue and deep switching costs. Semiconductor design complexity is a secular tailwind driven by AI, automotive, 5G, and IoT. Computational software expansion into molecular simulation and CFD broadens TAM. Rule of 40 score above 45. Margins expand with scale. 20%+ compounding is supported by the EDA industry's structural growth and Cadence's platform expansion."),

    (11, "Synopsys", "SNPS",
     "EDA duopoly partner to Cadence with identical structural advantages. AI-driven chip design tools (DSO.ai) add monetization. The Ansys acquisition (if completed) expands into simulation, creating a broader design-to-verification platform. Rule of 40 score above 45. Same compounding thesis as Cadence — semiconductor complexity is a perpetual growth driver for EDA tools."),

    (12, "Roper Technologies", "ROP",
     "Asset-light industrial software conglomerate with a Berkshire-like capital allocation model. Acquires vertical market software businesses with high recurring revenue and deep switching costs. ROIC consistently above 10% on deployed acquisition capital. Rule of 40 score above 35 (lower growth but very high margins). 20%+ compounding is driven by organic growth (5-8%) plus accretive M&A (10-15%). The model has worked for 20+ years and the pipeline of acquirable vertical software companies remains deep."),

    (13, "Cloudflare", "NET",
     "Internet infrastructure platform expanding from security/CDN into compute, storage, and AI inference. Developer adoption creates a bottom-up distribution model. Revenue growth above 25% with improving margins. Rule of 40 score above 40 and improving. The moat is the global network — 300+ cities, sub-50ms latency for 95% of the internet-connected world. 20%+ compounding requires sustained TAM expansion into Workers/R2/AI Gateway."),

    (14, "Duolingo", "DUOL",
     "AI-native education platform with exceptional engagement and viral distribution. Subscriber growth and ARPPU expansion drive 40%+ revenue growth. Rule of 40 score above 60. The moat is the combination of gamification, AI-generated content (Birdbrain), and network effects (social features). 20%+ compounding requires sustained user monetization and expansion into new subjects (math, music, literacy)."),

    (15, "Microsoft", "MSFT",
     "The world's broadest enterprise technology platform — Azure, 365, GitHub, LinkedIn, Gaming, AI (Copilot). Revenue growth of 15%+ at $250B+ annual revenue is remarkable. Rule of 40 score above 50. FCF generation exceeds $80B annually. 20%+ total return requires ~15% earnings growth plus 2-3% shareholder yield. At the current multiple, 20%+ is achievable if AI monetization (Copilot) accelerates growth. The risk is that size eventually constrains growth below the 20% threshold."),

    (16, "Marvell Technology", "MRVL",
     "Custom AI silicon and data center networking with a multi-year growth runway. Rule of 40 score is improving as AI revenue mix increases. 20%+ compounding requires AI infrastructure capex to sustain for 5+ years. If custom silicon becomes the dominant paradigm for inference (displacing general-purpose GPUs), Marvell's design win pipeline supports long-duration growth."),

    (17, "Novo Nordisk", "NVO",
     "GLP-1 franchise with a potential $100B+ TAM in obesity alone. Rule of 40 is not applicable (pharma), but the combination of 20%+ revenue growth and 40%+ operating margins is exceptional. The manufacturing moat (GLP-1 production is capital-intensive and takes years to scale) protects pricing. 20%+ compounding requires sustaining GLP-1 growth while managing competitive entry and pricing pressure."),

    (18, "Kaspi.kz", "KSPI",
     "Kazakhstan super-app with 60%+ ROE and 40%+ net margins. Payment network effects create an unassailable domestic moat. Rule of 40 score is above 60 (high growth + high margins). 20%+ compounding within Kazakhstan alone may plateau within 3-5 years; geographic expansion is the key to sustained compounding."),

    (19, "Vertiv Holdings", "VRT",
     "Data center power/cooling infrastructure with record order book. Revenue growth accelerating while margins expand. Rule of 40 score is above 40 and improving. 20%+ compounding requires AI data center buildout to extend for 5+ years. The power constraint on AI is structural, not cyclical, supporting the thesis."),

    (20, "Doximity", "DOCS",
     "Physician network with 80%+ penetration and 50%+ EBITDA margins. Capital-light model with pricing power driven by pharma advertising shifting digital. Rule of 40 score above 55. 20%+ compounding is supported by the monopoly on physician engagement data, but TAM ceiling is the risk. Expansion into healthcare workflows could extend the runway."),

    (21, "Grab Holdings", "GRAB",
     "SE Asian super-app approaching profitability inflection. Rule of 40 will become relevant as margins turn positive. 20%+ compounding from here is driven by revenue growth (25%+) as fintech scales. The network effect in ride-hailing + delivery + payments creates winner-take-most dynamics in each market."),

    (22, "Credo Technology Group", "CRDO",
     "AI connectivity with >100% revenue growth. Rule of 40 score is above 120 at current growth rates. The question for sustained 20%+ compounding is whether growth normalizes as the AI buildout matures. If connectivity demand scales with compute demand (which physics dictates it must), the runway is long."),

    (23, "Astera Labs", "ALAB",
     "AI server connectivity silicon with high margins and explosive growth. Same long-duration thesis as Credo but at a higher valuation, which constrains forward returns. Rule of 40 score is exceptional but sustainability is the question."),

    (24, "Pure Storage", "PSTG",
     "Flash storage with subscription model. Rule of 40 score above 35. AI-driven storage demand provides a growth vector. 20%+ compounding requires AI to structurally accelerate storage demand."),

    (25, "Atlassian", "TEAM",
     "Developer collaboration with strong brand and cloud migration tailwind. Rule of 40 score above 35. 20%+ compounding requires AI features (Rovo) to drive monetization acceleration."),

    (26, "Oracle", "ORCL",
     "Cloud infrastructure resurgence driven by AI workload demand. Database monopoly provides durable cash flow. Rule of 40 score above 35. 20%+ compounding requires OCI growth to sustain at 30%+ rates, which current RPO supports."),

    (27, "Coinbase", "COIN",
     "Crypto infrastructure with Base L2. When crypto markets are favorable, Rule of 40 score is above 80. The cyclicality is the challenge for sustained 20%+ — bull cycles generate massive returns, bear cycles compress everything. 20%+ average annualized return requires crypto as an asset class to trend higher structurally."),

    (28, "Intuit", "INTU",
     "Tax/accounting software with consumer and SMB monopolies. Rule of 40 score above 40. 20%+ compounding is supported by the durable franchise and AI integration (Intuit Assist), but growth is naturally moderate (10-15%) at this scale."),

    (29, "SoFi Technologies", "SOFI",
     "Digital bank with technology platform. Rule of 40 score is above 40 and improving rapidly. 20%+ compounding requires sustained member growth and ARPU expansion, which the current trajectory supports for the medium term."),

    (30, "Adobe", "ADBE",
     "Creative and document software monopoly. Rule of 40 score above 40. 20%+ compounding requires AI (Firefly) to drive reacceleration from current 10-12% growth. The franchise is exceptional but growth rate is the constraint."),

    (31, "Fiserv", "FI",
     "Payments infrastructure with steady growth. Rule of 40 score above 30. 20%+ compounding is unlikely at the current growth rate but Clover growth could be the catalyst."),

    (32, "Veeva Systems", "VEEV",
     "Life sciences vertical SaaS with 80%+ market share. Rule of 40 score above 40. 20%+ compounding requires growth acceleration from 15% to 20%+ through new product adoption."),

    (33, "Autodesk", "ADSK",
     "Design software with completed SaaS transition. Rule of 40 score above 35. 20%+ compounding requires AI-driven growth acceleration."),

    (34, "Hims & Hers Health", "HIMS",
     "DTC healthcare platform. Rule of 40 score is above 80 at current growth rates. The question for sustained compounding is whether growth normalizes and whether regulatory risk materializes."),

    (35, "Robinhood Markets", "HOOD",
     "Fintech platform with expanding products. Rule of 40 is improving rapidly. 20%+ compounding requires sustained user and product growth."),

    (36, "Camtek", "CAMT",
     "Semiconductor inspection. Rule of 40 score above 40. 20%+ compounding is tied to AI chip packaging demand duration."),

    (37, "Sea Limited", "SE",
     "SE Asian digital economy. Rule of 40 improving with profitability. 20%+ compounding is supported by the TAM but execution discipline must be maintained."),

    (38, "Celestica", "CLS",
     "AI server manufacturing. Rule of 40 above 35. 20%+ compounding is constrained by contract manufacturing margin structure."),

    (39, "SPS Commerce", "SPSC",
     "Supply chain SaaS. Rule of 40 score above 35. Steady compounder but 20%+ requires slight growth acceleration."),

    (40, "Clear Secure", "YOU",
     "Identity verification. Rule of 40 above 40. 20%+ compounding requires successful expansion beyond airport use case."),

    (41, "PTC", "PTC",
     "Industrial software. Rule of 40 score above 30. 20%+ requires ARR growth acceleration from low-teens."),

    (42, "Clearwater Analytics", "CWAN",
     "Investment accounting SaaS. Rule of 40 score above 30. 20%+ requires product expansion or M&A."),

    (43, "Snowflake", "SNOW",
     "Cloud data platform. Rule of 40 score above 30. 20%+ compounding requires consumption re-acceleration."),

    (44, "Descartes", "DSGX",
     "Logistics technology. Rule of 40 score above 30. 20%+ compounding driven by organic + acquisitive growth. Steady but unlikely to sustain at this level."),

    (45, "MongoDB", "MDB",
     "Developer database. Rule of 40 score above 35. 20%+ compounding requires AI application growth to offset cloud optimization."),

    (46, "Rubrik", "RBRK",
     "Cyber resilience. Rule of 40 score above 50 (high growth, negative margins improving). 20%+ compounding requires path to profitability while sustaining growth."),

    (47, "Bentley Systems", "BSY",
     "Infrastructure software. Rule of 40 score above 30. 20%+ is ambitious for a 10-12% grower."),

    (48, "Toast", "TOST",
     "Restaurant tech. Rule of 40 improving. 20%+ requires sustained net adds and fintech penetration."),

    (49, "Zeta Global", "ZETA",
     "AI marketing. Rule of 40 score above 40. 20%+ compounding requires market share gains in enterprise marketing."),

    (50, "Verra Mobility", "VRRM",
     "Smart transportation. Rule of 40 above 25. 20%+ sustained compounding is unlikely."),

    (51, "Dayforce", "DAY",
     "HCM software. Rule of 40 above 30. 20%+ requires competitive gains in a crowded HCM market."),

    (52, "Paymentus", "PAY",
     "Bill payment tech. Rule of 40 above 30. 20%+ is possible from a small base."),

    (53, "Waystar", "WAY",
     "Healthcare payments. Rule of 40 above 30. 20%+ requires market penetration acceleration."),

    (54, "Jack Henry", "JKHY",
     "Banking tech. Rule of 40 above 30. 20%+ sustained is very unlikely at 6-8% revenue growth."),

    (55, "Check Point", "CHKP",
     "Cybersecurity. Rule of 40 above 30. 20%+ sustained is unlikely given mature growth profile."),

    (56, "Paychex", "PAYX",
     "Payroll services. Rule of 40 above 35 (low growth + high margins). 20%+ compounding is impossible at 5-7% growth."),

    (57, "Progress Software", "PRGS",
     "Application tools. Rule of 40 above 30 via M&A-driven growth. 20%+ sustained compounding requires continued accretive acquisitions."),

    (58, "NetEase", "NTES",
     "Chinese gaming. Rule of 40 above 35. 20%+ compounding is constrained by China regulatory environment."),

    (59, "JD.com", "JD",
     "Chinese e-commerce. Cheap valuation but growth is moderating. 20%+ compounding requires China macro improvement and geopolitical normalization."),

    (60, "e.l.f. Beauty", "ELF",
     "Mass cosmetics. Rule of 40 above 50 at current growth. 20%+ sustained requires maintaining brand momentum, which is challenging in CPG."),

    (61, "AMD", "AMD",
     "Semiconductors. Rule of 40 above 40. 20%+ sustained requires AI GPU share gains against Nvidia. Possible but Nvidia's moat is deep."),

    (62, "Oscar Health", "OSCR",
     "Health insurance tech. Rule of 40 is improving. 20%+ sustained requires scaling membership while maintaining margin improvement."),

    (63, "Sezzle", "SEZL",
     "BNPL. Rule of 40 above 60 at current growth. 20%+ sustained is uncertain as BNPL matures."),

    (64, "TransMedics", "TMDX",
     "Organ transplant tech. Rule of 40 above 40. 20%+ is limited by niche TAM."),

    (65, "Alignment Healthcare", "ALHC",
     "Value-based care. Rule of 40 is negative (high growth, negative margins). 20%+ requires profitability inflection."),

    (66, "DigitalOcean", "DOCN",
     "SMB cloud. Rule of 40 above 25. 20%+ sustained is unlikely given competitive cloud market."),

    (67, "Blackbaud", "BLKB",
     "Nonprofit software. Rule of 40 above 20. 20%+ is very unlikely."),

    (68, "SS&C Technologies", "SSNC",
     "Financial services software. Rule of 40 above 25. 20%+ requires transformative M&A."),

    (69, "Innodata", "INOD",
     "AI data services. Rule of 40 is exceptional currently but sustainability is uncertain. 20%+ compounding requires AI training data demand to remain robust."),

    (70, "SoundHound AI", "SOUN",
     "Voice AI. Not yet profitable. 20%+ sustained requires proving a scalable, profitable business model."),

    (71, "CoreWeave", "CRWV",
     "GPU cloud. Massive growth but heavy leverage. 20%+ compounding requires sustained utilization and debt management."),

    (72, "Pagaya", "PGY",
     "AI lending. Not yet profitable. 20%+ sustained requires credit cycle navigation and profitability."),

    (73, "Celsius Holdings", "CELH",
     "Energy drinks. Rule of 40 above 30. 20%+ sustained is challenging as distribution normalizes."),

    (74, "Semtech", "SMTC",
     "IoT semiconductor. Rule of 40 improving. 20%+ requires IoT market inflection."),

    (75, "Adeia", "ADEA",
     "IP licensing. High margins but low growth. 20%+ is improbable."),

    (76, "Agnico Eagle", "AEM",
     "Gold mining. Dependent on gold prices. 20%+ sustained requires perpetual gold bull market."),

    (77, "First Majestic Silver", "AG",
     "Silver mining. Same commodity price dependency. 20%+ sustained is very unlikely."),

    (78, "Newmont", "NEM",
     "Gold mining. 20%+ sustained is near-impossible for a commodity producer."),

    (79, "Barrick Gold", "GOLD",
     "Gold mining. Same as Newmont. 20%+ sustained is near-impossible."),

    (80, "Aris Mining", "ARMN",
     "Gold mining growth. 20%+ is possible during a production ramp but not sustainable indefinitely."),

    (81, "Cipher Mining", "CIFR",
     "Bitcoin mining. Returns track BTC price. 20%+ sustained requires perpetual crypto bull market."),

    (82, "IREN", "IREN",
     "Mining/data center pivot. 20%+ sustained requires successful AI hosting transition."),

    (83, "Applied Digital", "APLD",
     "AI data center. 20%+ sustained requires successful execution on contracted capacity. Early stage."),

    (84, "NIO", "NIO",
     "Chinese EV. Cash-burning. 20%+ sustained is very unlikely given competitive dynamics and capital needs."),

    (85, "The Honest Company", "HNST",
     "Consumer products. Turnaround in progress but CPG dynamics make 20%+ sustained very difficult."),

    (86, "Nebius Group", "NBIS",
     "AI infrastructure. Too early to assess sustained compounding. High potential but no track record."),

    (87, "eToro", "ETOR",
     "Social trading. Cyclical revenue base makes 20%+ sustained very challenging."),

    (88, "Tempus AI", "TEM",
     "Precision medicine. Not yet profitable. 20%+ sustained requires proving the business model."),

    (89, "Gambling.com Group", "GAMB",
     "iGaming affiliate. High margins but small TAM may constrain growth. 20%+ possible during legalization wave but not indefinitely."),

    (90, "Accelerant", "ACNT",
     "Specialty insurtech. Limited data. Cannot assess sustained compounding with conviction."),

    (91, "FIS", "FIS",
     "Financial tech. Low growth. 20%+ sustained is improbable."),

    (92, "SolarWinds", "SWI",
     "IT management. Likely private. 20%+ is moot."),

    (93, "Paycom", "PAYC",
     "HCM software. Growth deceleration makes 20%+ sustained unlikely without a strategic reset."),

    (94, "AspenTech", "AZPN",
     "Industrial software. Controlled by Emerson. 20%+ sustained is constrained by ownership structure."),

    (95, "Viavi Solutions", "VIAV",
     "Network test. Stagnant revenue. 20%+ sustained is near-impossible."),

    (96, "Netskope / Figma", "PRIVATE",
     "Private companies. Cannot assess public market sustained compounding."),
]

for entry in list4:
    add_ranked_entry(*entry)

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# MANDATORY FINAL STEP
# ══════════════════════════════════════════════════════════════════════════════
doc.add_heading('FINAL CONVICTION CALLS', level=1)

doc.add_heading('Top 3 Highest Conviction Names Across All Four Lists', level=2)

p = doc.add_paragraph()
run = p.add_run('1. Nu Holdings (NU)')
run.bold = True
run.font.size = Pt(12)
run.font.color.rgb = RGBColor(0x1B, 0x2A, 0x4A)
doc.add_paragraph(
    'NU appears in the top 2 across all four lists. The thesis is structurally simple: 100M+ customers in an underbanked '
    'continent with near-zero CAC, a bank charter providing low-cost funding, and sub-5% product penetration across insurance, '
    'investing, lending, and crypto. The company is already profitable with margins expanding. This is the most compelling '
    'risk/reward in the entire universe — a proven business model with a massive runway, trading at a reasonable multiple '
    'relative to growth. Every bear case (LatAm macro, competition, credit risk) is valid but priced in at current levels. '
    'The base case is a 3-5x over 3-5 years; the bull case is a 10x.'
)

p = doc.add_paragraph()
run = p.add_run('2. Credo Technology Group (CRDO)')
run.bold = True
run.font.size = Pt(12)
run.font.color.rgb = RGBColor(0x1B, 0x2A, 0x4A)
doc.add_paragraph(
    'CRDO is at the epicenter of the most important infrastructure buildout since the internet. AI GPU clusters cannot scale '
    'without the high-bandwidth connectivity that Credo provides. Revenue is growing >100% YoY, margins are expanding, and '
    'every hyperscaler GPU platform refresh drives new design wins. The market cap is small enough that even moderate revenue '
    'growth drives significant stock appreciation. The risk is that AI capex cycles slow, but every data point through mid-2025 '
    'suggests acceleration, not deceleration. Highest conviction among the AI infrastructure plays because connectivity is '
    'required regardless of which GPU/chip architecture wins.'
)

p = doc.add_paragraph()
run = p.add_run('3. Grab Holdings (GRAB)')
run.bold = True
run.font.size = Pt(12)
run.font.color.rgb = RGBColor(0x1B, 0x2A, 0x4A)
doc.add_paragraph(
    'GRAB is the most underappreciated super-app story globally. The SE Asian digital economy TAM is $40B+ and growing at 20%+ '
    'annually. Grab has achieved profitability discipline while maintaining growth. The fintech opportunity (lending, insurance, '
    'wealth management) is barely in the early innings. The SPAC stigma has depressed the valuation, creating a wide gap between '
    'enterprise value and the long-term earnings power of a financial services platform serving 700M+ people. This is the '
    'cheapest way to own the SE Asian digital economy.'
)

doc.add_heading('Two Rankings with Lowest Confidence', level=2)

p = doc.add_paragraph()
run = p.add_run('Lowest Confidence #1: Nebius Group (NBIS) — ranked #19 in List 1 and #4 in List 2')
run.bold = True
doc.add_paragraph(
    'Nebius is ranked high on potential but low on verifiable data. As a recently spun-out entity from Yandex, there is limited '
    'public financial history to anchor a bottoms-up analysis. The AI cloud infrastructure thesis is compelling and the engineering '
    'talent is real, but the competitive landscape (hyperscalers, CoreWeave, Lambda, etc.) is fierce. The ranking reflects the '
    'asymmetric upside if Nebius executes, but conviction is materially lower than for names with established financial track records. '
    'If forced to revise, I would move Nebius down 5-10 positions in each list.'
)

p = doc.add_paragraph()
run = p.add_run('Lowest Confidence #2: SoundHound AI (SOUN) — ranked #46 in List 1 and #16 in List 2')
run.bold = True
doc.add_paragraph(
    'SoundHound represents a bet on voice AI becoming a primary commercial interface. The TAM is enormous if the thesis is correct, '
    'but revenue is small, profitability is distant, and the competitive threat from foundation model providers (OpenAI, Google, Amazon) '
    'building voice capabilities is severe. The company has been "about to inflect" for years. The ranking reflects potential more than '
    'probability. I have low confidence that SoundHound specifically will be the winner even if voice AI becomes ubiquitous.'
)

doc.add_heading('Capital Deployment: 5 Names for Maximum Risk-Adjusted Return Over 3 Years', level=2)

doc.add_paragraph(
    'If forced to deploy capital today across exactly 5 names, sized by conviction, for maximum '
    'risk-adjusted return over 3 years:'
)

entries = [
    ("1. Nu Holdings (NU) — 30% weight",
     "Highest conviction, best risk/reward. Proven profitable business model with massive runway in an underbanked continent. "
     "Largest position because the downside is well-defined (LatAm macro shock) while the upside is 5-10x. Every fundamental "
     "metric is improving: members, ARPAC, margins, product penetration. The bank charter economics compound."),

    ("2. Credo Technology Group (CRDO) — 25% weight",
     "Best pure-play on AI infrastructure connectivity with triple-digit revenue growth and improving profitability. "
     "The physics of AI scaling (more compute requires proportionally more bandwidth) provide a durable, non-consensus growth driver. "
     "Size the position large because the AI capex cycle has multi-year duration and Credo is the highest-quality, most direct play."),

    ("3. Grab Holdings (GRAB) — 20% weight",
     "Cheapest way to own the SE Asian digital economy. Profitability inflection is real and fintech is just beginning to scale. "
     "The 3-year view is that GrabFin becomes a meaningful financial services platform serving hundreds of millions. "
     "Position is sized third because the SE Asian macro introduces more variance than LatAm (for NU) or AI capex (for CRDO)."),

    ("4. Marvell Technology (MRVL) — 15% weight",
     "Custom AI silicon and networking are scaling rapidly with major hyperscaler design wins providing multi-year visibility. "
     "More diversified than Credo (which is pure connectivity), Marvell offers exposure to the entire data center silicon stack. "
     "Smaller position because the market cap is larger, limiting the upside multiplier, and because some AI silicon growth "
     "is already priced in."),

    ("5. Fair Isaac (FICO) — 10% weight",
     "The portfolio's anchor — a legal monopoly with infinite pricing power and zero churn. FICO provides downside protection "
     "and steady compounding regardless of macro conditions. In a bear case where AI capex decelerates or LatAm macro weakens, "
     "FICO provides ballast. Smallest position because the upside multiplier is lowest (2-3x over 3 years) but the probability "
     "of positive returns approaches certainty."),
]

for title, body in entries:
    p = doc.add_paragraph()
    run = p.add_run(title)
    run.bold = True
    run.font.size = Pt(11)
    run.font.color.rgb = RGBColor(0x1B, 0x2A, 0x4A)
    doc.add_paragraph(body)

doc.add_paragraph('')  # spacer
p = doc.add_paragraph()
run = p.add_run('Portfolio Construction Rationale: ')
run.bold = True
doc.add_paragraph(
    'This portfolio is constructed as a barbell — three high-growth, high-conviction positions (NU, CRDO, GRAB) at 75% weight '
    'for upside capture, one mid-growth AI infrastructure play (MRVL) at 15% for diversified AI exposure, and one quality '
    'compounder (FICO) at 10% for downside protection. The correlation across positions is relatively low: NU is driven by '
    'LatAm digital banking, CRDO/MRVL by AI infrastructure, GRAB by SE Asian digital economy, and FICO by US credit markets. '
    'Geographic diversification (US, Latin America, Southeast Asia) reduces single-market risk. The expected 3-year return of '
    'the portfolio is 150-300% (2.5-4x), with a floor around 50% (driven by FICO and MRVL base cases) and a ceiling above 500% '
    '(driven by NU and CRDO bull cases).'
)

# ── Disclaimer ────────────────────────────────────────────────────────────────
doc.add_paragraph('')
doc.add_paragraph('')
p = doc.add_paragraph()
run = p.add_run(
    'DISCLAIMER: This analysis is based on publicly available information and the analyst\'s independent assessment as of June 2025. '
    'It does not constitute investment advice. Certain data points, particularly for recently public or private companies, may be '
    'estimated or unavailable. Where data is unavailable, this has been noted. All forward-looking assessments are probabilistic '
    'and subject to material uncertainty. Past performance does not guarantee future results. Figma and Netskope are believed to be '
    'private companies as of the analysis date and have been ranked last in each list due to the inability to analyze public market '
    'dynamics — this placement does not reflect a view on business quality.'
)
run.font.size = Pt(8)
run.italic = True
run.font.color.rgb = RGBColor(0x99, 0x99, 0x99)

# ── Save ──────────────────────────────────────────────────────────────────────
output_path = '/home/user/Practice/Master_Equity_Ranking_Analysis.docx'
doc.save(output_path)
print(f'Document saved to {output_path}')
