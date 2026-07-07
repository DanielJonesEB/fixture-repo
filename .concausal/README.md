# .concausal/

Machine-written provenance for agent-applied fixes.

`failures/<coordinate-id>.json` records a build failure that an agent fixed:
the job and step that failed, and the resolved input versions it ran with.
A fix commit links to its failure via a `Concausal-Fixes: <coordinate-id>`
commit trailer; this directory explains those ids.
