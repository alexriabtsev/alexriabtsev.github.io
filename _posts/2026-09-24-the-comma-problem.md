---
title: "The Comma Problem: What Russian Pop Music Reveals About the Limits of Content Moderation"
date: 2026-09-24T00:05+03:00
author: alexrb
layout: post
permalink: /2026/09/the-comma-problem/
tags:
- content moderation
- recommender systems
- DSA
- Ukraine
---
In an old schoolhouse fable familiar across Eastern Europe, a schoolboy parses a monarch's decree about a condemned prisoner: "Execute impossible to pardon." Where the comma falls decides whether the prisoner lives or dies, and whoever places it takes responsibility for where the line is drawn. In information oversight, the verifier checks where someone else put it.

During a routine review of field reports, we received a summary from a cultural outreach team working near the front line. It described an open dialogue on rejecting Russian cultural products, supported by the unit's officers. It read like a collective civic shift, approved by leadership and filed for the archive.

The raw field note under the summary recorded something much smaller. One young woman went up to one member of the visiting team and asked whether she should keep listening to songs she liked. One officer nodded at the visitor's answer.

Each step from observation to official finding inflated it a little. One conversation became an open dialogue, and a single nodding officer became the unit's officers. Nobody lied; each round of compression just added a thin layer of administrative optimism. Our job as verifiers was to strip that layer off and ask what actually happened.

## The organic feedback loop

The raw note recorded ambivalence. The woman asked whether she should stop listening, which meant she was still listening, and she was checking the room to see what others did when the headphones went on.

Behind her question is a peer-to-peer distribution channel with no political intent. The same officer who nodded along complained that local teenagers play this music loudly and share it among themselves. Nobody organizes this. The people sharing tracks are sincere listeners acting out of habit, personal taste, and musical memory. Nothing in the chain is coordinated, and nobody in it is a sockpuppet or a fabricated persona.

Once a track plays to the end, the streaming app's recommendation engine logs the completion, updates affinity scores, and feeds the track back into daily playlists and autoplay queues. No human reviews that queue, and no cultural officer logs what it plays.

The security industry pictures hostile influence as a bot farm: synthetic networks, central funding, artificial spikes in engagement. This model has none of that. It runs on genuine human engagement, amplified by software built for retention. A cultural team visits, holds a conversation, and leaves. The recommender runs twenty-four hours a day on the phone in the listener's pocket.

## Blind spots in the detection model

Platform safety systems miss this distribution because they are built to find coordinated inauthentic behavior. Detection pipelines look for accounts created in sync, shared server infrastructure, copy-pasted content across clusters, and unusual network topologies. An organic feedback loop leaves none of those traces. The accounts belong to real people on registered mobile subscriptions.

Streaming platforms also file these tracks as commercial entertainment rather than political speech, which puts them outside civic integrity policies and the reach of election-monitoring teams. Unless a lyric calls for violence or contains banned symbols, the track is inventory, to be monetized and tuned for playback time.

Analysis pipelines fail in a second way. When language models summarize unstructured monitoring feeds, they smooth out nuance in the same direction the field report did: a hesitant question turns into a political stance, and one person's question turns into proof of community consensus. Human verifiers exist because machine summaries miss quiet, unresolved encounters like this one. And since platform metrics count only the violations that get caught, these blind spots show up on safety dashboards as zero incidents.

At an April 2025 meeting of the music industry subcommittee of the Verkhovna Rada's Committee on Humanitarian and Information Policy, a participant said that Russian music spreads through algorithms and enters domestic trends, and gave the viral track "Sigma Boy" as an example. If that account is right, platform features built to maximize engagement did the distributing.

## The limits of the rulebook

Regulators have tried to handle this with legal tools designed for physical space, and the timeline of Ukrainian policy shows their ambitions shrinking:

