# Session Ops

Capture: real UI login per role; snapshot cookies plus localStorage origins needed; strip analytics and ad state; store per-account files outside repos with tight permissions. Record capture time and expiry.

Isolation: one context per account always; separate state files, egress, and schedules; identity-check before sensitive steps. Cross-account reuse is a defect, not an optimization.

Refresh: proactive at 80 percent life; reactive re-login once on 401 then park; alert on two consecutive auth failures. MFA via human setup sessions only; document and timebox.

Hygiene: audit state files for over-collection; scan traces, videos, screenshots for tokens and PII; redact at capture; rotate on any exposure; review account access quarterly.
