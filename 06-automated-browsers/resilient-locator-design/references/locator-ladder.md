# Locator Ladder

Ladder top to bottom: getByRole plus accessible name; getByTestId for dynamic or nameless content; getByLabel for form fields; getByText for stable copy; getByPlaceholder sparingly; CSS by semantic classes; XPath last with comments. Each step down needs a reason.

Health scoring: test-id coverage on interactive elements over 80 percent is healthy; absolute XPath count should trend to zero; nth indexes need content filters; duplicate text matches need scoping. Audit quarterly and after redesigns.

List patterns: container locator plus filter(hasText) plus first/last only with sort guarantees; tables by row-header association; pagination by labeled controls. Never index into unsorted dynamic lists.

Standards: one page with ladder, examples, anti-examples, and review checklist. Enforce in PRs; measure breakage per sprint; celebrate redesign survival.
