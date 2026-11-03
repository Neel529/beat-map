# Premium grocery discovery — Jaipur

You are helping Nilesh find **independent premium grocery / gourmet / dry-fruit / organic stores in Jaipur** that could stock ChoKhoChhe AmlaPrash (premium Chyawanprash-style product, about ₹700 for 500 g). He will visit them himself. The output gets merged into the Beat Map app in this repo (`../../dev/index.html`).

## Why this is hard
These shops are almost never called "premium grocery". They show up as dry fruit marts, departmental stores, provision stores, organic stores, gourmet / imported-food stores, health-food stores, and supermarkets in rich neighbourhoods. You have to **judge** premium-ness from signals, not names.

## Rules
- Everything must be free. No paid APIs, no sign-ups.
- **Exclude chains and franchises** that buy from a head office: Reliance (Fresh/Smart), DMart, More, Easyday, Spencer's, Nature's Basket, Foodhall, Big Bazaar, 24Seven, 6Ten, Kirana King, Organic India / Himalaya / Patanjali brand stores, quick-commerce dark stores. (They can't decide to stock a new brand at the counter.) List them in `excluded.csv` with the reason, don't silently drop them.
- Don't invent shops, phones or coordinates. Every row needs a source URL you actually opened.
- `existing_shops.csv` holds the 571 shops already in the app. Mark a candidate `duplicate_of` if it matches one (same name nearby, same phone, or within ~40 m).
- Go slowly on Google Maps (human pace). If you hit a CAPTCHA or block, stop that source and say so.
- Ask Nilesh before anything that costs money, logs in, or posts anything.

## Workflow (do the steps in order; save after each so work can resume)
1. **Plan queries** → `queries.md`. Combine *signals* × *areas*:
   - signals: dry fruits, gourmet, imported food / chocolates, organic store, health food, departmental store, provision store, supermarket, cold-pressed oil, millet store, ayurvedic & organic
   - areas (affluent first): C-Scheme, Ashok Nagar, MI Road, Bani Park, Civil Lines, Raja Park, Jawahar Nagar, Bapu Nagar, Malviya Nagar (Gaurav Tower / Sector areas), Vaishali Nagar (Amrapali / Gautam Marg), Mansarovar (Madhyam Marg), Tonk Road / Durgapura, Jagatpura, Gandhi Path, C-Scheme malls & markets.
2. **Collect candidates** → `candidates.csv` (name, area, address, phone, lat, lng, rating, review_count, source_url, maps_url, found_by_query). Sources, in this order:
   - Google Maps in the browser (Claude in Chrome): search each query, open each result, read name, category, address, phone, rating, review count, price level, coordinates from the URL (`!3d<lat>!4d<lng>` or `@lat,lng`).
   - magicpin category pages for Jaipur (Grocery, Dry Fruits, Organic, Gourmet) — store pages carry exact coordinates in `<meta name="ICBM">`.
   - Justdial / Zomato-style listings only via the browser, for phone numbers.
3. **Score premium-ness** → add columns to `candidates.csv`. 0–2 each, max 10:
   | Signal | 0 | 1 | 2 |
   |---|---|---|---|
   | Range | Basic staples only | Some branded/packaged premium | Imported / gourmet / dry fruits / organic clearly visible in photos or reviews |
   | Location | Ordinary market | Good residential market | Affluent pocket / high-street |
   | Reviews mention quality, imported, organic, "costly", "premium" | None | 1–2 mentions | Several |
   | Rating & volume | <4.0 or <20 reviews | 4.0+ with 20–100 | 4.2+ with 100+ |
   | Price level / store format | Small counter shop | Self-service / neat shelving | Large self-service, gift hampers, billing counters |
   Keep a short `why` note (one line, with what you saw).
4. **Classify**: `premium` (score ≥7), `maybe` (4–6), `not premium` (≤3), `chain` (excluded).
5. **Deliver**:
   - `premium_grocery_jaipur.csv` — premium + maybe, not duplicates, sorted by score, columns: name, area, address, phone, lat, lng, score, class, why, source_url, maps_url.
   - `excluded.csv` — chains and duplicates with reason.
   - `SUMMARY.md` — counts per area, top 25, what sources failed.
6. **Stop and show Nilesh the top 25** before touching the app. Only after he says go: add the shops to the Beat Map data as list `R`, type "Premium grocery", with exact pins (q=1) where coordinates came from Maps/magicpin.

## Progress
Keep `PROGRESS.md` updated (last query done, counts, next step) so a new session can continue.
