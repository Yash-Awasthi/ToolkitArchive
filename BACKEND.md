# Backend / Database / Deploy / Auth — Free-Tier Reference (June 2026)

> Everything to ship the backend of a vibe-coded app for **$0** — BaaS, databases, hosting, auth, vector stores, and the glue (email/payments/storage).
> Free tiers verified ~June 2026. They change fast (PlanetScale killed its free tier in 2024; Fly.io dropped free for new users; Netlify went credit-based) — confirm before architecting.

---

## Part 1 — Backend-as-a-Service (auth + DB + storage + functions in one)

| Tool | Stack | Free tier | Self-host | Best for | Link |
|---|---|---|---|---|---|
| **Supabase** | Postgres + RLS + pgvector | 2 projects, 500MB DB, 5GB egress, 50K MAU | Yes (Docker) | Default pick; relational + AI | supabase.com |
| **Convex** | Reactive TS document store | Generous free, real-time built-in | No | Real-time TS apps, auto-sync | convex.dev |
| **Appwrite** | TS/Go, multi-DB | 2 projects (pause after 7d idle), no card | Yes (Docker, 50K★) | Open-source ownership | appwrite.io |
| **PocketBase** | Single Go binary + SQLite | Free — runs on $5 VPS | Yes (it's the binary) | Lightest backend, side projects | pocketbase.io |
| **Nhost** | Postgres + Hasura GraphQL | Free tier | Yes | GraphQL-first / JAMstack | nhost.io |
| **InstantDB** | Relational realtime ("Firebase + relations") | Generous free | No | Optimistic-UI realtime apps | instantdb.com |
| **Firebase** | NoSQL + auth + functions | Spark plan free (Google) | No | Google ecosystem, mobile | firebase.google.com |
| **Encore** | TS/Go backend framework + infra | Free OSS, cloud free tier | Yes | Type-safe backend + IaC | encore.dev |
| **Wasp** | Full-stack React/Node DSL | Free OSS | Yes | Opinionated full-stack | wasp.sh |
| **Microsoft Rayfin** | Fabric/OneLake BaaS (TS code → SQL DB + Entra ID auth + GraphQL API + hosting) | Preview, perpetual free tier | No (deploys to Fabric tenant) | Agent-first; data lands in OneLake (no ETL). Replit launch partner. ⚠️ Entra-ID-only auth | microsoft.com/microsoft-fabric |

---

## Part 2 — Serverless / Edge Databases

| DB | Engine | Free tier | Notes | Link |
|---|---|---|---|---|
| **Neon** | Serverless Postgres | 0.5GB/project, 100 CU-hrs/mo, up to 100 projects | Branching, scale-to-zero. Owned by Databricks | neon.tech |
| **Turso** | Edge SQLite/libSQL | 1–5GB, 500M row reads/mo, 3 active DBs | DB-per-user at scale; no scale-to-zero | turso.tech |
| **Xata** | Postgres + search | 10GB free | Built-in full-text search, branching | xata.io |
| **MongoDB Atlas** | Document | M0 cluster (~512MB) free | Classic NoSQL | mongodb.com |
| **CockroachDB** | Distributed SQL | Basic free tier | Global, Postgres-compatible | cockroachlabs.com |
| **Upstash** | Serverless Redis / Vector / Kafka | Redis 256MB + 500K cmds/mo; Vector 10K free | True pay-per-request | upstash.com |
| **Supabase DB** | Postgres | (see BaaS above) | pgvector for AI | supabase.com |
| **EdgeDB / Gel** | Graph-relational on Postgres | Free tier | Modern query language | geldata.com |
| **PlanetScale** | Vitess MySQL + Postgres | ❌ **no free tier** — from $5/mo | Killed free Hobby Apr 2024 | planetscale.com |

> **Most free storage:** Xata (10GB) > Turso (1–5GB) > Atlas/Neon (~0.5GB). **Most free reads:** Turso (500M rows/mo).

---

## Part 3 — Hosting / Deploy / PaaS

| Platform | Best for | Free tier | Gotcha | Link |
|---|---|---|---|---|
| **Cloudflare Pages** | Static / Jamstack | **Unlimited bandwidth**, 500 builds/mo, 100 sites | 1 concurrent build | pages.cloudflare.com |
| **Cloudflare Workers** | Edge functions/APIs | 100K req/day, 10ms CPU, 128MB; KV/D1/R2 free tiers; **no egress fees** | 10ms CPU on free | workers.cloudflare.com |
| **Vercel** | Next.js | Hobby: 100GB transfer, 1M func calls, 1GB Blob | **No commercial use** on Hobby; 60s timeout | vercel.com |
| **Netlify** | Static + commercial OK | 300 credits/mo (~30GB, ~20 builds) | Credit-based since Sep 2025 | netlify.com |
| **Render** | Full-stack + free Postgres | Free web service 512MB + free Postgres + custom domains | Cold start after 15min idle | render.com |
| **Railway** | Quick full-stack deploys | $5 first month, then $1/mo credit | Pauses when credit out | railway.app |
| **Koyeb** | Containers + free Postgres | 1 vCPU/512MB + Postgres scale-to-zero | **No outbound internet on free** | koyeb.com |
| **Fly.io** | Container control, multi-region | ❌ no free tier for new users (card + 2h demo) | Treat as paid | fly.io |
| **Deno Deploy** | TS/JS edge | Generous free | Deno runtime | deno.com/deploy |
| **Coolify** | Self-host PaaS (Heroku alt) | Free OSS — bring a $5 VPS | You run the server | coolify.io |
| **Dokku** | Git-push PaaS on your VPS | Free OSS | CLI-driven | dokku.com |
| **Northflank** | GPU PaaS + true BYOC (AWS/Azure/GCP/Oracle/bare-metal) | Always-on free sandbox (2 services, 2 DBs) | Full data plane in *your* VPC, infra billed at list (no markup). NVIDIA B200→A100, MIG/time-slicing. SOC 2 Type 2 | northflank.com |
| **SnapDeploy** | Minimal container hosting | 10 deploys/day free · $12/mo always-on | Lightweight; verify specs on vendor page | snapdeploy.io |
| **Zeabur / Sevalla / Koyeb** | Modern PaaS | Various free trials | — | — |

---

## Part 4 — Auth (MAU = monthly active users)

| Provider | Free tier | Notable | Self-host | Link |
|---|---|---|---|---|
| **WorkOS (AuthKit)** | **1,000,000 MAU** free (social, MFA, passkeys, RBAC) | SSO connections $125/mo each | No | workos.com |
| **Clerk** | 50,000 MAU (raised Feb 2026) | Best React/Next DX, drop-in UI; no SCIM | No | clerk.com |
| **Stytch** | 25,000 MAU | Passwordless-first (now Twilio) | No | stytch.com |
| **Kinde** | 10,500 MAU | Auth + flags + billing, flat pricing | No | kinde.com |
| **Better-Auth** | Unlimited (self-host) | OSS library; Auth.js folded into it | Yes | better-auth.com |
| **Supabase Auth** | Bundled w/ Supabase (50K MAU) | Free w/ the BaaS | Yes | supabase.com |
| **Logto** | Free tier (OSS) | OIDC, multi-tenant | Yes | logto.io |
| **SuperTokens** | Free self-host, 5K MAU cloud | OSS, full control | Yes | supertokens.com |
| **ZITADEL** | 25K MAU free cloud | Enterprise CIAM, Go single-binary, event-sourced, first-class multi-tenant (B2B SaaS). OIDC/SAML/LDAP. ~13.5K★ | Yes | zitadel.com |
| **Authentik** | Free (OSS) | **Proxy/forward-auth mode** — enforce MFA/SSO in front of ANY app (incl. legacy, no OIDC) with zero code changes. Also IdP + LDAP. ~21K★ | Yes | goauthentik.io |
| **Ory / Hanko / Stack Auth** | OSS free | Passkeys, modern | Yes | ory.sh · hanko.io · stack-auth.com |

> **Most free MAU:** WorkOS (1M). **Best DX:** Clerk. **Zero-cost full control:** Better-Auth / SuperTokens.

---

## Part 5 — Vector DBs / AI Data Infra

| Tool | Free tier | Notes | Link |
|---|---|---|---|
| **pgvector** | Free (Postgres ext) | Use inside Supabase/Neon — no extra service | github.com/pgvector |
| **Qdrant** | 1GB free cloud cluster | OSS, Rust, fast | qdrant.tech |
| **Pinecone** | Free starter index | Managed, popular | pinecone.io |
| **Weaviate** | 14-day sandbox / OSS self-host | Hybrid search | weaviate.io |
| **Chroma** | Free OSS (embedded) | Easiest local RAG | trychroma.com |
| **Milvus / Zilliz** | OSS + free cloud tier | Scale | milvus.io |
| **Zilliz Vector Lakebase** | Public preview, $100 credits | Milvus-based — unifies real-time search + batch analytics + external data-lake search on one zero-copy data plane. 3 serving tiers, BYOC, 30+ regions (Jun 2026) | zilliz.com |
| **ScyllaDB Vector Search** | In ScyllaDB Cloud | Native vector in the NoSQL DB (GA Jan 2026) — embeddings beside operational data, CQL `ANN OF`. Rust/USearch, HNSW, 1B+ vectors, ~1.7ms P99 | scylladb.com |
| **Actian VectorAI DB** | Free community (5K vectors) | Edge/air-gapped/on-prem — embeds in-app, runs on Jetson/Pi. ~22x faster vs Milvus/Qdrant (10M-vec VDBBench). HIPAA/GDPR/SOC2. Paid from $417/mo | actian.com |
| **LanceDB** | Free OSS (embedded) | Serverless, multimodal | lancedb.com |
| **Upstash Vector** | 10K vectors free | Serverless | upstash.com |
| **Turbopuffer** | Usage-based, cheap | Object-storage-backed | turbopuffer.com |

---

## Part 6 — Shipping Glue (email · payments · storage · cron)

| Need | Tool | Free tier | Link |
|---|---|---|---|
| Email | **Resend** | 3K emails/mo, 100/day | resend.com |
| Email | Loops / Postmark / Brevo | Free tiers | — |
| Payments | **Stripe** | Pay-as-you-go (no monthly) | stripe.com |
| Payments (MoR) | **Polar** / Lemon Squeezy / Paddle | % per sale, no monthly | polar.sh |
| File upload | **UploadThing** | 2GB free | uploadthing.com |
| Object storage | **Cloudflare R2** | 10GB free, no egress fee | r2.cloudflare.com |
| Background jobs | **Trigger.dev** / Inngest | Free tiers | trigger.dev · inngest.com |
| Realtime | Ably / Pusher / Liveblocks | Free tiers | — |
| Search | Meilisearch / Typesense / Algolia | OSS / free tier | — |

---

## Zero-Dollar Stack (reference)

```
Frontend  : Cloudflare Pages (unlimited bandwidth)
Backend   : Supabase (Postgres + Auth + Storage, 50K MAU)
   or      PocketBase on a $5 VPS (or free Oracle/Fly demo)
DB extra  : Neon / Turso for a second free Postgres/SQLite
Auth      : WorkOS (1M MAU) or Supabase Auth (bundled)
Vectors   : pgvector inside Supabase (no extra service)
Edge fns  : Cloudflare Workers (100K req/day)
Email     : Resend (3K/mo)
Payments  : Stripe / Polar (no monthly fee)
LLM       : free key from FREE-ACCESS.md (Groq / Google AI Studio)
```

Cross-ref: AI keys & credits → [FREE-ACCESS.md](./FREE-ACCESS.md) · builders → [FRONTEND.md](./FRONTEND.md)
