# METABRIC RandomForest Model — HER2+ Classification Limitation

## Mini-Report (for personal documentation)

### Problem
The RandomForestClassifier trained on the METABRIC clinical dataset (1700 patients, 4 target classes: ER+/HER2- High Prolif, ER+/HER2- Low Prolif, ER-/HER2-, HER2+) achieved 0.51 overall accuracy, but HER2+ recall was only 0.18 — the model correctly identified just 5 of 38 HER2+ cases in the test set.

### Attempted Fixes and Results

| Attempt | HER2+ Recall | Outcome |
|---|---|---|
| Baseline (no weighting) | 0.18 | Starting point |
| `class_weight='balanced'` | 0.18 | No change |
| `class_weight='balanced_subsample'` | 0.13 | Worse |

`class_weight='balanced'` reweights the cost of misclassifying each class based on overall class frequency, but RandomForest trains each of its ~100 trees on a random bootstrap sample of the data — a tree's individual sample may still contain very few HER2+ examples even if the global weight is high, leaving nothing for that tree to learn from. `balanced_subsample` recalculates weights per-tree from each tree's own bootstrap sample rather than the dataset as a whole; here it performed worse, likely because some trees' already-small HER2+ samples were further reduced or overcorrected.

### Evidence

**Confusion matrix (actual HER2+ row, 38 cases):**
`[15, 7, 11, 5]` → 15 misclassified as ER+/HER2- High Prolif, 7 as ER+/HER2- Low Prolif, 11 as ER-/HER2-, 5 correct.

Errors were **scattered across all three other classes** rather than concentrated in one — a pattern indicating a general separability problem rather than a specific two-class confusion that reweighting or threshold-tuning could fix.

**Feature-level comparison (`groupby('3-gene_classifier_subtype').mean()`):**
Of the 9 selected features (age, tumor size, histologic grade, lymph nodes positive, mutation count, Nottingham Prognostic Index, tumor stage, menopausal state, PR status), 6 showed HER2+ values nearly identical to ER-/HER2- values (age, grade, mutation count, NPI, tumor stage, menopausal state). Only lymph_nodes_positive and pr_status showed any HER2+-distinguishing signal, and neither strongly enough to carry a 4-way classification alone.

### Interpretation
HER2 status is driven by a specific molecular event — amplification of the HER2 gene, detected via FISH or IHC directly on tumor tissue — not by general tumor severity markers like size, grade, or stage. Two tumors can present with similar grade and stage for entirely different underlying molecular reasons; grade/stage are downstream, aggregate severity indicators, while HER2 amplification is a distinct upstream molecular cause. This is consistent with what the data showed: HER2+ and ER-/HER2- patients were statistically indistinguishable on 6 of 9 clinical features, because none of those features encode HER2-specific molecular information.

### Conclusion
Reweighting strategies were correctly ruled out as insufficient after direct testing, not skipped. The limitation is a features/information problem, not a training or class-imbalance-handling problem: clinical/pathological features alone do not carry enough HER2-specific signal to reliably separate HER2+ from the other three subtypes with this feature set. Resolving this would require molecular-level features (e.g., HER2 IHC/FISH scores) rather than further model or weighting adjustments.

---

## README Limitations Section (short version)

**Limitation — HER2+ subtype classification:** The model achieves 0.51 overall accuracy but only 0.18 recall on the HER2+ subtype. Class-weighting strategies (`balanced`, `balanced_subsample`) were tested and did not improve this, and confusion matrix analysis showed HER2+ misclassifications scattered across all other classes rather than concentrated in one — indicating a feature-availability limitation rather than a class-imbalance or training issue. This is consistent with HER2 status being driven by a specific molecular event (HER2 gene amplification) that isn't captured by the clinical/pathological features used here (tumor size, grade, stage, etc.). Reliable HER2+ classification would likely require molecular-level features such as HER2 IHC/FISH scores.