* **June 19, 2022:** The Verkhovna Rada adopted Law No. 2310-IX, restricting public performance and media broadcast of music by artists who were citizens of the Russian Federation at any point after 1991. The law covered public space, radio, and television, and left personal devices and algorithmic feeds alone.
* **April 2025:** The music industry subcommittee met to discuss restricting Russian-language music on Spotify, Apple Music, and YouTube Music — not only through blocking, but by throttling downloads and limiting algorithmic promotion. Attendees included the Ministry of Culture, the National Council on Television and Radio Broadcasting, the National Police, the Language Ombudsman, media experts, and people from the music industry. The National Council said global platforms are not prepared to write separate rules for Ukraine. The Digital Ministry said any measure would need a clear basis in domestic law.
* **December 2025:** Oleksandr Sanchenko, head of the subcommittee, said the platforms had described two routes they could act on: a statutory ban based on language, or National Security and Defense Council sanctions against specific artists followed by geoblocking in Ukraine. The language route, he said, does not fit Ukraine's course toward EU integration, so work shifted to sanctions. The process had been launched for roughly 120 artists, with some decisions already adopted and others pending. Whether all platforms would accept the mechanism was expected to become clear by March 2026.

In eight months the debate went from algorithmic amplification to manual lists of individual musicians. Sanctions were what remained: the platforms would act on only two routes, and EU integration closed one of them.

European law offers little help here. Under the Digital Services Act (Regulation (EU) 2022/2065), Article 34 requires designated very large online platforms to assess the systemic risks stemming from the design or functioning of their services, including their algorithmic systems, and Article 35 requires reasonable, proportionate, and effective measures to mitigate those risks. The DSA does not apply in Ukraine. And even inside the EU, these obligations reach only platforms the European Commission has designated. Spotify told the Commission in 2023 that it had fewer than 45 million monthly users in the EU and was not designated. The Commission's list, last updated on 31 August 2026, now includes ChatGPT, Reddit, and Roblox; it still does not include Spotify. The Commission has questioned YouTube, Snapchat, and TikTok about their recommender systems, but no dedicated music-streaming service appears on the list. For the service most associated with music recommendation, the strictest rules on algorithmic risk do not apply at all.

Music by Russian artists is also a different problem from Russian-language music by Ukrainian or diaspora creators. Sanctions can reach only the first; the second is exactly where the language route ran into EU integration. Sanctioning individual performers dealt with the artists and left the distribution software as it was.

## Designing for outcomes

If individual sanctions cannot reach automated distribution, policy has to target platform mechanics instead of artist rosters. Regulators should create a statutory, effect-based obligation for algorithmic systems operating in conflict environments. Major audio services would be legally required to treat automated amplification of state-restricted catalogs as a measurable systemic risk under national law, instead of leaving feed curation to commercial engagement metrics.

The main objection is that regulating recommendations amounts to state-directed content engineering and sets a dangerous precedent for censorship. That objection confuses human speech with platform delivery. Users would keep the legal right to search for and play any track they want. The rule would only stop a proprietary recommendation engine from reinforcing an unresolved cultural habit for profit.

A second objection is practical: Ukraine's own broadcasting regulator has said global platforms will not write separate rules for one country. But the Digital Ministry named the missing piece in the same discussion — a clear basis in national law — and the platforms themselves told lawmakers they could act on a statutory ban. What they decline to do is invent country-specific rules a state has not written. An effect-based obligation in national law is the rule that has not yet been written.

## Unresolved choices

The young woman in the field note was asking whether she should change what she listens to, caught between personal habit and national identity.

If she opened her streaming app that evening, it would have had no moral dialogue to offer, only a familiar chorus picked by code built to hold her attention for another three minutes. She has not decided where the comma goes in her own life. Until someone changes the rules that govern the feed, the machine will keep making its recommendation.

---

*The author has served in the Armed Forces of Ukraine since 2025, most recently in an analytical role, and is completing a medical discharge. He is the founder of Startup.in.UA, a community of Ukrainian technology founders.*
