# Dispatcher Patterns

Pattern: while(true){switch(state){case '0': ...; state='3'; break; ...}} with string or numeric states; sometimes split across functions with state passed around. Entry sets initial state; exits break the loop or return.

Sketching: one node per case with its statements summarized; edges labeled with assigned next-state; loops noted with trip conditions. Tools sketch; humans judge reachability.

Opaque predicates: conditions that look dynamic but fold constant (x*x>=0, known-constant compares, double negations). Prove by substitution; dynamic ones stay. Dead branches need unreachability proof from entry, not just suspicion.

Relinking: order live blocks by execution; replace state jumps with direct flow; keep a map from new lines to original cases. Verify by sampling inputs across both versions and comparing observable outputs.
