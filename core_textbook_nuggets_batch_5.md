## GeniusSIM Knowledge Extract – Core Textbooks (Batch 5)
*Compiled 2025-07-17*

Seven fresh references just landed. Their prime nuggets and how they wire into GeniusSIM modules are captured below.

| # | Reference | Stand‑out Topics / Assets | Direct Module Hooks |
|---|-----------|---------------------------|---------------------|
| 1 | *Advances in Reservoir Simulation* – **Zhao & Xia, 2025 MDPI compendium** fileciteturn18file0L6-L12 | • Ensemble smoother 4D‑seismic HM workflow (ES‑MDA) – front distance metric.<br>• PINN surrogates for fractured horizontal wells (paper p. 113).<br>• Virtual flow‑meter concept (ground infra mgmt). | **Auto‑Twin Sync**, CCSNet surrogate library, RiskRadar ML metrics |
| 2 | *Recent Advances in Reservoir Simulation & Carbon Utilization/Storage* – **Liu, Sun & Wang, 2025** fileciteturn18file1L6-L14 | • VOF pore‑scale CO₂–water flow models.<br>• Nano‑surfactant IFT optimisation (MgO).<br>• ML capacity prediction for shale CO₂ sequestration cases. | **CCS Module**, ScenarioLab CO₂ cases, PropertyDB (IFT correlations) |
| 3 | *Petroleum Reservoir Simulation: A Basic Approach* – **Abou‑Kassem et al., 2006** (new scan) fileciteturn18file2L1-L15 | • Pedagogical CVFD derivations incl. block‑center vs point‑distributed grid.<br>• FORTRAN‑95 WinB4D code + datasets.<br>• Extensive nomenclature glossary. | **Solver Validator**, Edu Demos, Glossary sync |
| 4 | *Inverse Theory for Reservoir Characterization & History Matching* – **Oliver, Reynolds & Liu, 2008** fileciteturn18file3L8-L15 | • MAP estimation, SVD resolution analysis, EnKF/ESM algorithms.<br>• Adjoint gradient framework with practical examples. | **AHM‑Engine**, Adjoint Library, Uncertainty Quantification toolkit |
| 5 | *Lecture Notes on Applied Reservoir Simulation* – **Koederitz, 2004** fileciteturn18file4L3-L11 | • Concise step‑by‑step examples for 1‑D → 3‑D grids.<br>• Field study exercises & problem sets.<br>• Discussion on ‘odds & ends’ incl. simulation pitfalls. | **PromptSim** training dataset, Education Demos, GridManager tips |
| 6 | *Practical Reservoir Engineering & Characterization* – **Baker, Yarranton & Jensen, 2015** fileciteturn18file5L8-L16 | • Integrated workflow chapters (volumetrics → SCAL → MBAL).<br>• Unique decision‑tree for reservoir classification (p. 25).<br>• Detailed cap‑press & rel‑perm lab protocols. | **Workflow Orchestrator**, PropertyDB defaults, ScenarioLab case builder |
| 7 | *Reservoir Simulation & Well Interference* – **Chin & Zhuang, 2020** fileciteturn18file6L6-L15 | • Parent‑child & frac‑hit analytical treatments.<br>• Boundary‑conforming grids & anisotropic tilted fractures.<br>• ‘Cube model’ optimisation for pad drilling. | **Fracture Engine**, WellManager interference module, GridManager (curvilinear) |

---
### Automation queue (kicks off tonight)
1. **OCR + vector tagging** of equations & diagrams for all seven books.
2. **Unit‑test harvest**: ES‑MDA front‑distance case, PINN surrogate comparison, cube‑model pad optimisation.
3. **Glossary augmentation** pulling 150+ new symbols from Abou‑Kassem and Koederitz.
4. Update **PromptSim** with decision‑tree prompts from Baker et al.

Heavy derivations, images & code stubs live in their respective deep‑dive docs and the code canvas; chat remains lean.

