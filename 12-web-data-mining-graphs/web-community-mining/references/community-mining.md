# Community Mining

Methods: label propagation (fast sketch, async, seeded); Louvain/modularity (stable partitions, resolution tuned); text+link hybrid (TF-IDF cosine blended with edges) for topical hoods. Filter nav/template links first or everything is one community.

Quality: modularity score; size distribution (giants get hierarchy, singletons reviewed); stability (NMI across seeded runs); sample validation (10+ pages per community judged coherent). Name from samples + top terms, human-approved.

Spam rings: dense + young + template-similar + cross-link heavy; confirm with registration/content evidence before action; prune from rank, quarantine from frontier. Never accuse on density alone.

Application: discovery (related per community), navigation (browse trees), spam defense, crawl budgeting per hood. Refresh on corpus change; monitor community drift (split/merge events) monthly.
