# Material Selection Project

This project investigates the optimal material and cross-sectional geometry for a lightweight chair leg modeled as a slender column under axial compression. The design objective is to maximize critical buckling load per unit mass while satisfying geometric, buckling, and yielding constraints. The work combines hand analysis based on Euler buckling theory, stochastic optimization in Python, and SolidWorks FEA validation.

## Project Objective

The goal of this project is to identify a high-performing chair-leg design subjected to a fixed compressive load. The leg is modeled as a slender column using Euler buckling theory, and the selected design must achieve high buckling resistance with low mass while satisfying the imposed design requirements.

## Design Requirements

The following assumptions and constraints were used in the study:

- Total occupant mass: 80 kg
- Load per leg: 20 kg equivalent mass, corresponding to approximately 196 N
- Column end condition: fixed-pinned
- Effective length factor: `K = 0.7`
- Maximum cross-sectional envelope: 30 mm x 30 mm
- Materials considered: isotropic metals and alloys only
- Minimum factor of safety: `n >= 2` against buckling and yielding
- Room-temperature, idealized conditions assumed
- Cross sections explored: hollow circular and hollow rectangular tubes only

## Methods

### 1. Analytical Modeling

The chair leg was modeled as a slender column and evaluated using Euler buckling theory:

```math
P_{cr} = \frac{\pi^2 E I}{(K L)^2}
```

Axial yielding was checked using the applied compressive stress approximation:

```math
\sigma = \frac{F}{A}
```

Johnson buckling theory was also reviewed, but the resulting candidate designs were determined to remain in the Euler buckling regime.

### 2. Optimization

A Python-based design framework was built to explore the design space. The optimization problem used:

- design variables: geometry and material properties
- objective: maximize critical buckling load per unit mass
- constraints: geometry, yielding, and buckling requirements

Two stochastic optimization methods were implemented:

- Monte Carlo search
- Particle Swarm Optimization (PSO)

The score function minimized the inverse of critical buckling load per unit mass, with large penalties applied to infeasible solutions.

### 3. Finite Element Analysis

SolidWorks Simulation 2025 was used to perform linear buckling analysis on the optimized candidate designs. Each model used:

- assigned material from the SolidWorks library
- fixed-pinned support condition
- 196 N applied axial compressive load
- coarse mesh
- buckling load factor output for comparison with hand calculations

## Optimization Summary

The design search produced four primary candidates: Monte Carlo circular, Monte Carlo rectangular, PSO circular, and PSO rectangular. The best-performing design found in the explored space was a thin-walled rectangular alloy-steel tube from the PSO search. More broadly, the high-performing candidates shared similar traits:

- large outer dimensions close to the 30 mm limit
- thin walls
- high stiffness-to-weight ratio
- high yield strength

## Final Selected Design

The final selected design was a hollow rectangular cross section made from alloy steel, with:

- outer dimensions: 28.26 mm x 29.06 mm
- inner dimensions: 25.06 mm x 26.19 mm
- material properties: `E = 210 GPa`, `rho = 7700 kg/m^3`

This design was selected because it provided strong buckling resistance with low mass and was supported by both optimization and the weighted decision matrix.

## FEA Validation

SolidWorks buckling studies were used to compare FEA critical loads against Euler predictions. The percent differences between the analytical and FEA results ranged from about 2.26% to 15.5%, indicating reasonable agreement under the idealized assumptions of the project. Rectangular sections showed larger disagreement than circular sections, likely due to mesh sensitivity and greater weak-axis sensitivity.

## Key Findings

- Rectangular tube designs outperformed circular tube designs in buckling resistance
- High modulus of elasticity and favorable stiffness-to-density ratio were dominant factors
- Thin-walled hollow sections were consistently favored
- The optimization framework successfully identified efficient candidate designs
- FEA and hand calculations showed reasonable agreement for all reported candidates

## Limitations

This project used several simplifying assumptions:

- ideal fixed-pinned supports
- perfect axial loading
- no geometric imperfections
- no attachment stress concentrations
- no fatigue, thermal, or manufacturing effects
- no standard stock-size restriction

As a result, the identified designs should be interpreted as best-performing designs within the simplified modeled design space, not final production-ready chair-leg designs.

## Tools Used

- Python 3.14.4
- SolidWorks Simulation 2025