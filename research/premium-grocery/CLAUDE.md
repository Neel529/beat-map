# Premium grocery discovery — Jaipur

You are helping Nilesh find **independent premium grocery / gourmet / dry-fruit / organic stores in Jaipur** that could stock ChoKhoChhe AmlaPrash (premium Chyawanprash-style product, about ₹700 for 500 g). He will visit them himself. The output will later be merged into the Beat Map app by Nilesh.

## Why this is hard
These shops are almost never called "premium grocery". They show up as dry fruit marts, departmental stores, provision stores, organic stores, gourmet / imported-food stores, health-food stores, and supermarkets in rich neighbourhoods. You have to **judge** premium-ness from signals, not names.

## Rules
- Everything must be free. No paid APIs, no sign-ups.
- **Exclude chains and franchises** that buy from a head office: Reliance (Fresh/Smart), DMart, More, Easyday, Spencer's, Nature's Basket, Foodhall, Big Bazaar, 24Seven, 6Ten, Kirana King, Organic India / Himalaya / Patanjali brand stores, quick-commerce dark stores. (They can't decide to stock a new brand at the counter.) List them in `excluded.csv` with the reason, don't silently drop them.
- Don't invent shops, phones or coordinates. Every row needs a source URL you actually opened.
- The 571 shops already in the app are in three files, one per category:
  - `existing_retail_grocery_stores.csv` (178): retail and grocery
  - `existing_medical_stores.csv` (353): chemists
  - `existing_patanjali_stores.csv` (40): Patanjali outlets
  Check every candidate against **all three**. Mark it `duplicate_of` = that shop's id if it matches (same name nearby, same phone, or within ~40 m). A retail shop already listed but never judged premium is still worth scoring: mark it `already_listed`, don't drop it.
- Go slowly on Google Maps (human pace). If you hit a CAPTCHA or block, stop that source and say so.
- Ask Nilesh before anything that costs money, logs in, or posts anything.

## Benchmark: shops Nilesh knows are premium (names as he remembers them, may be inexact)
- Exotica (Raja Park)
- Mashhoor Punjabi (Raja Park). Already in `existing_retail_grocery_stores.csv` as RP002 "Mashhoor Punjabi Kirana Store", but labelled plain "Kirana": it must come out as premium after scoring.
- Night Jar (several locations in Jaipur). Check what it is: web search mostly shows "The Night Jar Cocktail Room" (Malviya Nagar) and "Kohhee by The Night Jar" (C-Scheme). Find the retail / gourmet outlets, if any, and say clearly if it's a café/bar and not a shop.
- Town Market
Nilesh may add more to `benchmark.txt`; read it if present.

**Pass/fail rule:** the run is not finished until every benchmark shop has been found **by your method** (not typed in by hand) and scored. For each one record in `benchmark_check.md`: found by which query/sweep, score, class. If one is missed, write why (wrong words? not on the source? outside the swept area? scored low?), fix the method (add the search, widen the sweep, change the scoring), rerun that part, and note what else the fix surfaced.

## Lesson from the first attempt (why these were missed)
The original 571 shops came from listing sites (magicpin, directories) by category. Premium shops in Jaipur are mostly **not** on those sites, or are filed as plain "kirana" / "departmental". A quick web search for Exotica or Town Market returns almost nothing. They live on **Google Maps** (and Instagram / local city blogs). So:
1. **Primary source = a Google Maps area sweep, not keyword search.** For each affluent area: centre the map there, search the generic categories ("grocery store", "supermarket", "departmental store", "dry fruits", "gourmet", "organic store"), scroll the whole results list, and open **every** result. Then pan to the neighbouring blocks and repeat until results stop being new. Use the "Similar places / People also search for" list on every good shop.
2. **Re-score the already-listed retail shops** (`existing_retail_grocery_stores.csv`, 178 shops): open each on Google Maps and score it. Some premium shops are already there under a plain label (like Mashhoor Punjabi).
3. **Secondary sources:** local Jaipur city blogs and listicles (e.g. allaboutjaipur.com articles on gourmet / organic / dry-fruit stores), "best gourmet store in Jaipur" type articles, and Instagram handles mentioned there. Every shop found this way must then be confirmed on Google Maps (address, coordinates).
4. Keyword search with the vocabulary above is the **third** layer, to catch what the sweep missed.

## Search vocabulary (use all of it; names rarely say "premium")
Search with these terms, alone and combined with each area. The scoring in step 3 decides what is premium, not the search term.

**Store types (English):** grocery store, departmental store, department store, supermarket, super market, hypermarket, mini mart, mart, general store, provision store, provisions, convenience store, food store, food mart, fresh mart, family store, household store, daily needs, superstore, wholesale and retail.

**Store types (Hindi / Hinglish, as Jaipur shops write them):** kirana store, kirana bhandar, parchun / parchoon ki dukan, general store, provision bhandar, bhandar, mewa bhandar, meva bhandar, dry fruit bhandar, kaju badam store, misthan & namkeen with dry fruits, pansari / pansari ki dukan (herbs + spices), masala bhandar, ghee bhandar.

**Dry fruits & nuts:** dry fruits, dry fruit store, dry fruit mart, dry fruit house, dry fruit centre, nuts and dry fruits, dryfruits & spices, mewa, kesar / saffron, almonds, cashew, pista, dates / khajoor, makhana, premium dates, gift boxes, dry fruit hampers, Diwali hampers.

**Gourmet / imported:** gourmet store, gourmet foods, gourmet pantry, deli, delicatessen, imported food, imported products, imported chocolates, foreign goods, foreign items, international food store, chocolate shop, chocolate house, cheese, olive oil, pasta & sauces, breakfast cereals imported, Korean / Japanese snacks, specialty foods, fine foods, pantry store, food hall (only if not a chain), confectionery store, bakery & gourmet, hamper store, gift hampers.

**Organic / health / natural:** organic store, organic food store, organic shop, natural foods, health food store, health store, wellness store, nutrition store (food, not supplements only), millet store, millets, cold pressed oil, kachi ghani oil, wood pressed oil, A2 ghee, desi ghee store, bilona ghee, raw honey, jaggery / gur, farm fresh, farm to home, sugar-free store, diabetic food store, gluten free, ayurvedic & organic, herbal store.

**Name patterns that often hide premium shops:** "... Fresh", "... Mart", "... Basket", "... Pantry", "... Bazaar", "... Emporium", "... Super Store", "... Departmental", "... Sons", "... & Co", "... Traders" (retail counter only), "... Agencies" (check it's a shop, not a distributor), "... Nuts", "... Dry Fruits", "... Organics", "... Naturals", "... Foods", "... Gourmet", "... Deli".

**Places to look in (affluent markets / high streets):** MI Road, Ashok Marg & Bhagwan Das Road (C-Scheme), Prithviraj Road, Sardar Patel Marg, Bais Godam, Panch Batti, Raja Park main market, Adarsh Nagar, Jawahar Nagar shopping centres, Bapu Nagar / University Road, Malviya Nagar (Gaurav Tower area, sector markets), Vaishali Nagar (Amrapali Marg, Gautam Marg, Queens Road), Mansarovar (Madhyam Marg, Shipra Path), Tonk Road / Durgapura, Jagatpura (Mahal Road), Bani Park, Civil Lines, Gandhi Path, and malls / market complexes in these areas. Confirm each place on the map; don't assume.

**Also check:** "near me"-style searches on Google Maps while centred on each area, and the "People also search for" / "Similar places" list on each good shop's Maps page. That's often where the best premium shops show up.

## Workflow (do the steps in order; save after each so work can resume)
1. **Plan queries** → `queries.md`. Combine the search vocabulary above with each area, most promising first (dry fruits, gourmet/imported, organic, departmental store in affluent areas). Don't run every combination blindly: when an area keeps returning the same shops, move on. Note in `queries.md` which queries found new shops.
2. **Collect candidates** (sweep first, see 'Lesson' above; then re-score existing retail; then blogs; then keywords) → `candidates.csv` (name, area, address, phone, lat, lng, rating, review_count, source_url, maps_url, found_by_query). Sources, in this order:
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
6. **Stop and show Nilesh the top 25** with the one-line reason for each. Don't modify any app files; he will bring the final CSV to be merged.

## Progress
Keep `PROGRESS.md` updated (last query done, counts, next step) so a new session can continue.
