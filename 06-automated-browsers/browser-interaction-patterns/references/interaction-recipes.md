# Interaction Recipes

Forms: fill then assert inputValue; select options then assert; check boxes then assert checked; date pickers via fill plus change event; rich editors via keyboard plus content assertion. Wizards: assert step indicator per transition.

Files: uploads via setInputFiles on the input (no OS dialog); downloads via download-event wait with suggested path; verify size and checksum; clean fixtures before runs. Frames: frameLocator by URL or name; re-resolve after reloads; assert frame URL before acting.

Windows: await popup events before clicking openers; assert popup URL; close explicitly. Dialogs: register dialog handlers before triggers; assert message; accept or dismiss deliberately. Drag: locator.dragTo with verified drop state; scroll: scrollIntoView plus stable assertion; keyboard: press with focus assertion first.

Rule: act, then assert the resulting state before the next act. Failures then name their step with artifacts attached.
