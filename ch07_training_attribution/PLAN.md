# Chapter 7: Training Attribution — Where Do the Weights Come From?

## The Idea

PATE = Ch1's ensemble applied to training. The course comes full circle. Same `rdp_accountant.py` powers everything. DP-SGD is the sidebar.

## What the Student Builds

1. **PATE** — N teachers, data partitions, vote on student labels (~100 lines)
2. **End-to-end** — PATE (training) + Ch5 (inference). Two ε budgets. (~50 lines)
3. **Sidebar: DP-SGD** — clip gradients, add noise (~50 lines, optional)
4. **MoE discussion** — natural architectural partitioning

## The Artifact

**Notebook:** `ch07.ipynb` — PATE + end-to-end.
**Script:** `ch07.py`
**Viz:** dashboard shows both training ε and inference ε.

## Key Ideas

1. **PATE is Ch1's ensemble for training. Full circle.**
2. **Two ε budgets: training + inference.**
3. **Same accountant powers everything.**

## Assets Inherited (from Ch6)

- The fast app, all infrastructure

## Assets Produced (for Ch8)

- PATE pipeline, end-to-end attribution

## Course Completion

**Ch1-7 is the complete course.** The student has: ensemble attribution, weighted voting, private voting, single-model bounds, single-model DP, GPU acceleration, training attribution. All sharing one RDP accountant, all visible in one dashboard. Ch8 is the bonus level.
