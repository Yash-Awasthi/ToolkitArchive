# 🗄️ Backend — BaaS, Databases, Hosting, Auth, Vectors (verified 29 September 2026)

<p align="center"><a href="./README.md">🏠 Home</a> · <a href="./MODELS.md#whos-actually-best--head-to-head-across-34-benchmarks">📊 Benchmarks</a> · <a href="./NEWS.md">📰 News</a> · <a href="./STUDENTS.md">🎓 $0 guide</a> · <a href="./FREE-ACCESS.md">🆓 Free AI</a></p>

> [!NOTE]
> Everything to ship the backend of an app for **$0**. Every free tier below was read from the
> vendor's live pricing page on 29 Sep 2026.

> [!WARNING]
> **Changed since the last pass:** **InstantDB** was acquired by OpenAI — new sign-ups are closed and Instant Cloud shuts down Aug 31, 2027 (self-host guide available) · **CodeSandbox** acquired by Together AI · **Koyeb** is joining Mistral AI · **Gel (EdgeDB)** acquired by Vercel · **Stytch** free tier cut to 10,000 MAU · **Xata** no longer has a free cloud tier (free = self-host) · **CockroachDB** is now a 30-day $400 trial.

**Contents:** [BaaS](#part-1--backend-as-a-service) · [Sandboxes](#part-1a--sandboxes--cloud-dev-environments) · [Databases](#part-2--serverless--edge-databases) · [Hosting](#part-3--hosting--deploy--paas) · [Auth](#part-4--auth) · [Vector DBs](#part-5--vector-databases) · [Glue](#part-6--shipping-glue) · [$0 stack](#zero-dollar-stack)

---

## Part 1 — Backend-as-a-Service

| Tool | Stack | Free tier | Cheapest paid | Self-host | Link |
|---|---|---|---|---|---|
| ★ **Supabase** | Postgres + auth + storage + functions + pgvector | 50K MAU, 500 MB DB, 1 GB files, 5 GB egress (projects pause after 1 week idle) | Pro $25/mo | Yes | [supabase.com/pricing](https://supabase.com/pricing) |
| ★ **Firebase** | NoSQL + auth + functions (Google) | Spark plan, no cost | Blaze pay-as-you-go | No | [firebase.google.com/pricing](https://firebase.google.com/pricing) |
| **Convex** | Reactive TypeScript database, real-time | Free with built-in resources, then pay as you go | Professional $25/dev/mo | Yes (OSS) | [convex.dev/pricing](https://convex.dev/pricing) |
| **Appwrite** | Open-source BaaS (58K★) | $10/mo of compute credits included | Dedicated from $10/mo | Yes | [appwrite.io/pricing](https://appwrite.io/pricing) |
| **PocketBase** | Single Go binary + SQLite | Free, open source (no paid plan) | — | Yes (it's the binary) | [pocketbase.io](https://pocketbase.io) |
| **Nhost** | Postgres + Hasura GraphQL | 1 project (pauses after 1 week idle) | Pro $25/mo | Yes | [nhost.io/pricing](https://nhost.io/pricing) |
| **Encore** | TS/Go backend framework + infra | Free Starter (local dev, small projects) | Pro $49/member + usage | Yes | [encore.dev/pricing](https://encore.dev/pricing) |
| **Wasp** | Full-stack React/Node/Prisma framework | Free, open source | — | Yes | [wasp.sh](https://wasp.sh) |
| **Microsoft Rayfin** | Agent-friendly BaaS (auth, hosting, DB, data API) as SDK or on Fabric | Fabric trial capacity | Fabric pricing | No | [microsoft.com/microsoft-fabric/features/rayfin](https://microsoft.com/microsoft-fabric/features/rayfin) |
| ~~InstantDB~~ | Acquired by OpenAI — sign-ups closed, cloud ends Aug 31 2027 | — | — | Yes (self-host) | [instantdb.com](https://instantdb.com) |

---

## Part 1A — Sandboxes & Cloud Dev Environments

For running AI-generated or agent-driven code away from your own machine.

| Tool | Free | Paid | Link |
|---|---|---|---|
| ★ **Daytona** | **$200 free compute**, no card; startups up to $50K credits | Per-second (vCPU ~$0.05/h) | [daytona.io/pricing](https://daytona.io/pricing) |
| ★ **Blaxel** | Up to $200 free credits | Tier 1 $20/mo, usage-based | [blaxel.ai/pricing](https://blaxel.ai/pricing) |
| **E2B** | Hobby: $100 one-time usage credit, no card | Pro $150/mo + usage | [e2b.dev/pricing](https://e2b.dev/pricing) |
| **Modal** | **$30/mo free compute** (Starter $0) | Team $250/mo; academic/startup grants | [modal.com/pricing](https://modal.com/pricing) |
| **Northflank** | Sandbox: always-on, 2 services + 1 database + 2 cron jobs | From $2.70/mo compute | [northflank.com/pricing](https://northflank.com/pricing) |
| **Lightning.ai** | Free: up to 30 credits/mo | Pro $20/mo (annual) · academic pricing | [lightning.ai/pricing](https://lightning.ai/pricing) |
| **Vercel Sandbox** | Included in Hobby usage | Usage-based on Pro | [vercel.com/sandbox](https://vercel.com/sandbox) |
| **CodeSandbox** (Together AI) | Build $0 | Scale $170/mo · education/OSS discounts | [codesandbox.io/pricing](https://codesandbox.io/pricing) |
| **Fly.io** | No free tier; up to $15K startup credits | Machines from $1.94/mo | [fly.io/pricing](https://fly.io/pricing) |

---

## Part 2 — Serverless & Edge Databases

| DB | Type | Free tier | Cheapest paid | Link |
|---|---|---|---|---|
| ★ **Neon** | Serverless Postgres (branching, scale-to-zero) | 100 projects, 100 CU-hours/project/mo, 0.5 GB/project, no card | Launch usage-based (~$15/mo typical) | [neon.com/pricing](https://neon.com/pricing) |
| ★ **Turso** | Edge SQLite/libSQL | **100 DBs, 5 GB, 500M rows read, 10M rows written/mo** | Developer $4.99/mo | [turso.tech/pricing](https://turso.tech/pricing) |
| **Supabase** | Postgres | 500 MB (see BaaS) | Pro $25/mo | [supabase.com/pricing](https://supabase.com/pricing) |
| **MongoDB Atlas** | Document | Free forever cluster, 512 MB | Flex up to $30/mo | [mongodb.com/pricing](https://mongodb.com/pricing) |
| **Upstash** | Serverless Redis / Vector / QStash | 256 MB, 500K commands, 10 GB bandwidth/mo | Pay-as-you-go $0.20/100K cmds · Fixed 250 MB $10/mo | [upstash.com/pricing](https://upstash.com/pricing/redis) |
| **Gel** (ex-EdgeDB, Vercel) | Graph-relational on Postgres | 1/4 compute unit, 1 GB disk | Pro $19.50/mo | [geldata.com/pricing](https://geldata.com/pricing) |
| **PlanetScale** | Postgres + Vitess MySQL | ❌ none | From $5/mo (single node) | [planetscale.com/pricing](https://planetscale.com/pricing) |
| **CockroachDB** | Distributed SQL | 30-day trial, $400 credit | Standard $0.092/vCPU-hr | [cockroachlabs.com/pricing](https://cockroachlabs.com/pricing) |
| **Xata** | Postgres platform | Free self-host only | Cloud $0.012/hr + storage | [xata.io/pricing](https://xata.io/pricing) |

> **Most free storage:** Turso (5 GB). **Most free reads:** Turso (500M rows/mo). **Most free projects:** Neon (100).

---

## Part 3 — Hosting / Deploy / PaaS

| Platform | Best for | Free tier | Cheapest paid | Link |
|---|---|---|---|---|
| ★ **Cloudflare Pages** | Static / Jamstack | Free, **unlimited sites, requests and bandwidth** | — | [pages.cloudflare.com](https://pages.cloudflare.com) |
| ★ **Cloudflare Workers** | Edge functions / APIs | Free plan (Workers, KV, D1, R2 free tiers) | Workers Paid (usage) | [workers.cloudflare.com](https://workers.cloudflare.com) |
| ★ **Vercel** | Next.js | Hobby $0 (personal, non-commercial): first 100 GB Fast Data Transfer, 10 s function default | Pro $20/mo | [vercel.com/pricing](https://vercel.com/pricing) |
| **Netlify** | Static + functions | 300 credits/mo, free forever; credits for qualifying OSS | Personal $9/mo · Pro $20/mo | [netlify.com/pricing](https://netlify.com/pricing) |
| **Render** | Full-stack + Postgres | Hobby $0 + compute | Pro $25/mo + compute | [render.com/pricing](https://render.com/pricing) |
| **Railway** | Quick full-stack deploys | 30-day trial with $5, then $1/mo credit (1 vCPU / 0.5 GB per service) | Hobby $20/mo | [railway.com/pricing](https://railway.com/pricing) |
| **Sevalla** | Static + apps | Static hosting free: 100 sites, 100 GB bandwidth, 600 build min | Apps from $5/mo | [sevalla.com/pricing](https://sevalla.com/pricing) |
| **Zeabur** | PaaS | Free $0 plan | Dev $5/mo | [zeabur.com/pricing](https://zeabur.com/pricing) |
| **Northflank** | GPU PaaS + bring-your-own-cloud | Always-on sandbox (2 services, 1 DB, 2 cron) | From $2.70/mo | [northflank.com/pricing](https://northflank.com/pricing) |
| **Koyeb** (joining Mistral AI) | Containers + Postgres | 5 h free (0.25 vCPU, 1 GB) | Pro $29/mo | [koyeb.com/pricing](https://koyeb.com/pricing) |
| **Deno Deploy** | TS/JS edge | Free tier | Usage-based | [deno.com/deploy](https://deno.com/deploy) |
| **Fly.io** | Multi-region containers | ❌ none (startup credits only) | From $1.94/mo | [fly.io/pricing](https://fly.io/pricing) |
| **Coolify** | Self-host PaaS (Heroku alternative) | **Free forever self-hosted**, all features | Cloud $5/mo (2 servers) | [coolify.io/pricing](https://coolify.io/pricing) |
| **Dokku** | Git-push PaaS on your VPS | Free open source | Dokku Pro from $10/mo | [dokku.com](https://dokku.com) |

---

## Part 4 — Auth

| Provider | Free tier | Cheapest paid | Self-host | Link |
|---|---|---|---|---|
| ★ **WorkOS AuthKit** | **First 1,000,000 active users free** | Add-ons (SSO, Audit Logs $99/mo) | No | [workos.com/pricing](https://workos.com/pricing) |
| ★ **Clerk** | 50,000 monthly retained users per app, no card | Pro $20/mo | No | [clerk.com/pricing](https://clerk.com/pricing) |
| ★ **Supabase Auth** | 50K MAU (bundled) | Pro $25/mo | Yes | [supabase.com/pricing](https://supabase.com/pricing) |
| **Logto** | 50,000 MAU | Pro $24/mo | Yes (OSS) | [logto.io/pricing](https://logto.io/pricing) |
| **Kinde** | 10,500 MAU | Pro $25/mo | No | [kinde.com/pricing](https://kinde.com/pricing) |
| **Stytch** | 10,000 MAU + AI agents, 5 SSO/SCIM connections | Pay as you go | No | [stytch.com/pricing](https://stytch.com/pricing) |
| **Hanko** | 10,000 MAU, 2 projects | Starter $29/mo | Yes (OSS) | [hanko.io/pricing](https://hanko.io/pricing) |
| **Hexclave** (ex-Stack Auth) | 10,000 users | Team $49/mo | Yes (OSS) | [hexclave.com/pricing](https://www.hexclave.com/pricing) |
| **Better Auth** | Library free & open source; hosted dashboard Starter $0 | Pro $20/mo | Yes | [better-auth.com](https://better-auth.com) |
| **SuperTokens** | Self-host free with no limits; cloud free under 5K MAU | Add-ons from $100/mo minimum | Yes | [supertokens.com/pricing](https://supertokens.com/pricing) |
| **ZITADEL** | All features, 100 daily active users (15K★) | Pro $100/mo | Yes | [zitadel.com/pricing](https://zitadel.com/pricing) |
| **Authentik** | Open source (26K★), forward-auth proxy + IdP + LDAP | Enterprise $5/user/mo | Yes | [goauthentik.io/pricing](https://goauthentik.io/pricing) |
| **Ory** | Developer free | Production $770/year | Yes (OSS) | [ory.sh/pricing](https://ory.sh/pricing) |

> **Most free users:** WorkOS (1M). **Best DX:** Clerk. **Zero-cost full control:** Better Auth / SuperTokens self-hosted.

---

## Part 5 — Vector Databases

| DB | Free tier | Cheapest paid | Link |
|---|---|---|---|
| ★ **pgvector** | Free Postgres extension — use inside Supabase / Neon | — | [github.com/pgvector/pgvector](https://github.com/pgvector/pgvector) |
| ★ **Qdrant** | Free forever cluster: 0.5 vCPU, 1 GB RAM, 4 GB disk + free cloud inference | Standard usage-based | [qdrant.tech/pricing](https://qdrant.tech/pricing) |
| **Weaviate** | Always free: 1 cluster, 100K objects, 1 GB memory | Flex $45/mo | [weaviate.io/pricing](https://weaviate.io/pricing) |
| **Pinecone** | Starter free | Builder $20/mo flat | [pinecone.io/pricing](https://pinecone.io/pricing) |
| **Zilliz / Milvus** | Zilliz free: 5 GB, 5 collections; Milvus open source | Serverless usage / Dedicated | [zilliz.com/pricing](https://zilliz.com/pricing) · [milvus.io](https://milvus.io) |
| **Chroma** | Open source; cloud $0 + usage | Team $250/mo | [trychroma.com/pricing](https://trychroma.com/pricing) |
| **Upstash Vector** | Free tier (with Upstash) | Pay as you go | [upstash.com/pricing](https://upstash.com/pricing/redis) |
| **LanceDB** | Open source (embedded) | Cloud Pro $779/mo | [lancedb.com/pricing](https://lancedb.com/pricing) |
| **Turbopuffer** | None | Launch $16/mo | [turbopuffer.com/pricing](https://turbopuffer.com/pricing) |
| **ScyllaDB Vector Search** | 30-day developer trial | Standard plan | [scylladb.com/pricing](https://scylladb.com/pricing) |

---

## Part 6 — Shipping Glue

| Need | Pick | Free tier | Paid | Link |
|---|---|---|---|---|
| Email | ★ **Resend** | 3,000 emails/mo (100/day), 3 domains | Pro $20/mo | [resend.com/pricing](https://resend.com/pricing) |
| Email | **Loops** | Up to 4,000 sends per rolling 30 days | See site | [loops.so/pricing](https://loops.so/pricing) |
| Email | **Brevo** | Free forever | Starter $8.08/mo | [brevo.com/pricing](https://www.brevo.com/pricing) |
| Email | **Postmark** | 100 emails/mo | Basic $15/mo | [postmarkapp.com/pricing](https://postmarkapp.com/pricing) |
| Payments | ★ **Stripe** | No monthly fee | 2.9% + 30¢ (US domestic cards) | [stripe.com/pricing](https://stripe.com/pricing) |
| Payments (merchant of record) | **Polar** | Starter: 5% + 50¢, no monthly; startup program free 12 months | Pro $20/mo | [polar.sh](https://polar.sh) |
| Payments (MoR) | **Lemon Squeezy** · **Paddle** | No monthly fee | 5% + 50¢ per transaction | [lemonsqueezy.com](https://lemonsqueezy.com) · [paddle.com](https://paddle.com) |
| File upload | **UploadThing** | 2 GB storage | 100 GB $10/mo | [uploadthing.com/pricing](https://uploadthing.com/pricing) |
| Object storage | ★ **Cloudflare R2** | 10 GB-month, 1M Class A + 10M Class B ops/mo, **free egress** | Usage-based past the free tier | [developers.cloudflare.com/r2/pricing](https://developers.cloudflare.com/r2/pricing) |
| Background jobs | **Trigger.dev** | $5/mo credits, 20 concurrent runs (Apache 2.0) | Hobby $10/mo | [trigger.dev/pricing](https://trigger.dev/pricing) |
| Background jobs | **Inngest** | 50K executions/mo, 5 seats | Pro $99/mo | [inngest.com/pricing](https://inngest.com/pricing) |
| Realtime | **Ably** | 200 connections, 6M messages/mo | Standard $29/mo | [ably.com/pricing](https://ably.com/pricing) |
| Realtime | **Pusher** | 200K messages/day, 100 connections | Startup $49/mo | [pusher.com/channels/pricing](https://pusher.com/channels/pricing) |
| Realtime (collab) | **Liveblocks** | Free, no card | Pro $25/mo | [liveblocks.io/pricing](https://liveblocks.io/pricing) |
| Search | **Algolia** | 10K searches, 50K records/mo | Grow pay-as-you-go | [algolia.com/pricing](https://algolia.com/pricing) |
| Search | **Meilisearch** · **Typesense** | Open source; cloud trials (14 days · 720 cluster-hours) | Meilisearch Cloud $20/mo · Typesense from $0.03/hr | [meilisearch.com](https://meilisearch.com) · [typesense.org](https://typesense.org) |

---

## Zero-Dollar Stack

```
Frontend  : Cloudflare Pages (unlimited bandwidth)
Backend   : Supabase (Postgres + Auth + Storage, 50K MAU)  or  PocketBase on any small VPS
DB extra  : Neon (100 projects) / Turso (5 GB, 500M reads)
Auth      : WorkOS (1M users) or Supabase Auth
Vectors   : pgvector inside Supabase
Edge fns  : Cloudflare Workers (free plan)
Storage   : Cloudflare R2 (10 GB, free egress)
Email     : Resend (3K/mo)
Payments  : Stripe / Polar (no monthly fee)
Sandboxes : Daytona ($200) · Modal ($30/mo)
LLM       : free keys from FREE-ACCESS.md (Gemini 3.8 Flash on AI Studio, Token Harbor :free, Groq)
```

Cross-ref: AI keys & credits → [FREE-ACCESS.md](./FREE-ACCESS.md) · builders → [FRONTEND.md](./FRONTEND.md) · students → [STUDENTS.md](./STUDENTS.md)
