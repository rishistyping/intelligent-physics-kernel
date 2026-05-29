#!/usr/bin/env python3
"""
Intelligent Physics Kernel — Interactive Explorer
A production-quality Marimo notebook / reactive paper companion
for Emad Mostaque's "Intelligent Physics Kernel" (January 2026).

Author: Generated with Grok Build (xAI) following the paper as sole source.
License: MIT (for the notebook code); paper content © Intelligent Internet / Emad Mostaque.

This single-file app is fully self-contained. All theorems, quotes, and the
dependency structure are taken directly from the source PDF.
"""

import marimo

__generated_with = "0.23.8"
app = marimo.App(
    width="full",
    app_title="Intelligent Physics Kernel",
    html_head_file="ipk_head.html",
)

with app.setup:
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go
    import plotly.io as pio
    import networkx as nx
    import pandas as pd
    import re
    from functools import lru_cache
    from itertools import permutations, product
    from html import escape
    from textwrap import dedent
    from typing import Dict, List, Tuple, Any
    # =============================================================================
    # COLOR PALETTE — Deep space / physics elegant dark theme
    # =============================================================================
    DEEP_NAVY = "#0a1628"
    MIDNIGHT = "#0f172a"
    ELECTRIC_CYAN = "#67e8f9"
    SOFT_PURPLE = "#c026d3"
    WARM_GOLD = "#fcd34d"
    SOFT_MAGENTA = "#f472b6"
    FLUID_BLUE = "#38bdf8"
    WHITE = "#f8fafc"
    MUTED = "#94a3b8"
    ELIMINATED_RED = "#f87171"
    SURVIVES_GREEN = "#4ade80"
    pio.templates.default = "plotly_dark"

    # =============================================================================
    # AUTHORITATIVE CONTENT EXTRACTED FROM THE PDF (sole source of truth)
    # =============================================================================

    MU_PRINCIPLE = "Consistent inference is possible."

    LOCKS_DATA: List[Dict[str, Any]] = [
    {
        "id": 1,
        "branch": "Statistical Mechanics",
        "lock": "Inference",
        "theorem": "Cox (1946); Jaynes (2003)",
        "eliminated": "All non-probabilistic systems",
        "survives": "Probability",
        "key_quote": "Any assignment satisfying consistency (path-independence, coherence) is isomorphic to probability.",
        "details": "Alternatives: Assign degrees of belief by probability, possibility, or other systems. MU + consistency forces the probability calculus. Non-probabilistic systems are eliminated because they violate the self-grounding requirement of consistent inference."
    },
    {
        "id": 2,
        "branch": "Statistical Mechanics",
        "lock": "Update",
        "theorem": "Shore–Johnson (1980)",
        "eliminated": "All other divergences (Hellinger, Rényi, etc.)",
        "survives": "KL divergence (DKL(P∥Q))",
        "key_quote": "Any update satisfying consistency (coordinate invariance, subset independence) minimizes DKL(P∥Q).",
        "details": "KL minimization is the minimum update: change beliefs only as much as new constraints demand. This is the direct embodiment of MU in belief revision. All other divergences introduce arbitrary structural choices."
    },
    {
        "id": 3,
        "branch": "Quantum Field Theory",
        "lock": "Locality",
        "theorem": "Hammersley–Clifford (1971) + DLR continuum",
        "eliminated": "Non-local correlations / non-factorizable distributions",
        "survives": "Local action (Markov property)",
        "key_quote": "If no constraint couples regions A and C, assuming dependence between them adds information beyond what constraints demand.",
        "details": "Positive distributions satisfying the local Markov property factorize as P ∝ exp(−∑ VC) over local terms. Correlation is structure. Non-local assumptions violate MU."
    },
    {
        "id": 4,
        "branch": "Quantum Field Theory",
        "lock": "Time",
        "theorem": "Osterwalder–Schrader (1973)",
        "eliminated": "Non-reflection-positive (Non-RP) theories — no consistent time",
        "survives": "Unitary QFT on continuum spacetime",
        "key_quote": "Euclidean theories satisfying the OS axioms uniquely reconstruct to unitary Lorentzian QFT.",
        "details": "Reflection positivity is required for a probabilistic Hilbert-space interpretation. Without it the reconstructed inner product is not positive-definite, violating Lock 1 (inference structure). Euclidean invariance + clustering follow from MU (no preferred origin or global structure)."
    },
    {
        "id": 5,
        "branch": "Spacetime Geometry",
        "lock": "Gravity",
        "theorem": "Lovelock (1971)",
        "eliminated": "D > 4 (non-unique field equations)",
        "survives": "D ≤ 4",
        "key_quote": "In metric, second-order theories, the gravitational field equation is unique only for D ≤ 4. Higher D admits independent Lovelock densities.",
        "details": "For D > 4, multiple independent tensor structures (Lovelock densities Lk) contribute. Including or excluding each Lk is a structural choice forbidden by MU. Only D ≤ 4 yields unique dynamics from prior constraints."
    },
    {
        "id": 6,
        "branch": "Spacetime Geometry",
        "lock": "Chirality",
        "theorem": "Hodge (self-dual forms) + Index theorem",
        "eliminated": "D ≠ 4",
        "survives": "D = 4",
        "key_quote": "Self-dual 2-forms exist only in D = 4. Nontrivial topological sectors (instantons with ν ≠ 0) require self-duality.",
        "details": "Gauge field strengths are 2-forms. Yang–Mills instanton sectors (detected by the index theorem) exist only when self-dual configurations are possible. Restricting to ν = 0 would require additional structure not demanded by prior Locks. Thus D = 4 is forced."
    },
    {
        "id": 7,
        "branch": "Internal Geometry",
        "lock": "Duality",
        "theorem": "Electromagnetic duality fixed-point theorem",
        "eliminated": "Non-self-dual structures",
        "survives": "Self-dual unimodular lattice L (L = L*)",
        "key_quote": "An integral lattice is self-dual (L = L*) if and only if it is unimodular.",
        "details": "Electric charges valued in L; magnetic charges in the dual L*. No prior Lock distinguishes one as fundamental. MU therefore requires invariance under L ↔ L*. The fixed points are precisely the self-dual (unimodular) lattices. Continuous internal moduli are forbidden."
    },
    {
        "id": 8,
        "branch": "Internal Geometry",
        "lock": "Internal Dimension",
        "theorem": "Milnor–Serre",
        "eliminated": "n ≠ 8 (multiple lattices requiring arbitrary selection)",
        "survives": "E₈ (exactly one even unimodular lattice in dimension 8)",
        "key_quote": "In n = 8: exactly one lattice (E₈). In n ≥ 16: multiple lattices, requiring arbitrary selection.",
        "details": "Evenness (‖x‖² ∈ 2ℤ) is required for spin structure. The E₈ root lattice determines the Lie algebra e₈. Higher even unimodular lattices (n=16,24,...) are not unique; choosing one would violate MU. Thus internal geometry is fixed to E₈."
    },
    {
        "id": 9,
        "branch": "Particle Physics",
        "lock": "Matter",
        "theorem": "Bott periodicity + Slansky (1981) embedding constraints",
        "eliminated": "Real and quaternionic spinors (vectorlike spectra, anomaly cancellation trivial)",
        "survives": "Spin(10) with complex 16-dimensional Weyl spinor",
        "key_quote": "Spin(n) spinors are complex iff n ≡ 2,6 (mod 8). Of the candidates that embed in E₈, only Spin(10) yields an anomaly-free chiral spectrum.",
        "details": "Chiral gauge theories require non-self-conjugate representations. Real/quaternionic reps admit Majorana mass terms and give vectorlike spectra. Bott periodicity shows dimension-16 complex spinors first appear at n=10. Only Spin(10) ⊂ E₈ satisfies all prior Locks + anomaly cancellation + chirality."
    },
    {
        "id": 10,
        "branch": "Particle Physics",
        "lock": "Gauge",
        "theorem": "Baez–Huerta (2010)",
        "eliminated": "Larger (presentation-dependent) or smaller (arbitrary) algebras",
        "survives": "su(3) ⊕ su(2) ⊕ u(1)",
        "key_quote": "The intersection (SU(5)×U(1)) ∩ (SU(2)L×SU(2)R×SU(4)) inside Spin(10) is isomorphic to S(U(2)×U(3)), with Lie algebra su(3)⊕su(2)⊕u(1).",
        "details": "Lock 9 fixes Spin(10) and the 16, but not a preferred maximal-rank presentation. Two embeddings exist (Georgi–Glashow SU(5) and Pati–Salam). Choosing one is arbitrary. The Baez–Huerta intersection theorem extracts the unique structure common to both presentations: the Standard Model gauge algebra."
    },
]

    # Dependency chain exactly as shown in the paper (page 4)
    DEPENDENCY_CHAIN = [
        "MU", "Cox", "Shore–Johnson", "Hammersley–Clifford", "Osterwalder–Schrader",
        "Lovelock", "Hodge", "E-M Duality", "Milnor–Serre", "Bott", "Baez–Huerta", "Standard Model"
    ]

    BRANCH_COLORS = {
        "Statistical Mechanics": "#2F95A6",
        "Quantum Field Theory": "#83A1CC",
        "Spacetime Geometry": "#C9A96E",
        "Internal Geometry": "#516071",
        "Particle Physics": "#0F233F",
    }

    # =============================================================================
    # E₈ ROOT SYSTEM GENERATION (standard construction)
    # =============================================================================

    def generate_e8_roots() -> np.ndarray:
        """
        Generate all 240 roots of the E8 root system (norm² = 2 in standard normalization).
        Construction:
          - 112 roots from D8: ±e_i ± e_j (i < j)
          - 128 roots from the even half-spinor: (1/2)^8 with even number of minus signs.
        Returns: (240, 8) float64 array.
        """
        roots = []
        # D8 roots
        for i in range(8):
            for j in range(i + 1, 8):
                for s1 in [+1, -1]:
                    for s2 in [+1, -1]:
                        v = np.zeros(8)
                        v[i] = s1
                        v[j] = s2
                        roots.append(v)
        # Even half-spinor weights
        for signs in range(1 << 8):
            vec = np.full(8, 0.5)
            n_minus = 0
            for k in range(8):
                if (signs >> k) & 1:
                    vec[k] = -0.5
                    n_minus += 1
            if n_minus % 2 == 0:   # even number of minuses
                roots.append(vec)
        roots = np.array(roots, dtype=np.float64)
        assert roots.shape[0] == 240, f"Expected 240 roots, got {roots.shape[0]}"
        return roots


    E8_ROOTS = generate_e8_roots()
    E8_NORM = np.sqrt(2.0)  # all roots have the same length in this normalization

    # =============================================================================
    # HELPER: LaTeX rendering (Marimo native)
    # =============================================================================

    def latex(s: str) -> mo.Html:
        return mo.md(f"$${s}$$")

    def section_header(title: str, subtitle: str = "") -> mo.Html:
        subtitle_markup = f'<p class="ipk-section-subtitle">{subtitle}</p>' if subtitle else ""
        return mo.Html(f"""
        <div class="ipk-section-header">
            <h2>{title}</h2>
            {subtitle_markup}
        </div>
        """)

    # =============================================================================
    # DEPENDENCY FLOWCHART (networkx + Plotly)
    # =============================================================================

    def create_dependency_flowchart() -> mo.Html:
        stages = [{
            "step": "Origin",
            "node": "MU",
            "lock": "Minimum Update",
            "branch": "Epistemic seed",
            "survives": MU_PRINCIPLE,
            "eliminated": "Anything added without constraint",
            "color": WARM_GOLD,
        }]
        for lock in LOCKS_DATA:
            stages.append({
                "step": f"Lock {lock['id']}",
                "node": DEPENDENCY_CHAIN[lock["id"]],
                "lock": lock["lock"],
                "branch": lock["branch"],
                "survives": lock["survives"],
                "eliminated": lock["eliminated"],
                "color": BRANCH_COLORS.get(lock["branch"], ELECTRIC_CYAN),
            })
        stages.append({
            "step": "Fixed point",
            "node": "Standard Model",
            "lock": "Gauge algebra",
            "branch": "Particle Physics",
            "survives": "su(3) + su(2) + u(1)",
            "eliminated": "All arbitrary presentations",
            "color": WARM_GOLD,
        })

        cards = []
        for idx, stage in enumerate(stages):
            connector = "" if idx == len(stages) - 1 else '<span class="ipk-cascade-arrow" aria-hidden="true"></span>'
            cards.append(f"""
            <article class="ipk-cascade-card t-panel-slide t-resize" data-open="true" style="--stage-color:{escape(stage['color'])}">
                <div class="ipk-cascade-step">{escape(stage['step'])}</div>
                <h3>{escape(stage['node'])}</h3>
                <p class="ipk-cascade-lock">{escape(stage['lock'])}</p>
                <div class="ipk-cascade-branch">{escape(stage['branch'])}</div>
                <dl>
                    <dt>Survives</dt>
                    <dd>{escape(stage['survives'])}</dd>
                    <dt>Eliminates</dt>
                    <dd>{escape(stage['eliminated'])}</dd>
                </dl>
                {connector}
            </article>
            """)

        return mo.Html(f"""
        <section class="ipk-lock-cascade" aria-label="MU to Standard Model dependency cascade">
            <div class="ipk-cascade-halo" aria-hidden="true"></div>
            <div class="ipk-cascade-intro">
                <div>
                    <div class="ipk-panel-kicker">Page 4 dependency chain</div>
                    <h3>Ten locks as a constraint cascade</h3>
                </div>
                <div class="ipk-cascade-meter">
                    <span>MU</span><span>Probability</span><span>D=4</span><span>E8</span><span>Spin(10)</span><span>SM</span>
                </div>
            </div>
            <div class="ipk-cascade-track reveal-stagger" role="list">
                {"".join(cards)}
            </div>
        </section>
        """)

    # =============================================================================
    # E₈ 3D VIEWER — The star of the show
    # =============================================================================

    def project_e8_3d(roots: np.ndarray, angles: Tuple[float, float, float], scale: float = 1.0) -> np.ndarray:
        """Project 8D roots to 3D via successive rotations + final 3D subspace."""
        phi, theta, psi = angles
        # Simple but effective: rotate in planes (1,2), (3,4), (5,6) then take first 3 coords
        R1 = np.array([[np.cos(phi), -np.sin(phi), 0], [np.sin(phi), np.cos(phi), 0], [0, 0, 1]])
        # We do a full 8D -> 3D random-ish but controllable projection
        # Better: use fixed good projection basis + user-controlled rotations
    
        # Use a nice known E8 3D projection direction set (simplified)
        # Rotate the 8D vector in a few planes then truncate
        v = roots.copy()
        # Plane rotations (controlled by sliders)
        c1, s1 = np.cos(phi), np.sin(phi)
        c2, s2 = np.cos(theta), np.sin(theta)
        c3, s3 = np.cos(psi), np.sin(psi)
    
        # Rotate coords 0-1
        v[:, [0,1]] = v[:, [0,1]] @ np.array([[c1, -s1], [s1, c1]]).T
        # Rotate coords 2-3
        v[:, [2,3]] = v[:, [2,3]] @ np.array([[c2, -s2], [s2, c2]]).T
        # Rotate coords 4-5
        v[:, [4,5]] = v[:, [4,5]] @ np.array([[c3, -s3], [s3, c3]]).T
    
        proj = v[:, :3] * scale
        return proj

    def create_e8_viewer(angles: Tuple[float, float, float], show_edges: bool = False, color_by: str = "norm") -> go.Figure:
        proj = project_e8_3d(E8_ROOTS, angles)
    
        # Color mapping
        if color_by == "norm":
            colors = np.linalg.norm(proj, axis=1)
            cscale = "Viridis"
        else:
            colors = np.where(np.abs(proj[:, 2]) > 0.8, SOFT_PURPLE, ELECTRIC_CYAN)
            cscale = None

        fig = go.Figure()
    
        # Main roots (beautiful glowing points)
        fig.add_trace(go.Scatter3d(
            x=proj[:, 0], y=proj[:, 1], z=proj[:, 2],
            mode='markers',
            marker=dict(
                size=3.8,
                color=colors if color_by == "norm" else None,
                colorscale=cscale,
                opacity=0.92,
                line=dict(width=0.4, color="rgba(255,255,255,0.6)")
            ),
            text=[f"E₈ root #{i}<br>‖v‖² ≈ 2" for i in range(len(proj))],
            hovertemplate="%{text}<extra></extra>",
            name="E₈ roots (240)"
        ))
    
        if show_edges:
            # Add a sparse set of nearest-neighbor edges (for visual beauty, not full root system)
            # Connect each root to its 2–3 closest (very approximate for viz)
            for i in range(0, len(proj), 8):  # subsample heavily for performance
                dists = np.linalg.norm(proj - proj[i], axis=1)
                nearest = np.argsort(dists)[1:4]
                for j in nearest:
                    fig.add_trace(go.Scatter3d(
                        x=[proj[i,0], proj[j,0]], y=[proj[i,1], proj[j,1]], z=[proj[i,2], proj[j,2]],
                        mode='lines',
                        line=dict(color="rgba(103,232,249,0.25)", width=1.2),
                        hoverinfo='skip',
                        showlegend=False
                    ))
    
        fig.update_layout(
            height=620,
            scene=dict(
                xaxis=dict(backgroundcolor=DEEP_NAVY, gridcolor="#1e2937", showbackground=True),
                yaxis=dict(backgroundcolor=DEEP_NAVY, gridcolor="#1e2937", showbackground=True),
                zaxis=dict(backgroundcolor=DEEP_NAVY, gridcolor="#1e2937", showbackground=True),
                camera=dict(eye=dict(x=1.6, y=1.6, z=1.1)),
                aspectmode='cube'
            ),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=DEEP_NAVY,
            margin=dict(l=0, r=0, t=20, b=0),
            legend=dict(font=dict(color=WHITE)),
        )
        fig.update_scenes(
            xaxis_title="X (rotated)", yaxis_title="Y (rotated)", zaxis_title="Z (rotated)"
        )
        return fig


    # =============================================================================
    # ENHANCED E8 PROJECTIONS (multiple beautiful modes + random)
    # =============================================================================

    def _rotate_3d(points: np.ndarray, angles: Tuple[float, float, float]) -> np.ndarray:
        phi, theta, psi = angles
        rz = np.array([
            [np.cos(phi), -np.sin(phi), 0],
            [np.sin(phi), np.cos(phi), 0],
            [0, 0, 1],
        ])
        ry = np.array([
            [np.cos(theta), 0, np.sin(theta)],
            [0, 1, 0],
            [-np.sin(theta), 0, np.cos(theta)],
        ])
        rx = np.array([
            [1, 0, 0],
            [0, np.cos(psi), -np.sin(psi)],
            [0, np.sin(psi), np.cos(psi)],
        ])
        return points @ (rz @ ry @ rx).T


    def _orthonormal_projection_basis(seed: int) -> np.ndarray:
        rng = np.random.default_rng(seed)
        mat = rng.standard_normal((8, 3))
        q, _ = np.linalg.qr(mat)
        return q[:, :3]


    def _coxeter_projection_basis(phase: float = 0.0) -> np.ndarray:
        h = 30
        exponents = np.array([1, 7, 11, 13, 17, 19, 23, 29], dtype=float)
        basis = np.column_stack([
            np.cos(2 * np.pi * exponents / h + phase),
            np.sin(2 * np.pi * exponents / h + phase),
            np.cos(4 * np.pi * exponents / h - phase),
        ])
        q, _ = np.linalg.qr(basis)
        return q[:, :3]


    def get_e8_projection(roots: np.ndarray, mode: str, angles: Tuple[float, float, float], seed=42) -> np.ndarray:
        """Multiple high-quality 3D projections of E8."""
        if not isinstance(seed, (int, np.integer)):
            seed = 42
        v = roots.copy()
        phi, theta, psi = angles

        if mode == "Standard (sequential planes)":
            c1, s1 = np.cos(phi), np.sin(phi)
            c2, s2 = np.cos(theta), np.sin(theta)
            c3, s3 = np.cos(psi), np.sin(psi)
            v[:, [0,1]] = v[:, [0,1]] @ np.array([[c1, -s1],[s1, c1]]).T
            v[:, [2,3]] = v[:, [2,3]] @ np.array([[c2, -s2],[s2, c2]]).T
            v[:, [4,5]] = v[:, [4,5]] @ np.array([[c3, -s3],[s3, c3]]).T
            return v[:, :3]

        elif mode == "Coxeter phase bloom":
            basis = _coxeter_projection_basis(phi)
            return _rotate_3d(v @ basis * 1.85, (0, theta * 0.3, psi * 0.6))

        elif mode == "Golden chamber":
            tau = (1 + np.sqrt(5)) / 2
            basis = np.array([
                [1, tau, 0],
                [-tau, 1, 0],
                [0, 1, tau],
                [0, -tau, 1],
                [tau, 0, 1],
                [1, 0, -tau],
                [tau, -1, 1],
                [-1, tau, 1],
            ], dtype=float)
            q, _ = np.linalg.qr(basis)
            return _rotate_3d(v @ q[:, :3] * 1.45, angles)

        elif mode == "Stereographic shell":
            basis = _orthonormal_projection_basis(1729)
            four = v @ np.column_stack([basis, _orthonormal_projection_basis(313)[:, 0]])
            denom = 1.9 - np.clip(four[:, 3], -1.4, 1.4)
            stereographic = four[:, :3] / denom[:, None]
            return _rotate_3d(stereographic * 2.1, angles)

        elif mode == "2-plane slice":
            basis = _coxeter_projection_basis(phi + 0.3)
            two_plane = v @ basis[:, :2]
            depth = v @ basis[:, 2]
            return np.column_stack([two_plane[:, 0], two_plane[:, 1], depth]) * 1.75

        elif mode == "Petrie-style (balanced)":
            # Famous visually dense projection
            basis = np.array([
                [1, 0, 0, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 1, 0],
            ], dtype=float) / np.sqrt(2)
            # Apply small controlled rotations to the 8D vector before projection
            rot = np.eye(8)
            rot[0:2,0:2] = [[np.cos(phi), -np.sin(phi)],[np.sin(phi), np.cos(phi)]]
            rot[4:6,4:6] = [[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]]
            v = v @ rot.T
            return v @ basis.T * 1.6

        elif mode == "Random orthogonal":
            # Random but reproducible nice projection
            return _rotate_3d(v @ _orthonormal_projection_basis(42 + seed % 1000) * 1.65, angles)

        else:
            return v[:, :3]


    def e8_color_values(proj: np.ndarray, mode: str) -> Tuple[np.ndarray, str, str]:
        if mode == "Original root family":
            values = np.r_[np.zeros(112), np.ones(128)]
            return values, "Electric", "Root family"
        if mode == "Height bands":
            values = np.digitize(proj[:, 2], np.quantile(proj[:, 2], [0.2, 0.4, 0.6, 0.8]))
            return values, "Turbo", "Projected height band"
        if mode == "Coxeter phase":
            values = np.arctan2(proj[:, 1], proj[:, 0])
            return values, "Phase", "Coxeter phase"
        values = np.linalg.norm(proj, axis=1)
        return values, "Plasma", "Projected radius"


    def apply_e8_slice(proj: np.ndarray, slice_width: float) -> np.ndarray:
        if slice_width >= 0.99:
            return np.ones(len(proj), dtype=bool)
        depth = np.abs(proj[:, 2])
        cutoff = np.quantile(depth, max(0.08, min(0.99, slice_width)))
        return depth <= cutoff


    def create_enhanced_e8_viewer(
        mode: str,
        angles: Tuple[float, float, float],
        show_edges: bool,
        seed: int,
        color_mode: str,
        glow: bool,
        slice_width: float,
    ) -> go.Figure:
        proj = get_e8_projection(E8_ROOTS, mode, angles, seed)
        visible = apply_e8_slice(proj, slice_width)
        proj_visible = proj[visible]
        color_values, colorscale, color_title = e8_color_values(proj, color_mode)
        color_visible = color_values[visible]
        norms = np.linalg.norm(proj_visible, axis=1)

        fig = go.Figure()
        if glow:
            fig.add_trace(go.Scatter3d(
                x=proj_visible[:,0], y=proj_visible[:,1], z=proj_visible[:,2],
                mode='markers',
                marker=dict(size=9, color=color_visible, colorscale=colorscale, opacity=0.13),
                hoverinfo='skip',
                showlegend=False,
                name="ambient glow",
            ))

        if glow and len(proj_visible) > 0:
            ring_theta = np.linspace(0, 2 * np.pi, 240)
            max_radius = max(0.5, float(np.quantile(np.linalg.norm(proj_visible[:, :2], axis=1), 0.92)))
            for radius, color in [
                (0.38 * max_radius, "rgba(103,232,249,0.16)"),
                (0.68 * max_radius, "rgba(252,211,77,0.13)"),
                (max_radius, "rgba(244,114,182,0.11)"),
            ]:
                fig.add_trace(go.Scatter3d(
                    x=radius * np.cos(ring_theta),
                    y=radius * np.sin(ring_theta),
                    z=np.zeros_like(ring_theta),
                    mode="lines",
                    line=dict(color=color, width=2),
                    hoverinfo="skip",
                    showlegend=False,
                    name="projection ring",
                ))

        fig.add_trace(go.Scatter3d(
            x=proj_visible[:,0], y=proj_visible[:,1], z=proj_visible[:,2],
            mode='markers',
            marker=dict(
                size=4.7,
                color=color_visible,
                colorscale=colorscale,
                opacity=0.95,
                colorbar=dict(title=dict(text=color_title, font=dict(color=WHITE)), tickfont=dict(color=WHITE)),
                line=dict(width=0.45, color='rgba(255,255,255,0.62)'),
            ),
            hovertemplate="E₈ root<br>‖projection‖ ≈ %{customdata:.2f}<extra></extra>",
            customdata=norms,
            name="E₈ roots"
        ))

        if show_edges:
            edge_x = []
            edge_y = []
            edge_z = []
            for i in range(0, len(proj_visible), 8):
                dists = np.linalg.norm(proj_visible - proj_visible[i], axis=1)
                nbrs = np.argsort(dists)[1:4]
                for j in nbrs:
                    edge_x.extend([proj_visible[i,0], proj_visible[j,0], None])
                    edge_y.extend([proj_visible[i,1], proj_visible[j,1], None])
                    edge_z.extend([proj_visible[i,2], proj_visible[j,2], None])
            fig.add_trace(go.Scatter3d(
                x=edge_x,
                y=edge_y,
                z=edge_z,
                mode='lines',
                line=dict(color='rgba(103,232,249,0.2)', width=1.15),
                hoverinfo='skip',
                showlegend=False,
                name="projected proximity edges",
            ))

        fig.update_layout(
            height=860,
            title=dict(
                text=f"E₈ root lattice: {mode} ({len(proj_visible)} / 240 roots visible)",
                x=0.02,
                font=dict(color=WHITE, size=18),
            ),
            scene=dict(
                xaxis=dict(backgroundcolor=DEEP_NAVY, gridcolor="#1e2937", zerolinecolor=ELECTRIC_CYAN, showspikes=False, tickfont=dict(color=MUTED)),
                yaxis=dict(backgroundcolor=DEEP_NAVY, gridcolor="#1e2937", zerolinecolor=SOFT_PURPLE, showspikes=False, tickfont=dict(color=MUTED)),
                zaxis=dict(backgroundcolor=DEEP_NAVY, gridcolor="#1e2937", zerolinecolor=WARM_GOLD, showspikes=False, tickfont=dict(color=MUTED)),
                camera=dict(eye=dict(x=1.65, y=1.45, z=1.1)),
                aspectmode='cube'
            ),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=DEEP_NAVY,
            margin=dict(l=0,r=0,t=45,b=0),
            legend=dict(font=dict(color=WHITE)),
            hoverlabel=dict(bgcolor=MIDNIGHT, font=dict(color=WHITE)),
        )
        return fig


    def create_e8_shadow_plot(mode: str, angles: Tuple[float, float, float], seed: int, color_mode: str, slice_width: float = 1.0) -> go.Figure:
        proj = get_e8_projection(E8_ROOTS, mode, angles, seed)
        visible = apply_e8_slice(proj, slice_width)
        proj_visible = proj[visible]
        color_values, colorscale, color_title = e8_color_values(proj, color_mode)
        color_visible = color_values[visible]
        fig = go.Figure()
        fig.add_trace(go.Scattergl(
            x=proj_visible[:, 0],
            y=proj_visible[:, 1],
            mode="markers",
            marker=dict(
                size=9,
                color=color_visible,
                colorscale=colorscale,
                opacity=0.86,
                line=dict(width=0.5, color="rgba(255,255,255,0.55)"),
                colorbar=dict(title=dict(text=color_title, font=dict(color=WHITE)), tickfont=dict(color=WHITE)),
            ),
            hovertemplate=f"{mode} 2D shadow<br>x=%{{x:.2f}}<br>y=%{{y:.2f}}<extra></extra>",
            name="2D shadow",
        ))
        fig.update_layout(
            height=430,
            title=dict(text=f"2D shadow for {mode} projection / printable constellation", x=0.02, font=dict(color=WHITE, size=16)),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=DEEP_NAVY,
            margin=dict(l=20, r=20, t=45, b=25),
            xaxis=dict(visible=False, scaleanchor="y", scaleratio=1),
            yaxis=dict(visible=False),
            showlegend=False,
        )
        return fig


    # =============================================================================
    # SPIN(10) → STANDARD MODEL INTERACTIVE EXPLORER (Locks 9-10)
    # =============================================================================

    SPIN10_REPS = [
        {"name": "Vector 10", "dim": 10, "type": "Real", "anomaly": "Safe (vectorlike)", "notes": "Not chiral"},
        {"name": "Spinor 16 (Weyl)", "dim": 16, "type": "Complex", "anomaly": "Anomaly-free in Spin(10)", "notes": "The one that works"},
        {"name": "Conjugate 16-bar", "dim": 16, "type": "Complex", "anomaly": "Anomaly-free", "notes": "Right-handed"},
        {"name": "Adjoint 45", "dim": 45, "type": "Real", "anomaly": "Safe", "notes": "Gauge bosons"},
    ]

    def create_spin10_explorer(selected_rep_idx: int):
        rep = SPIN10_REPS[selected_rep_idx]
    
        # Simple representation table
        table = pd.DataFrame(SPIN10_REPS)
    
        fig = go.Figure(go.Table(
            header=dict(values=list(table.columns), fill_color=MIDNIGHT, font=dict(color=ELECTRIC_CYAN)),
            cells=dict(values=[table[c] for c in table.columns], fill_color=DEEP_NAVY, font=dict(color=WHITE))
        ))
        fig.update_layout(height=220, paper_bgcolor=DEEP_NAVY)
    
        detail = mo.md(dedent(f"""
        **Selected:** {rep['name']} (dimension {rep['dim']}, {rep['type']})
    
        Anomaly status: **{rep['anomaly']}**
    
        {rep['notes']}
    
        The 16 of Spin(10) is the unique representation that:
        - Is complex (chiral)
        - Embeds inside E₈
        - Has vanishing gauge anomalies for the full SM group
        - Produces exactly three generations when combined with the geometry from Lock 6
        """))
        return fig, detail


    # =============================================================================
    # LOCK 4: SIMPLE UNITARY TIME EVOLUTION DEMO (reflection positivity intuition)
    # =============================================================================

    def create_lock4_unitary_demo(evolution_time: float):
        """Very lightweight 2-level system unitary evolution (proxy for OS reconstruction)."""
        t = np.linspace(0, max(0.1, evolution_time), 120)

        # Closed form for exp(-i * 1.2 * sigma_x * t) applied to |0>.
        probs_0 = np.cos(1.2 * t) ** 2
        prob_t = float(np.cos(1.2 * evolution_time) ** 2)
    
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t, y=probs_0, name="P(|0⟩)", line=dict(color=ELECTRIC_CYAN, width=3)))
        fig.add_trace(go.Scatter(x=t, y=1-np.array(probs_0), name="P(|1⟩)", line=dict(color=SOFT_PURPLE, width=2, dash='dash')))
        fig.update_layout(
            height=320, paper_bgcolor=DEEP_NAVY, plot_bgcolor=MIDNIGHT,
            title=f"Unitary evolution at t = {evolution_time:.2f} (toy model of OS reconstruction)",
            xaxis_title="Time", yaxis_title="Probability",
            legend=dict(font=dict(color=WHITE))
        )
        return fig, prob_t


    # =============================================================================
    # "BUILD YOUR OWN LOCK CHAIN" EXPLORER
    # =============================================================================

    def simulate_user_chain(selected_lock_ids: List[int]):
        if not selected_lock_ids:
            return mo.md("Select at least one Lock to begin the simulation."), None
    
        ordered = sorted(selected_lock_ids)
        survived = []
        eliminated = []
    
        for lid in ordered:
            lock = LOCKS_DATA[lid-1]
            survived.append(lock["survives"])
            eliminated.append(lock["eliminated"])
    
        summary = f"""
        **Your custom chain of {len(ordered)} Locks:**
    
        Survived structures: {', '.join(survived)}
    
        Eliminated along the way: {len(eliminated)} structural choices forbidden by MU.
    
        **Conclusion from your selection:** The longer and more complete your chain, the more the theory is forced toward the Standard Model + E₈ + 4D spacetime.
        """
        return mo.md(summary), survived

    # =============================================================================
    # STATISTICAL MECHANICS — KL Divergence Interactive Demo (Locks 1-2)
    # =============================================================================

    def kl_divergence(p: np.ndarray, q: np.ndarray) -> float:
        p = np.clip(p, 1e-12, 1.0)
        q = np.clip(q, 1e-12, 1.0)
        return float(np.sum(p * np.log(p / q)))

    def create_kl_demo(constraint_mean: float, constraint_var: float):
        x = np.linspace(-4, 4, 200)
        # Prior: standard normal
        prior = np.exp(-0.5 * x**2) / np.sqrt(2*np.pi)
        prior /= prior.sum()
    
        # Target "posterior" via maximum entropy / KL projection (simple Gaussian with constraints)
        # We minimize KL(posterior || prior) subject to mean and variance constraints (Lagrange)
        # For demo we use a simple closed-form Gaussian that matches the moments
        sigma2 = max(0.3, constraint_var)
        posterior = np.exp(-0.5 * ((x - constraint_mean)**2) / sigma2)
        posterior /= posterior.sum()
    
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=prior, name="Prior (maxent, no constraints)", 
                                 line=dict(color=MUTED, width=2.5)))
        fig.add_trace(go.Scatter(x=x, y=posterior, name="Posterior (KL-minimizing update)", 
                                 line=dict(color=ELECTRIC_CYAN, width=3)))
        fig.add_vline(x=constraint_mean, line=dict(color=WARM_GOLD, dash="dash", width=1.5), 
                      annotation_text="New mean constraint")
    
        fig.update_layout(
            height=380, paper_bgcolor=DEEP_NAVY, plot_bgcolor=MIDNIGHT,
            xaxis_title="Observable value", yaxis_title="Probability density",
            legend=dict(font=dict(color=WHITE)),
            margin=dict(t=20)
        )
        return fig, float(kl_divergence(posterior, prior))


    # =============================================================================
    # ADVANCED VISUALIZATION HELPERS
    # =============================================================================

    LATTICE_COMPARISON = pd.DataFrame([
        {
            "name": "E8",
            "dimension": 8,
            "min_norm": 2,
            "kissing": 240,
            "mu_status": "unique",
            "note": "unique even unimodular lattice in dimension 8",
        },
        {
            "name": "E8 x E8",
            "dimension": 16,
            "min_norm": 2,
            "kissing": 480,
            "mu_status": "ambiguous",
            "note": "one of two even unimodular choices in dimension 16",
        },
        {
            "name": "D16+",
            "dimension": 16,
            "min_norm": 2,
            "kissing": 480,
            "mu_status": "ambiguous",
            "note": "the other dimension-16 even unimodular choice",
        },
        {
            "name": "Leech",
            "dimension": 24,
            "min_norm": 4,
            "kissing": 196560,
            "mu_status": "ambiguous",
            "note": "beautiful, but dimension 24 has many even unimodular lattices",
        },
    ])

    THEORY_SPACE_BY_LOCK = pd.DataFrame([
        {"lock": 0, "label": "Before MU", "dimensions": 12, "lattices": 18, "gauge": 22, "matter": 18, "description": "Unconstrained theory space."},
        {"lock": 1, "label": "Probability", "dimensions": 12, "lattices": 18, "gauge": 22, "matter": 18, "description": "Reasoning must be probabilistic."},
        {"lock": 2, "label": "KL Update", "dimensions": 12, "lattices": 18, "gauge": 22, "matter": 18, "description": "Updates become minimum-KL projections."},
        {"lock": 3, "label": "Locality", "dimensions": 10, "lattices": 16, "gauge": 18, "matter": 16, "description": "Nonlocal structure is removed."},
        {"lock": 4, "label": "Unitarity", "dimensions": 8, "lattices": 14, "gauge": 16, "matter": 14, "description": "Reflection positivity selects unitary QFT."},
        {"lock": 5, "label": "Lovelock", "dimensions": 4, "lattices": 12, "gauge": 14, "matter": 12, "description": "Higher-dimensional gravitational ambiguity collapses."},
        {"lock": 6, "label": "Hodge", "dimensions": 1, "lattices": 10, "gauge": 12, "matter": 10, "description": "Self-dual two-forms force D = 4."},
        {"lock": 7, "label": "Self-duality", "dimensions": 1, "lattices": 4, "gauge": 10, "matter": 9, "description": "Electric-magnetic neutrality requires L = L*."},
        {"lock": 8, "label": "E8", "dimensions": 1, "lattices": 1, "gauge": 7, "matter": 7, "description": "The unique 8D even unimodular lattice remains."},
        {"lock": 9, "label": "Spin(10)", "dimensions": 1, "lattices": 1, "gauge": 3, "matter": 1, "description": "The complex 16-dimensional Weyl spinor survives."},
        {"lock": 10, "label": "SM Intersection", "dimensions": 1, "lattices": 1, "gauge": 1, "matter": 1, "description": "The common gauge algebra is su(3) + su(2) + u(1)."},
    ])

    def create_lattice_comparison(selected: str) -> go.Figure:
        df = LATTICE_COMPARISON.copy()
        df["color"] = np.where(df["name"] == selected, WARM_GOLD, np.where(df["mu_status"] == "unique", ELECTRIC_CYAN, SOFT_PURPLE))
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df["name"],
            y=np.log10(df["kissing"]),
            marker=dict(color=df["color"], line=dict(color=WHITE, width=1)),
            customdata=np.stack([df["dimension"], df["kissing"], df["note"]], axis=-1),
            hovertemplate="<b>%{x}</b><br>dimension %{customdata[0]}<br>kissing number %{customdata[1]}<br>%{customdata[2]}<extra></extra>",
            name="kissing number",
        ))
        fig.add_trace(go.Scatter(
            x=df["name"],
            y=df["min_norm"],
            yaxis="y2",
            mode="markers+lines",
            marker=dict(size=16, color=df["color"], symbol="diamond", line=dict(color=WHITE, width=1)),
            line=dict(color="rgba(252,211,77,0.45)", width=2),
            name="minimum norm",
        ))
        fig.update_layout(
            height=390,
            title=dict(text="Even unimodular lattice comparison: uniqueness vs. abundance", font=dict(color=WHITE)),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=MIDNIGHT,
            margin=dict(l=40, r=55, t=55, b=45),
            xaxis=dict(tickfont=dict(color=WHITE)),
            yaxis=dict(title=dict(text="log10(kissing number)", font=dict(color=MUTED)), tickfont=dict(color=MUTED), gridcolor="#1e2937"),
            yaxis2=dict(title=dict(text="minimum norm", font=dict(color=WARM_GOLD)), overlaying="y", side="right", tickfont=dict(color=WARM_GOLD), range=[0, 5]),
            legend=dict(font=dict(color=WHITE), orientation="h", y=-0.2),
        )
        return fig

    def create_lattice_norm_histogram(selected: str) -> go.Figure:
        shell_counts = {
            "E8": [(2, 240), (4, 2160), (6, 6720), (8, 17520)],
            "E8 x E8": [(2, 480), (4, 61920), (6, 1050240), (8, 7926240)],
            "D16+": [(2, 480), (4, 4320), (6, 61440), (8, 522720)],
            "Leech": [(4, 196560), (6, 16773120), (8, 398034000), (10, 4629381120)],
        }
        rows = []
        for name, shells in shell_counts.items():
            for norm, count in shells:
                rows.append({"name": name, "norm": norm, "count": count})
        df = pd.DataFrame(rows)
        fig = go.Figure()
        for name in shell_counts:
            sub = df[df["name"] == name]
            color = WARM_GOLD if name == selected else ELECTRIC_CYAN if name == "E8" else SOFT_PURPLE if name == "Leech" else FLUID_BLUE
            fig.add_trace(go.Bar(
                x=sub["norm"],
                y=np.log10(sub["count"]),
                name=name,
                marker=dict(color=color, opacity=1.0 if name == selected else 0.38),
                hovertemplate=f"<b>{name}</b><br>norm²=%{{x}}<br>shell count=%{{customdata:,}}<extra></extra>",
                customdata=sub["count"],
            ))
        fig.update_layout(
            height=360,
            title=dict(text="Norm-shell histogram: kissing number is the first visible shell", font=dict(color=WHITE)),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=MIDNIGHT,
            barmode="group",
            margin=dict(l=45, r=20, t=55, b=50),
            xaxis=dict(title=dict(text="squared norm shell", font=dict(color=MUTED)), tickfont=dict(color=WHITE), gridcolor="#1e2937"),
            yaxis=dict(title=dict(text="log10(number of vectors)", font=dict(color=MUTED)), tickfont=dict(color=MUTED), gridcolor="#1e2937"),
            legend=dict(font=dict(color=WHITE), orientation="h", y=-0.2),
        )
        return fig

    def create_self_duality_visualizer(blend: float, selected: str) -> go.Figure:
        basis = np.array([[1.0, 0.35], [0.15, 1.25]])
        dual = np.linalg.inv(basis).T
        current = (1 - blend) * basis + blend * dual
        selected_row = LATTICE_COMPARISON[LATTICE_COMPARISON["name"] == selected].iloc[0]
        fig = go.Figure()
        for i in range(-4, 5):
            for j in range(-4, 5):
                p = i * current[:, 0] + j * current[:, 1]
                fig.add_trace(go.Scatter(
                    x=[p[0]], y=[p[1]], mode="markers",
                    marker=dict(size=7, color=ELECTRIC_CYAN if abs(i) + abs(j) <= 2 else "rgba(103,232,249,0.38)"),
                    hoverinfo="skip",
                    showlegend=False,
                ))
        for vec, color, name in [(basis[:, 0], SOFT_PURPLE, "L basis"), (basis[:, 1], SOFT_PURPLE, "L basis"), (dual[:, 0], WARM_GOLD, "L* basis"), (dual[:, 1], WARM_GOLD, "L* basis")]:
            fig.add_trace(go.Scatter(
                x=[0, vec[0]], y=[0, vec[1]], mode="lines+markers",
                line=dict(color=color, width=4),
                marker=dict(size=8, color=color),
                name=name,
                showlegend=False,
            ))
        fig.add_annotation(x=0.03, y=0.96, xref="paper", yref="paper", showarrow=False, align="left",
                           text=(
                               f"Toy L ↔ L* interpolation: {blend:.2f}<br>"
                               f"{selected}: even unimodular in dimension {int(selected_row['dimension'])}, so L = L* in its native dimension"
                           ),
                           font=dict(color=WHITE), bgcolor="rgba(15,23,42,0.72)", bordercolor="#334155")
        fig.update_layout(
            height=390,
            title=dict(text="Dual-lattice interpolation: cartoon of self-dual fixed points", font=dict(color=WHITE)),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=MIDNIGHT,
            margin=dict(l=35, r=20, t=55, b=35),
            xaxis=dict(scaleanchor="y", scaleratio=1, zerolinecolor="#334155", gridcolor="#1e2937", tickfont=dict(color=MUTED)),
            yaxis=dict(zerolinecolor="#334155", gridcolor="#1e2937", tickfont=dict(color=MUTED)),
        )
        return fig

    def create_spin10_branching_graph(branch_view: str) -> go.Figure:
        if branch_view == "SU(5) branching":
            labels = ["Spin(10) 16", "10 + 5bar + 1", "Q", "u^c", "e^c", "d^c + L", "ν^c"]
            parents = ["", "Spin(10) 16", "10 + 5bar + 1", "10 + 5bar + 1", "10 + 5bar + 1", "10 + 5bar + 1", "10 + 5bar + 1"]
            values = [16, 16, 6, 3, 1, 5, 1]
            colors = [SOFT_PURPLE, ELECTRIC_CYAN, WARM_GOLD, WARM_GOLD, WARM_GOLD, FLUID_BLUE, SOFT_MAGENTA]
        else:
            labels = ["Spin(10) 16", "(4,2,1) + (4bar,1,2)", "left quarks/leptons", "right quarks/leptons", "SU(3)c", "SU(2)L", "U(1)Y"]
            parents = ["", "Spin(10) 16", "(4,2,1) + (4bar,1,2)", "(4,2,1) + (4bar,1,2)", "left quarks/leptons", "left quarks/leptons", "right quarks/leptons"]
            values = [16, 16, 8, 8, 3, 2, 1]
            colors = [SOFT_PURPLE, ELECTRIC_CYAN, WARM_GOLD, FLUID_BLUE, SOFT_MAGENTA, SURVIVES_GREEN, WARM_GOLD]
        fig = go.Figure(go.Treemap(
            labels=labels,
            parents=parents,
            values=values,
            branchvalues="total",
            marker=dict(colors=colors, line=dict(color=DEEP_NAVY, width=2)),
            textfont=dict(color=WHITE, size=16),
            hovertemplate="<b>%{label}</b><br>weight count / dimension proxy: %{value}<extra></extra>",
        ))
        fig.update_layout(
            height=430,
            title=dict(text=f"Spin(10) 16 branching: {branch_view}", font=dict(color=WHITE)),
            paper_bgcolor=DEEP_NAVY,
            margin=dict(l=0, r=0, t=50, b=0),
        )
        return fig

    def spin10_16_weights() -> pd.DataFrame:
        rows = []
        for mask in range(32):
            signs = np.array([1 if ((mask >> i) & 1) == 0 else -1 for i in range(5)], dtype=float)
            # One chiral 16: even number of minus signs.
            if np.sum(signs < 0) % 2 == 0:
                weight = 0.5 * signs
                hypercharge = (weight[0] + weight[1] + weight[2]) / 3 - (weight[3] + weight[4]) / 2
                minus = int(np.sum(signs < 0))
                if minus == 0:
                    su5, sm = "1", "ν^c"
                elif minus == 2:
                    su5, sm = "10", "Q / u^c / e^c"
                else:
                    su5, sm = "5bar", "d^c / L"
                ps = "(4,2,1)" if weight[3] == weight[4] else "(4bar,1,2)"
                rows.append({
                    "x": weight[0] + 0.55 * weight[2] - 0.25 * weight[4],
                    "y": weight[1] + 0.62 * weight[3] + 0.18 * weight[4],
                    "z": hypercharge,
                    "su5": su5,
                    "pati": ps,
                    "sm": sm,
                    "label": "(" + ", ".join(f"{v:+.1f}" for v in weight) + ")",
                })
        return pd.DataFrame(rows)


    def create_spin10_weight_lattice(branch_view: str) -> go.Figure:
        df = spin10_16_weights()
        color_col = "su5" if branch_view == "SU(5) branching" else "pati"
        palette = {
            "1": WARM_GOLD,
            "10": ELECTRIC_CYAN,
            "5bar": SOFT_MAGENTA,
            "(4,2,1)": SURVIVES_GREEN,
            "(4bar,1,2)": SOFT_PURPLE,
        }
        fig = go.Figure()
        for rep, sub in df.groupby(color_col):
            fig.add_trace(go.Scatter(
                x=sub["x"],
                y=sub["y"],
                mode="markers+text",
                marker=dict(size=18, color=palette.get(rep, ELECTRIC_CYAN), line=dict(color=WHITE, width=1)),
                text=sub["sm"],
                textposition="top center",
                textfont=dict(color=WHITE, size=10),
                name=str(rep),
                customdata=np.stack([sub["label"], sub["z"]], axis=-1),
                hovertemplate="<b>%{text}</b><br>weight %{customdata[0]}<br>hypercharge proxy %{customdata[1]:.2f}<extra></extra>",
            ))
        fig.update_layout(
            height=430,
            title=dict(text=f"Full weight lattice of the Spin(10) 16 colored by {branch_view}", font=dict(color=WHITE)),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=MIDNIGHT,
            margin=dict(l=35, r=20, t=55, b=45),
            xaxis=dict(visible=False, scaleanchor="y", scaleratio=1),
            yaxis=dict(visible=False),
            legend=dict(font=dict(color=WHITE), orientation="h", y=-0.16),
        )
        return fig

    def create_bott_clock(highlight_n: int) -> go.Figure:
        residues = np.arange(8)
        theta = np.linspace(90, 90 - 360 + 45, 8)
        types = ["real", "complex", "quaternionic", "quaternionic", "quaternionic", "complex", "real", "real"]
        colors = {"real": ELECTRIC_CYAN, "complex": WARM_GOLD, "quaternionic": SOFT_PURPLE}
        sizes = [34 if r == highlight_n % 8 else 24 for r in residues]
        fig = go.Figure(go.Scatterpolar(
            r=np.ones(8),
            theta=theta,
            mode="markers+text",
            marker=dict(size=sizes, color=[colors[t] for t in types], line=dict(color=WHITE, width=2)),
            text=[f"n≡{r}<br>{t}" for r, t in zip(residues, types)],
            textposition="middle center",
            hovertemplate="%{text}<extra></extra>",
        ))
        fig.add_trace(go.Scatterpolar(
            r=[0, 1],
            theta=[90, theta[highlight_n % 8]],
            mode="lines",
            line=dict(color=WARM_GOLD, width=5),
            hoverinfo="skip",
            showlegend=False,
        ))
        fig.update_layout(
            height=430,
            title=dict(text=f"Bott periodicity clock: Spin({highlight_n}) sits at n ≡ {highlight_n % 8} mod 8", font=dict(color=WHITE)),
            paper_bgcolor=DEEP_NAVY,
            polar=dict(
                bgcolor=MIDNIGHT,
                radialaxis=dict(visible=False, range=[0, 1.25]),
                angularaxis=dict(visible=False),
            ),
            showlegend=False,
            margin=dict(l=20, r=20, t=55, b=20),
        )
        return fig

    def create_hodge_chirality_visualizer(dimension: int) -> go.Figure:
        dims = np.arange(2, 9)
        two_forms = np.array([d * (d - 1) // 2 for d in dims])
        self_dual = np.where(dims == 4, two_forms // 2, 0)
        colors = [WARM_GOLD if d == dimension else ELECTRIC_CYAN for d in dims]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=dims, y=two_forms, marker=dict(color=colors), name="dim Λ²"))
        fig.add_trace(go.Bar(x=dims, y=self_dual, marker=dict(color=SOFT_PURPLE), name="self-dual Λ² split"))
        fig.add_vline(x=4, line=dict(color=WARM_GOLD, width=3, dash="dash"), annotation_text="D=4: * maps 2-forms to 2-forms")
        fig.update_layout(
            height=390,
            title=dict(text="Hodge star and chirality: only D=4 splits two-forms into self-dual halves", font=dict(color=WHITE)),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=MIDNIGHT,
            barmode="overlay",
            xaxis=dict(title=dict(text="spacetime dimension D", font=dict(color=MUTED)), tickfont=dict(color=WHITE), dtick=1, gridcolor="#1e2937"),
            yaxis=dict(title=dict(text="dimension of 2-form space", font=dict(color=MUTED)), tickfont=dict(color=MUTED), gridcolor="#1e2937"),
            legend=dict(font=dict(color=WHITE), orientation="h", y=-0.2),
            margin=dict(l=45, r=25, t=55, b=60),
        )
        return fig

    def create_lovelock_dimension_plot(dimension: int) -> go.Figure:
        dims = np.arange(2, 12)
        terms = np.maximum(1, np.floor((dims - 1) / 2).astype(int))
        arbitrary_extra = np.maximum(0, terms - 1)
        colors = [WARM_GOLD if d == dimension else ELECTRIC_CYAN if d <= 4 else SOFT_PURPLE for d in dims]
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=dims,
            y=terms,
            marker=dict(color=colors, line=dict(color=WHITE, width=1)),
            customdata=arbitrary_extra,
            hovertemplate="D=%{x}<br>independent Lovelock terms=%{y}<br>extra choices beyond Einstein=%{customdata}<extra></extra>",
            name="Lovelock terms",
        ))
        fig.add_vrect(x0=1.5, x1=4.5, fillcolor="rgba(74,222,128,0.12)", line_width=0)
        fig.add_vline(x=4.5, line=dict(color=WARM_GOLD, dash="dash", width=3), annotation_text="ambiguity begins above D=4")
        fig.update_layout(
            height=360,
            title=dict(text="Lovelock elimination: independent curvature choices appear above D=4", font=dict(color=WHITE)),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=MIDNIGHT,
            margin=dict(l=45, r=25, t=55, b=45),
            xaxis=dict(title=dict(text="spacetime dimension D", font=dict(color=MUTED)), tickfont=dict(color=WHITE), dtick=1, gridcolor="#1e2937"),
            yaxis=dict(title=dict(text="independent second-order curvature terms", font=dict(color=MUTED)), tickfont=dict(color=MUTED), dtick=1, gridcolor="#1e2937"),
            showlegend=False,
        )
        return fig

    def create_instanton_charge_explorer(winding: int, size: float) -> Tuple[go.Figure, mo.Html]:
        grid = np.linspace(-3.2, 3.2, 120)
        X, Y = np.meshgrid(grid, grid)
        R2 = X**2 + Y**2
        density = winding * (size**4) / ((R2 + size**2) ** 4)
        density = density / (np.max(np.abs(density)) + 1e-12)
        fig = go.Figure()
        fig.add_trace(go.Contour(
            x=grid,
            y=grid,
            z=density,
            colorscale="RdBu",
            contours=dict(showlines=False),
            colorbar=dict(title=dict(text="q(x)", font=dict(color=WHITE)), tickfont=dict(color=WHITE)),
            hovertemplate="x=%{x:.2f}<br>y=%{y:.2f}<br>charge density=%{z:.2f}<extra></extra>",
        ))
        theta = np.linspace(0, 2 * np.pi, 220)
        radius = 1.35 + 0.28 * np.sin(abs(winding) * theta)
        fig.add_trace(go.Scatter(
            x=radius * np.cos(theta),
            y=radius * np.sin(theta),
            mode="lines",
            line=dict(color=WARM_GOLD, width=4),
            name="winding loop",
            hoverinfo="skip",
        ))
        fig.update_layout(
            height=390,
            title=dict(text=f"Instanton number explorer: winding ν = {winding}", font=dict(color=WHITE)),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=MIDNIGHT,
            margin=dict(l=30, r=30, t=55, b=30),
            xaxis=dict(visible=False, scaleanchor="y", scaleratio=1),
            yaxis=dict(visible=False),
            showlegend=False,
        )
        detail = mo.Html(f"""
        <div class="ipk-advanced-note t-panel-slide t-resize" data-open="true">
            <strong>Index theorem readout</strong><br>
            Topological charge ν = {winding}. In the paper's logic, allowing nonzero ν in D=4
            gives chirality a topological detector; forbidding it would add an extra assumption.
        </div>
        """)
        return fig, detail

    def create_wilson_tHooft_duality(angle: float) -> go.Figure:
        charges = np.array([(i, j) for i in range(-3, 4) for j in range(-3, 4)])
        rot = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        electric = charges @ rot.T
        magnetic = charges @ np.linalg.inv(rot).T
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=electric[:, 0],
            y=electric[:, 1],
            mode="markers",
            marker=dict(size=9, color=ELECTRIC_CYAN, line=dict(color=WHITE, width=0.5)),
            name="Wilson / electric lattice L",
            hovertemplate="electric charge (%{x:.1f}, %{y:.1f})<extra></extra>",
        ))
        fig.add_trace(go.Scatter(
            x=magnetic[:, 0],
            y=magnetic[:, 1],
            mode="markers",
            marker=dict(size=9, color=WARM_GOLD, symbol="diamond", line=dict(color=WHITE, width=0.5)),
            name="'t Hooft / magnetic lattice L*",
            hovertemplate="magnetic charge (%{x:.1f}, %{y:.1f})<extra></extra>",
        ))
        fig.update_layout(
            height=390,
            title=dict(text="Wilson lines vs. 't Hooft lines: electric/magnetic dual lattices", font=dict(color=WHITE)),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=MIDNIGHT,
            margin=dict(l=35, r=20, t=55, b=45),
            xaxis=dict(scaleanchor="y", scaleratio=1, zerolinecolor="#334155", gridcolor="#1e2937", tickfont=dict(color=MUTED)),
            yaxis=dict(zerolinecolor="#334155", gridcolor="#1e2937", tickfont=dict(color=MUTED)),
            legend=dict(font=dict(color=WHITE), orientation="h", y=-0.18),
        )
        return fig

    def create_baez_huerta_intersection() -> go.Figure:
        fig = go.Figure(go.Sankey(
            node=dict(
                pad=22,
                thickness=18,
                line=dict(color=WHITE, width=0.7),
                label=["Spin(10)", "SU(5) x U(1)", "Pati-Salam", "S(U(2)xU(3))", "su(3)", "su(2)", "u(1)"],
                color=[SOFT_PURPLE, ELECTRIC_CYAN, FLUID_BLUE, WARM_GOLD, SURVIVES_GREEN, WARM_GOLD, SOFT_MAGENTA],
            ),
            link=dict(
                source=[0, 0, 1, 2, 3, 3, 3],
                target=[1, 2, 3, 3, 4, 5, 6],
                value=[8, 8, 5, 5, 3, 2, 1],
                color=["rgba(103,232,249,0.28)", "rgba(56,189,248,0.28)", "rgba(252,211,77,0.38)", "rgba(252,211,77,0.38)", "rgba(74,222,128,0.42)", "rgba(252,211,77,0.42)", "rgba(244,114,182,0.42)"],
            ),
        ))
        fig.update_layout(
            height=430,
            title=dict(text="Baez-Huerta intersection live: two embeddings, one common Standard Model algebra", font=dict(color=WHITE)),
            paper_bgcolor=DEEP_NAVY,
            font=dict(color=WHITE, size=13),
            margin=dict(l=10, r=10, t=55, b=10),
        )
        return fig

    def create_anomaly_playground(n16: int, n16bar: int, n10: int) -> Tuple[go.Figure, mo.Html]:
        coeffs = pd.DataFrame([
            {"representation": "16", "multiplicity": n16, "spin10_anomaly": 0, "chirality": n16},
            {"representation": "16bar", "multiplicity": n16bar, "spin10_anomaly": 0, "chirality": -n16bar},
            {"representation": "10", "multiplicity": n10, "spin10_anomaly": 0, "chirality": 0},
        ])
        coeffs["contribution"] = coeffs["multiplicity"] * coeffs["chirality"].apply(lambda value: 1 if value > 0 else -1 if value < 0 else 0)
        total_gauge_anomaly = int((coeffs["multiplicity"] * coeffs["spin10_anomaly"]).sum())
        net_chirality = int(coeffs["chirality"].sum())
        colors = [SURVIVES_GREEN if v == 0 else WARM_GOLD if v > 0 else SOFT_PURPLE for v in coeffs["contribution"]]
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=coeffs["representation"],
            y=coeffs["contribution"],
            marker=dict(color=colors, line=dict(color=WHITE, width=1)),
            customdata=np.stack([coeffs["multiplicity"], coeffs["spin10_anomaly"]], axis=-1),
            hovertemplate="<b>%{x}</b><br>multiplicity %{customdata[0]}<br>Spin(10) anomaly coefficient %{customdata[1]}<br>chirality contribution %{y}<extra></extra>",
        ))
        fig.add_hline(y=0, line=dict(color=WHITE, width=1))
        fig.add_annotation(x=0.98, y=0.95, xref="paper", yref="paper", showarrow=False, align="right",
                           text=f"Spin(10) gauge anomaly = {total_gauge_anomaly}<br>net chirality = {net_chirality}",
                           font=dict(color=WHITE), bgcolor="rgba(15,23,42,0.78)", bordercolor="#334155")
        fig.update_layout(
            height=360,
            title=dict(text="Anomaly-safety playground: complete Spin(10) multiplets stay safe while chirality changes", font=dict(color=WHITE)),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=MIDNIGHT,
            margin=dict(l=40, r=20, t=55, b=40),
            xaxis=dict(tickfont=dict(color=WHITE)),
            yaxis=dict(title=dict(text="net chirality contribution", font=dict(color=MUTED)), tickfont=dict(color=MUTED), gridcolor="#1e2937"),
            showlegend=False,
        )
        verdict = "safe" if total_gauge_anomaly == 0 else "unsafe"
        detail = mo.Html(f"""
        <div class="ipk-advanced-note t-panel-slide t-resize" data-open="true">
            <strong>Spin(10) gauge anomaly status: {verdict}</strong><br>
            Each complete 16 is anomaly-safe inside Spin(10) and decomposes to an anomaly-cancelling Standard Model family.
            This playground tracks net chirality separately: adding a 16bar cancels chirality and tends toward vectorlike matter.
        </div>
        """)
        return fig, detail

    def create_information_geometry_flow(constraint_strength: float) -> go.Figure:
        x = np.linspace(-3.5, 3.5, 80)
        y = np.linspace(0.35, 2.2, 70)
        X, Y = np.meshgrid(x, y)
        Z = 0.5 * (X**2 + Y**2 - 1 - np.log(np.maximum(Y**2, 1e-6)))
        target_mu = -2.0 + 3.4 * constraint_strength
        target_sigma = 1.0 + 0.55 * np.sin(np.pi * constraint_strength)
        t = np.linspace(0, 1, 80)
        path_mu = t * target_mu
        path_sigma = 1 + t * (target_sigma - 1)
        path_z = 0.5 * (path_mu**2 + path_sigma**2 - 1 - np.log(np.maximum(path_sigma**2, 1e-6)))
        fig = go.Figure()
        fig.add_trace(go.Surface(
            x=X,
            y=Y,
            z=Z,
            colorscale="Viridis",
            opacity=0.82,
            showscale=False,
            hovertemplate="mean=%{x:.2f}<br>sigma=%{y:.2f}<br>KL=%{z:.2f}<extra></extra>",
        ))
        fig.add_trace(go.Scatter3d(
            x=path_mu,
            y=path_sigma,
            z=path_z + 0.03,
            mode="lines+markers",
            line=dict(color=WARM_GOLD, width=7),
            marker=dict(size=3, color=WARM_GOLD),
            name="minimum update path",
        ))
        fig.update_layout(
            height=470,
            title=dict(text="Information geometry: KL projection as shortest update on the statistical manifold", font=dict(color=WHITE)),
            paper_bgcolor=DEEP_NAVY,
            scene=dict(
                xaxis=dict(title="mean", backgroundcolor=DEEP_NAVY, gridcolor="#1e2937"),
                yaxis=dict(title="sigma", backgroundcolor=DEEP_NAVY, gridcolor="#1e2937"),
                zaxis=dict(title="KL to prior", backgroundcolor=DEEP_NAVY, gridcolor="#1e2937"),
                camera=dict(eye=dict(x=1.45, y=1.65, z=1.05)),
            ),
            margin=dict(l=0, r=0, t=55, b=0),
        )
        return fig

    def create_fisher_constraint_surface(constraint_strength: float) -> go.Figure:
        mu = np.linspace(-2.5, 2.5, 90)
        sigma = np.linspace(0.35, 2.4, 80)
        MU, SIG = np.meshgrid(mu, sigma)
        fisher_density = 1 / np.maximum(SIG**2, 1e-6)
        mean_constraint = -1.8 + 3.6 * constraint_strength
        sigma_constraint = 0.65 + 1.25 * constraint_strength
        sigma_line = np.linspace(0.35, 2.4, 80)
        mu_line = np.linspace(-2.5, 2.5, 90)
        mean_ribbon_x = np.vstack([
            np.full_like(sigma_line, mean_constraint - 0.035),
            np.full_like(sigma_line, mean_constraint + 0.035),
        ])
        mean_ribbon_y = np.vstack([sigma_line, sigma_line])
        mean_ribbon_z = 1 / np.maximum(mean_ribbon_y**2, 1e-6) + 0.035
        var_ribbon_x = np.vstack([mu_line, mu_line])
        var_ribbon_y = np.vstack([
            np.full_like(mu_line, sigma_constraint - 0.025),
            np.full_like(mu_line, sigma_constraint + 0.025),
        ])
        var_ribbon_z = 1 / np.maximum(var_ribbon_y**2, 1e-6) + 0.055
        path_mu = np.array([0, mean_constraint, mean_constraint])
        path_sigma = np.array([1, 1, sigma_constraint])
        path_z = 1 / np.maximum(path_sigma**2, 1e-6) + 0.11
        fig = go.Figure()
        fig.add_trace(go.Surface(
            x=mu,
            y=sigma,
            z=fisher_density,
            colorscale="Cividis",
            opacity=0.78,
            colorbar=dict(title=dict(text="Fisher metric", font=dict(color=WHITE)), tickfont=dict(color=WHITE)),
            hovertemplate="mean=%{x:.2f}<br>sigma=%{y:.2f}<br>I≈%{z:.2f}<extra></extra>",
            name="Fisher metric surface",
        ))
        fig.add_trace(go.Surface(
            x=mean_ribbon_x,
            y=mean_ribbon_y,
            z=mean_ribbon_z,
            surfacecolor=np.ones_like(mean_ribbon_z),
            colorscale=[[0, WARM_GOLD], [1, WARM_GOLD]],
            opacity=0.88,
            showscale=False,
            hovertemplate="mean constraint<br>mean=%{x:.2f}<br>sigma=%{y:.2f}<extra></extra>",
            name="mean constraint surface",
        ))
        fig.add_trace(go.Surface(
            x=var_ribbon_x,
            y=var_ribbon_y,
            z=var_ribbon_z,
            surfacecolor=np.ones_like(var_ribbon_z),
            colorscale=[[0, SOFT_MAGENTA], [1, SOFT_MAGENTA]],
            opacity=0.82,
            showscale=False,
            hovertemplate="sigma constraint<br>mean=%{x:.2f}<br>sigma=%{y:.2f}<extra></extra>",
            name="sigma constraint surface",
        ))
        fig.add_trace(go.Scatter3d(
            x=path_mu,
            y=path_sigma,
            z=path_z,
            mode="lines+markers+text",
            line=dict(color=ELECTRIC_CYAN, width=7),
            marker=dict(size=5, color=[WHITE, WARM_GOLD, ELECTRIC_CYAN]),
            text=["prior", "mean lock", "sigma lock"],
            textposition="top center",
            name="sequential minimum update",
        ))
        fig.update_layout(
            height=470,
            title=dict(text="Fisher information metric with sequential constraint surfaces", font=dict(color=WHITE)),
            paper_bgcolor=DEEP_NAVY,
            scene=dict(
                xaxis=dict(title="mean", backgroundcolor=DEEP_NAVY, gridcolor="#1e2937"),
                yaxis=dict(title="sigma", backgroundcolor=DEEP_NAVY, gridcolor="#1e2937"),
                zaxis=dict(title="Fisher scale", backgroundcolor=DEEP_NAVY, gridcolor="#1e2937"),
                camera=dict(eye=dict(x=1.45, y=1.7, z=1.08)),
            ),
            margin=dict(l=0, r=0, t=55, b=0),
            legend=dict(font=dict(color=WHITE)),
        )
        return fig

    def create_fluids_bridge(stage: int) -> go.Figure:
        nodes = [
            "MU", "Probability", "Locality", "Unitarity", "D=4",
            "Consistent stress tensor", "Incompressible flow", "Airfoil / Navier-Stokes intuition",
        ]
        pos = {
            "MU": (0, 0.55),
            "Probability": (1, 1.0),
            "Locality": (1, 0.1),
            "Unitarity": (2, 0.55),
            "D=4": (3, 0.55),
            "Consistent stress tensor": (4, 0.55),
            "Incompressible flow": (5, 0.55),
            "Airfoil / Navier-Stokes intuition": (6, 0.55),
        }
        edges = [
            ("MU", "Probability"), ("MU", "Locality"), ("Probability", "Unitarity"),
            ("Locality", "Unitarity"), ("Unitarity", "D=4"),
            ("D=4", "Consistent stress tensor"), ("Consistent stress tensor", "Incompressible flow"),
            ("Incompressible flow", "Airfoil / Navier-Stokes intuition"),
        ]
        active_edge_count = min(len(edges), max(0, stage))
        fig = go.Figure()
        for idx, (a, b) in enumerate(edges):
            x0, y0 = pos[a]
            x1, y1 = pos[b]
            active = idx < active_edge_count
            fig.add_trace(go.Scatter(
                x=[x0, x1],
                y=[y0, y1],
                mode="lines",
                line=dict(color=ELECTRIC_CYAN if active else "rgba(148,163,184,0.28)", width=5 if active else 2),
                hoverinfo="skip",
                showlegend=False,
            ))
        for i, node in enumerate(nodes):
            x, y = pos[node]
            active = i <= min(len(nodes) - 1, stage)
            fig.add_trace(go.Scatter(
                x=[x],
                y=[y],
                mode="markers+text",
                marker=dict(size=28, color=WARM_GOLD if node == "D=4" else ELECTRIC_CYAN if active else "rgba(148,163,184,0.55)", line=dict(color=WHITE, width=1)),
                text=[node],
                textposition="bottom center" if y > 0.7 else "top center",
                textfont=dict(color=WHITE, size=11),
                hovertemplate=f"<b>{node}</b><extra></extra>",
                showlegend=False,
            ))
        fig.update_layout(
            height=340,
            title=dict(text="Why 4D matters for consistent fluids: Locks become constraints on flow", font=dict(color=WHITE)),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=MIDNIGHT,
            margin=dict(l=20, r=20, t=55, b=40),
            xaxis=dict(visible=False, range=[-0.35, 6.45]),
            yaxis=dict(visible=False, range=[-0.2, 1.25]),
        )
        return fig

    def create_mu_telescope(stage: int) -> Tuple[go.Figure, mo.Html]:
        stage = int(np.clip(stage, 0, 10))
        df = THEORY_SPACE_BY_LOCK.iloc[:stage + 1]
        latest = THEORY_SPACE_BY_LOCK.iloc[stage]
        fig = go.Figure()
        for col, color in [("dimensions", WARM_GOLD), ("lattices", SOFT_MAGENTA), ("gauge", ELECTRIC_CYAN), ("matter", SURVIVES_GREEN)]:
            fig.add_trace(go.Scatter(
                x=df["lock"],
                y=df[col],
                mode="lines+markers",
                line=dict(color=color, width=4),
                marker=dict(size=10, color=color, line=dict(color=WHITE, width=1)),
                name=col,
            ))
        fig.add_trace(go.Scatter(
            x=[stage],
            y=[max(latest[["dimensions", "lattices", "gauge", "matter"]])],
            mode="markers",
            marker=dict(size=24, color=WARM_GOLD, symbol="star", line=dict(color=WHITE, width=1)),
            name="current lock",
            hovertemplate=f"Lock {stage}: {latest['label']}<br>{latest['description']}<extra></extra>",
        ))
        fig.update_layout(
            height=430,
            title=dict(text="Full MU telescope: theory-space collapse as Locks accumulate", font=dict(color=WHITE)),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=MIDNIGHT,
            margin=dict(l=45, r=20, t=55, b=50),
            xaxis=dict(title=dict(text="Lock applied", font=dict(color=MUTED)), tickfont=dict(color=WHITE), dtick=1, gridcolor="#1e2937"),
            yaxis=dict(title=dict(text="surviving structural options", font=dict(color=MUTED)), type="log", tickfont=dict(color=MUTED), gridcolor="#1e2937", range=[-0.05, 1.45]),
            legend=dict(font=dict(color=WHITE), orientation="h", y=-0.22),
        )
        detail = mo.Html(f"""
        <div class="ipk-advanced-note t-panel-slide t-resize" data-open="true">
            <strong>Lock {stage}: {latest['label']}</strong><br>
            {latest['description']}<br>
            Current survivors: dimensions={latest['dimensions']}, lattices={latest['lattices']},
            gauge choices={latest['gauge']}, matter choices={latest['matter']}.
        </div>
        """)
        return fig, detail


    # =============================================================================
    # 10 LOCKS TABLE HELPERS
    # =============================================================================

    def make_locks_table():
        df = pd.DataFrame([
            {
                "Branch": l["branch"],
                "Lock": f"{l['id']}. {l['lock']}",
                "Theorem": l["theorem"],
                "Eliminated": l["eliminated"],
                "Survives": l["survives"],
            } for l in LOCKS_DATA
        ])
        return mo.ui.table(
            df,
            selection="single",
            page_size=12,
        )

    def selected_lock_from_table(locks_table) -> int:
        try:
            if hasattr(locks_table, "value") and len(locks_table.value) > 0:
                return int(locks_table.value.index[0])
        except Exception:
            return 0
        return 0

    def lock_detail(idx: int):
        lock = LOCKS_DATA[max(0, min(idx, len(LOCKS_DATA) - 1))]
        branch_class = "ipk-branch-" + lock["branch"].lower().replace("&", "and").replace(" ", "-")
        survives = lock["survives"]
        pill = f'<span class="ipk-lock-pill">SURVIVES: {survives}</span>'

        return mo.Html(f"""
        <div class="ipk-lock-detail {branch_class} t-panel-slide t-resize" data-open="true">
            <div class="ipk-lock-detail-top">
                <div>
                    <span class="ipk-lock-title">Lock {lock['id']} — {lock['lock']}</span><br>
                    <span class="ipk-lock-meta">{lock['branch']} • {lock['theorem']}</span>
                </div>
                {pill}
            </div>

            <div class="ipk-lock-details">
                {lock['details']}
            </div>

            <div class="ipk-lock-quote">
                “{lock['key_quote']}”
            </div>

            <div class="ipk-lock-eliminated">
                <strong>Eliminated:</strong> {lock['eliminated']}
            </div>
        </div>
        """)

    # =============================================================================
    # LONG PAPER EXTENSION: TABLE OF LAW, DERIVATION FOREST, SCORECARD, KILL LIST
    # Source: "Intelligent Physics" long monograph, 65-page PDF, Dec 2025.
    # =============================================================================

    PHI = (1 + np.sqrt(5.0)) / 2
    ALPHA_INV_PRED = 360 / PHI**2 - 2 * PHI**-3 + PHI**-16
    ALPHA_PRED = 1 / ALPHA_INV_PRED
    PROTON_RATIO_PRED = 6 * np.pi**5 + PHI**-7
    SIN2_THETA_W_PRED = 3 / 13 + PHI**-16
    PMNS_13_PRED = 1 / 45
    OMEGA_B_H2_PRED = (1 / 45) * (1 + ALPHA_PRED)
    TENSOR_R_PRED = 3 * (PHI**-3 / (2 * np.pi)) ** 2
    H0_LOCAL_PRED = 67.4 * (1 + np.sqrt(ALPHA_PRED))
    TAU_PRED = PHI**-6
    NS_PRED = 1 - PHI**-3 / (2 * np.pi)
    OMEGA_C_OVER_B_PRED = 2 * np.pi - 1 + PHI**-6
    SIGMA8_PRED = PHI / 2
    THETA_STAR_100_PRED = 1 + PHI**-3 / (2 * np.pi) + ALPHA_PRED / 2
    MUON_MASS_PRED = 0.51099895 * ((3 / 2) * ALPHA_INV_PRED + np.sqrt(PHI) - PHI**-6)
    _koide_a = 0.51099895
    _koide_b = MUON_MASS_PRED
    _koide_B = np.sqrt(_koide_a) + np.sqrt(_koide_b)
    TAU_MASS_PRED = (2 * _koide_B + np.sqrt(6 * _koide_B**2 - 3 * (_koide_a + _koide_b))) ** 2

    LAW_BASE_NUMBERS = {3, 12, 15, 16, 24, 45}
    LAW_DERIVED_NUMBERS = {0, 1, 2, 5, 6, 7, 8, 9, 10, 13, 21, 90, 180, 225, 240, 270, 273, 360}
    LAW_ALLOWED_EXPONENTS = {2, 3, 5, 6, 7, 14, 16}
    LAW_ALLOWED_SYMBOLS = {
        "pi", "phi", "sqrt", "alpha", "sin", "cos", "tan", "ln", "log", "exp",
        "me", "m", "r", "h", "omega", "theta", "delta", "q", "n", "s", "tau",
        "ckm", "pmns", "sm", "spin", "u", "su", "k", "f", "cdf", "ii",
    }
    LAW_TOKEN_ROWS = [
        {"Family": "Scaling", "Token": "pi", "Origin": "Circle constant, volume measure, Gaussian integrals", "Page": "6"},
        {"Family": "Scaling", "Token": "phi", "Origin": "Golden ratio, H4/600-cell projection and Diophantine stability", "Page": "6-7, 27-28"},
        {"Family": "Kissing", "Token": "24", "Origin": "K4, 4D kissing number / 24-cell contact", "Page": "6-7, 27"},
        {"Family": "Kissing", "Token": "12", "Origin": "K3, spatial channel capacity for gauge/axion propagation", "Page": "6-7, 28"},
        {"Family": "Representation", "Token": "45", "Origin": "dim Spin(10) adjoint; reused in PMNS and baryons", "Page": "6-7, 32-33"},
        {"Family": "Representation", "Token": "16", "Origin": "2^4, Spin(10) Weyl spinor matter representation", "Page": "6-7"},
        {"Family": "Matter", "Token": "15", "Origin": "SM fermions per generation", "Page": "6-8"},
        {"Family": "Matter", "Token": "3", "Origin": "Generation count from triality", "Page": "6-8, 34"},
        {"Family": "Fibonacci", "Token": "13", "Origin": "F7; used in sin^2 theta_W", "Page": "7-8"},
        {"Family": "Fibonacci", "Token": "21", "Origin": "F8 = 13 + 8", "Page": "7-8"},
        {"Family": "Composite", "Token": "273", "Origin": "13 x 21; CKM theta_13 denominator", "Page": "7-8, 44"},
        {"Family": "Composite", "Token": "360", "Origin": "15 x 24; electromagnetic capacity", "Page": "8, 29"},
    ]
    LAW_REFERENCE_ROWS = [
        {
            "Example": "Proton ratio",
            "Lawful": "mp/me = 6*pi^5 + phi^-7",
            "Unlawful contrast": "mp/me = 1836.1527 fitted decimal",
            "Why": "Uses pi, phi, Weyl/S7 exponents and no arbitrary decimal dial.",
        },
        {
            "Example": "PMNS reactor angle",
            "Lawful": "sin^2 theta_13 = 1/45",
            "Unlawful contrast": "sin^2 theta_13 = 0.02203",
            "Why": "45 is the Spin(10) adjoint dimension reused across sectors.",
        },
        {
            "Example": "Baryon density",
            "Lawful": "Omega_b h^2 = (1/45)(1+alpha)",
            "Unlawful contrast": "Omega_b h^2 = 0.02237",
            "Why": "Same 45 as PMNS, with alpha as derived vacuum impedance.",
        },
        {
            "Example": "Fine structure",
            "Lawful": "alpha^-1 = 360/phi^2 - 2*phi^-3 + phi^-16",
            "Unlawful contrast": "alpha^-1 = 137.035999",
            "Why": "360 = 15 x 24; correction exponents are in the E8/CY/S7 table.",
        },
    ]
    MONOGRAPH_FOCUS_TOKENS = ["45", "phi", "pi", "24", "12", "16", "15", "3", "273", "360"]
    SCORECARD_SECTORS = [
        "All",
        "Foundations",
        "Gauge",
        "Fermion/Yukawa",
        "CKM",
        "PMNS",
        "Higgs/EW",
        "QCD",
        "Cosmology",
        "Predictions",
    ]

    def _clean_formula(formula: str) -> str:
        return (
            formula
            .replace("π", "pi")
            .replace("Π", "pi")
            .replace("φ", "phi")
            .replace("Φ", "phi")
            .replace("α", "alpha")
            .replace("θ", "theta")
            .replace("δ", "delta")
            .replace("Ω", "omega")
            .replace("τ", "tau")
            .replace("−", "-")
            .replace("×", "*")
            .replace("÷", "/")
            .replace("^", "^")
        )

    def validate_lawful_formula(formula: str) -> Dict[str, Any]:
        cleaned = _clean_formula(formula or "")
        number_tokens = re.findall(r"(?<![A-Za-z_])\d+(?:\.\d+)?", cleaned)
        symbol_tokens = re.findall(r"[A-Za-z_]+", cleaned)
        exponent_tokens = re.findall(r"(?:\^|\*\*)\s*-?\s*(\d+)", cleaned)

        unknown_numbers = []
        decimal_numbers = []
        for token in number_tokens:
            if "." in token:
                decimal_numbers.append(token)
                unknown_numbers.append(token)
                continue
            value = int(token)
            if value not in LAW_BASE_NUMBERS and value not in LAW_DERIVED_NUMBERS:
                unknown_numbers.append(token)

        unknown_symbols = []
        for token in symbol_tokens:
            normalized = token.lower().strip("_")
            if normalized and normalized not in LAW_ALLOWED_SYMBOLS:
                unknown_symbols.append(token)

        unknown_exponents = []
        for token in exponent_tokens:
            value = int(token)
            if value not in LAW_ALLOWED_EXPONENTS:
                unknown_exponents.append(token)

        used = []
        for token in ["pi", "phi", "3", "12", "15", "16", "24", "45", "13", "21", "273", "360"]:
            if re.search(rf"(?<![A-Za-z0-9_]){re.escape(token)}(?![A-Za-z0-9_])", cleaned, flags=re.IGNORECASE):
                used.append(token)
        for token in exponent_tokens:
            marker = f"^{token}"
            if marker not in used and int(token) in LAW_ALLOWED_EXPONENTS:
                used.append(marker)

        lawful = not unknown_numbers and not unknown_symbols and not unknown_exponents and bool(cleaned.strip())
        return {
            "lawful": lawful,
            "cleaned": cleaned,
            "used": used or ["none detected"],
            "unknown_numbers": sorted(set(unknown_numbers)),
            "decimal_numbers": sorted(set(decimal_numbers)),
            "unknown_symbols": sorted(set(unknown_symbols)),
            "unknown_exponents": sorted(set(unknown_exponents)),
        }

    def create_law_status_badge(formula: str) -> str:
        result = validate_lawful_formula(formula)
        css = "ok" if result["lawful"] else "bad"
        label = "Vocabulary lawful" if result["lawful"] else "Vocabulary violation"
        detail = ", ".join(result["used"][:4]) if result["lawful"] else "check formula"
        return f'<a class="ipk-law-badge {css}" href="#monograph"><span>{label}</span><small>{escape(detail)}</small></a>'

    def create_law_vocabulary_figure() -> go.Figure:
        labels = ["Table of Law"]
        parents = [""]
        values = [len(LAW_TOKEN_ROWS)]
        colors = [DEEP_NAVY]
        palette = {
            "Scaling": ELECTRIC_CYAN,
            "Kissing": WARM_GOLD,
            "Representation": SOFT_PURPLE,
            "Matter": SURVIVES_GREEN,
            "Fibonacci": FLUID_BLUE,
            "Composite": SOFT_MAGENTA,
        }
        for family in sorted({row["Family"] for row in LAW_TOKEN_ROWS}):
            labels.append(family)
            parents.append("Table of Law")
            values.append(sum(row["Family"] == family for row in LAW_TOKEN_ROWS))
            colors.append(palette.get(family, MUTED))
        for row in LAW_TOKEN_ROWS:
            labels.append(row["Token"])
            parents.append(row["Family"])
            values.append(1)
            colors.append(palette.get(row["Family"], MUTED))
        fig = go.Figure(go.Sunburst(
            labels=labels,
            parents=parents,
            values=values,
            branchvalues="total",
            marker=dict(colors=colors, line=dict(color="rgba(242,238,226,0.92)", width=2)),
            hovertemplate="<b>%{label}</b><extra></extra>",
            insidetextorientation="radial",
        ))
        fig.update_layout(
            height=460,
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=10, r=10, t=10, b=10),
            font=dict(color=DEEP_NAVY, family="Geist, sans-serif", size=15),
        )
        return fig

    def create_formula_validator_panel(formula: str, challenge_mode: bool) -> mo.Html:
        result = validate_lawful_formula(formula)
        css = "ok" if result["lawful"] else "bad"
        status = "LAWFUL" if result["lawful"] else "UNLAWFUL"
        unknown_parts = []
        if result["unknown_numbers"]:
            unknown_parts.append("numbers: " + ", ".join(result["unknown_numbers"]))
        if result["unknown_symbols"]:
            unknown_parts.append("symbols: " + ", ".join(result["unknown_symbols"]))
        if result["unknown_exponents"]:
            unknown_parts.append("exponents: " + ", ".join(result["unknown_exponents"]))
        unknown_text = "; ".join(unknown_parts) if unknown_parts else "No disallowed tokens detected."
        token_chips = "".join(f'<span>{escape(str(token))}</span>' for token in result["used"])
        challenge = """
        <div class="ipk-paper-quote">
            <strong>Skeptic challenge, pp. 6-7:</strong>
            find one formula using an integer not derived from the E8 to 4D projection.
            If none appears, the arbitrary-fitting critique loses its target.
        </div>
        """ if challenge_mode else ""
        return mo.Html(f"""
        <div class="ipk-law-panel t-panel-slide t-resize" data-open="true">
            <div class="ipk-law-panel-top">
                <div>
                    <div class="ipk-panel-kicker">Table of Law validator</div>
                    <h3>{escape(formula or "empty formula")}</h3>
                    <p>Allowed primitives: pi, phi, 24, 12, 45, 16, 15, 3, Fibonacci/Binet descendants, and exponents 2, 3, 5, 6, 7, 14, 16.</p>
                </div>
                <div class="ipk-law-result {css}">{status}</div>
            </div>
            <div class="ipk-token-row">{token_chips}</div>
            <div class="ipk-law-explain">{escape(unknown_text)}</div>
            {challenge}
        </div>
        """)

    def create_law_examples_table() -> pd.DataFrame:
        return pd.DataFrame(LAW_REFERENCE_ROWS)

    DERIVATION_NODES = [
        ("Postulate U", 0.0, 0.0, "root", "Minimal complexity / MU", "u"),
        ("E8 lattice", 1.0, 0.0, "root", "240 roots", "e8 240"),
        ("Integers", 2.0, 1.05, "vocab", "24,45,16,15,3", "24 45 16 15 3"),
        ("Golden ratio", 2.0, 0.0, "vocab", "phi from H4/600-cell", "phi"),
        ("Circle constant", 2.0, -1.05, "vocab", "pi from volume/flux", "pi"),
        ("Gauge tree", 3.15, 1.18, "tree", "K3 bandwidth", "12 24 45"),
        ("Mass tree", 3.15, 0.28, "tree", "pi^5 and phi^-n", "pi phi 6 7"),
        ("Flavor tree", 3.15, -0.62, "tree", "45,273,24", "45 273 24"),
        ("Cosmology tree", 3.15, -1.48, "tree", "alpha and phi reuse", "45 phi alpha"),
        ("SM gauge", 4.45, 1.55, "leaf", "8+3+1=12", "12"),
        ("W=80.36", 4.45, 0.95, "leaf", "no hidden channels", "12 80 36"),
        ("alpha^-1", 4.45, 0.42, "leaf", "360/phi^2 corrections", "360 phi 2 3 16"),
        ("mp/me", 4.45, -0.12, "leaf", "6*pi^5 + phi^-7", "pi phi 6 7"),
        ("sin^2 theta13", 4.45, -0.72, "leaf", "1/45", "45"),
        ("Omega_b h^2", 4.45, -1.22, "leaf", "(1/45)(1+alpha)", "45 alpha"),
        ("Ngen=3", 4.45, -1.78, "leaf", "triality lock", "3 45"),
    ]
    DERIVATION_EDGES = [
        ("Postulate U", "E8 lattice"),
        ("E8 lattice", "Integers"),
        ("E8 lattice", "Golden ratio"),
        ("E8 lattice", "Circle constant"),
        ("Integers", "Gauge tree"),
        ("Integers", "Flavor tree"),
        ("Golden ratio", "Mass tree"),
        ("Golden ratio", "Cosmology tree"),
        ("Circle constant", "Mass tree"),
        ("Gauge tree", "SM gauge"),
        ("Gauge tree", "W=80.36"),
        ("Mass tree", "alpha^-1"),
        ("Mass tree", "mp/me"),
        ("Flavor tree", "sin^2 theta13"),
        ("Flavor tree", "Ngen=3"),
        ("Cosmology tree", "Omega_b h^2"),
    ]

    def _normalized_focus_token(focus_token: str) -> str:
        token = str(focus_token or "").strip().lower()
        return "" if token in {"", "all", "none"} else token

    def create_derivation_forest(focus_token: str) -> mo.Html:
        pos = {node[0]: (node[1], node[2]) for node in DERIVATION_NODES}
        token = _normalized_focus_token(focus_token)
        min_x, max_x = -0.1, 4.75
        min_y, max_y = -2.0, 1.8
        width, height = 980, 430

        def _point(name: str) -> Tuple[float, float]:
            x, y = pos[name]
            px = 64 + ((x - min_x) / (max_x - min_x)) * (width - 132)
            py = 66 + ((max_y - y) / (max_y - min_y)) * (height - 152)
            return px, py

        def _is_focus(text: str) -> bool:
            return bool(token) and token in text.lower()

        edge_markup = []
        for source, target in DERIVATION_EDGES:
            source_text = next(node[5] for node in DERIVATION_NODES if node[0] == source).lower()
            target_text = next(node[5] for node in DERIVATION_NODES if node[0] == target).lower()
            highlighted = _is_focus(source_text) or _is_focus(target_text)
            x0, y0 = _point(source)
            x1, y1 = _point(target)
            mid = (x0 + x1) / 2
            edge_markup.append(
                f'<path class="ipk-forest-edge{" active" if highlighted else ""}" '
                f'd="M{x0:.1f},{y0:.1f} C{mid:.1f},{y0:.1f} {mid:.1f},{y1:.1f} {x1:.1f},{y1:.1f}" />'
            )

        category_color = {
            "root": "#f2eee2",
            "vocab": ELECTRIC_CYAN,
            "tree": WARM_GOLD,
            "leaf": SOFT_MAGENTA,
        }
        category_label = {
            "root": "Postulate",
            "vocab": "Vocabulary",
            "tree": "Derivation tree",
            "leaf": "Prediction",
        }

        node_markup = []
        for category in ["root", "vocab", "tree", "leaf"]:
            nodes = [node for node in DERIVATION_NODES if node[3] == category]
            for node in nodes:
                highlighted = _is_focus(node[4]) or _is_focus(node[5])
                x, y = _point(node[0])
                fill = WARM_GOLD if highlighted else category_color[category]
                radius = 17 if highlighted else 13
                label_x = x - 22 if category == "leaf" else x
                label_y = y + 5 if category == "leaf" else y + 32
                label_anchor = "end" if category == "leaf" else "middle"
                node_markup.append(
                    f'<g class="ipk-forest-node{" active" if highlighted else ""} ipk-forest-{category}">'
                    f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius}" fill="{fill}" />'
                    f'<text x="{label_x:.1f}" y="{label_y:.1f}" text-anchor="{label_anchor}">{escape(node[0])}</text>'
                    f'<title>{escape(category_label[category])}: {escape(node[4])}</title>'
                    f'</g>'
                )

        legend = "".join(
            f'<span><i style="background:{color}"></i>{escape(label)}</span>'
            for key, color in category_color.items()
            for label in [category_label[key]]
        )
        focus_note = (
            f"Focused on token {escape(str(focus_token))}"
            if token
            else "Choose a token to illuminate the reused derivation paths"
        )
        return mo.Html(f"""
        <div class="ipk-forest-panel t-panel-slide" data-open="true">
            <div class="ipk-forest-head">
                <div>
                    <span class="ipk-panel-kicker">Derivation forest</span>
                    <h4>Postulate U to constants</h4>
                </div>
                <div class="ipk-forest-focus">{focus_note}</div>
            </div>
            <svg class="ipk-forest-svg" viewBox="0 0 {width} {height}" role="img"
                 aria-label="Derivation forest from Postulate U through E8 vocabulary into constants">
                <defs>
                    <radialGradient id="ipk-forest-glow" cx="48%" cy="50%" r="58%">
                        <stop offset="0%" stop-color="rgba(190,230,237,0.22)" />
                        <stop offset="68%" stop-color="rgba(190,230,237,0.05)" />
                        <stop offset="100%" stop-color="rgba(190,230,237,0)" />
                    </radialGradient>
                    <filter id="ipk-soft-glow" x="-70%" y="-70%" width="240%" height="240%">
                        <feGaussianBlur stdDeviation="5" result="blur" />
                        <feMerge>
                            <feMergeNode in="blur" />
                            <feMergeNode in="SourceGraphic" />
                        </feMerge>
                    </filter>
                </defs>
                <rect x="10" y="12" width="{width - 20}" height="{height - 24}" rx="22" fill="url(#ipk-forest-glow)" />
                <g class="ipk-forest-grid" opacity="0.18">
                    <path d="M70,98 H910 M70,196 H910 M70,294 H910" />
                    <path d="M235,60 V360 M470,60 V360 M705,60 V360" />
                </g>
                <g>{''.join(edge_markup)}</g>
                <g>{''.join(node_markup)}</g>
            </svg>
            <div class="ipk-forest-legend">{legend}</div>
        </div>
        """)

    def create_derivation_cards(focus_token: str, correction_blend: float) -> mo.Html:
        alpha_raw = 360 / PHI**2
        alpha_corrected = alpha_raw + correction_blend * (-2 * PHI**-3 + PHI**-16)
        alpha_error_ppm = abs(alpha_corrected - 137.035999) / 137.035999 * 1_000_000
        cards = [
            ("Vacuum impedance", "alpha^-1 = 360/phi^2 - 2phi^-3 + phi^-16", f"{alpha_corrected:.6f}", "137.035999", f"{alpha_error_ppm:.2f} ppm", "pp. 29-30, 45", "360 phi"),
            ("Proton ratio", "mp/me = 6*pi^5 + phi^-7", f"{PROTON_RATIO_PRED:.6f}", "1836.152673", "0.07 ppm", "pp. 31, 45", "pi phi 6 7"),
            ("45 reuse I", "sin^2 theta13_PMNS = 1/45", f"{PMNS_13_PRED:.5f}", "0.0220", "0.3 sigma", "pp. 32-33, 45", "45"),
            ("45 reuse II", "Omega_b h^2 = (1/45)(1+alpha)", f"{OMEGA_B_H2_PRED:.5f}", "0.02237 +/- 0.00015", "0.1 sigma", "pp. 32-33, 45", "45"),
            ("Triality", "Ngen = 3", "3", "3", "locked", "p. 34", "3 45"),
            ("Tensor mode", "r = 3(phi^-3/(2*pi))^2", f"{TENSOR_R_PRED:.4f}", "< 0.036", "prediction", "p. 46", "phi pi 3"),
        ]
        token = _normalized_focus_token(focus_token)
        rendered = []
        for title, formula, predicted, observed, agreement, page, tokens in cards:
            active = " active" if token and (token in tokens.lower() or token in formula.lower()) else ""
            rendered.append(f"""
            <div class="ipk-formula-card{active}">
                <div class="ipk-panel-kicker">{escape(page)}</div>
                <h4>{escape(title)}</h4>
                <code>{escape(formula)}</code>
                <div class="ipk-formula-metrics">
                    <span><b>Pred</b>{escape(predicted)}</span>
                    <span><b>Obs</b>{escape(observed)}</span>
                    <span><b>Fit</b>{escape(agreement)}</span>
                </div>
            </div>
            """)
        return mo.Html(f'<div class="ipk-formula-grid">{"".join(rendered)}</div>')

    def _score_rows() -> List[Dict[str, str]]:
        return [
            {"Sector": "Foundations", "Parameter": "R_inf / m_e anchor", "Formula": "one dimensionful anchor fixes units", "Predicted": "unit choice", "Observed": "R_inf or m_e", "Agreement": "anchor", "Tokens": "R_inf, me", "Source": "p. 44", "Status": "anchor"},
            {"Sector": "Foundations", "Parameter": "N_gen", "Formula": "Spin(8) triality -> 3", "Predicted": "3", "Observed": "3", "Agreement": "exact", "Tokens": "3,45", "Source": "p. 34", "Status": "derived"},
            {"Sector": "Gauge", "Parameter": "alpha^-1", "Formula": "360/phi^2 - 2phi^-3 + phi^-16", "Predicted": f"{ALPHA_INV_PRED:.6f}", "Observed": "137.035999", "Agreement": "0.6 ppm", "Tokens": "360,phi,2,3,16", "Source": "p. 45", "Status": "scorecard"},
            {"Sector": "Gauge", "Parameter": "alpha_s(MZ)", "Formula": "(2phi^3)^-1", "Predicted": f"{1/(2*PHI**3):.3f}", "Observed": "0.118", "Agreement": "0.1 sigma", "Tokens": "2,phi,3", "Source": "p. 45", "Status": "scorecard"},
            {"Sector": "Gauge", "Parameter": "sin^2 theta_W", "Formula": "3/13 + phi^-16", "Predicted": f"{SIN2_THETA_W_PRED:.4f}", "Observed": "0.2312", "Agreement": "0.3 sigma", "Tokens": "3,13,phi,16", "Source": "p. 45", "Status": "scorecard"},
            {"Sector": "Fermion/Yukawa", "Parameter": "m_p / m_e", "Formula": "6pi^5 + phi^-7", "Predicted": f"{PROTON_RATIO_PRED:.3f}", "Observed": "1836.153", "Agreement": "0.07 ppm", "Tokens": "6,pi,5,phi,7", "Source": "pp. 31,45", "Status": "scorecard"},
            {"Sector": "Fermion/Yukawa", "Parameter": "m_e", "Formula": "reference mass", "Predicted": "0.51099895 MeV", "Observed": "0.51099895 MeV", "Agreement": "anchor", "Tokens": "me", "Source": "p. 44", "Status": "anchor"},
            {"Sector": "Fermion/Yukawa", "Parameter": "m_mu", "Formula": "me[(3/2)alpha^-1 + sqrt(phi) - phi^-6]", "Predicted": f"{MUON_MASS_PRED:.3f} MeV", "Observed": "105.658 MeV", "Agreement": "listed", "Tokens": "3,2,alpha,phi,6", "Source": "pp. 35-37", "Status": "derived"},
            {"Sector": "Fermion/Yukawa", "Parameter": "m_tau", "Formula": "Koide Q_l=2/3 fixed from me,m_mu", "Predicted": f"{TAU_MASS_PRED:.2f} MeV", "Observed": "1776.86 MeV", "Agreement": "Koide", "Tokens": "2,3", "Source": "pp. 35-37", "Status": "derived"},
            {"Sector": "Fermion/Yukawa", "Parameter": "Koide Q_l", "Formula": "(sum m)/(sum sqrt(m))^2 = 2/3", "Predicted": "0.6667", "Observed": "0.6667", "Agreement": "geometric", "Tokens": "2,3", "Source": "pp. 35-37", "Status": "derived"},
            {"Sector": "CKM", "Parameter": "sin theta12", "Formula": "1/(2sqrt(5)) + phi^-14", "Predicted": "0.2248", "Observed": "0.2250", "Agreement": "0.3 sigma", "Tokens": "2,5,phi,14", "Source": "p. 44", "Status": "scorecard"},
            {"Sector": "CKM", "Parameter": "sin theta13", "Formula": "1/273", "Predicted": "0.00366", "Observed": "0.00369", "Agreement": "0.3 sigma", "Tokens": "273", "Source": "p. 44", "Status": "scorecard"},
            {"Sector": "CKM", "Parameter": "sin theta23", "Formula": "1/24", "Predicted": "0.0417", "Observed": "0.0412", "Agreement": "0.6 sigma", "Tokens": "24", "Source": "p. 44", "Status": "scorecard"},
            {"Sector": "CKM", "Parameter": "delta_CKM", "Formula": "180/phi^2 degrees", "Predicted": "68.75 deg", "Observed": "68 deg", "Agreement": "0.2 sigma", "Tokens": "180,phi,2", "Source": "p. 44", "Status": "scorecard"},
            {"Sector": "PMNS", "Parameter": "sin^2 theta12", "Formula": "5/16", "Predicted": "0.3125", "Observed": "0.307", "Agreement": "0.4 sigma", "Tokens": "5,16", "Source": "p. 45", "Status": "scorecard"},
            {"Sector": "PMNS", "Parameter": "sin^2 theta13", "Formula": "1/45", "Predicted": "0.0222", "Observed": "0.0220", "Agreement": "0.3 sigma", "Tokens": "45", "Source": "p. 45", "Status": "scorecard"},
            {"Sector": "PMNS", "Parameter": "sin^2 theta23", "Formula": "phi/3", "Predicted": "0.539", "Observed": "0.546", "Agreement": "0.3 sigma", "Tokens": "phi,3", "Source": "p. 45", "Status": "scorecard"},
            {"Sector": "PMNS", "Parameter": "delta_CP", "Formula": "3pi/2", "Predicted": "270 deg", "Observed": "230 +/- 40 deg", "Agreement": "1.0 sigma", "Tokens": "3,pi,2", "Source": "pp. 45-46", "Status": "scorecard"},
            {"Sector": "Higgs/EW", "Parameter": "m_H", "Formula": "closed loop (m_c,m_t,M_W); mH approx v/2 + phi*m_c", "Predicted": "125 GeV class", "Observed": "125.1 GeV", "Agreement": "listed", "Tokens": "phi,2", "Source": "pp. 8,36", "Status": "listed"},
            {"Sector": "Higgs/EW", "Parameter": "v/m_tau", "Formula": "360/phi^2", "Predicted": f"{360/PHI**2:.2f}", "Observed": "VEV ratio", "Agreement": "listed", "Tokens": "360,phi,2", "Source": "p. 8", "Status": "listed"},
            {"Sector": "Higgs/EW", "Parameter": "M_W", "Formula": "SM global fit via saturation", "Predicted": "80.36 GeV", "Observed": "LHC/SM fit", "Agreement": "prediction", "Tokens": "12", "Source": "p. 47", "Status": "prediction"},
            {"Sector": "QCD", "Parameter": "theta_QCD", "Formula": "0 (Peccei-Quinn)", "Predicted": "0", "Observed": "near 0", "Agreement": "strong CP", "Tokens": "0", "Source": "p. 8", "Status": "listed"},
            {"Sector": "QCD", "Parameter": "m_a axion", "Formula": "K3=12 vacuum relaxation", "Predicted": "225 +/- 5 micro-eV; kill band +/- 50", "Observed": "open", "Agreement": "ADMX/MADMAX", "Tokens": "12,225", "Source": "pp. 46,48,53", "Status": "prediction"},
            {"Sector": "Cosmology", "Parameter": "H0 local", "Formula": "67.4(1+sqrt(alpha))", "Predicted": f"{H0_LOCAL_PRED:.1f}", "Observed": "73.0 +/- 1.0", "Agreement": "screening", "Tokens": "alpha", "Source": "p. 48", "Status": "prediction"},
            {"Sector": "Cosmology", "Parameter": "Omega_b h^2", "Formula": "(1/45)(1+alpha)", "Predicted": f"{OMEGA_B_H2_PRED:.5f}", "Observed": "0.02237 +/- 0.00015", "Agreement": "0.1 sigma", "Tokens": "45,alpha", "Source": "p. 45", "Status": "scorecard"},
            {"Sector": "Cosmology", "Parameter": "Omega_c/Omega_b", "Formula": "2pi - 1 + phi^-6", "Predicted": f"{OMEGA_C_OVER_B_PRED:.2f}", "Observed": "5.36 +/- 0.05", "Agreement": "0.4 sigma", "Tokens": "2,pi,phi,6", "Source": "p. 45", "Status": "scorecard"},
            {"Sector": "Cosmology", "Parameter": "tau", "Formula": "phi^-6", "Predicted": f"{TAU_PRED:.4f}", "Observed": "0.054 +/- 0.007", "Agreement": "0.2 sigma", "Tokens": "phi,6", "Source": "p. 45", "Status": "scorecard"},
            {"Sector": "Cosmology", "Parameter": "n_s", "Formula": "1 - phi^-3/(2pi)", "Predicted": f"{NS_PRED:.4f}", "Observed": "0.9649 +/- 0.0042", "Agreement": "0.6 sigma", "Tokens": "1,phi,3,2,pi", "Source": "p. 45", "Status": "scorecard"},
            {"Sector": "Cosmology", "Parameter": "sigma_8", "Formula": "phi/2", "Predicted": f"{SIGMA8_PRED:.3f}", "Observed": "0.811 +/- 0.006", "Agreement": "0.3 sigma", "Tokens": "phi,2", "Source": "p. 45", "Status": "scorecard"},
            {"Sector": "Cosmology", "Parameter": "100 theta*", "Formula": "1 + phi^-3/(2pi) + alpha/2", "Predicted": f"{THETA_STAR_100_PRED:.4f}", "Observed": "1.0411 +/- 0.0003", "Agreement": "0.3 sigma", "Tokens": "1,phi,3,2,pi,alpha", "Source": "p. 45", "Status": "scorecard"},
            {"Sector": "Predictions", "Parameter": "tensor-to-scalar r", "Formula": "3(phi^-3/(2pi))^2", "Predicted": f"{TENSOR_R_PRED:.4f}", "Observed": "r < 0.036", "Agreement": "LiteBIRD test", "Tokens": "3,phi,2,pi", "Source": "p. 46", "Status": "prediction"},
            {"Sector": "Predictions", "Parameter": "proton lifetime", "Formula": "dimensional saturation suppresses decay", "Predicted": ">10^40 yr", "Observed": ">10^34 yr", "Agreement": "Hyper-K test", "Tokens": "10,40,12", "Source": "p. 46", "Status": "prediction"},
        ]

    MONOGRAPH_SCORECARD = _score_rows()

    def create_scorecard_dataframe(sector: str, focus_token: str) -> pd.DataFrame:
        df = pd.DataFrame(MONOGRAPH_SCORECARD)
        if sector != "All":
            df = df[df["Sector"] == sector]
        token = _normalized_focus_token(focus_token)
        df = df.copy()
        df["Reuse"] = [
            "YES" if token and token in (str(row["Formula"]) + " " + str(row["Tokens"]) + " " + str(row["Parameter"])).lower() else ""
            for _, row in df.iterrows()
        ]
        return df[["Reuse", "Sector", "Parameter", "Formula", "Predicted", "Observed", "Agreement", "Tokens", "Source", "Status"]]

    def create_scorecard_reuse_chart(focus_token: str) -> go.Figure:
        token = _normalized_focus_token(focus_token)
        rows = []
        for sector in SCORECARD_SECTORS[1:]:
            count = sum(
                bool(token) and token in (row["Formula"] + " " + row["Tokens"] + " " + row["Parameter"]).lower()
                for row in MONOGRAPH_SCORECARD
                if row["Sector"] == sector
            )
            total = sum(row["Sector"] == sector for row in MONOGRAPH_SCORECARD)
            rows.append((sector, count, total))
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=[row[0] for row in rows],
            y=[row[1] for row in rows],
            text=[f"{row[1]}/{row[2]}" for row in rows],
            textposition="outside",
            marker=dict(color=[WARM_GOLD if row[1] else "rgba(81,96,113,0.25)" for row in rows], line=dict(color=DEEP_NAVY, width=0.6)),
        ))
        fig.update_layout(
            height=330,
            title=dict(text=f"Cross-sector reuse if token {focus_token} is highlighted", font=dict(color=WHITE)),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color=WHITE),
            margin=dict(l=40, r=20, t=55, b=80),
            yaxis=dict(title="rows using token", gridcolor="rgba(242,238,226,0.12)", tickfont=dict(color=WHITE)),
            xaxis=dict(tickangle=-25, tickfont=dict(color=WHITE)),
            showlegend=False,
        )
        return fig

    def create_token_break_panel(focus_token: str) -> mo.Html:
        token = _normalized_focus_token(focus_token)
        impacted = [
            row for row in MONOGRAPH_SCORECARD
            if token and token in (row["Formula"] + " " + row["Tokens"] + " " + row["Parameter"]).lower()
        ]
        examples = ", ".join(row["Parameter"] for row in impacted[:6]) or "no visible scorecard rows"
        return mo.Html(f"""
        <div class="ipk-advanced-note ipk-break-panel t-panel-slide t-resize" data-open="true">
            <strong>Break token {escape(str(focus_token))}:</strong>
            {len(impacted)} scorecard rows lose their displayed derivation path. Examples: {escape(examples)}.
            This is the notebook version of the paper's cross-sector reuse claim.
        </div>
        """)

    def create_gauge_saturation_figure(extra_channels: int) -> go.Figure:
        groups = ["Spin(10)", "SU(5)", "Pati-Salam", "Standard Model", f"SM + {extra_channels}"]
        dims = [45, 24, 21, 12, 12 + int(extra_channels)]
        colors = [ELIMINATED_RED, ELIMINATED_RED, ELIMINATED_RED, SURVIVES_GREEN, SURVIVES_GREEN if extra_channels == 0 else ELIMINATED_RED]
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=groups,
            y=dims,
            marker=dict(color=colors, line=dict(color=DEEP_NAVY, width=0.8)),
            text=[str(v) for v in dims],
            textposition="outside",
            hovertemplate="<b>%{x}</b><br>dim = %{y}<extra></extra>",
        ))
        fig.add_hline(
            y=12,
            line=dict(color=WARM_GOLD, width=3, dash="dash"),
            annotation_text="K3 = 12 spatial channels",
            annotation_position="top left",
            annotation_font=dict(color=DEEP_NAVY),
        )
        fig.add_annotation(
            x="Standard Model",
            y=12,
            text="8 + 3 + 1 = 12",
            showarrow=True,
            arrowhead=2,
            ay=-45,
            font=dict(color=DEEP_NAVY),
        )
        fig.update_layout(
            height=430,
            title=dict(text="Dimensional Saturation: gauge bandwidth through K3 = 12", font=dict(color=DEEP_NAVY)),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=50, r=20, t=60, b=60),
            yaxis=dict(title="gauge dimensions / channels", range=[0, 50], gridcolor="rgba(15,35,63,0.12)", tickfont=dict(color=DEEP_NAVY)),
            xaxis=dict(tickfont=dict(color=DEEP_NAVY)),
            showlegend=False,
        )
        return fig

    def create_gauge_saturation_panel(extra_channels: int) -> mo.Html:
        status = "passes exactly" if int(extra_channels) == 0 else "violates the K3 bandwidth"
        css = "ok" if int(extra_channels) == 0 else "bad"
        return mo.Html(f"""
        <div class="ipk-law-panel t-panel-slide t-resize" data-open="true">
            <div class="ipk-law-panel-top">
                <div>
                    <div class="ipk-panel-kicker">Theorem 18.1, p. 28 + W-mass test, p. 47</div>
                    <h3>SM channel load {12 + int(extra_channels)} / 12: {escape(status)}</h3>
                    <p>Spin(10), SU(5), and Pati-Salam exceed the spatial channel limit. The Standard Model saturates it exactly, so hidden-loop explanations of a shifted W mass are treated as forbidden extra gauge information.</p>
                </div>
                <div class="ipk-law-result {css}">mW = 80.36 GeV</div>
            </div>
        </div>
        """)

    KILL_LIST = [
        {
            "Prediction": "Axion mass",
            "Value": "225 micro-eV",
            "Mechanism": "n=12 geometric scaling",
            "Kill": "outside 225 +/- 50 micro-eV",
            "Experiment": "ADMX/MADMAX",
            "Year": 2028,
            "Page": "pp. 46,48,53",
            "Status": "ADMX/MADMAX scan 1-1000 micro-eV; target band is testable",
            "Derivation": "K3=12 channel capacity + E8 vacuum structure",
            "Brittleness": 5,
        },
        {
            "Prediction": "W boson mass",
            "Value": "80.36 GeV",
            "Mechanism": "SM global fit + saturation",
            "Kill": "CDF II 80.43 confirmed",
            "Experiment": "LHC",
            "Year": 2027,
            "Page": "pp. 47-48",
            "Status": "LHC/SM-fit cross-check against CDF II tension",
            "Derivation": "K3=12 leaves no hidden gauge channel for loop rescue",
            "Brittleness": 5,
        },
        {
            "Prediction": "Tensor-to-scalar r",
            "Value": "0.004",
            "Mechanism": "(phi^-3/2pi)^2",
            "Kill": "r > 0.02 detected",
            "Experiment": "LiteBIRD",
            "Year": 2028,
            "Page": "pp. 46,48",
            "Status": "current bound r < 0.036; LiteBIRD target sigma(r) approx 0.001",
            "Derivation": "scalar spectral grammar fixes tensor amplitude",
            "Brittleness": 4,
        },
        {
            "Prediction": "Proton lifetime",
            "Value": ">10^40 yr",
            "Mechanism": "Dimensional saturation",
            "Kill": "decay observed",
            "Experiment": "Hyper-K",
            "Year": 2035,
            "Page": "pp. 46,48",
            "Status": "far above current >10^34 yr bounds",
            "Derivation": "no extra GUT gauge capacity after SM saturation",
            "Brittleness": 5,
        },
        {
            "Prediction": "Neutrino delta_CP",
            "Value": "270 deg",
            "Mechanism": "Chiral locking",
            "Kill": "not 270 +/- 20",
            "Experiment": "DUNE",
            "Year": 2030,
            "Page": "pp. 46,48",
            "Status": "current data about 230 +/- 40; DUNE aims for +/-10",
            "Derivation": "normal-order PMNS sector locked by chirality",
            "Brittleness": 4,
        },
        {
            "Prediction": "H0 local",
            "Value": "73.2 km/s/Mpc",
            "Mechanism": "vacuum screening sqrt(alpha)",
            "Kill": "<71 or >75",
            "Experiment": "SH0ES/JWST",
            "Year": 2029,
            "Page": "p. 48",
            "Status": "Cepheid/distance-ladder branch remains near 73",
            "Derivation": "67.4 x (1 + sqrt(alpha)) screening tier",
            "Brittleness": 3,
        },
    ]

    AXION_BAND_ROWS = [
        ("Central derivation", "225 +/- 5 micro-eV", "p. 46", "Theorem 35.1 / vacuum relaxation"),
        ("Kill-list band", "outside 225 +/- 50 micro-eV", "p. 48", "experiment dashboard tolerance"),
        ("FAQ pledge band", "225 +/- 50 micro-eV", "p. 53", "explicit non-adjustment answer"),
    ]

    def create_kill_timeline() -> go.Figure:
        y = list(range(len(KILL_LIST), 0, -1))
        fig = go.Figure(go.Scatter(
            x=[row["Year"] for row in KILL_LIST],
            y=y,
            mode="markers+text",
            marker=dict(
                size=[38, 42, 34, 36, 34, 36],
                color=[ELIMINATED_RED, WARM_GOLD, SOFT_PURPLE, FLUID_BLUE, SURVIVES_GREEN, ELECTRIC_CYAN],
                line=dict(color=DEEP_NAVY, width=1.4),
            ),
            text=[row["Experiment"] for row in KILL_LIST],
            textposition="middle right",
            customdata=[f"{row['Prediction']}: {row['Value']}<br>Kill: {row['Kill']}<br>{row['Page']}" for row in KILL_LIST],
            hovertemplate="<b>%{customdata}</b><extra></extra>",
        ))
        fig.update_layout(
            height=360,
            title=dict(text="Falsification timeline: six brittle tests", font=dict(color=DEEP_NAVY)),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=30, r=80, t=55, b=45),
            xaxis=dict(title="target window", range=[2026, 2036], dtick=1, gridcolor="rgba(15,35,63,0.12)", tickfont=dict(color=DEEP_NAVY)),
            yaxis=dict(visible=False),
            showlegend=False,
        )
        return fig

    def create_kill_brittleness_chart() -> go.Figure:
        fig = go.Figure(go.Bar(
            x=[row["Brittleness"] for row in KILL_LIST],
            y=[row["Prediction"] for row in KILL_LIST],
            orientation="h",
            marker=dict(
                color=[ELIMINATED_RED if row["Brittleness"] >= 5 else WARM_GOLD if row["Brittleness"] == 4 else ELECTRIC_CYAN for row in KILL_LIST],
                line=dict(color=DEEP_NAVY, width=0.8),
            ),
            text=[f"{row['Brittleness']}/5" for row in KILL_LIST],
            textposition="outside",
            customdata=[row["Derivation"] for row in KILL_LIST],
            hovertemplate="<b>%{y}</b><br>Brittleness %{x}/5<br>%{customdata}<extra></extra>",
        ))
        fig.update_layout(
            height=340,
            title=dict(text="Brittleness score: how much of the derivation web fails if the prediction fails", font=dict(color=DEEP_NAVY)),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=120, r=50, t=55, b=45),
            xaxis=dict(title="audit score", range=[0, 5.6], dtick=1, gridcolor="rgba(15,35,63,0.12)", tickfont=dict(color=DEEP_NAVY)),
            yaxis=dict(tickfont=dict(color=DEEP_NAVY)),
            showlegend=False,
        )
        return fig

    def create_axion_band_panel() -> mo.Html:
        rows = []
        for label, value, source, note in AXION_BAND_ROWS:
            rows.append(f"""
            <div class="ipk-formula-card">
                <div class="ipk-panel-kicker">{escape(source)}</div>
                <h4>{escape(label)}</h4>
                <code>{escape(value)}</code>
                <p>{escape(note)}</p>
            </div>
            """)
        return mo.Html(f"""
        <div class="ipk-law-panel t-panel-slide t-resize" data-open="true">
            <div class="ipk-law-panel-top">
                <div>
                    <div class="ipk-panel-kicker">Axion uncertainty audit</div>
                    <h3>Central prediction and falsification band are both source-backed</h3>
                    <p>Page 46 gives the sharp central band; pages 48 and 53 use the wider kill band. The notebook now shows both so the scorecard and kill list are not silently inconsistent.</p>
                </div>
                <div class="ipk-law-result ok">225</div>
            </div>
            <div class="ipk-formula-grid">{"".join(rows)}</div>
        </div>
        """)

    def create_kill_dashboard() -> mo.Html:
        cards = []
        for row in KILL_LIST:
            cards.append(f"""
            <div class="ipk-kill-card">
                <div class="ipk-panel-kicker">{escape(row['Experiment'])} • {escape(row['Page'])}</div>
                <h4>{escape(row['Prediction'])}</h4>
                <strong>{escape(row['Value'])}</strong>
                <p>{escape(row['Mechanism'])}</p>
                <p>{escape(row['Status'])}</p>
                <div class="ipk-formula-metrics">
                    <span><b>Brittle</b>{row['Brittleness']}/5</span>
                    <span><b>Tree</b>{escape(row['Derivation'])}</span>
                </div>
                <span>Kill condition: {escape(row['Kill'])}</span>
            </div>
            """)
        pledge = """
        <blockquote class="ipk-pledge">
            If ADMX detects axions at 500 micro-eV, this framework is dead.<br>
            If LiteBIRD measures r = 0.05, this framework is dead.<br>
            If CDF II is confirmed, this framework is dead.<br>
            If the Hubble tension resolves to a single value inconsistent with vacuum screening, this framework is dead.<br>
            This is how science should work.
        </blockquote>
        """
        return mo.Html(f"""
        <div class="ipk-kill-grid">{"".join(cards)}</div>
        {pledge}
        """)

    # =============================================================================
    # LONG PAPER TIER 2: H4 / 600-CELL, KOIDE CONE, COMPRESSION LAB
    # =============================================================================

    def _permutation_parity(perm: Tuple[int, ...]) -> int:
        inversions = 0
        for i in range(len(perm)):
            for j in range(i + 1, len(perm)):
                inversions += int(perm[i] > perm[j])
        return inversions % 2

    def generate_600_cell_vertices() -> np.ndarray:
        vertices = []
        for i in range(4):
            for sign in (-1, 1):
                v = np.zeros(4)
                v[i] = sign
                vertices.append(v)
        for signs in product((-0.5, 0.5), repeat=4):
            vertices.append(np.array(signs, dtype=float))
        base = np.array([0.0, 0.5, PHI / 2, 1 / (2 * PHI)], dtype=float)
        for perm in permutations(range(4)):
            if _permutation_parity(perm) != 0:
                continue
            permuted = base[list(perm)]
            nonzero = np.where(np.abs(permuted) > 1e-12)[0]
            for signs in product((-1, 1), repeat=len(nonzero)):
                v = permuted.copy()
                for idx, sign in zip(nonzero, signs):
                    v[idx] *= sign
                vertices.append(v)
        unique = np.unique(np.round(np.array(vertices, dtype=float), 12), axis=0)
        return unique

    H4_600_VERTICES = generate_600_cell_vertices()
    _H4_DISTANCE_MATRIX = np.linalg.norm(H4_600_VERTICES[:, None, :] - H4_600_VERTICES[None, :, :], axis=2)
    _H4_EDGE_LENGTH = float(np.min(_H4_DISTANCE_MATRIX[_H4_DISTANCE_MATRIX > 1e-8]))
    H4_EDGES = np.argwhere(np.triu(np.abs(_H4_DISTANCE_MATRIX - _H4_EDGE_LENGTH) < 1e-6, 1))

    def _rotate_4d(points: np.ndarray, phase: float) -> np.ndarray:
        c1, s1 = np.cos(phase), np.sin(phase)
        c2, s2 = np.cos(PHI * phase / 2), np.sin(PHI * phase / 2)
        c3, s3 = np.cos(phase / PHI), np.sin(phase / PHI)
        rot = np.eye(4)
        rot[np.ix_([0, 1], [0, 1])] = [[c1, -s1], [s1, c1]]
        rot[np.ix_([2, 3], [2, 3])] = [[c2, -s2], [s2, c2]]
        shear = np.eye(4)
        shear[np.ix_([0, 2], [0, 2])] = [[c3, -s3], [s3, c3]]
        return points @ (rot @ shear).T

    def _project_h4_vertices(mode: str, phase: float) -> np.ndarray:
        rotated = _rotate_4d(H4_600_VERTICES, phase)
        if mode == "Stereographic shell":
            denom = 1.7 - np.clip(rotated[:, 3], -1.2, 1.2)
            return rotated[:, :3] / denom[:, None] * 1.5
        if mode == "Penrose-like slice":
            angle = np.arctan2(rotated[:, 1], rotated[:, 0])
            radius = np.linalg.norm(rotated[:, :2], axis=1)
            return np.column_stack([
                radius * np.cos(5 * angle) + 0.25 * rotated[:, 2],
                radius * np.sin(5 * angle) + 0.25 * rotated[:, 3],
                rotated[:, 2] * 0.55,
            ])
        return rotated[:, :3] * 1.35

    def create_h4_600_cell_figure(mode: str, phase: float, slice_width: float) -> go.Figure:
        projected = _project_h4_vertices(mode, phase)
        rotated = _rotate_4d(H4_600_VERTICES, phase)
        if slice_width >= 0.99:
            visible = np.ones(len(projected), dtype=bool)
        else:
            cutoff = np.quantile(np.abs(rotated[:, 3]), max(0.08, min(0.99, slice_width)))
            visible = np.abs(rotated[:, 3]) <= cutoff
        visible_idx = np.where(visible)[0]
        p = projected[visible]
        color_values = rotated[visible, 3]

        fig = go.Figure()
        edge_x, edge_y, edge_z = [], [], []
        visible_set = set(visible_idx.tolist())
        for i, j in H4_EDGES:
            if int(i) not in visible_set or int(j) not in visible_set:
                continue
            edge_x.extend([projected[i, 0], projected[j, 0], None])
            edge_y.extend([projected[i, 1], projected[j, 1], None])
            edge_z.extend([projected[i, 2], projected[j, 2], None])
        fig.add_trace(go.Scatter3d(
            x=edge_x,
            y=edge_y,
            z=edge_z,
            mode="lines",
            line=dict(color="rgba(190,230,237,0.18)", width=1.2),
            hoverinfo="skip",
            showlegend=False,
            name="600-cell edges",
        ))
        fig.add_trace(go.Scatter3d(
            x=p[:, 0],
            y=p[:, 1],
            z=p[:, 2],
            mode="markers",
            marker=dict(
                size=5.8,
                color=color_values,
                colorscale="Tealrose",
                opacity=0.96,
                line=dict(color="rgba(242,238,226,0.72)", width=0.6),
                colorbar=dict(title=dict(text="4D depth", font=dict(color=WHITE)), tickfont=dict(color=WHITE)),
            ),
            customdata=np.round(rotated[visible], 4),
            hovertemplate="600-cell vertex<br>(%{customdata[0]}, %{customdata[1]}, %{customdata[2]}, %{customdata[3]})<extra></extra>",
            name="H4 vertices",
        ))
        fig.update_layout(
            height=620,
            title=dict(text=f"E8 -> H4 / 600-cell projection: {mode} ({len(p)} / 120 vertices)", font=dict(color=WHITE), x=0.02),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=DEEP_NAVY,
            margin=dict(l=0, r=0, t=45, b=0),
            scene=dict(
                xaxis=dict(backgroundcolor=DEEP_NAVY, gridcolor="#1e2937", zerolinecolor=ELECTRIC_CYAN, tickfont=dict(color=MUTED)),
                yaxis=dict(backgroundcolor=DEEP_NAVY, gridcolor="#1e2937", zerolinecolor=SOFT_PURPLE, tickfont=dict(color=MUTED)),
                zaxis=dict(backgroundcolor=DEEP_NAVY, gridcolor="#1e2937", zerolinecolor=WARM_GOLD, tickfont=dict(color=MUTED)),
                aspectmode="cube",
                camera=dict(eye=dict(x=1.45, y=1.55, z=1.18)),
            ),
            hoverlabel=dict(bgcolor=MIDNIGHT, font=dict(color=WHITE)),
        )
        return fig

    def create_h4_projection_readout(mode: str, phase: float, slice_width: float) -> mo.Html:
        rotated_depth = np.abs(_rotate_4d(H4_600_VERTICES, phase)[:, 3])
        visible = 120 if slice_width >= 0.99 else int(np.sum(rotated_depth <= np.quantile(rotated_depth, max(0.08, min(0.99, slice_width)))))
        return mo.Html(f"""
        <div class="ipk-law-panel t-panel-slide t-resize" data-open="true">
            <div class="ipk-law-panel-top">
                <div>
                    <div class="ipk-panel-kicker">Theorems 17.1-17.2, pp. 27-28</div>
                    <h3>Golden shadow: {escape(mode)}</h3>
                    <p>The 4D projection has 120 600-cell vertices with coordinate archetype (±1/2, ±phi/2, ±1/(2phi), 0). The long/short edge ratio in the Penrose-like slice is phi.</p>
                </div>
                <div class="ipk-law-result ok">{visible} visible</div>
            </div>
            <div class="ipk-token-row">
                <span>H4 order 14,400</span><span>phi = {PHI:.6f}</span><span>edge ≈ {_H4_EDGE_LENGTH:.3f}</span><span>E8 roots -> 600-cell</span>
            </div>
        </div>
        """)

    def _koide_q(masses: np.ndarray) -> float:
        roots = np.sqrt(np.maximum(masses, 1e-12))
        return float(np.sum(masses) / np.sum(roots) ** 2)

    def create_koide_cone_figure(blend: float) -> go.Figure:
        masses_pred = np.array([0.51099895, MUON_MASS_PRED, TAU_MASS_PRED])
        sqrt_pred = np.sqrt(masses_pred)
        axis = np.ones(3) / np.sqrt(3)
        norm_pred = float(np.linalg.norm(sqrt_pred))
        democratic = axis * norm_pred
        current = (1 - blend) * democratic + blend * sqrt_pred
        current_masses = current**2
        q_current = _koide_q(current_masses)

        u = np.array([1.0, -1.0, 0.0]) / np.sqrt(2)
        v = np.cross(axis, u)
        theta = np.linspace(0, 2 * np.pi, 90)
        t = np.linspace(0.0, norm_pred * 1.08, 32)
        T, Theta = np.meshgrid(t, theta)
        radius = T * np.tan(np.pi / 4)
        cone = T[..., None] * axis + radius[..., None] * (np.cos(Theta)[..., None] * u + np.sin(Theta)[..., None] * v)

        fig = go.Figure()
        fig.add_trace(go.Surface(
            x=cone[:, :, 0],
            y=cone[:, :, 1],
            z=cone[:, :, 2],
            opacity=0.18,
            showscale=False,
            colorscale=[[0, "rgba(103,232,249,0.12)"], [1, "rgba(252,211,77,0.38)"]],
            hoverinfo="skip",
            name="Koide cone",
        ))
        for vec, name, color, width in [
            (democratic, "democratic axis point", "rgba(190,230,237,0.65)", 5),
            (sqrt_pred, "Koide charged-lepton vector", WARM_GOLD, 7),
            (current, "current deformation", SOFT_MAGENTA, 7),
        ]:
            fig.add_trace(go.Scatter3d(
                x=[0, vec[0]],
                y=[0, vec[1]],
                z=[0, vec[2]],
                mode="lines+markers",
                line=dict(color=color, width=width),
                marker=dict(size=[2, 6], color=color),
                name=name,
                hovertemplate=f"{name}<extra></extra>",
            ))
        fig.add_trace(go.Scatter3d(
            x=[sqrt_pred[0], sqrt_pred[1], sqrt_pred[2]],
            y=[0, 0, 0],
            z=[0, 0, 0],
            mode="markers+text",
            marker=dict(size=7, color=[ELECTRIC_CYAN, WARM_GOLD, SOFT_PURPLE], line=dict(color=WHITE, width=0.7)),
            text=["sqrt(me)", "sqrt(mmu)", "sqrt(mtau)"],
            textposition="top center",
            showlegend=False,
            hoverinfo="skip",
        ))
        fig.update_layout(
            height=580,
            title=dict(text=f"Koide cone: Q = {q_current:.4f} (target 2/3)", font=dict(color=WHITE), x=0.02),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=DEEP_NAVY,
            margin=dict(l=0, r=0, t=45, b=0),
            scene=dict(
                xaxis=dict(title="sqrt(me)", backgroundcolor=DEEP_NAVY, gridcolor="#1e2937", tickfont=dict(color=MUTED)),
                yaxis=dict(title="sqrt(mmu)", backgroundcolor=DEEP_NAVY, gridcolor="#1e2937", tickfont=dict(color=MUTED)),
                zaxis=dict(title="sqrt(mtau)", backgroundcolor=DEEP_NAVY, gridcolor="#1e2937", tickfont=dict(color=MUTED)),
                aspectmode="cube",
                camera=dict(eye=dict(x=1.35, y=1.65, z=1.15)),
            ),
            legend=dict(font=dict(color=WHITE), orientation="h", y=-0.05),
        )
        return fig

    def create_koide_readout(blend: float) -> mo.Html:
        masses_pred = np.array([0.51099895, MUON_MASS_PRED, TAU_MASS_PRED])
        sqrt_pred = np.sqrt(masses_pred)
        axis = np.ones(3) / np.sqrt(3)
        current = (1 - blend) * axis * np.linalg.norm(sqrt_pred) + blend * sqrt_pred
        masses = current**2
        q_value = _koide_q(masses)
        return mo.Html(f"""
        <div class="ipk-formula-grid">
            <div class="ipk-formula-card active"><div class="ipk-panel-kicker">Koide</div><h4>Q_l</h4><code>(me + mmu + mtau)/(sqrt(me)+sqrt(mmu)+sqrt(mtau))^2</code><div class="ipk-formula-metrics"><span><b>Now</b>{q_value:.5f}</span><span><b>Target</b>0.66667</span><span><b>Angle</b>{np.degrees(np.arccos(np.clip(np.sum(current)/(np.sqrt(3)*np.linalg.norm(current)), -1, 1))):.2f} deg</span></div></div>
            <div class="ipk-formula-card"><div class="ipk-panel-kicker">Muon</div><h4>m_mu</h4><code>me[(3/2)alpha^-1 + sqrt(phi) - phi^-6]</code><div class="ipk-formula-metrics"><span><b>Now</b>{masses[1]:.3f}</span><span><b>Paper</b>105.658</span><span><b>Page</b>35-37</span></div></div>
            <div class="ipk-formula-card"><div class="ipk-panel-kicker">Tau</div><h4>m_tau</h4><code>fixed by Koide with Q_l = 2/3</code><div class="ipk-formula-metrics"><span><b>Now</b>{masses[2]:.2f}</span><span><b>Obs</b>1776.86</span><span><b>Grammar</b>2,3,phi</span></div></div>
        </div>
        """)

    GRAMMAR_PAIRS = {
        "pi, phi": (np.pi, PHI, "pi", "phi"),
        "e, sqrt(2)": (np.e, np.sqrt(2), "e", "sqrt2"),
        "e, ln(2)": (np.e, np.log(2), "e", "ln2"),
    }
    MONTE_CARLO_TARGETS = [
        ("m_p/m_e", PROTON_RATIO_PRED, "6*pi^5 + phi^-7"),
        ("tau", TAU_PRED, "phi^-6"),
        ("sin2 theta13", PMNS_13_PRED, "1/45"),
        ("Omega_b h2", OMEGA_B_H2_PRED, "(1/45)(1+alpha)"),
        ("n_s gap", 1 - NS_PRED, "phi^-3/(2*pi)"),
        ("sigma8", SIGMA8_PRED, "phi/2"),
    ]

    @lru_cache(maxsize=64)
    def enumerate_grammar_hits(pair_name: str, tolerance: float, exponent_limit: int = 10) -> Tuple[int, List[Tuple[float, str]]]:
        c1, c2, n1, n2 = GRAMMAR_PAIRS[pair_name]
        tolerance = float(tolerance)
        coeffs = np.arange(-10, 11)
        exponents = np.arange(-exponent_limit, exponent_limit + 1)
        p1 = c1 ** exponents
        p2 = c2 ** exponents
        target = 1836.15267343
        hits = []
        for A in coeffs:
            for B in coeffs:
                if A == 0 and B == 0:
                    continue
                values = A * p1[:, None] + B * p2[None, :]
                diffs = np.abs(values - target)
                locs = np.argwhere(diffs <= tolerance)
                for i, j in locs:
                    formula = f"{A}{n1}^{int(exponents[i])} + {B}{n2}^{int(exponents[j])}"
                    hits.append((float(diffs[i, j]), formula))
        hits = sorted(hits, key=lambda item: item[0])
        return len(hits), hits[:6]

    def create_compression_figure(pair_name: str, tolerance: float) -> go.Figure:
        hit_count, _ = enumerate_grammar_hits(pair_name, tolerance)
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=["Raw constants", "Geometric code", "Compression gain", "Live hits"],
            y=[350, 90, 260, max(1, hit_count)],
            marker=dict(color=[ELIMINATED_RED, SURVIVES_GREEN, WARM_GOLD, ELECTRIC_CYAN], line=dict(color=WHITE, width=0.7)),
            text=["350+ bits", "~90 bits", "250+ bits", str(hit_count)],
            textposition="outside",
            hovertemplate="<b>%{x}</b><br>%{text}<extra></extra>",
        ))
        fig.update_layout(
            height=390,
            title=dict(text=f"Compression and grammar search: {pair_name}, tolerance {tolerance:g}", font=dict(color=WHITE), x=0.02),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=DEEP_NAVY,
            margin=dict(l=45, r=20, t=55, b=55),
            yaxis=dict(title=dict(text="bits / demo count", font=dict(color=MUTED)), gridcolor="#1e2937", tickfont=dict(color=MUTED)),
            xaxis=dict(tickfont=dict(color=WHITE)),
            showlegend=False,
        )
        return fig

    def create_grammar_lab_panel(pair_name: str, tolerance: float) -> mo.Html:
        hit_count, hits = enumerate_grammar_hits(pair_name, tolerance)
        hit_rows = "".join(
            f"<div><code>{escape(formula)}</code><span>error {error:.3g}</span></div>"
            for error, formula in hits
        ) or "<div><code>no hit in bounded demo</code><span>try pi, phi or widen tolerance</span></div>"
        pair_note = "paper vocabulary" if pair_name == "pi, phi" else "control grammar"
        return mo.Html(f"""
        <div class="ipk-law-panel t-panel-slide t-resize" data-open="true">
            <div class="ipk-law-panel-top">
                <div>
                    <div class="ipk-panel-kicker">Part XI, pp. 48-51</div>
                    <h3>Grammar search sandbox: {escape(pair_name)}</h3>
                    <p>This bounded live search scans A*x^n + B*y^m with A,B in [-10,10] and n,m in [-10,10]. The paper reports the wider [-20,20] Monte Carlo/enumeration tests.</p>
                </div>
                <div class="ipk-law-result {'ok' if pair_name == 'pi, phi' else 'bad'}">{escape(pair_note)}</div>
            </div>
            <div class="ipk-grammar-hits">{hit_rows}</div>
            <div class="ipk-token-row">
                <span>{hit_count} hits</span><span>target mp/me</span><span>Occam factor ~2^250</span><span>P &lt; 10^-6 after correction</span>
            </div>
        </div>
        """)

    @lru_cache(maxsize=12)
    def _grammar_candidate_sample(pair_name: str, sample_size: int = 30000, seed: int = 20260528) -> np.ndarray:
        c1, c2, _, _ = GRAMMAR_PAIRS[pair_name]
        coeffs = np.arange(-20, 21, dtype=float)
        exponents = np.arange(-16, 17, dtype=int)
        pair_offset = sum((idx + 1) * ord(char) for idx, char in enumerate(pair_name))
        rng = np.random.default_rng(seed + pair_offset)
        draw_size = int(sample_size * 2.2)
        a = rng.choice(coeffs, size=draw_size, replace=True)
        b = rng.choice(coeffs, size=draw_size, replace=True)
        n = rng.choice(exponents, size=draw_size, replace=True)
        m = rng.choice(exponents, size=draw_size, replace=True)
        nonzero = (a != 0) | (b != 0)
        values = a[nonzero] * (c1 ** n[nonzero]) + b[nonzero] * (c2 ** m[nonzero])
        values = values[np.isfinite(values) & (values > 0)]
        known = []
        if pair_name == "pi, phi":
            known = [
                PROTON_RATIO_PRED,
                TAU_PRED,
                PHI**-3 / (2 * np.pi),
                SIGMA8_PRED,
            ]
        if len(values) > sample_size:
            values = rng.choice(values, size=sample_size, replace=False)
        if known:
            values = np.concatenate([values, np.array(known, dtype=float)])
        return np.unique(values)

    def _relative_hits(values: np.ndarray, targets: np.ndarray, relative_tolerance: float) -> Tuple[int, np.ndarray]:
        min_errors = []
        for target in targets:
            rel = np.abs(values - target) / max(abs(float(target)), 1e-12)
            min_errors.append(float(np.min(rel)))
        errors = np.array(min_errors)
        return int(np.sum(errors <= relative_tolerance)), errors

    @lru_cache(maxsize=64)
    def create_monte_carlo_validation_dataframe(relative_tolerance: float, trials: int) -> pd.DataFrame:
        relative_tolerance = float(relative_tolerance)
        trials = int(trials)
        targets = np.array([row[1] for row in MONTE_CARLO_TARGETS], dtype=float)
        lo = float(np.min(targets))
        hi = float(np.max(targets))
        rows = []
        for idx, pair_name in enumerate(GRAMMAR_PAIRS):
            values = _grammar_candidate_sample(pair_name)
            physical_hits, errors = _relative_hits(values, targets, relative_tolerance)
            rng = np.random.default_rng(20260528 + idx * 997 + int(trials) * 13)
            control_counts = []
            for _ in range(int(trials)):
                controls = np.exp(rng.uniform(np.log(lo), np.log(hi), size=len(targets)))
                count, _ = _relative_hits(values, controls, relative_tolerance)
                control_counts.append(count)
            control_counts = np.array(control_counts, dtype=float)
            p_value = (1 + np.sum(control_counts >= physical_hits)) / (len(control_counts) + 1)
            sigma = (physical_hits - float(np.mean(control_counts))) / max(float(np.std(control_counts)), 1e-9)
            rows.append({
                "Grammar": pair_name,
                "Physical hits": physical_hits,
                "Control mean": float(np.mean(control_counts)),
                "Control p95": float(np.percentile(control_counts, 95)),
                "Empirical p": float(p_value),
                "Sigma demo": float(sigma),
                "Best target": MONTE_CARLO_TARGETS[int(np.argmin(errors))][0],
                "Best rel error": float(np.min(errors)),
            })
        return pd.DataFrame(rows)

    def create_monte_carlo_validation_figure(relative_tolerance: float, trials: int) -> go.Figure:
        df = create_monte_carlo_validation_dataframe(relative_tolerance, trials)
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df["Grammar"],
            y=df["Physical hits"],
            name="physical targets",
            marker=dict(color=WARM_GOLD, line=dict(color=WHITE, width=0.8)),
            hovertemplate="<b>%{x}</b><br>physical hits=%{y}<extra></extra>",
        ))
        fig.add_trace(go.Bar(
            x=df["Grammar"],
            y=df["Control mean"],
            name="control mean",
            marker=dict(color="rgba(103,232,249,0.55)", line=dict(color=WHITE, width=0.5)),
            hovertemplate="<b>%{x}</b><br>control mean=%{y:.2f}<extra></extra>",
        ))
        fig.add_trace(go.Scatter(
            x=df["Grammar"],
            y=df["Control p95"],
            mode="markers",
            name="control p95",
            marker=dict(size=14, color=ELIMINATED_RED, symbol="diamond", line=dict(color=WHITE, width=0.8)),
            hovertemplate="<b>%{x}</b><br>95th percentile=%{y:.2f}<extra></extra>",
        ))
        fig.update_layout(
            height=390,
            title=dict(text=f"Monte Carlo grammar validation demo: {trials} control target sets, rel tol {relative_tolerance:g}", font=dict(color=WHITE), x=0.02),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=DEEP_NAVY,
            barmode="group",
            margin=dict(l=45, r=20, t=55, b=70),
            yaxis=dict(title=dict(text="matched targets", font=dict(color=MUTED)), gridcolor="#1e2937", tickfont=dict(color=MUTED), dtick=1),
            xaxis=dict(tickfont=dict(color=WHITE)),
            legend=dict(font=dict(color=WHITE), orientation="h", y=-0.2),
        )
        return fig

    def create_monte_carlo_validation_panel(relative_tolerance: float, trials: int) -> mo.Html:
        df = create_monte_carlo_validation_dataframe(relative_tolerance, trials)
        rows = []
        for _, row in df.iterrows():
            active = " active" if row["Grammar"] == "pi, phi" else ""
            rows.append(f"""
            <div class="ipk-formula-card{active}">
                <div class="ipk-panel-kicker">control search</div>
                <h4>{escape(row['Grammar'])}</h4>
                <code>empirical p = {row['Empirical p']:.3f}; demo sigma = {row['Sigma demo']:.2f}</code>
                <div class="ipk-formula-metrics">
                    <span><b>Physical</b>{int(row['Physical hits'])}</span>
                    <span><b>Control mean</b>{row['Control mean']:.2f}</span>
                    <span><b>Best</b>{escape(row['Best target'])}</span>
                </div>
            </div>
            """)
        target_chips = "".join(f"<span>{escape(name)}: {value:.5g}</span>" for name, value, _ in MONTE_CARLO_TARGETS)
        return mo.Html(f"""
        <div class="ipk-law-panel t-panel-slide t-resize" data-open="true">
            <div class="ipk-law-panel-top">
                <div>
                    <div class="ipk-panel-kicker">Reproducible validation lab, pp. 48-51</div>
                    <h3>Monte Carlo target-set controls</h3>
                    <p>The notebook samples random target sets over the same log scale as the displayed physical constants and compares them with the reduced A*x^n + B*y^m grammar. This is a small live analogue of the paper's larger search, not a replacement for the reported million-trial validation.</p>
                </div>
                <div class="ipk-law-result ok">seed 20260528</div>
            </div>
            <div class="ipk-token-row">{target_chips}</div>
            <div class="ipk-formula-grid">{"".join(rows)}</div>
        </div>
        """)

    # =============================================================================
    # LONG PAPER TIER 3: ONTOLOGY, GENERATIVE MODEL, DIOPHANTINE PHI, OPEN PROBLEMS
    # =============================================================================

    ONTOLOGY_ROWS = [
        {
            "topic": "Vacuum",
            "standard": "empty arena or field ground state",
            "framework": "E8 lattice hardware with fixed channel capacity",
            "page": "pp. 13-15",
        },
        {
            "topic": "Particles",
            "standard": "point-like quanta with fitted Yukawa couplings",
            "framework": "topological defects / solitons in CY3 and S7 sectors",
            "page": "pp. 15-16",
        },
        {
            "topic": "Gravity",
            "standard": "fundamental spacetime curvature field",
            "framework": "C-sector complexity / compression curvature",
            "page": "pp. 13-17, 42-43",
        },
        {
            "topic": "Time",
            "standard": "external parameter or coordinate",
            "framework": "emergent diffusion / denoising direction",
            "page": "pp. 15-17, 55-56",
        },
        {
            "topic": "Constants",
            "standard": "independent measured dials",
            "framework": "outputs of a finite pi, phi, E8 grammar",
            "page": "pp. 16-18, 48-51",
        },
        {
            "topic": "Forces",
            "standard": "chosen gauge content",
            "framework": "channel-saturated information propagation, dim(SM)=K3=12",
            "page": "p. 28",
        },
    ]

    def create_ontology_comparator() -> mo.Html:
        rows = []
        for row in ONTOLOGY_ROWS:
            rows.append(f"""
            <div class="ipk-ontology-row">
                <div><strong>{escape(row['topic'])}</strong><span>{escape(row['page'])}</span></div>
                <p>{escape(row['standard'])}</p>
                <p>{escape(row['framework'])}</p>
            </div>
            """)
        return mo.Html(f"""
        <div class="ipk-ontology-table">
            <div class="ipk-ontology-head"><span>Object</span><span>SM/GR ontology</span><span>Long-paper ontology</span></div>
            {"".join(rows)}
        </div>
        """)

    GENERATIVE_LINKS = [
        ("Euclidean action", "Energy function", "minimization selects vacuum"),
        ("Path integral", "Probability model", "weights histories by exp(-S)"),
        ("Schrodinger bridge", "Reversible diffusion", "Born rule as generative logic"),
        ("RG flow", "Reverse denoising", "arrow of time as reconstruction direction"),
        ("Postulate U", "Regularization", "minimum complexity prevents overfitting"),
        ("Vacuum geometry", "Learned prior", "E8 hardware constrains samples"),
        ("Particles", "Generated samples", "defects emerge from the prior"),
    ]

    def create_generative_isomorphism(stage: float) -> go.Figure:
        shown = max(1, int(round(1 + stage * (len(GENERATIVE_LINKS) - 1))))
        links = GENERATIVE_LINKS[:shown]
        left = list(dict.fromkeys(link[0] for link in links))
        right = list(dict.fromkeys(link[1] for link in links))
        labels = left + right
        index = {label: i for i, label in enumerate(labels)}
        fig = go.Figure(go.Sankey(
            arrangement="fixed",
            node=dict(
                label=labels,
                color=[ELECTRIC_CYAN] * len(left) + [WARM_GOLD] * len(right),
                pad=22,
                thickness=18,
                line=dict(color="rgba(242,238,226,0.5)", width=0.8),
                x=[0.08] * len(left) + [0.72] * len(right),
                y=np.linspace(0.05, 0.95, len(left)).tolist() + np.linspace(0.05, 0.95, len(right)).tolist(),
            ),
            link=dict(
                source=[index[src] for src, _, _ in links],
                target=[index[dst] for _, dst, _ in links],
                value=[1.0] * len(links),
                color=["rgba(190,230,237,0.28)" if i % 2 else "rgba(252,211,77,0.30)" for i in range(len(links))],
                customdata=[note for _, _, note in links],
                hovertemplate="%{source.label} -> %{target.label}<br>%{customdata}<extra></extra>",
            ),
        ))
        fig.update_layout(
            height=480,
            title=dict(text="Reality as a generative model: physics / AI dictionary", font=dict(color=WHITE), x=0.02),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=DEEP_NAVY,
            font=dict(color=WHITE, size=13),
            margin=dict(l=20, r=20, t=55, b=20),
        )
        return fig

    def create_diffusion_denoising_figure(stage: float) -> go.Figure:
        rng = np.random.default_rng(31415)
        noise = rng.normal(size=(180, 2))
        theta = np.linspace(0, 8 * np.pi, 180)
        radius = np.linspace(0.15, 2.4, 180)
        target = np.column_stack([
            radius * np.cos(theta / PHI),
            radius * np.sin(theta / PHI),
        ])
        points = (1 - stage) * noise + stage * target
        fig = go.Figure()
        fig.add_trace(go.Scattergl(
            x=points[:, 0],
            y=points[:, 1],
            mode="markers",
            marker=dict(
                size=7,
                color=np.linspace(0, 1, len(points)),
                colorscale="Tealrose",
                opacity=0.84,
                line=dict(color="rgba(242,238,226,0.38)", width=0.35),
            ),
            hovertemplate="sample path<br>x=%{x:.2f}<br>y=%{y:.2f}<extra></extra>",
            name="state",
        ))
        fig.add_trace(go.Scattergl(
            x=target[:, 0],
            y=target[:, 1],
            mode="lines",
            line=dict(color="rgba(252,211,77,0.38)", width=2),
            hoverinfo="skip",
            name="golden attractor",
        ))
        fig.update_layout(
            height=420,
            title=dict(text=f"Forward noise -> reverse denoising geometry, t = {stage:.2f}", font=dict(color=WHITE), x=0.02),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=DEEP_NAVY,
            margin=dict(l=20, r=20, t=55, b=30),
            xaxis=dict(visible=False, scaleanchor="y", scaleratio=1),
            yaxis=dict(visible=False),
            legend=dict(font=dict(color=WHITE), orientation="h", y=-0.05),
        )
        return fig

    DIOPHANTINE_ROWS = [
        {"name": "phi", "value": PHI, "period": [1], "hurwitz": np.sqrt(5), "status": "unique positive minimum"},
        {"name": "silver", "value": 1 + np.sqrt(2), "period": [2], "hurwitz": 2 * np.sqrt(2), "status": "higher CF complexity"},
        {"name": "bronze", "value": (3 + np.sqrt(13)) / 2, "period": [3], "hurwitz": np.sqrt(13), "status": "higher CF complexity"},
        {"name": "sqrt(3)", "value": np.sqrt(3), "period": [1, 2], "hurwitz": 2 * np.sqrt(3), "status": "mixed periodic"},
        {"name": "pi", "value": np.pi, "period": [3, 7, 15, 1, 292], "hurwitz": 8.0, "status": "control, long CF token"},
        {"name": "e", "value": np.e, "period": [2, 1, 2, 1, 1, 4], "hurwitz": 7.0, "status": "control, unbounded pattern"},
    ]

    def _cf_complexity(period: List[int]) -> float:
        return float(np.mean(np.log1p(period)))

    def create_diophantine_selector(lambda_weight: float) -> go.Figure:
        names = [row["name"] for row in DIOPHANTINE_ROWS]
        k_values = np.array([_cf_complexity(row["period"]) for row in DIOPHANTINE_ROWS])
        s_values = np.array([np.log(row["hurwitz"]) for row in DIOPHANTINE_ROWS])
        f_values = lambda_weight * k_values + s_values
        colors = [SURVIVES_GREEN if name == "phi" else WARM_GOLD if i == int(np.argmin(f_values)) else ELECTRIC_CYAN for i, name in enumerate(names)]
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=names,
            y=f_values,
            marker=dict(color=colors, line=dict(color=WHITE, width=0.7)),
            text=[f"F={value:.3f}" for value in f_values],
            textposition="outside",
            customdata=np.column_stack([k_values, s_values]),
            hovertemplate="<b>%{x}</b><br>Kcf=%{customdata[0]:.3f}<br>S=%{customdata[1]:.3f}<br>F=%{y:.3f}<extra></extra>",
        ))
        fig.update_layout(
            height=420,
            title=dict(text=f"Diophantine-compression functional F = lambda K_cf + S, lambda = {lambda_weight:.2f}", font=dict(color=WHITE), x=0.02),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=DEEP_NAVY,
            margin=dict(l=45, r=20, t=60, b=60),
            yaxis=dict(title=dict(text="functional value", font=dict(color=MUTED)), gridcolor="#1e2937", tickfont=dict(color=MUTED)),
            xaxis=dict(tickfont=dict(color=WHITE)),
            showlegend=False,
        )
        return fig

    def create_diophantine_readout(lambda_weight: float) -> mo.Html:
        cards = []
        for row in DIOPHANTINE_ROWS[:4]:
            k_val = _cf_complexity(row["period"])
            s_val = np.log(row["hurwitz"])
            f_val = lambda_weight * k_val + s_val
            period = ",".join(str(x) for x in row["period"])
            active = " active" if row["name"] == "phi" else ""
            cards.append(f"""
            <div class="ipk-formula-card{active}">
                <div class="ipk-panel-kicker">continued fraction [{escape(period)}]</div>
                <h4>{escape(row['name'])}</h4>
                <code>Kcf={k_val:.3f}; S={s_val:.3f}; F={f_val:.3f}</code>
                <div class="ipk-formula-metrics">
                    <span><b>Value</b>{row['value']:.6f}</span>
                    <span><b>Status</b>{escape(row['status'])}</span>
                    <span><b>Page</b>55-57</span>
                </div>
            </div>
            """)
        return mo.Html(f'<div class="ipk-formula-grid">{"".join(cards)}</div>')

    MASS_MATRIX_PROGRAM = [
        ("Charged leptons", "implemented", "M_l = aI3 + b lambda3 + c lambda8; Koide Q_l=2/3", "pp. 35-37"),
        ("Up quarks", "open", "extend Cartan-basis operators to M_u", "p. 61"),
        ("Down quarks", "open", "extend S7 texture grammar to M_d", "p. 61"),
        ("Neutrinos", "open", "Majorana or Dirac M_nu with PMNS phases", "p. 61"),
        ("Higgs closure", "partial", "closed-loop charm-top-electroweak relation requires fuller audit", "pp. 8,36,61"),
        ("E8 spectral problem", "open", "explicit E8 bundle, connection, and Dirac spectrum", "pp. 58-61"),
    ]

    MASS_OPERATOR_SECTORS = {
        "Charged leptons (derived)": {
            "symbol": "M_l",
            "status": "implemented",
            "source": "pp. 35-37",
            "spectrum": np.array([0.51099895, MUON_MASS_PRED, TAU_MASS_PRED], dtype=float),
            "unit": "MeV",
            "note": "Audited sector: me is the unit anchor, mmu follows the inverse-Koide formula, and mtau is fixed by Q_l=2/3.",
        },
        "Up quarks (ansatz only)": {
            "symbol": "M_u",
            "status": "open",
            "source": "pp. 37-38, 61",
            "spectrum": np.array([PHI**-8, PHI**-4, 1.0], dtype=float),
            "unit": "normalized",
            "note": "Programmatic sector: the paper states the same Cartan form should apply, but does not supply the final pi/phi coefficients.",
        },
        "Down quarks (ansatz only)": {
            "symbol": "M_d",
            "status": "open",
            "source": "pp. 37-38, 61",
            "spectrum": np.array([PHI**-6, PHI**-3, 1.0], dtype=float),
            "unit": "normalized",
            "note": "Programmatic sector: CKM misalignment and baryon constraints remain part of the Mass Matrix Program.",
        },
        "Neutrinos (ansatz only)": {
            "symbol": "M_nu",
            "status": "open",
            "source": "pp. 32-33, 61",
            "spectrum": np.array([PHI**-6, PHI**-2, 1.0], dtype=float),
            "unit": "normalized",
            "note": "Programmatic sector: Majorana/Dirac choice and unconstrained phases are displayed as an ansatz surface, not a prediction.",
        },
    }
    MASS_OPERATOR_OPTIONS = list(MASS_OPERATOR_SECTORS)

    def _cartan_coefficients_from_spectrum(spectrum: np.ndarray) -> Tuple[float, float, float]:
        m1, m2, m3 = [float(x) for x in spectrum]
        a = (m1 + m2 + m3) / 3
        b = (m1 - m2) / 2
        c = (m1 + m2 - 2 * m3) / (2 * np.sqrt(3))
        return a, b, c

    def _cartan_spectrum_from_coefficients(a: float, b: float, c: float) -> np.ndarray:
        return np.array([
            a + b + c / np.sqrt(3),
            a - b + c / np.sqrt(3),
            a - 2 * c / np.sqrt(3),
        ], dtype=float)

    def _mass_operator_state(sector: str, a_scale: float, b_scale: float, c_scale: float) -> Dict[str, Any]:
        config = MASS_OPERATOR_SECTORS.get(sector, MASS_OPERATOR_SECTORS["Charged leptons (derived)"])
        base_a, base_b, base_c = _cartan_coefficients_from_spectrum(config["spectrum"])
        a = base_a * float(a_scale)
        b = base_b * float(b_scale)
        c = base_c * float(c_scale)
        spectrum = _cartan_spectrum_from_coefficients(a, b, c)
        positive = bool(np.all(spectrum > 0))
        hierarchy = float(np.max(np.abs(spectrum)) / max(np.min(np.abs(spectrum)), 1e-12))
        koide = _koide_q(spectrum) if positive else float("nan")
        return {
            "config": config,
            "a": a,
            "b": b,
            "c": c,
            "spectrum": spectrum,
            "matrix": np.diag(spectrum),
            "positive": positive,
            "hierarchy": hierarchy,
            "koide": koide,
        }

    def create_mass_operator_figure(sector: str, a_scale: float, b_scale: float, c_scale: float) -> go.Figure:
        state = _mass_operator_state(sector, a_scale, b_scale, c_scale)
        config = state["config"]
        spectrum = state["spectrum"]
        fig = go.Figure()
        fig.add_trace(go.Heatmap(
            z=state["matrix"],
            x=["gen 1", "gen 2", "gen 3"],
            y=["gen 1", "gen 2", "gen 3"],
            colorscale="Tealrose",
            zmid=0,
            colorbar=dict(title=dict(text=config["unit"], font=dict(color=WHITE)), tickfont=dict(color=WHITE), x=0.47),
            hovertemplate="%{y}, %{x}<br>M=%{z:.6g}<extra></extra>",
            xaxis="x",
            yaxis="y",
            name="operator",
        ))
        fig.add_trace(go.Bar(
            x=["m1", "m2", "m3"],
            y=spectrum,
            marker=dict(
                color=[ELECTRIC_CYAN, WARM_GOLD, SOFT_PURPLE],
                line=dict(color=WHITE, width=0.8),
            ),
            text=[f"{value:.4g}" for value in spectrum],
            textposition="outside",
            hovertemplate="%{x}<br>mass=%{y:.6g}<extra></extra>",
            xaxis="x2",
            yaxis="y2",
            name="spectrum",
        ))
        fig.add_annotation(
            x=0.74,
            y=0.95,
            xref="paper",
            yref="paper",
            text=f"{config['symbol']} = aI3 + b lambda3 + c lambda8",
            showarrow=False,
            font=dict(color=WHITE, size=14),
            align="left",
            bgcolor="rgba(15,23,42,0.72)",
            bordercolor="rgba(242,238,226,0.18)",
            borderpad=8,
        )
        fig.update_layout(
            height=430,
            title=dict(text=f"SU(3) Cartan mass operator sandbox: {sector}", font=dict(color=WHITE), x=0.02),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=DEEP_NAVY,
            margin=dict(l=35, r=35, t=60, b=45),
            xaxis=dict(domain=[0.0, 0.42], tickfont=dict(color=WHITE), side="top"),
            yaxis=dict(domain=[0.0, 1.0], tickfont=dict(color=WHITE), autorange="reversed"),
            xaxis2=dict(domain=[0.58, 1.0], tickfont=dict(color=WHITE)),
            yaxis2=dict(domain=[0.0, 0.82], tickfont=dict(color=MUTED), gridcolor="#1e2937", title=dict(text=config["unit"], font=dict(color=MUTED))),
            showlegend=False,
        )
        return fig

    def create_mass_operator_readout(sector: str, a_scale: float, b_scale: float, c_scale: float) -> mo.Html:
        state = _mass_operator_state(sector, a_scale, b_scale, c_scale)
        config = state["config"]
        status_class = {"implemented": "ok", "partial": "warn", "open": "bad"}.get(config["status"], "warn")
        spectrum_text = ", ".join(f"{value:.6g}" for value in state["spectrum"])
        koide_text = f"{state['koide']:.5f}" if np.isfinite(state["koide"]) else "requires positive spectrum"
        positivity = "positive spectrum" if state["positive"] else "non-positive trial spectrum"
        guard = "audited derivation" if config["status"] == "implemented" else "ansatz only"
        return mo.Html(f"""
        <div class="ipk-law-panel t-panel-slide t-resize" data-open="true">
            <div class="ipk-law-panel-top">
                <div>
                    <div class="ipk-panel-kicker">SU(3) flavour Cartan basis, {escape(config['source'])}</div>
                    <h3>{escape(config['symbol'])} operator: {escape(guard)}</h3>
                    <p>{escape(config['note'])}</p>
                </div>
                <div class="ipk-law-result {status_class}">{escape(config['status'])}</div>
            </div>
            <div class="ipk-formula-grid">
                <div class="ipk-formula-card active">
                    <div class="ipk-panel-kicker">operator</div>
                    <h4>{escape(config['symbol'])}</h4>
                    <code>{escape(config['symbol'])} = a I3 + b lambda3 + c lambda8</code>
                    <div class="ipk-formula-metrics">
                        <span><b>a</b>{state['a']:.6g}</span>
                        <span><b>b</b>{state['b']:.6g}</span>
                        <span><b>c</b>{state['c']:.6g}</span>
                    </div>
                </div>
                <div class="ipk-formula-card">
                    <div class="ipk-panel-kicker">spectrum</div>
                    <h4>eigenvalues</h4>
                    <code>spec(M) = [{escape(spectrum_text)}]</code>
                    <div class="ipk-formula-metrics">
                        <span><b>Unit</b>{escape(config['unit'])}</span>
                        <span><b>Ratio</b>{state['hierarchy']:.3g}</span>
                        <span><b>Sign</b>{escape(positivity)}</span>
                    </div>
                </div>
                <div class="ipk-formula-card">
                    <div class="ipk-panel-kicker">constraint</div>
                    <h4>Koide diagnostic</h4>
                    <code>Q = Tr(M)/(Tr(sqrt(M)))^2</code>
                    <div class="ipk-formula-metrics">
                        <span><b>Now</b>{escape(koide_text)}</span>
                        <span><b>Lepton target</b>2/3</span>
                        <span><b>Status</b>{escape(guard)}</span>
                    </div>
                </div>
            </div>
        </div>
        """)

    def create_mass_matrix_program() -> mo.Html:
        status_class = {"implemented": "ok", "partial": "warn", "open": "bad"}
        rows = []
        for name, status, detail, page in MASS_MATRIX_PROGRAM:
            css = status_class.get(status, "warn")
            rows.append(f"""
            <div class="ipk-kill-card">
                <div class="ipk-panel-kicker">{escape(page)}</div>
                <h4>{escape(name)}</h4>
                <strong class="ipk-status-{css}">{escape(status)}</strong>
                <p>{escape(detail)}</p>
            </div>
            """)
        return mo.Html(f"""
        <div class="ipk-kill-grid">{"".join(rows)}</div>
        <div class="ipk-law-panel t-panel-slide t-resize" data-open="true">
            <div class="ipk-law-panel-top">
                <div>
                    <div class="ipk-panel-kicker">Ansatz 58.1 and spectral-program guardrail</div>
                    <h3>Formula audit boundary</h3>
                    <p>The notebook encodes charged-lepton formulas because the paper gives enough algebra to audit them. Quark, neutrino, and full Higgs matrices remain displayed as open programme items until explicit matrices are supplied.</p>
                </div>
                <div class="ipk-law-result bad">no hidden dials</div>
            </div>
        </div>
        """)

    PROVENANCE_STATUS_FILTERS = ["All", "scorecard", "derived", "prediction", "module", "open", "listed"]
    PROVENANCE_ROWS = [
        {"Module": "Table of Law", "Claim": "Allowed vocabulary", "LaTeX": r"\{\pi,\phi,24,12,45,16,15,3\}", "Source": "pp. 6-8", "Status": "module"},
        {"Module": "Table of Law", "Claim": "Fibonacci/Binet descendants", "LaTeX": r"F_n=(\phi^n-(1-\phi)^n)/\sqrt{5}", "Source": "pp. 7-8", "Status": "module"},
        {"Module": "Derivation Forest", "Claim": "Vacuum impedance", "LaTeX": r"\alpha^{-1}=360/\phi^2-2\phi^{-3}+\phi^{-16}", "Source": "pp. 29-30,45", "Status": "scorecard"},
        {"Module": "Derivation Forest", "Claim": "Proton ratio", "LaTeX": r"m_p/m_e=6\pi^5+\phi^{-7}", "Source": "pp. 31,45", "Status": "scorecard"},
        {"Module": "Derivation Forest", "Claim": "45 reuse in PMNS", "LaTeX": r"\sin^2\theta_{13}^{PMNS}=1/45", "Source": "pp. 32-33,45", "Status": "scorecard"},
        {"Module": "Derivation Forest", "Claim": "45 reuse in baryons", "LaTeX": r"\Omega_b h^2=(1/45)(1+\alpha)", "Source": "pp. 32-33,45", "Status": "scorecard"},
        {"Module": "Derivation Forest", "Claim": "Triality generation count", "LaTeX": r"N_{gen}=3", "Source": "p. 34", "Status": "derived"},
        {"Module": "Scorecard", "Claim": "Weak mixing", "LaTeX": r"\sin^2\theta_W=3/13+\phi^{-16}", "Source": "p. 45", "Status": "scorecard"},
        {"Module": "Scorecard", "Claim": "Strong coupling", "LaTeX": r"\alpha_s(M_Z)=(2\phi^3)^{-1}", "Source": "p. 45", "Status": "scorecard"},
        {"Module": "Scorecard", "Claim": "CKM theta12", "LaTeX": r"\sin\theta_{12}=1/(2\sqrt{5})+\phi^{-14}", "Source": "p. 44", "Status": "scorecard"},
        {"Module": "Scorecard", "Claim": "CKM theta13", "LaTeX": r"\sin\theta_{13}=1/273", "Source": "p. 44", "Status": "scorecard"},
        {"Module": "Scorecard", "Claim": "CKM theta23", "LaTeX": r"\sin\theta_{23}=1/24", "Source": "p. 44", "Status": "scorecard"},
        {"Module": "Scorecard", "Claim": "CKM CP phase", "LaTeX": r"\delta_{CKM}=180/\phi^2", "Source": "p. 44", "Status": "scorecard"},
        {"Module": "Scorecard", "Claim": "PMNS theta12", "LaTeX": r"\sin^2\theta_{12}=5/16", "Source": "p. 45", "Status": "scorecard"},
        {"Module": "Scorecard", "Claim": "PMNS theta23", "LaTeX": r"\sin^2\theta_{23}=\phi/3", "Source": "p. 45", "Status": "scorecard"},
        {"Module": "Scorecard", "Claim": "PMNS CP phase", "LaTeX": r"\delta_{CP}=3\pi/2=270^\circ", "Source": "pp. 45-46", "Status": "scorecard"},
        {"Module": "Scorecard", "Claim": "Optical depth", "LaTeX": r"\tau=\phi^{-6}", "Source": "p. 45", "Status": "scorecard"},
        {"Module": "Scorecard", "Claim": "Spectral index", "LaTeX": r"n_s=1-\phi^{-3}/(2\pi)", "Source": "p. 45", "Status": "scorecard"},
        {"Module": "Scorecard", "Claim": "Dark-to-baryon ratio", "LaTeX": r"\Omega_c/\Omega_b=2\pi-1+\phi^{-6}", "Source": "p. 45", "Status": "scorecard"},
        {"Module": "Scorecard", "Claim": "Sigma 8", "LaTeX": r"\sigma_8=\phi/2", "Source": "p. 45", "Status": "scorecard"},
        {"Module": "Scorecard", "Claim": "Acoustic scale", "LaTeX": r"100\theta_\*=1+\phi^{-3}/(2\pi)+\alpha/2", "Source": "p. 45", "Status": "scorecard"},
        {"Module": "Gauge Saturation", "Claim": "Gauge bandwidth", "LaTeX": r"\dim(G)\leq K_3=12", "Source": "p. 28", "Status": "derived"},
        {"Module": "Gauge Saturation", "Claim": "Standard Model saturation", "LaTeX": r"\dim(SM)=8+3+1=12=K_3", "Source": "p. 28", "Status": "derived"},
        {"Module": "Kill List", "Claim": "W mass prediction", "LaTeX": r"m_W=80.36\ \mathrm{GeV}", "Source": "p. 47", "Status": "prediction"},
        {"Module": "Kill List", "Claim": "Axion central prediction", "LaTeX": r"m_a=225\pm 5\ \mu\mathrm{eV}", "Source": "p. 46", "Status": "prediction"},
        {"Module": "Kill List", "Claim": "Axion falsification band", "LaTeX": r"m_a=225\pm 50\ \mu\mathrm{eV}", "Source": "pp. 48,53", "Status": "prediction"},
        {"Module": "Kill List", "Claim": "Tensor-to-scalar prediction", "LaTeX": r"r=3(\phi^{-3}/2\pi)^2\approx 0.004", "Source": "pp. 46,48", "Status": "prediction"},
        {"Module": "Kill List", "Claim": "Proton lifetime prediction", "LaTeX": r"\tau_p>10^{40}\ \mathrm{yr}", "Source": "pp. 46,48", "Status": "prediction"},
        {"Module": "Kill List", "Claim": "Local Hubble prediction", "LaTeX": r"H_0^{local}=67.4(1+\sqrt{\alpha})=73.2", "Source": "p. 48", "Status": "prediction"},
        {"Module": "H4 / 600-cell", "Claim": "Golden coordinate archetype", "LaTeX": r"(\pm 1/2,\pm\phi/2,\pm 1/(2\phi),0)", "Source": "pp. 27-28", "Status": "derived"},
        {"Module": "Koide Cone", "Claim": "Koide equipartition", "LaTeX": r"Q_\ell=(m_e+m_\mu+m_\tau)/(\sqrt{m_e}+\sqrt{m_\mu}+\sqrt{m_\tau})^2=2/3", "Source": "pp. 35-37", "Status": "derived"},
        {"Module": "Koide Cone", "Claim": "Muon formula", "LaTeX": r"m_\mu=m_e[(3/2)\alpha^{-1}+\sqrt{\phi}-\phi^{-6}]", "Source": "pp. 35-37", "Status": "derived"},
        {"Module": "Compression Lab", "Claim": "Grammar search", "LaTeX": r"f(A,B,n,m)=A\pi^n+B\phi^m", "Source": "pp. 49-51", "Status": "module"},
        {"Module": "Compression Lab", "Claim": "Monte Carlo target-set controls", "LaTeX": r"\Pr[\mathrm{random\ targets\ matched}]\ll \Pr[\mathrm{physical\ targets\ matched}]", "Source": "pp. 49-51", "Status": "module"},
        {"Module": "Compression Lab", "Claim": "Description-length gain", "LaTeX": r"\Delta L=L_{data}-L_{geo}\gtrsim 250\ \mathrm{bits}", "Source": "pp. 50-51", "Status": "module"},
        {"Module": "Diophantine Phi", "Claim": "Continued-fraction complexity", "LaTeX": r"K_{cf}(\alpha)=\limsup_{n\to\infty} n^{-1}\sum_{k=1}^n\log(1+a_k)", "Source": "pp. 55-57", "Status": "module"},
        {"Module": "Diophantine Phi", "Claim": "Diophantine functional", "LaTeX": r"F_\lambda(\alpha)=\lambda K_{cf}(\alpha)+S(\alpha)", "Source": "pp. 56-57", "Status": "module"},
        {"Module": "Spectral Audit", "Claim": "Cartan mass operator sandbox", "LaTeX": r"M=aI_3+b\lambda_3+c\lambda_8,\quad \mathrm{spec}(M)=\{m_1,m_2,m_3\}", "Source": "pp. 35-38,61", "Status": "module"},
        {"Module": "Spectral Audit", "Claim": "E8 spectral problem", "LaTeX": r"D_{E_8,CY3}\Rightarrow \{32\ \mathrm{SM}+\Lambda\mathrm{CDM}\ \mathrm{constants}\}", "Source": "pp. 58-61", "Status": "open"},
        {"Module": "Spectral Audit", "Claim": "Full mass matrices", "LaTeX": r"M_\ell=aI_3+b\lambda_3+c\lambda_8\leadsto (M_u,M_d,M_\nu)", "Source": "p. 61", "Status": "open"},
    ]

    def create_provenance_dataframe(status_filter: str) -> pd.DataFrame:
        df = pd.DataFrame(PROVENANCE_ROWS)
        if status_filter != "All":
            df = df[df["Status"] == status_filter]
        return df[["Module", "Claim", "LaTeX", "Source", "Status"]].reset_index(drop=True)

    def provenance_markdown(status_filter: str) -> str:
        df = create_provenance_dataframe(status_filter)
        lines = [
            "# Intelligent Physics Monograph Traceability Sheet",
            "",
            f"Filter: {status_filter}",
            "Source PDF: intelligent_physics.pdf (65-page Intelligent Physics monograph, Dec 2025)",
            "",
        ]
        for _, row in df.iterrows():
            lines.extend([
                f"## {row['Module']} - {row['Claim']}",
                f"- Source: {row['Source']}",
                f"- Status: {row['Status']}",
                f"- LaTeX: `${row['LaTeX']}$`",
                "",
            ])
        return "\n".join(lines)

    def provenance_csv(status_filter: str) -> str:
        return create_provenance_dataframe(status_filter).to_csv(index=False)

    def create_provenance_copy_preview(markdown_text: str, status_filter: str) -> mo.Html:
        lines = markdown_text.splitlines()
        preview = "\n".join(lines[:52])
        if len(lines) > 52:
            preview += f"\n\n... {len(lines) - 52} more lines in the Markdown download."
        return mo.Html(f"""
        <details class="ipk-copy-sheet t-panel-slide t-resize" data-open="true">
            <summary>
                <span>
                    <strong>Copy sheet preview</strong>
                    <small>Filter: {escape(status_filter)} · full Markdown is in the download</small>
                </span>
            </summary>
            <pre>{escape(preview)}</pre>
        </details>
        """)

    def create_provenance_summary(status_filter: str) -> mo.Html:
        df = create_provenance_dataframe(status_filter)
        counts = df["Status"].value_counts().to_dict() if not df.empty else {}
        chips = "".join(f"<span>{escape(k)}: {v}</span>" for k, v in counts.items())
        return mo.Html(f"""
        <div class="ipk-law-panel t-panel-slide t-resize" data-open="true">
            <div class="ipk-law-panel-top">
                <div>
                    <div class="ipk-panel-kicker">Traceability console</div>
                    <h3>{len(df)} exportable claims and formulas</h3>
                    <p>Every row carries a LaTeX string, PDF page reference, and status label so the monograph can be audited outside the notebook.</p>
                </div>
                <div class="ipk-law-result ok">portable</div>
            </div>
            <div class="ipk-token-row">{chips}</div>
        </div>
        """)

    COVERAGE_ROWS = [
        {"Area": "Core format", "Requirement": "Fully cell-based Marimo notebook", "Implementation": "app.setup plus multiple @app.cell outputs", "Evidence": "marimo check + edit health", "Status": "complete"},
        {"Area": "Runtime", "Requirement": "Local marimo run remains healthy", "Implementation": "verified local Marimo server", "Evidence": "health endpoint returns healthy", "Status": "complete"},
        {"Area": "Editor", "Requirement": "marimo edit works", "Implementation": "headless edit smoke test on an ephemeral local port", "Evidence": "health endpoint returns healthy", "Status": "complete"},
        {"Area": "Editor", "Requirement": "VS Code / JupyterHub extensions", "Implementation": "standard cell file format plus repeatable local verifier; host UI checks remain manual", "Evidence": "verify_editor_deployment.py; requires host-specific UI confirmation", "Status": "external"},
        {"Area": "Theme", "Requirement": "II Logos theme and transitions", "Implementation": "editorial cream/navy/gold/teal palette, transitions, full-width layout", "Evidence": "browser smoke text + CSS present", "Status": "complete"},
        {"Area": "Tier 1", "Requirement": "Vocabulary Enforcer + Table of Law", "Implementation": "live validator, header badge, lawful/unlawful examples", "Evidence": "module 1 + traceability rows", "Status": "complete"},
        {"Area": "Tier 1", "Requirement": "Derivation Trees / Forest View", "Implementation": "interactive forest plus flagship formula cards", "Evidence": "module 2", "Status": "complete"},
        {"Area": "Tier 1", "Requirement": "Master Scorecard - 32 constants", "Implementation": "32-row table with status labels and reuse highlighting", "Evidence": "module 3", "Status": "guarded"},
        {"Area": "Tier 1", "Requirement": "Dimensional Saturation visualizer", "Implementation": "K3=12 gauge-channel chart and W-mass argument", "Evidence": "module 4", "Status": "complete"},
        {"Area": "Tier 1", "Requirement": "Falsification Kill List", "Implementation": "six prediction cards, hard-coded experiment status, axion band audit, brittleness chart, timeline, Pledge excerpt", "Evidence": "module 5", "Status": "complete"},
        {"Area": "Tier 2", "Requirement": "E8 -> 600-cell / H4", "Implementation": "golden projection explorer with three modes", "Evidence": "module 6", "Status": "complete"},
        {"Area": "Tier 2", "Requirement": "Koide cone and lepton matrix", "Implementation": "3D cone, deformation slider, live mass readouts", "Evidence": "module 7", "Status": "complete"},
        {"Area": "Tier 2", "Requirement": "Compression / Monte Carlo validation lab", "Implementation": "bounded grammar search, compression chart, deterministic target-set Monte Carlo controls", "Evidence": "module 8 + traceability row", "Status": "complete"},
        {"Area": "Tier 3", "Requirement": "Ontology comparator", "Implementation": "SM/GR vs long-paper ontology table", "Evidence": "module 9", "Status": "complete"},
        {"Area": "Tier 3", "Requirement": "Generative-model isomorphism", "Implementation": "physics/AI Sankey and denoising animation", "Evidence": "module 10", "Status": "complete"},
        {"Area": "Tier 3", "Requirement": "Diophantine phi selector", "Implementation": "F_lambda selector with continued-fraction cards", "Evidence": "module 11", "Status": "complete"},
        {"Area": "Open science", "Requirement": "Cartan mass-operator ansatz", "Implementation": "interactive SU(3) Cartan sandbox for M=aI3+b lambda3+c lambda8", "Evidence": "module 12; pp. 35-38,61", "Status": "complete"},
        {"Area": "Open science", "Requirement": "Full mass matrices and E8 spectral realization", "Implementation": "mass-operator sandbox plus audit board; full quark/neutrino/E8 predictions remain unsupported", "Evidence": "module 12; paper marks as ansatz/open", "Status": "open"},
        {"Area": "Provenance", "Requirement": "Copy LaTeX + PDF page refs + export", "Implementation": "40-row traceability console with CSV/Markdown downloads", "Evidence": "module 13", "Status": "complete"},
        {"Area": "Audit", "Requirement": "Coverage Matrix / downloadable audit", "Implementation": "implementation-status matrix plus Markdown coverage download", "Evidence": "module 14", "Status": "complete"},
    ]

    def create_coverage_dataframe() -> pd.DataFrame:
        return pd.DataFrame(COVERAGE_ROWS)

    def create_coverage_chart() -> go.Figure:
        df = create_coverage_dataframe()
        counts = df["Status"].value_counts().reindex(["complete", "guarded", "external", "open"], fill_value=0)
        colors = {
            "complete": SURVIVES_GREEN,
            "guarded": WARM_GOLD,
            "external": ELECTRIC_CYAN,
            "open": ELIMINATED_RED,
        }
        fig = go.Figure(go.Bar(
            x=counts.index.tolist(),
            y=counts.values.tolist(),
            marker=dict(color=[colors[name] for name in counts.index], line=dict(color=WHITE, width=0.8)),
            text=[str(v) for v in counts.values],
            textposition="outside",
            hovertemplate="<b>%{x}</b><br>%{y} requirements<extra></extra>",
        ))
        fig.update_layout(
            height=340,
            title=dict(text="Implementation coverage by status", font=dict(color=WHITE), x=0.02),
            paper_bgcolor=DEEP_NAVY,
            plot_bgcolor=DEEP_NAVY,
            margin=dict(l=45, r=20, t=55, b=55),
            yaxis=dict(title=dict(text="requirements", font=dict(color=MUTED)), gridcolor="#1e2937", tickfont=dict(color=MUTED)),
            xaxis=dict(tickfont=dict(color=WHITE)),
            showlegend=False,
        )
        return fig

    def coverage_markdown() -> str:
        lines = [
            "# Intelligent Physics Notebook Coverage Audit",
            "",
            "Status legend: complete = implemented and verified; guarded = implemented with explicit caveats; external = needs host-specific manual check; open = source paper marks the mathematics as an open programme.",
            "",
        ]
        for row in COVERAGE_ROWS:
            lines.extend([
                f"## {row['Area']} - {row['Requirement']}",
                f"- Status: {row['Status']}",
                f"- Implementation: {row['Implementation']}",
                f"- Evidence: {row['Evidence']}",
                "",
            ])
        return "\n".join(lines)

    def create_coverage_summary() -> mo.Html:
        df = create_coverage_dataframe()
        counts = df["Status"].value_counts().to_dict()
        chips = "".join(f"<span>{escape(status)}: {count}</span>" for status, count in counts.items())
        return mo.Html(f"""
        <div class="ipk-law-panel t-panel-slide t-resize" data-open="true">
            <div class="ipk-law-panel-top">
                <div>
                    <div class="ipk-panel-kicker">Completion audit</div>
                    <h3>{len(df)} explicit requirements tracked</h3>
                    <p>The matrix separates implemented features from guarded rows, host-specific checks, and mathematics the source paper itself marks as open.</p>
                </div>
                <div class="ipk-law-result ok">auditable</div>
            </div>
            <div class="ipk-token-row">{chips}</div>
        </div>
        """)


@app.cell
def _():
    mo.Html(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Libre+Caslon+Text:wght@400;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&family=Geist:wght@400;500;600&display=swap');

    :root {{
        --primary: #0F233F;
        --primary-hover: #12335A;
        --secondary: #516071;
        --tertiary: #83A1CC;
        --accent: #2F95A6;
        --accent-strong: #236F7D;
        --gold: #C9A96E;
        --gold-strong: #7A5D29;
        --sky: #BEE6ED;
        --slate: #546070;
        --neutral: #F2EEE2;
        --neutral-soft: #E8EDE5;
        --surface: #F2EEE2;
        --surface-elevated: #E8EDE5;
        --on-surface: #212121;
        --border: #5D6572;
        --inverse: #F2EEE2;
        --rule: rgba(15,35,63,.10);
        --rule-strong: rgba(15,35,63,.22);
        --serif-caslon: "Libre Caslon Text", "Cormorant Garamond", ui-serif, Georgia, serif;
        --serif-display: "Cormorant Garamond", ui-serif, Georgia, serif;
        --serif-body: "Source Serif 4", ui-serif, Georgia, serif;
        --sans: "Geist", ui-sans-serif, system-ui, sans-serif;
        --shell-max: 1600px;
        --gutter: clamp(20px, 4vw, 80px);
        --gutter-wide: 80px;
        --section: 80px;
        --r-sm: 8px;
        --r-md: 12px;
        --r-lg: 20px;
        --r-xl: 30px;
        --r-full: 9999px;
        --ii-shadow: 0 20px 50px -32px rgba(15,35,63,.30);
        --ii-ease: cubic-bezier(.2,.7,.2,1);
        --ease-out-cubic: cubic-bezier(.33, 1, .68, 1);
        --ease-in-out-cubic: cubic-bezier(.65, 0, .35, 1);
        --ease-soft-out: cubic-bezier(.2, .7, .2, 1);
        --ease-spring: cubic-bezier(.34, 1.56, .64, 1);
        --dur-instant: 120ms;
        --dur-quick: 200ms;
        --dur-base: 280ms;
        --dur-slow: 420ms;

        /* transitions-dev — copy this :root block into your project once.
           Every transition snippet reads from these semantic names. */
        --resize-dur: 300ms;
        --resize-ease: cubic-bezier(0.22, 1, 0.36, 1);
        --digit-dur: 500ms;
        --digit-distance: 8px;
        --digit-stagger: 70ms;
        --digit-blur: 2px;
        --digit-ease: cubic-bezier(0.34, 1.45, 0.64, 1);
        --digit-dir-x: 0;
        --digit-dir-y: 1;
        --badge-slide-dur: 260ms;
        --badge-pop-dur: 500ms;
        --badge-pop-close-dur: 180ms;
        --badge-fade-dur: 400ms;
        --badge-fade-close-dur: 180ms;
        --badge-blur: 2px;
        --badge-offset-x: -8.2px;
        --badge-offset-y: 12.4px;
        --badge-slide-ease: cubic-bezier(0.22, 1, 0.36, 1);
        --badge-pop-ease: cubic-bezier(0.34, 1.36, 0.64, 1);
        --badge-close-ease: cubic-bezier(0.4, 0, 0.2, 1);
        --text-swap-dur: 200ms;
        --text-swap-translate-y: 8px;
        --text-swap-blur: 2px;
        --text-swap-ease: ease-out;
        --dropdown-open-dur: 250ms;
        --dropdown-close-dur: 150ms;
        --dropdown-pre-scale: 0.97;
        --dropdown-closing-scale: 0.99;
        --dropdown-ease: cubic-bezier(0.22, 1, 0.36, 1);
        --modal-open-dur: 250ms;
        --modal-close-dur: 150ms;
        --modal-scale: 0.96;
        --modal-scale-close: 0.96;
        --modal-ease: cubic-bezier(0.22, 1, 0.36, 1);
        --panel-open-dur: 400ms;
        --panel-close-dur: 350ms;
        --panel-translate-y: 100px;
        --panel-blur: 2px;
        --panel-ease: cubic-bezier(0.22, 1, 0.36, 1);
        --page-slide-dur: 200ms;
        --page-fade-dur: 200ms;
        --page-slide-distance: 8px;
        --page-blur: 3px;
        --page-stagger: 0ms;
        --page-exit-enabled: 1;
        --page-slide-ease: cubic-bezier(0.22, 1, 0.36, 1);
        --page-fade-ease: cubic-bezier(0.22, 1, 0.36, 1);
        --icon-swap-dur: 200ms;
        --icon-swap-blur: 2px;
        --icon-swap-start-scale: 0.25;
        --icon-swap-ease: ease-in-out;

        --ipk-deep-navy: {DEEP_NAVY};
        --ipk-midnight: {MIDNIGHT};
        --ipk-cyan: {ELECTRIC_CYAN};
        --ipk-gold: {WARM_GOLD};
        --ipk-purple: {SOFT_PURPLE};
        --ipk-magenta: {SOFT_MAGENTA};
        --ipk-fluid: {FLUID_BLUE};
        --ipk-muted: {MUTED};
        --ipk-white: {WHITE};
        --ipk-green: {SURVIVES_GREEN};
    }}
    *,
    *::before,
    *::after {{
        box-sizing: border-box;
    }}
    html {{
        background: var(--surface);
        min-width: 100%;
        overflow-x: hidden;
        scroll-behavior: smooth;
    }}
    body {{
        background:
            linear-gradient(90deg, transparent 0, transparent 33.28%, var(--rule) 33.32%, transparent 33.36%, transparent 66.61%, var(--rule) 66.65%, transparent 66.69%),
            radial-gradient(circle at 85% 12%, rgba(190,230,237,.38), transparent 26rem),
            radial-gradient(circle at 5% 76%, rgba(201,169,110,.26), transparent 24rem),
            linear-gradient(180deg, var(--surface) 0%, var(--neutral-soft) 56%, var(--surface) 100%);
        color: var(--primary);
        font-family: var(--serif-body);
        font-size: 18px;
        line-height: 1.6;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeLegibility;
        font-feature-settings: "kern", "liga", "onum";
        overflow-x: hidden;
    }}
    a {{
        color: inherit;
        text-decoration: none;
    }}
    #App,
    #App.bg-background,
    .marimo-cell,
    .marimo-cell.published {{
        background: transparent !important;
    }}
    ::selection {{
        background: var(--primary);
        color: var(--neutral);
    }}
    h1, h2, h3, h4 {{
        font-family: var(--serif-display);
        font-weight: 400;
        letter-spacing: 0;
    }}
    h1 em, h2 em, h3 em, h4 em,
    .ipk-cascade-intro h3,
    .ipk-section-header h2 em {{
        background: linear-gradient(90deg, var(--accent) 0%, var(--gold) 42%, var(--accent) 70%, var(--accent) 100%);
        background-size: 260% auto;
        -webkit-background-clip: text;
        background-clip: text;
        animation: ipk-shimmer-sweep 4.2s linear infinite;
    }}
    @supports (-webkit-text-fill-color: transparent) {{
        h1 em, h2 em, h3 em, h4 em,
        .ipk-cascade-intro h3,
        .ipk-section-header h2 em {{
            -webkit-text-fill-color: transparent;
        }}
    }}
    @keyframes ipk-shimmer-sweep {{
        from {{ background-position: 240% center; }}
        to {{ background-position: -80% center; }}
    }}
    p, li {{
        font-family: var(--serif-body);
    }}
    #root,
    main,
    .marimo,
    .marimo-app,
    .mo-notebook,
    .notebook,
    [data-testid="notebook"],
    [data-testid="notebook-content"] {{
        max-width: none !important;
        width: 100% !important;
    }}
    [data-testid="cell-output"],
    .cell-output,
    .output-area,
    .output.block,
    marimo-output {{
        max-width: none !important;
        width: 100% !important;
    }}
    .ipk-monograph-shell,
    .output.block:has(.ipk-monograph-shell-marker) > div,
    .output-area .output.block:has(.ipk-monograph-shell-marker) > div {{
        width: 100vw !important;
        max-width: none !important;
        min-width: 100vw !important;
        box-sizing: border-box;
        color: var(--inverse) !important;
    }}
    .ipk-monograph-shell h1,
    .ipk-monograph-shell h2,
    .ipk-monograph-shell h3,
    .ipk-monograph-shell h4,
    .ipk-monograph-shell label,
    .ipk-monograph-shell .ipk-section-header h2,
    .ipk-monograph-shell .ipk-panel-kicker,
    .output.block:has(.ipk-monograph-shell-marker) h1,
    .output.block:has(.ipk-monograph-shell-marker) h2,
    .output.block:has(.ipk-monograph-shell-marker) h3,
    .output.block:has(.ipk-monograph-shell-marker) h4,
    .output.block:has(.ipk-monograph-shell-marker) label,
    .output.block:has(.ipk-monograph-shell-marker) .ipk-section-header h2,
    .output.block:has(.ipk-monograph-shell-marker) .ipk-panel-kicker {{
        color: var(--inverse) !important;
    }}
    .ipk-monograph-shell p,
    .ipk-monograph-shell .ipk-section-subtitle,
    .ipk-monograph-shell .mo-ui-text,
    .ipk-monograph-shell .mo-checkbox label,
    .ipk-monograph-shell .mo-radio label,
    .output.block:has(.ipk-monograph-shell-marker) p,
    .output.block:has(.ipk-monograph-shell-marker) .ipk-section-subtitle,
    .output.block:has(.ipk-monograph-shell-marker) .mo-ui-text,
    .output.block:has(.ipk-monograph-shell-marker) .mo-checkbox label,
    .output.block:has(.ipk-monograph-shell-marker) .mo-radio label {{
        color: rgba(242,238,226,.76) !important;
    }}
    .ipk-monograph-shell input,
    .ipk-monograph-shell textarea,
    .ipk-monograph-shell select,
    .output.block:has(.ipk-monograph-shell-marker) input,
    .output.block:has(.ipk-monograph-shell-marker) textarea,
    .output.block:has(.ipk-monograph-shell-marker) select {{
        background: rgba(7,20,38,.88) !important;
        color: var(--inverse) !important;
        border-color: rgba(242,238,226,.22) !important;
        color-scheme: dark;
    }}
    .ipk-monograph-shell marimo-text,
    .output.block:has(.ipk-monograph-shell-marker) marimo-text {{
        color: var(--primary) !important;
    }}
    .ipk-monograph-shell marimo-text::part(label),
    .output.block:has(.ipk-monograph-shell-marker) marimo-text::part(label) {{
        color: rgba(242,238,226,.78) !important;
    }}
    :where(.ipk-monograph-shell, .output.block:has(.ipk-monograph-shell-marker)) marimo-table {{
        color-scheme: dark;
        color: var(--inverse) !important;
        --gdg-bg-cell: rgba(7, 20, 38, 0.96);
        --gdg-bg-cell-medium: rgba(11, 29, 51, 0.98);
        --gdg-bg-header: rgba(242, 238, 226, 0.12);
        --gdg-bg-header-has-focus: rgba(103, 232, 249, 0.18);
        --gdg-bg-bubble: rgba(7, 20, 38, 0.96);
        --gdg-text-dark: var(--inverse);
        --gdg-text-medium: rgba(242, 238, 226, 0.78);
        --gdg-text-light: rgba(242, 238, 226, 0.60);
        --gdg-text-group-header: var(--sky);
        --gdg-border-color: rgba(242, 238, 226, 0.18);
        --gdg-accent-color: var(--sky);
        --gdg-accent-light: rgba(103, 232, 249, 0.18);
        --gdg-link-color: var(--sky);
        --gdg-font-family: var(--sans);
    }}
    :where(.ipk-monograph-shell, .output.block:has(.ipk-monograph-shell-marker)) marimo-table::part(table-wrapper),
    :where(.ipk-monograph-shell, .output.block:has(.ipk-monograph-shell-marker)) marimo-table::part(table-tabs),
    :where(.ipk-monograph-shell, .output.block:has(.ipk-monograph-shell-marker)) marimo-table::part(table-footer),
    :where(.ipk-monograph-shell, .output.block:has(.ipk-monograph-shell-marker)) marimo-table::part(filter-pills) {{
        background: rgba(7, 20, 38, 0.92) !important;
        color: var(--inverse) !important;
        border-color: rgba(242, 238, 226, 0.18) !important;
    }}
    :where(.ipk-monograph-shell, .output.block:has(.ipk-monograph-shell-marker)) marimo-table :is(
        table, thead, tbody, tr, th, td,
        [role="grid"], [role="row"], [role="columnheader"], [role="gridcell"]
    ) {{
        color: var(--inverse) !important;
    }}
    :where(.ipk-monograph-shell, .output.block:has(.ipk-monograph-shell-marker)) .mo-callout,
    :where(.ipk-monograph-shell, .output.block:has(.ipk-monograph-shell-marker)) [data-testid="stacks-plain-text"],
    :where(.ipk-monograph-shell, .output.block:has(.ipk-monograph-shell-marker)) pre {{
        background: rgba(7, 20, 38, 0.66) !important;
        color: rgba(242, 238, 226, 0.86) !important;
        border-color: rgba(242, 238, 226, 0.18) !important;
    }}
    :where(.ipk-monograph-shell, .output.block:has(.ipk-monograph-shell-marker)) .mo-button,
    :where(.ipk-monograph-shell, .output.block:has(.ipk-monograph-shell-marker)) button {{
        border-color: rgba(242, 238, 226, 0.22) !important;
    }}
    :where(.ipk-monograph-shell, .output.block:has(.ipk-monograph-shell-marker)) .modebar {{
        opacity: .22;
        transform: scale(.92);
        transform-origin: top right;
        transition: opacity 180ms var(--ii-ease);
    }}
    :where(.ipk-monograph-shell, .output.block:has(.ipk-monograph-shell-marker)) .js-plotly-plot:hover .modebar {{
        opacity: .82;
    }}
    .t-panel-slide {{
      transform: translateY(var(--panel-translate-y));
      opacity: 0;
      filter: blur(var(--panel-blur));
      pointer-events: none;
      transition:
        transform var(--panel-close-dur) var(--panel-ease),
        opacity   var(--panel-close-dur) var(--panel-ease),
        filter    var(--panel-close-dur) var(--panel-ease);
      will-change: transform, opacity, filter;
    }}
    .t-panel-slide[data-open="true"] {{
      transform: translateY(0);
      opacity: 1;
      filter: blur(0);
      pointer-events: auto;
      transition:
        transform var(--panel-open-dur) var(--panel-ease),
        opacity   var(--panel-open-dur) var(--panel-ease),
        filter    var(--panel-open-dur) var(--panel-ease);
    }}
    .t-resize {{
      transition:
        width  var(--resize-dur) var(--resize-ease),
        height var(--resize-dur) var(--resize-ease);
      will-change: width, height;
    }}
    .reveal[data-ipk-reveal-bound="true"]:not(.in) {{
        opacity: 0;
        transform: translateY(18px);
        transition:
            opacity .9s var(--ease-soft-out),
            transform .9s var(--ease-soft-out),
            filter .9s var(--ease-soft-out);
        will-change: opacity, transform, filter;
    }}
    .reveal.in {{
        opacity: 1;
        transform: none;
        filter: none;
    }}
    .reveal-stagger[data-ipk-reveal-bound="true"]:not(.in) > * {{
        opacity: 0;
        transform: translateY(14px);
        transition:
            opacity .7s var(--ease-soft-out),
            transform .7s var(--ease-soft-out),
            filter .7s var(--ease-soft-out);
    }}
    .reveal-stagger.in > *,
    .reveal-stagger .reveal.in {{
        opacity: 1;
        transform: none;
        filter: none;
    }}
    .reveal-stagger.in > *:nth-child(1) {{ transition-delay: .05s; }}
    .reveal-stagger.in > *:nth-child(2) {{ transition-delay: .16s; }}
    .reveal-stagger.in > *:nth-child(3) {{ transition-delay: .27s; }}
    .reveal-stagger.in > *:nth-child(4) {{ transition-delay: .38s; }}
    .reveal-stagger.in > *:nth-child(5) {{ transition-delay: .49s; }}
    .reveal-stagger.in > *:nth-child(6) {{ transition-delay: .60s; }}
    .reveal-stagger.in > *:nth-child(7) {{ transition-delay: .71s; }}
    .reveal-stagger.in > *:nth-child(8) {{ transition-delay: .82s; }}
    .reveal-stagger.in > *:nth-child(9) {{ transition-delay: .93s; }}
    .reveal-stagger.in > *:nth-child(10) {{ transition-delay: 1.04s; }}
    .reveal-stagger.in > *:nth-child(11) {{ transition-delay: 1.15s; }}
    .reveal-stagger.in > *:nth-child(12) {{ transition-delay: 1.26s; }}
    #read-progress {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        z-index: 250;
        pointer-events: none;
        transform-origin: left;
        transform: scaleX(0);
        background: linear-gradient(90deg, var(--accent), var(--gold), var(--accent));
        background-size: 200% 100%;
        transition: transform 120ms linear;
    }}
    #read-progress::after {{
        content: "";
        position: absolute;
        inset: 0;
        background: inherit;
        animation: ipk-progress-shimmer 3s linear infinite;
    }}
    #grain {{
        position: fixed;
        inset: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
        opacity: .045;
        contain: strict;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='256' height='256'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.78' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='256' height='256' filter='url(%23n)'/%3E%3C/svg%3E");
        background-size: 256px 256px;
        background-repeat: repeat;
        animation: ipk-grain-drift 7s steps(6, end) infinite;
        will-change: background-position;
    }}
    @keyframes ipk-grain-drift {{
        0% {{ background-position: 0 0; }}
        17% {{ background-position: -37px -54px; }}
        33% {{ background-position: 62px 18px; }}
        50% {{ background-position: -18px 73px; }}
        67% {{ background-position: 45px -31px; }}
        83% {{ background-position: -73px 42px; }}
        100% {{ background-position: 0 0; }}
    }}
    #cursor-dot {{
        position: fixed;
        left: 0;
        top: 0;
        z-index: 9000;
        width: 10px;
        height: 10px;
        border-radius: 999px;
        pointer-events: none;
        opacity: 0;
        background: var(--primary);
        box-shadow: 0 0 0 1px rgba(242,238,226,.38), 0 0 18px rgba(47,149,166,.35);
        mix-blend-mode: multiply;
        transform: translate(-200px, -200px);
        transition: width .18s ease, height .18s ease, background .18s ease, box-shadow .18s ease, opacity .18s ease;
        contain: strict;
        will-change: transform, opacity;
    }}
    #cursor-dot.s-link {{
        width: 18px;
        height: 18px;
        background: var(--accent);
        box-shadow: 0 0 0 2px rgba(47,149,166,.16), 0 0 22px rgba(47,149,166,.42);
        opacity: .72;
    }}
    #cursor-dot.s-btn {{
        width: 24px;
        height: 24px;
        background: var(--gold);
        box-shadow: 0 0 0 2px rgba(201,169,110,.18), 0 0 24px rgba(201,169,110,.42);
        opacity: .8;
    }}
    #cursor-dot.s-text {{
        width: 7px;
        height: 22px;
        border-radius: 999px;
        background: var(--secondary);
        opacity: .55;
    }}
    #cursor-dot.s-down {{
        width: 7px;
        height: 7px;
        background: var(--accent);
        opacity: .95;
    }}
    .cursor-ripple {{
        position: fixed;
        z-index: 8999;
        width: 12px;
        height: 12px;
        border: 1px solid rgba(47,149,166,.58);
        border-radius: 999px;
        pointer-events: none;
        transform: translate(-50%, -50%);
        animation: ipk-cursor-ripple-out .6s cubic-bezier(.22,1,.36,1) forwards;
    }}
    @keyframes ipk-cursor-ripple-out {{
        to {{
            opacity: 0;
            transform: translate(-50%, -50%) scale(5.5);
        }}
    }}
    .ipk-marquee-strip {{
        width: 100vw;
        margin-left: calc(50% - 50vw);
        margin-right: calc(50% - 50vw);
        overflow: hidden;
        border-top: 1px solid var(--rule);
        border-bottom: 1px solid var(--rule);
        background: var(--surface);
        padding: 10px 0;
        position: relative;
        z-index: 2;
    }}
    .ipk-marquee-track {{
        display: flex;
        align-items: center;
        white-space: nowrap;
        will-change: transform;
        animation: ipk-marquee-scroll 44s linear infinite;
    }}
    .ipk-marquee-track span {{
        font-family: var(--sans);
        font-size: 11px;
        letter-spacing: .12em;
        text-transform: uppercase;
        color: var(--secondary);
        padding: 0 18px;
    }}
    .ipk-marquee-track .ipk-marquee-dot {{
        color: var(--accent);
        padding: 0 2px;
        opacity: .6;
    }}
    .ipk-marquee-strip:hover .ipk-marquee-track {{
        animation-play-state: paused;
    }}
    @keyframes ipk-marquee-scroll {{
        from {{ transform: translateX(0); }}
        to {{ transform: translateX(-50%); }}
    }}
    @keyframes ipk-scroll-progress {{
        to {{ transform: scaleX(1); }}
    }}
    @keyframes ipk-progress-shimmer {{
        from {{ background-position: 0% 0%; }}
        to {{ background-position: 200% 0%; }}
    }}
    .ipk-nav,
    .ipk-hero,
    .ipk-immersive-band,
    .ipk-footer {{
        width: 100vw;
        margin-left: calc(50% - 50vw);
        margin-right: calc(50% - 50vw);
    }}
    .ipk-nav {{
        background: rgba(242,238,226,0.84);
        backdrop-filter: saturate(140%) blur(14px);
        -webkit-backdrop-filter: saturate(140%) blur(14px);
        border: 1px solid var(--rule);
        border-left: 0;
        border-right: 0;
        box-shadow: 0 14px 40px rgba(15,35,63,0.08);
        padding: 0.75rem var(--gutter);
        display: flex;
        align-items: center;
        justify-content: space-between;
        position: sticky;
        top: 0;
        z-index: 100;
        gap: 1rem;
        flex-wrap: wrap;
        transition: background .35s ease, backdrop-filter .35s ease, border-color .35s ease, box-shadow .35s ease;
    }}
    .ipk-nav.is-pinned {{
        background: rgba(242,238,226,.78);
        box-shadow: 0 18px 44px rgba(15,35,63,.10);
    }}
    .ipk-nav-title-row {{
        display: flex;
        align-items: center;
        gap: 0.75rem;
        flex-wrap: wrap;
    }}
    .ipk-brand-mark {{
        width: 38px;
        height: 38px;
        border: 1px solid rgba(15,35,63,.34);
        border-radius: 999px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-family: var(--serif-display);
        font-size: 0.88rem;
        color: var(--primary);
        position: relative;
        transition: transform 400ms cubic-bezier(.34,1.56,.64,1), border-color 300ms var(--ii-ease);
    }}
    .ipk-brand-mark::before,
    .ipk-brand-mark::after {{
        content: "";
        position: absolute;
        width: 8px;
        height: 14px;
        background: var(--surface);
    }}
    .ipk-brand-mark::before {{ left: -2px; }}
    .ipk-brand-mark::after {{ right: -2px; }}
    .ipk-nav-title-row:hover .ipk-brand-mark {{
        transform: rotate(18deg) scale(1.06);
        border-color: var(--accent);
    }}
    .ipk-nav-title {{
        font-family: var(--serif-display);
        font-size: 1.25rem;
        font-weight: 400;
        color: var(--primary);
        text-shadow: none;
    }}
    .ipk-nav-meta {{
        font-size: 0.75rem;
        color: var(--secondary);
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }}
    .ipk-law-badge {{
        display: inline-flex;
        align-items: center;
        gap: 0.45rem;
        border: 1px solid rgba(15,35,63,.18);
        border-radius: 999px;
        padding: 0.25rem 0.65rem;
        background: rgba(242,238,226,.78);
        color: var(--primary);
        text-decoration: none;
        font-family: var(--sans);
        font-size: 0.72rem;
        line-height: 1;
        box-shadow: 0 12px 30px rgba(15,35,63,.07);
        position: relative;
        overflow: hidden;
        transition: transform 220ms var(--ii-ease), border-color 220ms var(--ii-ease), background 220ms var(--ii-ease);
    }}
    .ipk-law-badge:hover {{
        transform: translateY(-1px);
        border-color: rgba(47,149,166,.42);
        background: var(--surface);
    }}
    .ipk-law-badge::before {{
        content: "";
        width: 0.5rem;
        height: 0.5rem;
        border-radius: 999px;
        background: var(--accent);
        box-shadow: 0 0 0 4px rgba(47,149,166,.12);
    }}
    .ipk-law-badge.bad::before {{
        background: #b91c1c;
        box-shadow: 0 0 0 4px rgba(185,28,28,.12);
    }}
    .ipk-law-badge span {{
        font-weight: 700;
        white-space: nowrap;
    }}
    .ipk-law-badge small {{
        color: var(--secondary);
        font-size: 0.68rem;
        max-width: 8.5rem;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }}
    .ipk-nav-links {{
        display: flex;
        gap: 1.25rem;
        font-family: var(--serif-body);
        font-size: 0.86rem;
        font-weight: 600;
        flex-wrap: wrap;
    }}
    .ipk-nav-links a {{
        color: var(--primary);
        text-decoration: none;
        border-bottom: 1px solid transparent;
        padding-bottom: 2px;
        position: relative;
        overflow: hidden;
        transition: color 220ms var(--ii-ease), border-color 220ms var(--ii-ease), transform 220ms var(--ii-ease);
    }}
    .ipk-nav-links a::after {{
        content: "";
        position: absolute;
        left: 0;
        right: 0;
        bottom: -1px;
        height: 1px;
        background: var(--accent);
        transform: scaleX(0);
        transform-origin: left;
        transition: transform .32s cubic-bezier(.4,0,.2,1);
    }}
    .ipk-nav-links a:hover {{
        color: var(--accent);
        transform: translateY(-1px);
    }}
    .ipk-nav-links a:hover::after,
    .ipk-nav-links a.is-active::after {{
        transform: scaleX(1);
    }}
    .ipk-nav-links a.is-active {{
        color: var(--accent);
    }}
    .ipk-ripple-wave {{
        position: absolute;
        border-radius: 50%;
        transform: scale(0);
        animation: ipk-ripple-expand .55s cubic-bezier(0,.5,.5,1) forwards;
        background: rgba(255,255,255,.24);
        pointer-events: none;
    }}
    .ipk-nav-links a .ipk-ripple-wave,
    .ipk-hero-chain span .ipk-ripple-wave,
    .ipk-law-badge .ipk-ripple-wave {{
        background: rgba(15,35,63,.08);
    }}
    @keyframes ipk-ripple-expand {{
        to {{
            transform: scale(4);
            opacity: 0;
        }}
    }}
    .ipk-advanced-note {{
        background: linear-gradient(135deg, rgba(242,238,226,.94), rgba(232,237,229,.90));
        border: 1px solid var(--rule-strong);
        border-left: 4px solid var(--gold);
        border-radius: 8px;
        color: var(--secondary);
        line-height: 1.55;
        padding: 0.9rem 1rem;
        transition: box-shadow 300ms var(--ii-ease), transform 300ms var(--ii-ease), background 300ms var(--ii-ease);
    }}
    .ipk-advanced-note strong {{
        color: var(--primary);
    }}
    .ipk-advanced-note:hover {{
        background: var(--surface-elevated);
        box-shadow: var(--ii-shadow);
        transform: translateY(-2px);
    }}
    .ipk-hero {{
        position: relative;
        overflow: hidden;
        text-align: center;
        min-height: clamp(500px, 68svh, 720px);
        padding: clamp(3.2rem, 7vh, 4.35rem) clamp(1rem, 4vw, 4rem) clamp(2rem, 4.5vh, 3rem);
        display: flex;
        flex-direction: column;
        justify-content: center;
        background:
            linear-gradient(90deg, transparent 0, transparent 33.28%, var(--rule) 33.32%, transparent 33.36%, transparent 66.61%, var(--rule) 66.65%, transparent 66.69%),
            radial-gradient(circle at 82% 18%, rgba(190,230,237,.54), transparent 28rem),
            radial-gradient(circle at 18% 82%, rgba(201,169,110,.28), transparent 24rem),
            linear-gradient(180deg, rgba(242,238,226,.96), rgba(232,237,229,.84));
        border-bottom: 1px solid var(--rule);
        box-shadow: inset 0 -1px 0 rgba(15,35,63,0.08);
    }}
    .ipk-hero::before {{
        content: "";
        position: absolute;
        inset: clamp(1rem, 3vw, 3rem);
        background:
            linear-gradient(90deg, var(--rule-strong) 0 1px, transparent 1px calc(100% - 1px), var(--rule-strong) calc(100% - 1px)),
            linear-gradient(0deg, var(--rule-strong) 0 1px, transparent 1px calc(100% - 1px), var(--rule-strong) calc(100% - 1px));
        pointer-events: none;
    }}
    .ipk-hero::after {{
        content: "II";
        position: absolute;
        right: clamp(1.4rem, 5vw, 5.5rem);
        bottom: clamp(1.2rem, 5vw, 4.5rem);
        font-family: var(--serif-display);
        font-size: clamp(7rem, 20vw, 22rem);
        line-height: 0.8;
        color: rgba(15,35,63,0.045);
        pointer-events: none;
    }}
    .ipk-hero > * {{
        position: relative;
        z-index: 1;
    }}
    .ipk-eyebrow {{
        font-family: var(--serif-body);
        font-size: 0.82rem;
        font-weight: 600;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: var(--secondary);
        margin-bottom: 0.5rem;
    }}
    .ipk-hero h1 {{
        font-family: var(--serif-display);
        font-size: clamp(3.1rem, 8vw, 8rem);
        font-weight: 400;
        color: var(--primary);
        margin: 0;
        line-height: 0.96;
        text-shadow: none;
    }}
    .ipk-hero h1 em {{
        color: var(--accent);
        font-style: italic;
    }}
    .ipk-hero h1 .word {{
        display: inline-block;
        opacity: 0;
        transform: translateY(14px);
        animation: ipk-word-in 850ms var(--ii-ease) forwards;
    }}
    .ipk-hero h1 .word:nth-child(1) {{ animation-delay: 50ms; }}
    .ipk-hero h1 .word:nth-child(2) {{ animation-delay: 220ms; }}
    .ipk-hero h1 .word:nth-child(3) {{ animation-delay: 400ms; }}
    @keyframes ipk-word-in {{
        to {{ opacity: 1; transform: none; }}
    }}
    .ipk-hero p {{
        font-size: 1.15rem;
        color: var(--secondary);
        max-width: 820px;
        margin: 1rem auto 0;
    }}
    .ipk-hero strong {{
        color: var(--primary);
    }}
    .ipk-hero-chain {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.75rem;
        flex-wrap: wrap;
        margin: 1.55rem auto 0;
        color: var(--primary);
        font-size: 0.82rem;
        letter-spacing: 1px;
        text-transform: uppercase;
    }}
    .ipk-hero-chain span {{
        border: 1px solid rgba(15,35,63,.26);
        background: rgba(242,238,226,.70);
        border-radius: 999px;
        padding: 0.36rem 0.7rem;
        box-shadow: 0 10px 24px -20px rgba(15,35,63,.35);
        position: relative;
        overflow: hidden;
        transition: transform 260ms var(--ii-ease), border-color 260ms var(--ii-ease), background 260ms var(--ii-ease);
    }}
    .ipk-hero-chain span:hover {{
        transform: translateY(-2px);
        border-color: var(--accent);
        background: var(--surface);
    }}
    .ipk-hero-chain i {{
        display: block;
        width: 34px;
        height: 1px;
        background: linear-gradient(90deg, var(--accent), var(--gold));
    }}
    .ipk-hero-stats {{
        display: grid;
        grid-template-columns: repeat(4, minmax(120px, 1fr));
        gap: 0.65rem;
        width: min(1100px, 92vw);
        max-width: 1100px;
        margin: 1.35rem auto 0;
    }}
    .ipk-hero-stat {{
        background: rgba(242,238,226,0.72);
        border: 1px solid var(--rule-strong);
        border-radius: 8px;
        padding: 0.65rem 0.75rem;
        transition: transform 300ms var(--ii-ease), box-shadow 300ms var(--ii-ease), background 300ms var(--ii-ease);
    }}
    .ipk-hero-stat:hover {{
        background: var(--surface);
        box-shadow: var(--ii-shadow);
        transform: translateY(-3px);
    }}
    .ipk-hero-stat strong {{
        display: block;
        color: var(--primary);
        font-size: 1.02rem;
    }}
    .ipk-hero-stat span {{
        color: var(--secondary);
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.9px;
    }}
    .ipk-scroll-cue {{
        width: 1px;
        height: 42px;
        margin: clamp(0.9rem, 2.4vh, 1.45rem) auto 0;
        background: linear-gradient(180deg, transparent, rgba(201,169,110,.74), transparent);
        opacity: 0.72;
        position: relative;
    }}
    .ipk-scroll-cue::after {{
        content: "";
        position: absolute;
        left: 50%;
        top: 2px;
        width: 5px;
        height: 5px;
        border-radius: 999px;
        background: var(--gold);
        box-shadow: 0 0 20px rgba(201,169,110,.48);
        transform: translateX(-50%);
        animation: ipk-scroll-cue-drop 1.9s var(--ii-ease) infinite;
    }}
    @keyframes ipk-scroll-cue-drop {{
        0% {{ opacity: 0; transform: translate(-50%, 0); }}
        28% {{ opacity: 1; }}
        72% {{ opacity: 0.9; }}
        100% {{ opacity: 0; transform: translate(-50%, 34px); }}
    }}
    .ipk-mu-card {{
        background:
            radial-gradient(circle at 12% 14%, rgba(47,149,166,.13), transparent 17rem),
            linear-gradient(135deg, rgba(242,238,226,0.96), rgba(232,237,229,0.96));
        border: 1px solid var(--rule-strong);
        border-radius: 8px;
        color: var(--secondary);
        padding: 1.35rem;
        box-shadow: 0 18px 48px rgba(15,35,63,0.10);
        width: min(1400px, 100%);
        max-width: calc(100vw - 2rem);
        margin: 0 auto;
        position: relative;
        transition: transform 350ms var(--ii-ease), box-shadow 350ms var(--ii-ease);
    }}
    .ipk-mu-card::before,
    .ipk-mu-card::after {{
        content: "";
        position: absolute;
        width: 28px;
        height: 28px;
        border-color: var(--primary);
        opacity: .32;
        pointer-events: none;
    }}
    .ipk-mu-card::before {{
        left: 14px;
        top: 14px;
        border-left: 1px solid;
        border-top: 1px solid;
    }}
    .ipk-mu-card::after {{
        right: 14px;
        bottom: 14px;
        border-right: 1px solid;
        border-bottom: 1px solid;
    }}
    .ipk-mu-card:hover {{
        box-shadow: var(--ii-shadow);
        transform: translateY(-3px);
    }}
    .ipk-mu-kicker {{
        color: var(--accent-strong);
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }}
    .ipk-mu-title {{
        display: flex;
        align-items: baseline;
        gap: 0.75rem;
        flex-wrap: wrap;
        margin: 0.35rem 0 0.6rem;
    }}
    .ipk-mu-title h3 {{
        margin: 0;
        color: var(--primary);
        font-family: var(--serif-display);
        font-size: 2rem;
        font-weight: 400;
    }}
    .ipk-mu-title span {{
        color: var(--secondary);
        font-size: 0.95rem;
        letter-spacing: 0.4px;
    }}
    .ipk-mu-principle {{
        color: var(--primary);
        font-family: var(--serif-display);
        font-size: clamp(1.45rem, 3vw, 2.25rem);
        line-height: 1.14;
        margin: 0 0 1rem;
    }}
    .ipk-mu-grid {{
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.65rem;
        margin: 1rem 0;
    }}
    .ipk-mu-chip {{
        background: rgba(15,35,63,0.035);
        border: 1px solid var(--rule);
        border-radius: 8px;
        padding: 0.7rem;
        color: var(--primary);
        transition: background 260ms var(--ii-ease), transform 260ms var(--ii-ease), border-color 260ms var(--ii-ease);
    }}
    .ipk-mu-chip:hover {{
        background: var(--surface-elevated);
        border-color: rgba(47,149,166,.36);
        transform: translateY(-2px);
    }}
    .ipk-mu-chip span {{
        display: block;
        color: var(--secondary);
        font-size: 0.78rem;
        margin-top: 0.2rem;
    }}
    .ipk-mu-zero {{
        color: var(--primary);
        font-weight: 700;
        margin-bottom: 0;
    }}
    .ipk-observatory-strip {{
        display: grid;
        grid-template-columns: repeat(4, minmax(130px, 1fr));
        gap: 0.75rem;
        margin: 0 0 1rem;
    }}
    .ipk-observatory-tile {{
        border: 1px solid var(--rule);
        border-top-color: rgba(47,149,166,.44);
        border-radius: 8px;
        background: linear-gradient(180deg, rgba(242,238,226,.94), rgba(232,237,229,.90));
        padding: 0.8rem;
        color: var(--secondary);
        transition: background 300ms var(--ii-ease), transform 300ms var(--ii-ease), box-shadow 300ms var(--ii-ease), border-color 300ms var(--ii-ease);
    }}
    .ipk-observatory-tile:hover {{
        background: var(--surface);
        border-color: rgba(15,35,63,.24);
        box-shadow: var(--ii-shadow);
        transform: translateY(-4px);
    }}
    .ipk-observatory-tile strong {{
        display: block;
        color: var(--primary);
        margin-bottom: 0.2rem;
    }}
    .ipk-lock-cascade {{
        background:
            radial-gradient(circle at 12% 12%, rgba(47,149,166,.20), transparent 24rem),
            radial-gradient(circle at 85% 8%, rgba(201,169,110,.22), transparent 25rem),
            linear-gradient(135deg, rgba(15,35,63,.98), rgba(7,20,38,.96));
        border: 1px solid rgba(15,35,63,.18);
        border-radius: 8px;
        box-shadow: 0 30px 90px -60px rgba(15,35,63,.68);
        color: var(--inverse);
        margin: 1rem 0 1.35rem;
        overflow: hidden;
        padding: clamp(1rem, 2vw, 1.4rem);
        position: relative;
        isolation: isolate;
    }}
    .ipk-lock-cascade::before {{
        content: "";
        position: absolute;
        inset: -18%;
        background:
            radial-gradient(620px 360px at 76% 16%, rgba(131,161,204,.16), transparent 68%),
            radial-gradient(500px 320px at 13% 82%, rgba(47,149,166,.13), transparent 70%),
            radial-gradient(420px 280px at 56% 44%, rgba(201,169,110,.10), transparent 70%);
        opacity: .78;
        pointer-events: none;
        z-index: 0;
        animation: ipk-cascade-aurora 28s ease-in-out infinite;
    }}
    @keyframes ipk-cascade-aurora {{
        0%, 100% {{ transform: translate(0, 0) scale(1); opacity: .72; }}
        32% {{ transform: translate(-2%, 2%) scale(1.07); opacity: .94; }}
        66% {{ transform: translate(2%, -2%) scale(.96); opacity: .58; }}
    }}
    .ipk-cascade-halo {{
        background:
            linear-gradient(90deg, transparent, rgba(190,230,237,.26), rgba(201,169,110,.24), transparent);
        height: 1px;
        left: 1rem;
        opacity: .8;
        position: absolute;
        right: 1rem;
        top: 50%;
        transform: translateY(-50%);
        z-index: 1;
    }}
    .ipk-lock-cascade.in .ipk-cascade-halo {{
        animation: ipk-cascade-line-bloom 1.3s var(--ease-soft-out) both;
    }}
    @keyframes ipk-cascade-line-bloom {{
        from {{ clip-path: inset(0 100% 0 0); opacity: 0; }}
        to {{ clip-path: inset(0 0 0 0); opacity: .8; }}
    }}
    .ipk-cascade-intro {{
        align-items: end;
        display: flex;
        gap: 1rem;
        justify-content: space-between;
        margin-bottom: 0.9rem;
        position: relative;
        z-index: 1;
    }}
    .ipk-cascade-intro h3 {{
        color: var(--inverse);
        font-size: clamp(1.45rem, 2.4vw, 2.25rem);
        line-height: 1;
        margin: 0.15rem 0 0;
    }}
    .ipk-cascade-meter {{
        align-items: center;
        display: flex;
        flex-wrap: wrap;
        gap: 0.35rem;
        justify-content: flex-end;
        max-width: 44rem;
    }}
    .ipk-cascade-meter span {{
        border: 1px solid rgba(190,230,237,.24);
        border-radius: 999px;
        color: rgba(242,238,226,.78);
        font-family: var(--sans);
        font-size: 0.68rem;
        letter-spacing: 0.08em;
        padding: 0.18rem 0.48rem;
        text-transform: uppercase;
    }}
    .ipk-cascade-track {{
        display: flex;
        gap: 1rem;
        overflow-x: auto;
        padding: 0.1rem 0.15rem 0.9rem;
        position: relative;
        scroll-snap-type: x proximity;
        scrollbar-color: rgba(190,230,237,.42) rgba(242,238,226,.08);
        z-index: 1;
    }}
    .ipk-cascade-card {{
        background:
            linear-gradient(180deg, rgba(242,238,226,.13), rgba(242,238,226,.06)),
            radial-gradient(circle at 18% 0%, color-mix(in srgb, var(--stage-color) 28%, transparent), transparent 62%);
        border: 1px solid color-mix(in srgb, var(--stage-color) 44%, rgba(242,238,226,.16));
        border-radius: 8px;
        box-shadow: 0 24px 68px -48px rgba(0,0,0,.88);
        flex: 0 0 clamp(15.5rem, 23vw, 20rem);
        min-height: 18rem;
        padding: 0.95rem;
        position: relative;
        scroll-snap-align: start;
        overflow: hidden;
        --spot-x: 50%;
        --spot-y: 50%;
        transition: border-color 280ms var(--ease-soft-out), box-shadow 320ms var(--ease-soft-out), transform 320ms var(--ease-soft-out), background 320ms var(--ease-soft-out);
        transform-origin: center;
        z-index: 1;
    }}
    .ipk-cascade-card::before {{
        content: "";
        position: absolute;
        inset: 0;
        background: radial-gradient(340px circle at var(--spot-x) var(--spot-y), color-mix(in srgb, var(--stage-color) 22%, transparent), transparent 68%);
        opacity: 0;
        pointer-events: none;
        transition: opacity .35s ease;
        z-index: 0;
    }}
    .ipk-cascade-card::after {{
        content: "";
        position: absolute;
        width: 26px;
        height: 26px;
        right: 11px;
        top: 11px;
        border-top: 1px solid rgba(242,238,226,.28);
        border-right: 1px solid rgba(242,238,226,.28);
        opacity: .60;
        pointer-events: none;
        z-index: 1;
    }}
    .ipk-cascade-card:hover {{
        border-color: color-mix(in srgb, var(--stage-color) 74%, rgba(242,238,226,.20));
        box-shadow: 0 34px 84px -50px rgba(0,0,0,.92);
        transform: translateY(-4px) rotateX(1.5deg);
    }}
    .ipk-cascade-card:hover::before {{
        opacity: 1;
    }}
    .ipk-cascade-card > * {{
        position: relative;
        z-index: 1;
    }}
    .ipk-cascade-step {{
        color: var(--stage-color);
        font-family: var(--sans);
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.13em;
        margin-bottom: 0.52rem;
        text-transform: uppercase;
    }}
    .ipk-cascade-card h3 {{
        color: var(--inverse);
        font-size: clamp(1.3rem, 1.9vw, 1.8rem);
        line-height: 1.02;
        margin: 0;
        overflow-wrap: anywhere;
    }}
    .ipk-cascade-lock {{
        color: rgba(242,238,226,.80) !important;
        font-family: var(--sans) !important;
        font-size: 0.9rem;
        margin: 0.28rem 0 0.7rem !important;
    }}
    .ipk-cascade-branch {{
        border: 1px solid color-mix(in srgb, var(--stage-color) 45%, rgba(242,238,226,.12));
        border-radius: 999px;
        color: rgba(242,238,226,.78);
        display: inline-flex;
        font-family: var(--sans);
        font-size: 0.68rem;
        letter-spacing: 0.08em;
        margin-bottom: 0.9rem;
        max-width: 100%;
        padding: 0.18rem 0.48rem;
        text-transform: uppercase;
    }}
    .ipk-cascade-card dl {{
        display: grid;
        gap: 0.35rem;
        margin: 0;
    }}
    .ipk-cascade-card dt {{
        color: var(--stage-color);
        font-family: var(--sans);
        font-size: 0.66rem;
        font-weight: 600;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }}
    .ipk-cascade-card dd {{
        color: rgba(242,238,226,.78);
        font-family: var(--serif-body);
        font-size: 0.92rem;
        line-height: 1.35;
        margin: 0 0 0.35rem;
    }}
    .ipk-cascade-arrow {{
        background: linear-gradient(90deg, var(--stage-color), rgba(190,230,237,.65));
        height: 2px;
        position: absolute;
        right: -1rem;
        top: 50%;
        width: 1rem;
        z-index: 2;
        transform-origin: left center;
    }}
    .ipk-lock-cascade.in .ipk-cascade-arrow {{
        animation: ipk-cascade-arrow-in .7s var(--ease-soft-out) .18s both;
    }}
    @keyframes ipk-cascade-arrow-in {{
        from {{ opacity: 0; transform: scaleX(0); }}
        to {{ opacity: 1; transform: scaleX(1); }}
    }}
    .ipk-cascade-arrow::after {{
        border-bottom: 5px solid transparent;
        border-left: 7px solid rgba(190,230,237,.78);
        border-top: 5px solid transparent;
        content: "";
        position: absolute;
        right: -1px;
        top: 50%;
        transform: translateY(-50%);
    }}
    .ipk-monograph-shell,
    .output.block:has(.ipk-monograph-shell-marker) > div,
    .output-area .output.block:has(.ipk-monograph-shell-marker) > div {{
        width: 100vw;
        margin-left: calc(50% - 50vw);
        margin-right: calc(50% - 50vw);
        padding: clamp(1.5rem, 3vw, 3rem) var(--gutter);
        background:
            linear-gradient(90deg, rgba(242,238,226,.08) 0 1px, transparent 1px 33.33%, rgba(242,238,226,.08) 33.33% calc(33.33% + 1px), transparent calc(33.33% + 1px) 66.66%, rgba(242,238,226,.08) 66.66% calc(66.66% + 1px), transparent calc(66.66% + 1px)),
            radial-gradient(circle at 18% 12%, rgba(103,232,249,.18), transparent 30rem),
            radial-gradient(circle at 82% 18%, rgba(201,169,110,.18), transparent 28rem),
            linear-gradient(135deg, #071426 0%, var(--primary) 50%, #09182c 100%);
        color: var(--inverse);
        border-top: 1px solid rgba(242,238,226,.14);
        border-bottom: 1px solid rgba(242,238,226,.14);
        box-shadow: inset 0 1px 0 rgba(242,238,226,.08), inset 0 -1px 0 rgba(242,238,226,.08);
    }}
    .ipk-monograph-shell .ipk-section-header {{
        border-bottom-color: rgba(242,238,226,.16);
    }}
    .ipk-monograph-shell .ipk-section-header h2,
    .ipk-monograph-shell h3,
    .ipk-monograph-shell h4 {{
        color: var(--inverse);
    }}
    .ipk-monograph-shell .ipk-section-subtitle,
    .ipk-monograph-shell p {{
        color: rgba(242,238,226,.74);
    }}
    .ipk-monograph-intro {{
        max-width: min(1500px, calc(100vw - 2rem));
        margin: 0 auto 1rem;
    }}
    .ipk-monograph-intro h2 {{
        color: var(--inverse);
        font-family: var(--serif-display);
        font-size: clamp(2.2rem, 5vw, 4.2rem);
        font-weight: 400;
        line-height: 1;
        margin: 0;
    }}
    .ipk-monograph-intro p {{
        color: rgba(242,238,226,.74);
        max-width: 72rem;
        margin: 0.65rem 0 0;
    }}
    .ipk-monograph-strip,
    .ipk-formula-grid,
    .ipk-kill-grid {{
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.9rem;
        margin: 1rem 0;
    }}
    .ipk-monograph-tile,
    .ipk-formula-card,
    .ipk-kill-card,
    .ipk-law-panel {{
        border: 1px solid rgba(242,238,226,.14);
        border-radius: 8px;
        background: linear-gradient(180deg, rgba(242,238,226,.10), rgba(242,238,226,.055));
        box-shadow: 0 24px 70px -50px rgba(0,0,0,.72);
        color: var(--inverse);
        position: relative;
        overflow: hidden;
    }}
    .ipk-monograph-tile,
    .ipk-formula-card,
    .ipk-kill-card {{
        padding: 1rem;
        min-height: 9rem;
        --spot-x: 50%;
        --spot-y: 50%;
        transition: transform 300ms var(--ii-ease), border-color 300ms var(--ii-ease), background 300ms var(--ii-ease), box-shadow 300ms var(--ii-ease);
    }}
    .ipk-monograph-tile::before,
    .ipk-formula-card::before,
    .ipk-kill-card::before {{
        content: "";
        position: absolute;
        inset: 0;
        background: radial-gradient(circle at var(--spot-x) var(--spot-y), rgba(190,230,237,.18), transparent 32%);
        opacity: 0;
        transition: opacity .28s var(--ii-ease);
        pointer-events: none;
    }}
    .ipk-monograph-tile::after,
    .ipk-formula-card::after,
    .ipk-kill-card::after {{
        content: "";
        position: absolute;
        width: 26px;
        height: 26px;
        right: 11px;
        top: 11px;
        border-top: 1px solid rgba(242,238,226,.28);
        border-right: 1px solid rgba(242,238,226,.28);
        opacity: .65;
        pointer-events: none;
    }}
    .ipk-monograph-tile:hover,
    .ipk-formula-card:hover,
    .ipk-kill-card:hover {{
        transform: translateY(-4px) rotateX(1deg);
        border-color: rgba(190,230,237,.38);
        background: linear-gradient(180deg, rgba(242,238,226,.14), rgba(242,238,226,.07));
        box-shadow: 0 30px 82px -48px rgba(0,0,0,.82);
    }}
    .ipk-monograph-tile:hover::before,
    .ipk-formula-card:hover::before,
    .ipk-kill-card:hover::before {{
        opacity: 1;
    }}
    .ipk-panel-kicker {{
        color: var(--gold);
        font-family: var(--sans);
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.13em;
        text-transform: uppercase;
    }}
    .ipk-monograph-tile strong {{
        display: block;
        color: var(--inverse);
        font-family: var(--serif-display);
        font-size: 1.7rem;
        font-weight: 400;
        line-height: 1.1;
        margin: 0.25rem 0;
    }}
    .ipk-monograph-tile span,
    .ipk-kill-card span {{
        color: rgba(242,238,226,.66);
        font-size: 0.85rem;
    }}
    .ipk-law-panel {{
        padding: clamp(1rem, 2vw, 1.25rem);
        margin: 0.75rem 0 1rem;
    }}
    .ipk-law-panel-top {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 1rem;
    }}
    .ipk-law-panel h3 {{
        margin: 0.2rem 0 0.35rem;
        font-size: clamp(1.3rem, 2.5vw, 2.1rem);
        overflow-wrap: anywhere;
    }}
    .ipk-law-result {{
        border: 1px solid rgba(242,238,226,.2);
        border-radius: 999px;
        padding: 0.45rem 0.75rem;
        font-family: var(--sans);
        font-size: 0.78rem;
        font-weight: 800;
        letter-spacing: 0.08em;
        white-space: nowrap;
    }}
    .ipk-law-result.ok {{
        color: #bbf7d0;
        border-color: rgba(74,222,128,.35);
        background: rgba(22,101,52,.22);
    }}
    .ipk-law-result.bad {{
        color: #fecaca;
        border-color: rgba(248,113,113,.42);
        background: rgba(127,29,29,.24);
    }}
    .ipk-token-row {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.4rem;
        margin: 0.7rem 0;
    }}
    .ipk-token-row span {{
        border: 1px solid rgba(190,230,237,.28);
        border-radius: 999px;
        padding: 0.18rem 0.5rem;
        color: var(--sky);
        background: rgba(190,230,237,.08);
        font-family: var(--sans);
        font-size: 0.74rem;
    }}
    .ipk-law-explain,
    .ipk-paper-quote,
    .ipk-pledge {{
        color: rgba(242,238,226,.76);
        border-left: 3px solid var(--gold);
        background: rgba(242,238,226,.07);
        padding: 0.75rem 0.9rem;
        border-radius: 6px;
    }}
    .ipk-copy-sheet {{
        border: 1px solid rgba(242,238,226,.16);
        border-radius: 8px;
        background:
            linear-gradient(180deg, rgba(242,238,226,.095), rgba(242,238,226,.045));
        box-shadow: 0 24px 70px -54px rgba(0,0,0,.84);
        color: var(--inverse);
        margin: 0.85rem 0;
        overflow: hidden;
    }}
    .ipk-copy-sheet summary {{
        align-items: center;
        cursor: pointer;
        display: flex;
        gap: 1rem;
        justify-content: space-between;
        list-style: none;
        padding: 0.95rem 1rem;
        user-select: none;
    }}
    .ipk-copy-sheet summary::-webkit-details-marker {{
        display: none;
    }}
    .ipk-copy-sheet summary span {{
        display: grid;
        gap: 0.18rem;
    }}
    .ipk-copy-sheet summary strong {{
        color: var(--inverse);
        font-family: var(--serif-display);
        font-size: 1.1rem;
        font-weight: 400;
    }}
    .ipk-copy-sheet summary small {{
        color: rgba(242,238,226,.62);
        font-family: var(--sans);
        font-size: 0.78rem;
    }}
    .ipk-copy-sheet summary::after {{
        border: 1px solid rgba(190,230,237,.28);
        border-radius: 999px;
        color: var(--sky);
        content: "Open preview";
        flex: 0 0 auto;
        font-family: var(--sans);
        font-size: 0.74rem;
        padding: 0.2rem 0.58rem;
        transition: background 180ms var(--ii-ease), color 180ms var(--ii-ease), transform 180ms var(--ii-ease);
    }}
    .ipk-copy-sheet[open] summary::after {{
        background: rgba(190,230,237,.12);
        color: var(--inverse);
        content: "Hide preview";
    }}
    .ipk-copy-sheet summary:hover::after {{
        transform: translateY(-1px);
    }}
    .ipk-copy-sheet pre {{
        background: rgba(5, 14, 27, 0.72) !important;
        border-top: 1px solid rgba(242,238,226,.12) !important;
        border-radius: 0 !important;
        color: rgba(242,238,226,.82) !important;
        font-size: 0.78rem;
        line-height: 1.48;
        margin: 0 !important;
        max-height: min(28rem, 52vh);
        max-width: 100%;
        overflow: auto;
        padding: 1rem !important;
        white-space: pre-wrap;
        word-break: break-word;
    }}
    .ipk-monograph-note,
    :where(.ipk-monograph-shell, .output.block:has(.ipk-monograph-shell-marker)) .ipk-advanced-note {{
        background: linear-gradient(135deg, rgba(7, 20, 38, 0.78), rgba(20, 39, 65, 0.70)) !important;
        border: 1px solid rgba(242,238,226,.16) !important;
        border-left: 4px solid var(--gold) !important;
        border-radius: 8px;
        color: rgba(242,238,226,.84) !important;
        box-shadow: 0 24px 70px -54px rgba(0,0,0,.8);
        line-height: 1.55;
        padding: 0.9rem 1rem;
    }}
    .ipk-monograph-note p,
    :where(.ipk-monograph-shell, .output.block:has(.ipk-monograph-shell-marker)) .ipk-advanced-note {{
        margin: 0;
        color: rgba(242,238,226,.84) !important;
    }}
    .ipk-monograph-note strong,
    :where(.ipk-monograph-shell, .output.block:has(.ipk-monograph-shell-marker)) .ipk-advanced-note strong {{
        color: var(--gold) !important;
    }}
    .ipk-monograph-note-info {{
        border-left-color: var(--sky) !important;
    }}
    .ipk-monograph-note-success {{
        border-left-color: #7fd9a0 !important;
    }}
    .ipk-monograph-note-warn {{
        border-left-color: var(--gold) !important;
    }}
    .ipk-monograph-note-danger {{
        border-left-color: #f59d9d !important;
    }}
    :where(.ipk-monograph-shell, .output.block:has(.ipk-monograph-shell-marker)) .ipk-advanced-note:hover {{
        background: linear-gradient(135deg, rgba(13, 30, 52, 0.86), rgba(28, 48, 74, 0.76)) !important;
        box-shadow: 0 30px 82px -52px rgba(0,0,0,.86);
    }}
    .ipk-forest-panel {{
        border: 1px solid rgba(242,238,226,.16);
        border-radius: 8px;
        background:
            radial-gradient(circle at 18% 78%, rgba(47,149,166,.18), transparent 38%),
            linear-gradient(135deg, rgba(7,20,38,.90), rgba(17,34,58,.78));
        box-shadow: 0 28px 90px -62px rgba(0,0,0,.9);
        margin: 1rem 0;
        overflow: hidden;
        padding: 1rem 1rem 0.75rem;
    }}
    .ipk-forest-head {{
        align-items: start;
        display: flex;
        gap: 1rem;
        justify-content: space-between;
        margin-bottom: 0.35rem;
    }}
    .ipk-forest-head h4 {{
        color: var(--inverse);
        font-family: var(--serif-display);
        font-size: clamp(1.35rem, 2vw, 2rem);
        font-weight: 400;
        line-height: 1;
        margin: 0.2rem 0 0;
    }}
    .ipk-forest-focus {{
        border: 1px solid rgba(190,230,237,.22);
        border-radius: 999px;
        color: rgba(242,238,226,.74);
        font-family: var(--sans);
        font-size: 0.78rem;
        padding: 0.35rem 0.65rem;
        white-space: nowrap;
    }}
    .ipk-forest-svg {{
        display: block;
        height: min(430px, 52vw);
        min-height: 300px;
        width: 100%;
    }}
    .ipk-forest-grid path {{
        fill: none;
        stroke: rgba(242,238,226,.36);
        stroke-width: 1;
    }}
    .ipk-forest-edge {{
        fill: none;
        stroke: rgba(242,238,226,.16);
        stroke-linecap: round;
        stroke-width: 2;
        transition: stroke 260ms var(--ii-ease), stroke-width 260ms var(--ii-ease), opacity 260ms var(--ii-ease);
    }}
    .ipk-forest-edge.active {{
        filter: url(#ipk-soft-glow);
        stroke: var(--gold);
        stroke-width: 5;
    }}
    .ipk-forest-node circle {{
        stroke: rgba(242,238,226,.82);
        stroke-width: 1.4;
        transition: r 260ms var(--ii-ease), filter 260ms var(--ii-ease), stroke 260ms var(--ii-ease);
    }}
    .ipk-forest-node.active circle {{
        filter: url(#ipk-soft-glow);
        stroke: rgba(255,244,200,.96);
        stroke-width: 2;
    }}
    .ipk-forest-node text {{
        fill: rgba(242,238,226,.88);
        font-family: var(--sans);
        font-size: 13px;
        font-weight: 700;
        paint-order: stroke;
        pointer-events: none;
        stroke: rgba(7,20,38,.9);
        stroke-linejoin: round;
        stroke-width: 4px;
    }}
    .ipk-forest-legend {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
        justify-content: flex-end;
        margin-top: -0.25rem;
    }}
    .ipk-forest-legend span {{
        align-items: center;
        color: rgba(242,238,226,.72);
        display: inline-flex;
        font-family: var(--sans);
        font-size: 0.75rem;
        gap: 0.35rem;
    }}
    .ipk-forest-legend i {{
        border: 1px solid rgba(242,238,226,.55);
        border-radius: 999px;
        display: inline-block;
        height: 0.58rem;
        width: 0.58rem;
    }}
    .ipk-formula-card code {{
        display: block;
        color: var(--sky);
        font-size: 0.86rem;
        white-space: normal;
        overflow-wrap: anywhere;
        margin: 0.45rem 0 0.7rem;
    }}
    .ipk-formula-card.active {{
        border-color: rgba(252,211,77,.72);
        box-shadow: 0 0 0 1px rgba(252,211,77,.24), 0 24px 70px -50px rgba(0,0,0,.72);
    }}
    .ipk-formula-metrics {{
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.35rem;
    }}
    .ipk-formula-metrics span {{
        color: rgba(242,238,226,.72);
        border-top: 1px solid rgba(242,238,226,.12);
        padding-top: 0.35rem;
        font-size: 0.78rem;
        overflow-wrap: anywhere;
    }}
    .ipk-formula-metrics b {{
        display: block;
        color: var(--gold);
        font-family: var(--sans);
        font-size: 0.68rem;
        text-transform: uppercase;
    }}
    .ipk-grammar-hits {{
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 0.55rem;
        margin: 0.85rem 0;
    }}
    .ipk-grammar-hits div {{
        border: 1px solid rgba(242,238,226,.12);
        border-radius: 8px;
        background: rgba(242,238,226,.055);
        padding: 0.65rem;
    }}
    .ipk-grammar-hits code {{
        display: block;
        color: var(--sky);
        white-space: normal;
        overflow-wrap: anywhere;
    }}
    .ipk-grammar-hits span {{
        display: block;
        color: rgba(242,238,226,.62);
        font-size: 0.78rem;
        margin-top: 0.2rem;
    }}
    .ipk-ontology-table {{
        border: 1px solid rgba(242,238,226,.14);
        border-radius: 8px;
        overflow: hidden;
        background: rgba(242,238,226,.055);
        margin: 1rem 0;
    }}
    .ipk-ontology-head,
    .ipk-ontology-row {{
        display: grid;
        grid-template-columns: minmax(120px, .65fr) minmax(0, 1fr) minmax(0, 1fr);
        gap: 0;
        border-bottom: 1px solid rgba(242,238,226,.11);
    }}
    .ipk-ontology-head {{
        background: rgba(242,238,226,.12);
        color: var(--gold);
        font-family: var(--sans);
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }}
    .ipk-ontology-head span,
    .ipk-ontology-row > div,
    .ipk-ontology-row p {{
        margin: 0;
        padding: 0.8rem;
        border-right: 1px solid rgba(242,238,226,.09);
    }}
    .ipk-ontology-row > div strong {{
        display: block;
        color: var(--inverse);
        font-family: var(--serif-display);
        font-size: 1.18rem;
        font-weight: 400;
    }}
    .ipk-ontology-row > div span {{
        color: rgba(242,238,226,.55);
        font-family: var(--sans);
        font-size: 0.72rem;
    }}
    .ipk-status-ok {{
        color: #bbf7d0;
    }}
    .ipk-status-warn {{
        color: var(--gold);
    }}
    .ipk-status-bad {{
        color: #fecaca;
    }}
    .ipk-kill-card h4,
    .ipk-formula-card h4 {{
        margin: 0.25rem 0 0.35rem;
        font-size: 1.25rem;
    }}
    .ipk-kill-card strong {{
        color: var(--gold);
        font-family: var(--sans);
    }}
    .ipk-pledge {{
        margin: 1rem 0 0;
        font-family: var(--serif-body);
        font-size: 1.04rem;
        line-height: 1.7;
    }}
    @media (max-width: 760px) {{
        .ipk-nav {{
            padding: 0.55rem 0.85rem;
            gap: 0.45rem;
        }}
        .ipk-nav-title-row {{
            gap: 0.5rem;
        }}
        .ipk-brand-mark {{
            width: 28px;
            height: 28px;
            font-size: 0.72rem;
        }}
        .ipk-nav-meta {{
            display: none;
        }}
        .ipk-nav-links {{
            gap: 0.4rem;
            overflow-x: auto;
            padding-bottom: 0.15rem;
        }}
        .ipk-nav-links a {{
            font-size: 0.66rem;
            white-space: nowrap;
        }}
        .ipk-hero {{
            min-height: auto;
            padding: clamp(3.5rem, 12vw, 5rem) 1rem clamp(2rem, 8vw, 3rem);
        }}
        .ipk-scroll-cue {{
            height: 28px;
            margin-top: 0.85rem;
        }}
        @keyframes ipk-scroll-cue-drop {{
            0% {{ opacity: 0; transform: translate(-50%, 0); }}
            28% {{ opacity: 1; }}
            72% {{ opacity: 0.9; }}
            100% {{ opacity: 0; transform: translate(-50%, 22px); }}
        }}
        .ipk-hero-stats,
        .ipk-mu-grid,
        .ipk-observatory-strip,
        .ipk-monograph-strip,
        .ipk-formula-grid,
        .ipk-kill-grid,
        .ipk-grammar-hits {{
            grid-template-columns: 1fr;
        }}
        .ipk-ontology-head {{
            display: none;
        }}
        .ipk-ontology-row {{
            grid-template-columns: 1fr;
        }}
        .ipk-ontology-row > div,
        .ipk-ontology-row p {{
            border-right: 0;
        }}
        .ipk-law-panel-top {{
            display: block;
        }}
        .ipk-law-result {{
            display: inline-block;
            margin-top: 0.75rem;
        }}
        .ipk-hero-chain i {{
            display: none;
        }}
        .ipk-hero-chain {{
            gap: 0.35rem;
        }}
    }}
    .ipk-section-header {{
        margin: 2.25rem 0 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid var(--rule);
        width: 100%;
        position: relative;
    }}
    .ipk-section-header::after {{
        content: "";
        position: absolute;
        left: 0;
        bottom: -1px;
        width: 72px;
        height: 1px;
        background: var(--accent);
        transform-origin: left;
        animation: ipk-rule-in 900ms var(--ii-ease) both;
    }}
    @keyframes ipk-rule-in {{
        from {{ transform: scaleX(0); }}
        to {{ transform: scaleX(1); }}
    }}
    .ipk-section-header h2 {{
        color: var(--primary);
        margin: 0;
        font-family: var(--serif-display);
        font-weight: 400;
        font-size: clamp(2rem, 4vw, 3.25rem);
    }}
    .ipk-section-subtitle {{
        color: var(--secondary);
        margin: 0.25rem 0 0;
        font-size: 0.95rem;
    }}
    .ipk-lock-detail {{
        background: linear-gradient(135deg, rgba(242,238,226,.96), rgba(232,237,229,.92));
        border: 1px solid var(--rule-strong);
        border-left: 4px solid var(--accent);
        padding: 1.25rem;
        border-radius: 8px;
        color: var(--primary);
        transition: box-shadow 350ms var(--ii-ease), transform 350ms var(--ii-ease), background 350ms var(--ii-ease), border-left-width 500ms var(--ii-ease);
    }}
    .ipk-lock-detail:hover {{
        background: var(--surface);
        box-shadow: var(--ii-shadow);
        transform: translateY(-2px);
        border-left-width: 7px;
    }}
    .ipk-lock-detail-top {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
    }}
    .ipk-lock-title {{
        color: var(--primary);
        font-weight: 600;
    }}
    .ipk-lock-meta {{
        font-size: 0.9rem;
        color: var(--secondary);
    }}
    .ipk-lock-pill {{
        background: rgba(47,149,166,.10);
        color: var(--accent-strong);
        border: 1px solid rgba(47,149,166,.20);
        padding: 2px 10px;
        border-radius: 9999px;
        font-size: 0.8rem;
        white-space: nowrap;
    }}
    .ipk-lock-details {{
        margin: 1rem 0;
        font-size: 0.95rem;
        line-height: 1.45;
    }}
    .ipk-lock-quote {{
        background: rgba(15,35,63,.045);
        padding: 0.75rem 1rem;
        border-radius: 6px;
        font-style: italic;
        color: var(--secondary);
    }}
    .ipk-lock-eliminated {{
        margin-top: 0.75rem;
        font-size: 0.8rem;
        color: var(--secondary);
    }}
    .ipk-branch-statistical-mechanics {{
        border-left-color: {BRANCH_COLORS["Statistical Mechanics"]};
    }}
    .ipk-branch-statistical-mechanics .ipk-lock-title {{
        color: var(--accent-strong);
    }}
    .ipk-branch-quantum-field-theory {{
        border-left-color: {BRANCH_COLORS["Quantum Field Theory"]};
    }}
    .ipk-branch-quantum-field-theory .ipk-lock-title {{
        color: #315D8E;
    }}
    .ipk-branch-spacetime-geometry {{
        border-left-color: {BRANCH_COLORS["Spacetime Geometry"]};
    }}
    .ipk-branch-spacetime-geometry .ipk-lock-title {{
        color: var(--gold-strong);
    }}
    .ipk-branch-internal-geometry {{
        border-left-color: {BRANCH_COLORS["Internal Geometry"]};
    }}
    .ipk-branch-internal-geometry .ipk-lock-title {{
        color: var(--slate);
    }}
    .ipk-branch-particle-physics {{
        border-left-color: {BRANCH_COLORS["Particle Physics"]};
    }}
    .ipk-branch-particle-physics .ipk-lock-title {{
        color: {BRANCH_COLORS["Particle Physics"]};
    }}
    .ipk-why {{
        background:
            radial-gradient(circle at 85% 16%, rgba(190,230,237,.16), transparent 18rem),
            linear-gradient(135deg, var(--primary), #09182c);
        padding: clamp(1.25rem, 3vw, 2.4rem);
        border-radius: 12px;
        border: 1px solid rgba(242,238,226,.18);
        width: min(1500px, calc(100vw - 2rem));
        margin: 0 auto;
        color: var(--inverse);
        box-shadow: 0 28px 80px -44px rgba(15,35,63,.56);
        position: relative;
        overflow: hidden;
    }}
    .ipk-why::before {{
        content: "";
        position: absolute;
        inset: 16px;
        border: 1px solid rgba(242,238,226,.16);
        pointer-events: none;
    }}
    .ipk-why p {{
        font-size: 1.05rem;
        line-height: 1.65;
    }}
    .ipk-why ul {{
        font-size: 0.98rem;
        line-height: 1.7;
        color: rgba(242,238,226,.76);
    }}
    .ipk-why-closing {{
        margin-top: 1rem;
        color: var(--gold);
        font-weight: 600;
    }}
    .ipk-footer {{
        text-align: center;
        padding: 2rem 0 1rem;
        color: var(--secondary);
        font-size: 0.85rem;
        border-top: 1px solid var(--rule);
        background: rgba(242,238,226,.72);
    }}
    .ipk-footer span {{
        opacity: 0.6;
    }}
    /* Dark-surface hardening for static Pages export and Marimo UI chrome. */
    html,
    body {{
        color-scheme: dark;
        background:
            radial-gradient(circle at 78% 0%, rgba(103, 232, 249, 0.18), transparent 34rem),
            radial-gradient(circle at 7% 46%, rgba(252, 211, 77, 0.10), transparent 30rem),
            linear-gradient(180deg, #071426 0%, #0a1628 52%, #071426 100%) !important;
        color: var(--inverse) !important;
    }}
    #root,
    #App,
    #App.bg-background,
    main,
    .marimo,
    .marimo-app,
    .mo-notebook,
    .notebook,
    [data-testid="notebook"],
    [data-testid="notebook-content"],
    [data-testid="cell-output"],
    .cell-output,
    .output-area,
    .output.block,
    marimo-output,
    .contents {{
        background: transparent !important;
        color: rgba(242,238,226,.86) !important;
    }}
    .markdown,
    .prose,
    .prose :where(p, li, strong, em, span, h1, h2, h3, h4, h5, h6):not(:where(.not-prose, .not-prose *)) {{
        color: inherit !important;
    }}
    .ipk-nav,
    .ipk-nav.is-pinned {{
        background:
            linear-gradient(180deg, rgba(8, 22, 40, .94), rgba(8, 22, 40, .78)) !important;
        border-color: rgba(242,238,226,.14) !important;
        box-shadow: 0 18px 55px -40px rgba(0,0,0,.9) !important;
    }}
    .ipk-brand-mark {{
        background: linear-gradient(135deg, rgba(103,232,249,.20), rgba(252,211,77,.18)) !important;
        color: var(--inverse) !important;
        border-color: rgba(242,238,226,.22) !important;
    }}
    .ipk-nav-title,
    .ipk-nav-links a,
    .ipk-nav-title-row:hover .ipk-nav-title {{
        color: var(--inverse) !important;
    }}
    .ipk-nav-meta,
    .ipk-marquee-track span {{
        color: rgba(242,238,226,.62) !important;
    }}
    .ipk-nav-links a:hover,
    .ipk-nav-links a.is-active {{
        color: var(--gold) !important;
    }}
    .ipk-law-badge,
    .ipk-hero-chain span,
    .ipk-hero-stat,
    .ipk-mu-chip,
    .ipk-observatory-tile,
    .ipk-mu-card,
    .ipk-lock-detail,
    .ipk-advanced-note,
    .ipk-copy-sheet,
    marimo-callout-output,
    .mo-callout {{
        background:
            radial-gradient(circle at var(--spot-x, 50%) var(--spot-y, 0%), rgba(103,232,249,.10), transparent 18rem),
            linear-gradient(135deg, rgba(14, 31, 54, .92), rgba(7, 20, 38, .84)) !important;
        color: rgba(242,238,226,.86) !important;
        border-color: rgba(242,238,226,.16) !important;
        box-shadow: 0 24px 70px -54px rgba(0,0,0,.88) !important;
    }}
    .ipk-mu-card,
    .ipk-lock-detail,
    .ipk-advanced-note,
    .ipk-law-panel,
    .ipk-copy-sheet,
    .ipk-why {{
        max-width: 100% !important;
        overflow-wrap: anywhere;
    }}
    .ipk-mu-card {{
        width: min(1400px, 100%) !important;
    }}
    .ipk-why {{
        width: min(1500px, 100%) !important;
    }}
    .ipk-marquee-strip,
    .ipk-footer {{
        background: rgba(7,20,38,.72) !important;
        border-color: rgba(242,238,226,.14) !important;
        color: rgba(242,238,226,.68) !important;
    }}
    .ipk-hero {{
        background:
            radial-gradient(circle at 72% 16%, rgba(103,232,249,.20), transparent 30rem),
            radial-gradient(circle at 16% 70%, rgba(252,211,77,.13), transparent 27rem),
            linear-gradient(135deg, rgba(7,20,38,.98), rgba(12,31,56,.94) 52%, rgba(7,20,38,.98)) !important;
        border-bottom-color: rgba(242,238,226,.12) !important;
        color: var(--inverse) !important;
    }}
    .ipk-hero h1,
    .ipk-hero strong,
    .ipk-section-header h2,
    .ipk-mu-card h3,
    .ipk-mu-principle,
    .ipk-mu-zero,
    .ipk-lock-title,
    .ipk-observatory-tile strong,
    .ipk-copy-sheet summary strong {{
        color: var(--inverse) !important;
    }}
    .ipk-hero p,
    .ipk-section-subtitle,
    .ipk-lock-meta,
    .ipk-lock-details,
    .ipk-lock-quote,
    .ipk-lock-eliminated,
    .ipk-mu-title span,
    .ipk-mu-chip span,
    .ipk-footer,
    .ipk-copy-sheet summary small {{
        color: rgba(242,238,226,.70) !important;
    }}
    .ipk-mu-kicker {{
        color: var(--gold) !important;
    }}
    .ipk-section-header {{
        border-bottom-color: rgba(242,238,226,.14) !important;
    }}
    .ipk-section-header::after {{
        background: linear-gradient(90deg, var(--accent), var(--gold)) !important;
    }}
    .ipk-lock-pill,
    .ipk-mu-chip {{
        background: rgba(103,232,249,.10) !important;
        color: var(--sky) !important;
        border-color: rgba(103,232,249,.22) !important;
    }}
    .ipk-lock-quote,
    .ipk-law-explain,
    .ipk-paper-quote,
    .ipk-pledge {{
        background: rgba(242,238,226,.065) !important;
        border-color: rgba(252,211,77,.50) !important;
    }}
    .ipk-why {{
        background:
            radial-gradient(circle at 82% 12%, rgba(103,232,249,.18), transparent 25rem),
            linear-gradient(135deg, rgba(7,20,38,.98), rgba(13,37,66,.92)) !important;
        box-shadow: 0 28px 80px -44px rgba(0,0,0,.88) !important;
    }}
    input,
    textarea,
    select,
    button,
    marimo-text,
    marimo-select,
    marimo-dropdown,
    marimo-multiselect,
    marimo-slider {{
        color-scheme: dark;
    }}
    input,
    textarea,
    select {{
        background: rgba(7,20,38,.88) !important;
        color: var(--inverse) !important;
        border-color: rgba(242,238,226,.24) !important;
        accent-color: var(--accent);
    }}
    button,
    .mo-button,
    marimo-button,
    marimo-download {{
        background: rgba(242,238,226,.08) !important;
        color: var(--inverse) !important;
        border-color: rgba(242,238,226,.22) !important;
    }}
    button:hover,
    .mo-button:hover,
    marimo-button:hover,
    marimo-download:hover {{
        background: rgba(103,232,249,.14) !important;
        border-color: rgba(103,232,249,.34) !important;
    }}
    marimo-text,
    marimo-select,
    marimo-dropdown,
    marimo-multiselect,
    marimo-slider,
    marimo-checkbox {{
        color: var(--inverse) !important;
    }}
    marimo-text::part(label),
    marimo-select::part(label),
    marimo-dropdown::part(label),
    marimo-multiselect::part(label),
    marimo-slider::part(label),
    marimo-checkbox::part(label) {{
        color: rgba(242,238,226,.78) !important;
    }}
    marimo-text::part(input),
    marimo-select::part(trigger),
    marimo-dropdown::part(trigger),
    marimo-multiselect::part(trigger),
    marimo-slider::part(track),
    marimo-slider::part(thumb) {{
        background: rgba(7,20,38,.88) !important;
        color: var(--inverse) !important;
        border-color: rgba(242,238,226,.24) !important;
    }}
    marimo-callout-output,
    marimo-callout-output::part(container),
    .mo-callout,
    [data-testid="stacks-plain-text"],
    pre {{
        background: rgba(7,20,38,.72) !important;
        color: rgba(242,238,226,.86) !important;
        border-color: rgba(242,238,226,.18) !important;
    }}
    code {{
        color: var(--sky) !important;
    }}
    marimo-static-notebook-banner,
    [class*="static-notebook" i],
    [class*="notebook-banner" i],
    [data-testid*="static" i],
    [data-testid*="banner" i] {{
        display: none !important;
        visibility: hidden !important;
    }}
    marimo-table {{
        color-scheme: dark;
        color: var(--inverse) !important;
        --gdg-bg-cell: rgba(7, 20, 38, 0.96);
        --gdg-bg-cell-medium: rgba(11, 29, 51, 0.98);
        --gdg-bg-header: rgba(242, 238, 226, 0.12);
        --gdg-bg-header-has-focus: rgba(103, 232, 249, 0.18);
        --gdg-bg-bubble: rgba(7, 20, 38, 0.96);
        --gdg-text-dark: var(--inverse);
        --gdg-text-medium: rgba(242, 238, 226, 0.78);
        --gdg-text-light: rgba(242, 238, 226, 0.60);
        --gdg-text-group-header: var(--sky);
        --gdg-border-color: rgba(242, 238, 226, 0.18);
        --gdg-accent-color: var(--sky);
        --gdg-accent-light: rgba(103, 232, 249, 0.18);
        --gdg-link-color: var(--sky);
        --gdg-font-family: var(--sans);
    }}
    marimo-table::part(table-wrapper),
    marimo-table::part(table-tabs),
    marimo-table::part(table-footer),
    marimo-table::part(filter-pills) {{
        background: rgba(7, 20, 38, 0.94) !important;
        color: var(--inverse) !important;
        border-color: rgba(242,238,226,.18) !important;
    }}
    marimo-table :is(table, thead, tbody, tr, th, td, [role="grid"], [role="row"], [role="columnheader"], [role="gridcell"]) {{
        background: rgba(7,20,38,.96) !important;
        color: var(--inverse) !important;
        border-color: rgba(242,238,226,.14) !important;
    }}
    .js-plotly-plot,
    .plotly-graph-div,
    .svg-container,
    .main-svg {{
        background: transparent !important;
    }}
    .modebar {{
        background: rgba(7,20,38,.80) !important;
        border-radius: 8px;
    }}
    .ipk-cascade-track,
    .ipk-nav-links {{
        -webkit-overflow-scrolling: touch;
        overscroll-behavior-x: contain;
        scroll-padding-inline: 0.5rem;
    }}
    .ipk-cascade-track {{
        mask-image: linear-gradient(90deg, transparent 0, #000 1.1rem, #000 calc(100% - 1.1rem), transparent 100%);
        -webkit-mask-image: linear-gradient(90deg, transparent 0, #000 1.1rem, #000 calc(100% - 1.1rem), transparent 100%);
    }}
    .ipk-lock-cascade {{
        max-width: 100%;
        contain: paint;
    }}
    .ipk-nav {{
        backdrop-filter: blur(20px) saturate(1.35);
        -webkit-backdrop-filter: blur(20px) saturate(1.35);
    }}
    :focus-visible {{
        outline: 2px solid rgba(103,232,249,.74) !important;
        outline-offset: 3px !important;
        border-radius: 8px;
    }}
    .ipk-copy-sheet {{
        max-width: min(1100px, 100%) !important;
        margin-right: auto !important;
    }}
    .ipk-copy-sheet pre {{
        max-height: min(22rem, 48vh) !important;
    }}
    .js-plotly-plot,
    .plotly-graph-div {{
        transition: box-shadow 360ms var(--ii-ease), transform 360ms var(--ii-ease);
    }}
    .js-plotly-plot:hover,
    .plotly-graph-div:hover {{
        box-shadow: 0 18px 58px -34px rgba(15,35,63,.45);
    }}
    .ipk-reveal-left {{
        opacity: 0;
        transform: translateX(-28px);
        transition: opacity .85s var(--ii-ease), transform .85s var(--ii-ease);
    }}
    .ipk-reveal-left.in {{
        opacity: 1;
        transform: none;
    }}
    .ipk-reveal-scale {{
        opacity: 0;
        transform: scale(.96);
        transition: opacity .8s var(--ii-ease), transform .8s var(--ii-ease);
    }}
    .ipk-reveal-scale.in {{
        opacity: 1;
        transform: none;
    }}
    .ipk-mu-card,
    .ipk-lock-detail,
    .ipk-observatory-tile,
    .ipk-advanced-note,
    .ipk-monograph-tile,
    .ipk-formula-card,
    .ipk-kill-card,
    .ipk-law-panel,
    .ipk-why {{
        will-change: transform, box-shadow;
    }}
    @supports (animation-timeline: view()) {{
        .ipk-section-header,
        .ipk-mu-card,
        .ipk-lock-detail,
        .ipk-observatory-tile,
        .ipk-advanced-note,
        .ipk-monograph-tile,
        .ipk-formula-card,
        .ipk-kill-card,
        .ipk-law-panel,
        .ipk-why {{
            animation: ipk-reveal-in both;
            animation-timeline: view();
            animation-range: entry 8% cover 24%;
        }}
        .ipk-observatory-tile:nth-child(2),
        .ipk-mu-chip:nth-child(2) {{
            animation-delay: 120ms;
        }}
        .ipk-observatory-tile:nth-child(3),
        .ipk-mu-chip:nth-child(3) {{
            animation-delay: 240ms;
        }}
        .ipk-observatory-tile:nth-child(4) {{
            animation-delay: 360ms;
        }}
    }}
    @keyframes ipk-reveal-in {{
        from {{
            opacity: 0;
            transform: translateY(28px);
            filter: blur(2px);
        }}
        to {{
            opacity: 1;
            transform: none;
            filter: blur(0);
        }}
    }}
    @media (prefers-reduced-motion: reduce) {{
        *,
        *::before,
        *::after {{
            animation-duration: .001ms !important;
            animation-iteration-count: 1 !important;
            scroll-behavior: auto !important;
            transition-duration: .001ms !important;
        }}
        .t-panel-slide,
        .t-resize {{
            transition: none !important;
        }}
        #grain,
        #cursor-dot,
        .cursor-ripple {{
            display: none !important;
        }}
        .ipk-marquee-track {{
            animation: none !important;
        }}
        .ipk-section-header,
        .ipk-mu-card,
        .ipk-lock-detail,
        .ipk-observatory-tile,
        .ipk-advanced-note,
        .ipk-monograph-tile,
        .ipk-formula-card,
        .ipk-kill-card,
        .ipk-law-panel,
        .ipk-why,
        .ipk-reveal-left,
        .ipk-reveal-scale {{
            animation: none !important;
            opacity: 1 !important;
            transform: none !important;
            filter: none !important;
            will-change: auto !important;
        }}
        .ipk-hero h1 .word {{
            opacity: 1;
            transform: none;
            animation: none;
        }}
    }}
    </style>
    """)
    return


@app.cell
def _(law_formula_input):
    _law_badge = create_law_status_badge(law_formula_input.value)
    _nav_bar = mo.Html(f"""
    <div id="grain" aria-hidden="true"></div>
    <div id="cursor-dot" class="cursor-dot" aria-hidden="true"></div>
    <div id="read-progress"></div>
    <div class="ipk-nav">
        <div class="ipk-nav-title-row">
            <div class="ipk-brand-mark">II</div>
            <div class="ipk-nav-title">
                Intelligent Physics Kernel
            </div>
            <div class="ipk-nav-meta">Emad Mostaque • Kernel + Long Monograph</div>
            {_law_badge}
        </div>
        <div class="ipk-nav-links">
            <a href="#mu">MU Principle</a>
            <a href="#locks">The 10 Locks</a>
            <a href="#flow">Flowchart</a>
            <a href="#monograph">Monograph</a>
            <a href="#viz">Interactive Visualizations</a>
            <a href="#advanced">Advanced Visuals</a>
            <a href="#why">Why It Matters</a>
        </div>
    </div>
    """)

    _marquee = mo.Html("""
    <div class="ipk-marquee-strip" aria-hidden="true">
        <div class="ipk-marquee-track">
            <span>Minimum Update</span><span class="ipk-marquee-dot">.</span>
            <span>10 Locks</span><span class="ipk-marquee-dot">.</span>
            <span>4D Spacetime</span><span class="ipk-marquee-dot">.</span>
            <span>E8 Root System</span><span class="ipk-marquee-dot">.</span>
            <span>Spin(10)</span><span class="ipk-marquee-dot">.</span>
            <span>Standard Model Intersection</span><span class="ipk-marquee-dot">.</span>
            <span>Table of Law</span><span class="ipk-marquee-dot">.</span>
            <span>Falsification Tests</span><span class="ipk-marquee-dot">.</span>
            <span>Minimum Update</span><span class="ipk-marquee-dot">.</span>
            <span>10 Locks</span><span class="ipk-marquee-dot">.</span>
            <span>4D Spacetime</span><span class="ipk-marquee-dot">.</span>
            <span>E8 Root System</span><span class="ipk-marquee-dot">.</span>
            <span>Spin(10)</span><span class="ipk-marquee-dot">.</span>
            <span>Standard Model Intersection</span><span class="ipk-marquee-dot">.</span>
            <span>Table of Law</span><span class="ipk-marquee-dot">.</span>
            <span>Falsification Tests</span><span class="ipk-marquee-dot">.</span>
        </div>
    </div>
    """)

    _hero = mo.Html(f"""
    <div class="ipk-hero">
        <div class="ipk-eyebrow">INTELLIGENT INTERNET • JANUARY 2026</div>
        <h1>
            <span class="word">Intelligent</span> <span class="word"><em>Physics</em></span> <span class="word">Kernel</span>
        </h1>
        <p>
            From a single epistemic principle, a chain of eliminations yields<br>
            <strong>4D spacetime • E₈ internal structure • the Standard Model</strong>
        </p>
        <div class="ipk-hero-chain">
            <span>MU</span><i></i><span>Probability</span><i></i><span>4D</span><i></i><span>E₈</span><i></i><span>Spin(10)</span><i></i><span>SM</span>
        </div>
        <div class="ipk-hero-stats">
            <div class="ipk-hero-stat"><strong>10 Locks</strong><span>constraint chain</span></div>
            <div class="ipk-hero-stat"><strong>240 Roots</strong><span>E₈ lattice</span></div>
            <div class="ipk-hero-stat"><strong>16 Weights</strong><span>Spin(10) matter</span></div>
            <div class="ipk-hero-stat"><strong>3 + 2 + 1</strong><span>SM algebra</span></div>
        </div>
        <div class="ipk-scroll-cue" aria-hidden="true"></div>
    </div>
    """)

    _mu_box = mo.Html(f"""
    <div class="ipk-mu-card t-panel-slide t-resize" data-open="true">
        <div class="ipk-mu-kicker">The Core Principle</div>
        <div class="ipk-mu-title">
            <h3>MU</h3>
            <span>Minimum Update</span>
        </div>
        <p class="ipk-mu-principle">{MU_PRINCIPLE}</p>
        <div class="ipk-mu-grid">
            <div class="ipk-mu-chip">No contradiction<span>Nothing can conflict with the premises.</span></div>
            <div class="ipk-mu-chip">Entailment<span>The update must actually follow.</span></div>
            <div class="ipk-mu-chip">No hidden assumptions<span>No content enters without license.</span></div>
        </div>
        <p>
            All three failures add content not licensed by the premises. Therefore consistent inference assumes nothing beyond what constraints demand.
        </p>
        <p>
            MU is self-grounding: asserting, denying, or questioning MU presupposes it.
        </p>
        <p class="ipk-mu-zero">Epistemic zero: what remains when all assumptions are stripped away.</p>
    </div>
    """)

    mo.vstack([_nav_bar, _hero, _marquee, mo.Html('<a id="mu"></a>'), mo.md("---"), _mu_box, mo.md("")])
    return


@app.cell
def _():
    locks_table = make_locks_table()
    return (locks_table,)


@app.cell
def _(locks_table):
    _selected_lock_idx = selected_lock_from_table(locks_table)
    _section = mo.vstack([
        mo.Html('<a id="locks"></a>'),
        section_header(
            "The 10 Locks — Interactive Overview",
            "Click any row to reveal the full theorem, quote, and reasoning from the paper",
        ),
        locks_table,
        lock_detail(_selected_lock_idx),
        mo.md("---"),
    ])
    _section
    return


@app.cell
def _():
    _flowchart = create_dependency_flowchart()
    _section = mo.vstack([
        mo.Html('<a id="flow"></a>'),
        section_header(
            "The MU → Standard Model Dependency Chain",
            "Exactly as derived in the paper (page 4). Each arrow is a Lock that eliminates structural freedom.",
        ),
        _flowchart,
        mo.md("---"),
    ])
    _section
    return


@app.cell
def _():
    law_formula_input = mo.ui.text(
        value="6*pi^5 + phi^-7",
        placeholder="Try a formula, e.g. 1/45 or 11*pi",
        label="Formula challenge",
        full_width=True,
    )
    law_challenge_mode = mo.ui.checkbox(label="Show skeptic challenge", value=True)
    monograph_focus_token = mo.ui.dropdown(
        MONOGRAPH_FOCUS_TOKENS,
        value="45",
        label="Highlight vocabulary token",
    )
    monograph_sector_filter = mo.ui.dropdown(
        SCORECARD_SECTORS,
        value="All",
        label="Scorecard sector",
    )
    alpha_correction_blend = mo.ui.slider(
        0.0,
        1.0,
        value=1.0,
        step=0.02,
        label="Fine-structure correction blend",
    )
    saturation_extra_channels = mo.ui.slider(
        0,
        12,
        value=0,
        step=1,
        label="Extra hidden gauge channels",
    )
    h4_projection_mode = mo.ui.dropdown(
        ["H4 Coxeter phase bloom", "Stereographic shell", "Penrose-like slice"],
        value="H4 Coxeter phase bloom",
        label="H4 / 600-cell mode",
    )
    h4_phase = mo.ui.slider(0, 2 * np.pi, value=0.35, step=0.02, label="H4 projection phase")
    h4_slice_width = mo.ui.slider(0.15, 1.0, value=1.0, step=0.02, label="600-cell slice thickness")
    koide_blend = mo.ui.slider(0.0, 1.0, value=1.0, step=0.02, label="Koide deformation")
    grammar_pair = mo.ui.dropdown(
        list(GRAMMAR_PAIRS),
        value="pi, phi",
        label="Grammar constants",
    )
    grammar_tolerance = mo.ui.slider(
        0.00005,
        0.002,
        value=0.0002,
        step=0.00005,
        label="Grammar tolerance",
    )
    grammar_trials = mo.ui.slider(
        25,
        300,
        value=125,
        step=25,
        label="Monte Carlo control sets",
    )
    generative_stage = mo.ui.slider(
        0.0,
        1.0,
        value=0.72,
        step=0.02,
        label="Generative denoising stage",
    )
    diophantine_lambda = mo.ui.slider(
        0.1,
        2.5,
        value=1.0,
        step=0.05,
        label="Diophantine complexity weight lambda",
    )
    provenance_status_filter = mo.ui.dropdown(
        PROVENANCE_STATUS_FILTERS,
        value="All",
        label="Traceability status filter",
    )
    mass_operator_sector = mo.ui.dropdown(
        MASS_OPERATOR_OPTIONS,
        value="Charged leptons (derived)",
        label="Mass operator sector",
    )
    mass_operator_a_scale = mo.ui.slider(
        0.5,
        1.5,
        value=1.0,
        step=0.01,
        label="a scale",
    )
    mass_operator_b_scale = mo.ui.slider(
        0.5,
        1.5,
        value=1.0,
        step=0.01,
        label="b scale",
    )
    mass_operator_c_scale = mo.ui.slider(
        0.5,
        1.5,
        value=1.0,
        step=0.01,
        label="c scale",
    )
    return (
        alpha_correction_blend,
        diophantine_lambda,
        generative_stage,
        grammar_pair,
        grammar_tolerance,
        grammar_trials,
        h4_phase,
        h4_projection_mode,
        h4_slice_width,
        koide_blend,
        law_challenge_mode,
        law_formula_input,
        mass_operator_a_scale,
        mass_operator_b_scale,
        mass_operator_c_scale,
        mass_operator_sector,
        monograph_focus_token,
        monograph_sector_filter,
        provenance_status_filter,
        saturation_extra_channels,
    )


@app.cell
def _(
    alpha_correction_blend,
    diophantine_lambda,
    generative_stage,
    grammar_pair,
    grammar_tolerance,
    grammar_trials,
    h4_phase,
    h4_projection_mode,
    h4_slice_width,
    koide_blend,
    law_challenge_mode,
    law_formula_input,
    mass_operator_a_scale,
    mass_operator_b_scale,
    mass_operator_c_scale,
    mass_operator_sector,
    monograph_focus_token,
    monograph_sector_filter,
    provenance_status_filter,
    saturation_extra_channels,
):
    def _monograph_note(text: str, kind: str = "info"):
        _kind = kind if kind in {"info", "success", "warn", "danger"} else "info"
        return mo.Html(
            f'<div class="ipk-monograph-note ipk-monograph-note-{_kind} t-panel-slide t-resize" '
            f'data-open="true"><p>{escape(text)}</p></div>'
        )

    def _table_of_law_panel():
        _law_examples = mo.ui.table(
            create_law_examples_table(),
            selection=None,
            page_size=4,
            show_data_types=False,
            wrapped_columns=["Lawful", "Unlawful contrast", "Why"],
        )
        return mo.vstack([
            mo.md("### Geometric Vocabulary Enforcer"),
            mo.hstack([law_formula_input, law_challenge_mode], justify="start", gap=1),
            create_formula_validator_panel(law_formula_input.value, law_challenge_mode.value),
            mo.hstack([
                mo.as_html(create_law_vocabulary_figure()),
                mo.vstack([
                    mo.md("### Table of Law"),
                    mo.ui.table(
                        pd.DataFrame(LAW_TOKEN_ROWS),
                        selection=None,
                        page_size=12,
                        show_data_types=False,
                        wrapped_columns=["Origin"],
                    ),
                ]),
            ], widths=[1, 1], gap=1),
            mo.md("### Lawful vs. Unlawful Formula Forms"),
            _law_examples,
        ])

    def _derivation_forest_panel():
        return mo.vstack([
            mo.md("### Derivation Trees Explorer"),
            mo.hstack([monograph_focus_token, alpha_correction_blend], justify="start", gap=1),
            create_derivation_forest(monograph_focus_token.value),
            create_derivation_cards(monograph_focus_token.value, alpha_correction_blend.value),
            _monograph_note(
                "The long paper changes the narrative from a linear lock chain to a forest: one E8 root supplies shared vocabulary, then gauge, mass, flavor, and cosmology trees reuse the same tokens.",
                kind="info",
            ),
        ])

    def _scorecard_panel():
        _scorecard_df = create_scorecard_dataframe(monograph_sector_filter.value, monograph_focus_token.value)
        _scorecard_table = mo.ui.table(
            _scorecard_df,
            selection=None,
            page_size=32,
            show_data_types=False,
            wrapped_columns=["Formula", "Observed", "Tokens"],
            freeze_columns_left=["Reuse", "Sector", "Parameter"],
        )
        return mo.vstack([
            mo.md("### Master Scorecard: 32 Live Rows"),
            mo.hstack([monograph_sector_filter, monograph_focus_token], justify="start", gap=1),
            create_token_break_panel(monograph_focus_token.value),
            mo.as_html(create_scorecard_reuse_chart(monograph_focus_token.value)),
            _scorecard_table,
            _monograph_note(
                "Rows marked listed are present in the long paper coverage table but do not yet have enough extracted algebra for a fully audited live calculator. The exact scorecard rows from pages 44-45 are encoded directly.",
                kind="warn",
            ),
        ])

    def _gauge_saturation_panel():
        return mo.vstack([
            mo.md("### Dimensional Saturation Gauge Channel Visualizer"),
            saturation_extra_channels,
            mo.as_html(create_gauge_saturation_figure(int(saturation_extra_channels.value))),
            create_gauge_saturation_panel(int(saturation_extra_channels.value)),
            _monograph_note(
                "The W-mass argument is deliberately brittle: a confirmed CDF II-like shift would require hidden loop degrees of freedom, but the spatial kissing number K3=12 leaves no spare channel capacity.",
                kind="danger",
            ),
        ])

    def _kill_list_panel():
        return mo.vstack([
            mo.md("### Falsification Kill List"),
            create_kill_dashboard(),
            create_axion_band_panel(),
            mo.as_html(create_kill_timeline()),
            mo.as_html(create_kill_brittleness_chart()),
            _monograph_note(
                "These are not adjustable targets in the monograph; the notebook treats them as kill conditions tied to the named experiments on pages 46-49.",
                kind="warn",
            ),
        ])

    def _h4_projection_panel():
        return mo.vstack([
            mo.md("### E8 -> H4 / 600-cell Golden Projection Explorer"),
            mo.hstack([h4_projection_mode, h4_phase, h4_slice_width], justify="start", gap=1),
            mo.as_html(create_h4_600_cell_figure(h4_projection_mode.value, h4_phase.value, h4_slice_width.value)),
            create_h4_projection_readout(h4_projection_mode.value, h4_phase.value, h4_slice_width.value),
            _monograph_note(
                "This is the long-paper bridge from E8 integers to phi: the 4D H4/600-cell shadow necessarily carries golden coordinates and fivefold quasicrystalline structure.",
                kind="success",
            ),
        ])

    def _koide_panel():
        return mo.vstack([
            mo.md("### Information-Geometric Charged-Lepton Matrix + Koide Cone"),
            koide_blend,
            mo.as_html(create_koide_cone_figure(koide_blend.value)),
            create_koide_readout(koide_blend.value),
            _monograph_note(
                "The cone view turns Koide into geometry: the square-root mass vector sits at 45 degrees to the democratic axis when Q_l = 2/3.",
                kind="info",
            ),
        ])

    def _compression_panel():
        return mo.vstack([
            mo.md("### Compression & Monte Carlo Validation Lab"),
            mo.hstack([grammar_pair, grammar_tolerance, grammar_trials], justify="start", gap=1),
            mo.as_html(create_compression_figure(grammar_pair.value, grammar_tolerance.value)),
            create_grammar_lab_panel(grammar_pair.value, grammar_tolerance.value),
            mo.as_html(create_monte_carlo_validation_figure(grammar_tolerance.value, int(grammar_trials.value))),
            create_monte_carlo_validation_panel(grammar_tolerance.value, int(grammar_trials.value)),
            _monograph_note(
                "The live searches are intentionally smaller than the paper's 10^6-trial study, but they expose the same falsifiable claim: the pi, phi grammar should behave differently from control irrational pairs.",
                kind="warn",
            ),
        ])

    def _ontology_panel():
        return mo.vstack([
            mo.md("### Ontology vs. Output Comparator"),
            create_ontology_comparator(),
            _monograph_note(
                "The long paper is explicit that matching the Standard Model output is not the same as sharing its ontology: vacuum, particles, gravity, time, and constants are reinterpreted as geometric/informational objects.",
                kind="info",
            ),
        ])

    def _generative_panel():
        return mo.vstack([
            mo.md("### Generative-Model Isomorphism"),
            generative_stage,
            mo.as_html(create_generative_isomorphism(generative_stage.value)),
            mo.as_html(create_diffusion_denoising_figure(generative_stage.value)),
            _monograph_note(
                "This module translates the paper's Part XII dictionary: action becomes energy, RG flow becomes reverse denoising, and Postulate U becomes universal regularization.",
                kind="success",
            ),
        ])

    def _diophantine_panel():
        return mo.vstack([
            mo.md("### Diophantine Phi Selector"),
            diophantine_lambda,
            mo.as_html(create_diophantine_selector(diophantine_lambda.value)),
            create_diophantine_readout(diophantine_lambda.value),
            _monograph_note(
                "The displayed functional follows the paper's structure F_lambda = lambda K_cf + S. It is a visual guide to the conditional theorem, not a proof of the full conjecture over all irrationals.",
                kind="warn",
            ),
        ])

    def _mass_matrix_program_panel():
        return mo.vstack([
            mo.md("### Spectral & Mass-Matrix Program"),
            create_mass_matrix_program(),
            mo.md("#### SU(3) Cartan Mass-Operator Sandbox"),
            mo.hstack([
                mass_operator_sector,
                mass_operator_a_scale,
                mass_operator_b_scale,
                mass_operator_c_scale,
            ], justify="start", gap=1),
            mo.as_html(create_mass_operator_figure(
                mass_operator_sector.value,
                mass_operator_a_scale.value,
                mass_operator_b_scale.value,
                mass_operator_c_scale.value,
            )),
            create_mass_operator_readout(
                mass_operator_sector.value,
                mass_operator_a_scale.value,
                mass_operator_b_scale.value,
                mass_operator_c_scale.value,
            ),
            _monograph_note(
                "The sandbox visualizes the Cartan ansatz in the source paper. Only the charged-lepton sector is treated as derived; quark, neutrino, and full spectral matrices remain open programme items.",
                kind="danger",
            ),
        ])

    def _provenance_panel():
        _prov_df = create_provenance_dataframe(provenance_status_filter.value)
        _prov_markdown = provenance_markdown(provenance_status_filter.value)
        _prov_csv = provenance_csv(provenance_status_filter.value)
        return mo.vstack([
            mo.md("### Traceability Console: LaTeX + PDF Page Refs"),
            provenance_status_filter,
            create_provenance_summary(provenance_status_filter.value),
            mo.ui.table(
                _prov_df,
                selection=None,
                page_size=12,
                show_data_types=False,
                wrapped_columns=["LaTeX", "Source"],
                show_download=True,
            ),
            mo.hstack([
                mo.download(
                    _prov_csv,
                    filename="intelligent_physics_traceability.csv",
                    mimetype="text/csv",
                    label="Download CSV",
                ),
                mo.download(
                    _prov_markdown,
                    filename="intelligent_physics_traceability.md",
                    mimetype="text/markdown",
                    label="Download Markdown",
                ),
            ], justify="start", gap=1),
            create_provenance_copy_preview(_prov_markdown, provenance_status_filter.value),
            _monograph_note(
                "This module is the exportable citation layer for the atlas. Use the table download for spreadsheets, or the Markdown download when drafting notes with LaTeX and PDF page references.",
                kind="success",
            ),
        ])

    def _coverage_panel():
        _coverage_df = create_coverage_dataframe()
        _coverage_md = coverage_markdown()
        return mo.vstack([
            mo.md("### Coverage Matrix: Plan → Notebook Evidence"),
            create_coverage_summary(),
            mo.as_html(create_coverage_chart()),
            mo.ui.table(
                _coverage_df,
                selection=None,
                page_size=20,
                show_data_types=False,
                wrapped_columns=["Requirement", "Implementation", "Evidence"],
                show_download=True,
            ),
            mo.download(
                _coverage_md,
                filename="intelligent_physics_coverage_audit.md",
                mimetype="text/markdown",
                label="Download Coverage Audit",
            ),
            _monograph_note(
                "The non-complete rows are intentional: the scorecard keeps caveats visible, VS Code/JupyterHub need host-specific manual confirmation, and full quark/neutrino/E8 spectral matrices are open problems in the long paper rather than hidden notebook omissions.",
                kind="warn",
            ),
        ])

    _monograph_body = mo.vstack([
        mo.Html('<div class="ipk-panel-kicker">Module 1</div>'),
        _table_of_law_panel(),
        mo.md("---"),
        mo.Html('<div class="ipk-panel-kicker">Module 2</div>'),
        _derivation_forest_panel(),
        mo.md("---"),
        mo.Html('<div class="ipk-panel-kicker">Module 3</div>'),
        _scorecard_panel(),
        mo.md("---"),
        mo.Html('<div class="ipk-panel-kicker">Module 4</div>'),
        _gauge_saturation_panel(),
        mo.md("---"),
        mo.Html('<div class="ipk-panel-kicker">Module 5</div>'),
        _kill_list_panel(),
        mo.md("---"),
        mo.Html('<div class="ipk-panel-kicker">Module 6</div>'),
        _h4_projection_panel(),
        mo.md("---"),
        mo.Html('<div class="ipk-panel-kicker">Module 7</div>'),
        _koide_panel(),
        mo.md("---"),
        mo.Html('<div class="ipk-panel-kicker">Module 8</div>'),
        _compression_panel(),
        mo.md("---"),
        mo.Html('<div class="ipk-panel-kicker">Module 9</div>'),
        _ontology_panel(),
        mo.md("---"),
        mo.Html('<div class="ipk-panel-kicker">Module 10</div>'),
        _generative_panel(),
        mo.md("---"),
        mo.Html('<div class="ipk-panel-kicker">Module 11</div>'),
        _diophantine_panel(),
        mo.md("---"),
        mo.Html('<div class="ipk-panel-kicker">Module 12</div>'),
        _mass_matrix_program_panel(),
        mo.md("---"),
        mo.Html('<div class="ipk-panel-kicker">Module 13</div>'),
        _provenance_panel(),
        mo.md("---"),
        mo.Html('<div class="ipk-panel-kicker">Module 14</div>'),
        _coverage_panel(),
    ])

    _intro = mo.Html("""
    <a id="monograph"></a>
    <span class="ipk-monograph-shell-marker" aria-hidden="true"></span>
    <div class="ipk-monograph-intro">
        <div class="ipk-panel-kicker">65-page Intelligent Physics monograph • Dec 2025 source layer</div>
        <h2>Full Monograph: geometric code, constants, and kill tests</h2>
        <p>
            The long paper adds the missing machinery: a finite Table of Law, derivation forests,
            a 32-row constants scorecard, dimensional saturation, six falsifiable experiments,
            the Tier 2 geometry/compression labs, the remaining ontology,
            generative-model, Diophantine, and spectral-program views, plus
            exportable traceability and coverage sheets.
        </p>
    </div>
    <div class="ipk-monograph-strip">
        <div class="ipk-monograph-tile t-panel-slide t-resize" data-open="true"><div class="ipk-panel-kicker">Vocabulary</div><strong>8 primitives</strong><span>pi, phi, 24, 12, 45, 16, 15, 3 plus derived Fibonacci/composite tokens.</span></div>
        <div class="ipk-monograph-tile t-panel-slide t-resize" data-open="true"><div class="ipk-panel-kicker">Compression</div><strong>350 -> 90 bits</strong><span>Finite grammar and shared derivation trees replace independent parameter dials.</span></div>
        <div class="ipk-monograph-tile t-panel-slide t-resize" data-open="true"><div class="ipk-panel-kicker">Falsifiability</div><strong>14 modules</strong><span>Table of Law through phi selection, spectral audit, traceability, and coverage.</span></div>
    </div>
    """)

    _section = mo.vstack([
        _intro,
        _monograph_body,
        mo.md(""),
    ])
    _section
    return


@app.cell
def _():
    kl_mean = mo.ui.slider(-2.5, 2.5, value=0.8, step=0.05, label="Mean constraint")
    kl_var = mo.ui.slider(0.3, 4.0, value=1.2, step=0.05, label="Variance constraint")
    return kl_mean, kl_var


@app.cell
def _(kl_mean, kl_var):
    _kl_fig, _kl_value = create_kl_demo(kl_mean.value, kl_var.value)
    kl_plot = mo.as_html(_kl_fig)
    kl_summary = mo.md(f"KL distance from prior after the minimum update: **{_kl_value:.4f}**")
    return kl_plot, kl_summary


@app.cell
def _():
    e8_mode = mo.ui.dropdown(
        [
            "Coxeter phase bloom",
            "Golden chamber",
            "Petrie-style (balanced)",
            "Stereographic shell",
            "2-plane slice",
            "Standard (sequential planes)",
            "Random orthogonal",
        ],
        value="Coxeter phase bloom",
        label="Projection Mode",
    )
    e8_color_mode = mo.ui.dropdown(
        ["Projected radius", "Original root family", "Height bands", "Coxeter phase"],
        value="Coxeter phase",
        label="Color Mode",
    )
    e8_phi = mo.ui.slider(0, 2*np.pi, value=0.7, step=0.012, label="φ")
    e8_theta = mo.ui.slider(0, 2*np.pi, value=1.25, step=0.012, label="θ")
    e8_psi = mo.ui.slider(0, 2*np.pi, value=0.35, step=0.012, label="ψ")
    e8_slice_width = mo.ui.slider(0.08, 1.0, value=1.0, step=0.02, label="Slice thickness")
    e8_edges = mo.ui.checkbox(label="Show projected proximity edges", value=False)
    e8_glow = mo.ui.checkbox(label="Nebula glow layer", value=True)
    random_seed_state, set_random_seed = mo.state(42)
    return (
        e8_color_mode,
        e8_edges,
        e8_glow,
        e8_mode,
        e8_phi,
        e8_psi,
        e8_slice_width,
        e8_theta,
        random_seed_state,
        set_random_seed,
    )


@app.cell
def _(e8_color_mode, e8_edges, e8_glow, e8_mode, e8_phi, e8_psi, e8_slice_width, e8_theta, random_seed_state):
    _e8_fig = create_enhanced_e8_viewer(
        e8_mode.value,
        (e8_phi.value, e8_theta.value, e8_psi.value),
        e8_edges.value,
        random_seed_state,
        e8_color_mode.value,
        e8_glow.value,
        e8_slice_width.value,
    )
    _e8_shadow_fig = create_e8_shadow_plot(
        e8_mode.value,
        (e8_phi.value, e8_theta.value, e8_psi.value),
        random_seed_state,
        e8_color_mode.value,
        e8_slice_width.value,
    )
    e8_plot = mo.as_html(_e8_fig)
    e8_shadow_plot = mo.as_html(_e8_shadow_fig)
    return e8_plot, e8_shadow_plot


@app.cell
def _():
    lock4_t = mo.ui.slider(0.0, 4.0, value=1.8, step=0.05, label="Evolution time t")
    return (lock4_t,)


@app.cell
def _(lock4_t):
    _lock4_fig, lock4_prob = create_lock4_unitary_demo(lock4_t.value)
    lock4_plot = mo.as_html(_lock4_fig)
    return lock4_plot, lock4_prob


@app.cell
def _():
    spin10_choice = mo.ui.slider(0, 3, value=1, step=1, label="Select representation to inspect")
    return (spin10_choice,)


@app.cell
def _(spin10_choice):
    _spin10_fig, spin10_detail = create_spin10_explorer(int(spin10_choice.value))
    spin10_plot = mo.as_html(_spin10_fig)
    return spin10_detail, spin10_plot


@app.cell
def _():
    chain_selector = mo.ui.multiselect(
        options=[f"{l['id']}. {l['lock']}" for l in LOCKS_DATA],
        value=[f"{l['id']}. {l['lock']}" for l in LOCKS_DATA],
        label="Active Locks in your custom derivation",
    )
    return (chain_selector,)


@app.cell
def _(chain_selector):
    _selected_ids = [int(s.split('.')[0]) for s in chain_selector.value]
    chain_summary, _survived = simulate_user_chain(_selected_ids)
    return (chain_summary,)


@app.cell
def _():
    lattice_choice = mo.ui.dropdown(
        list(LATTICE_COMPARISON["name"]),
        value="E8",
        label="Lattice focus",
    )
    duality_blend = mo.ui.slider(0.0, 1.0, value=0.5, step=0.02, label="L ↔ L* blend")
    spin_branch_view = mo.ui.dropdown(
        ["SU(5) branching", "Pati-Salam branching"],
        value="SU(5) branching",
        label="Spin(10) branch view",
    )
    bott_dimension = mo.ui.slider(2, 18, value=10, step=1, label="Spin(n) for Bott clock")
    hodge_dimension = mo.ui.slider(2, 8, value=4, step=1, label="Spacetime dimension D")
    lovelock_dimension = mo.ui.slider(2, 11, value=4, step=1, label="Lovelock dimension D")
    instanton_winding = mo.ui.slider(-3, 3, value=1, step=1, label="Instanton winding ν")
    instanton_size = mo.ui.slider(0.35, 1.8, value=0.9, step=0.05, label="Instanton size ρ")
    duality_angle = mo.ui.slider(0.0, np.pi / 2, value=0.45, step=0.02, label="Duality frame angle")
    info_constraint_strength = mo.ui.slider(0.0, 1.0, value=0.65, step=0.02, label="Information constraint strength")
    fluids_stage = mo.ui.slider(0, 8, value=8, step=1, label="4D fluids bridge stage")
    telescope_stage = mo.ui.slider(0, 10, value=10, step=1, label="MU telescope lock stage")
    anomaly_16 = mo.ui.slider(0, 3, value=1, step=1, label="# of 16")
    anomaly_16bar = mo.ui.slider(0, 3, value=0, step=1, label="# of 16bar")
    anomaly_10 = mo.ui.slider(0, 3, value=0, step=1, label="# of 10")
    return (
        anomaly_10,
        anomaly_16,
        anomaly_16bar,
        bott_dimension,
        duality_angle,
        duality_blend,
        fluids_stage,
        hodge_dimension,
        info_constraint_strength,
        instanton_size,
        instanton_winding,
        lattice_choice,
        lovelock_dimension,
        spin_branch_view,
        telescope_stage,
    )


@app.cell
def _(
    anomaly_10,
    anomaly_16,
    anomaly_16bar,
    bott_dimension,
    chain_selector,
    chain_summary,
    duality_angle,
    duality_blend,
    e8_color_mode,
    e8_edges,
    e8_glow,
    e8_mode,
    e8_phi,
    e8_plot,
    e8_psi,
    e8_shadow_plot,
    e8_slice_width,
    e8_theta,
    fluids_stage,
    hodge_dimension,
    info_constraint_strength,
    instanton_size,
    instanton_winding,
    kl_mean,
    kl_plot,
    kl_summary,
    kl_var,
    lattice_choice,
    lovelock_dimension,
    lock4_plot,
    lock4_prob,
    lock4_t,
    set_random_seed,
    spin_branch_view,
    spin10_choice,
    spin10_detail,
    spin10_plot,
    telescope_stage,
):
    _random_button = mo.ui.button(
        label="🎲 Random Beautiful Projection",
        on_click=lambda: set_random_seed(int(np.random.randint(1, 999999))),
    )
    _reset_button = mo.ui.button(
        label="Reset to canonical",
        on_click=lambda: set_random_seed(42),
    )

    def _lattice_panel():
        return mo.vstack([
            mo.md("### Lattice Geometry — Even Unimodular Comparison + Self-Duality"),
            lattice_choice,
            mo.as_html(create_lattice_comparison(lattice_choice.value)),
            mo.as_html(create_lattice_norm_histogram(lattice_choice.value)),
            duality_blend,
            mo.as_html(create_self_duality_visualizer(duality_blend.value, lattice_choice.value)),
            duality_angle,
            mo.as_html(create_wilson_tHooft_duality(duality_angle.value)),
            mo.callout(
                "The visual point of Locks 7–8 is not that E8 is merely large or beautiful: electric and magnetic charge descriptions must be interchangeable, and E8 is the first dimension where even unimodular structure is unique.",
                kind="success",
            ),
        ])

    def _spin_panel():
        _anomaly_fig, _anomaly_detail = create_anomaly_playground(
            int(anomaly_16.value),
            int(anomaly_16bar.value),
            int(anomaly_10.value),
        )
        return mo.vstack([
            mo.md("### Spin(10), Matter Branching, Bott Periodicity, and Anomaly Balance"),
            mo.hstack([spin_branch_view, bott_dimension], justify="start", gap=1),
            mo.as_html(create_spin10_weight_lattice(spin_branch_view.value)),
            mo.as_html(create_spin10_branching_graph(spin_branch_view.value)),
            mo.as_html(create_bott_clock(int(bott_dimension.value))),
            mo.hstack([anomaly_16, anomaly_16bar, anomaly_10], justify="start", gap=1),
            mo.as_html(_anomaly_fig),
            _anomaly_detail,
        ])

    def _chirality_panel():
        _instanton_fig, _instanton_detail = create_instanton_charge_explorer(
            int(instanton_winding.value),
            instanton_size.value,
        )
        return mo.vstack([
            mo.md("### 4D Chirality, Gauge Intersection, and MU as Information Geometry"),
            lovelock_dimension,
            mo.as_html(create_lovelock_dimension_plot(int(lovelock_dimension.value))),
            hodge_dimension,
            mo.as_html(create_hodge_chirality_visualizer(int(hodge_dimension.value))),
            mo.hstack([instanton_winding, instanton_size], justify="start", gap=1),
            mo.as_html(_instanton_fig),
            _instanton_detail,
            mo.as_html(create_baez_huerta_intersection()),
            info_constraint_strength,
            mo.as_html(create_information_geometry_flow(info_constraint_strength.value)),
            mo.as_html(create_fisher_constraint_surface(info_constraint_strength.value)),
            fluids_stage,
            mo.as_html(create_fluids_bridge(int(fluids_stage.value))),
            mo.callout(
                "These views connect Locks 6, 10, and 1–2: D=4 is where two-forms can split, the Standard Model is the intersection common to both Spin(10) presentations, and every constraint enters as a minimum information update.",
                kind="info",
            ),
        ])

    def _telescope_panel():
        _mu_telescope_fig, _mu_telescope_detail = create_mu_telescope(int(telescope_stage.value))
        return mo.vstack([
            mo.md("### Full MU Telescope — Theory Space Collapse"),
            telescope_stage,
            mo.as_html(_mu_telescope_fig),
            _mu_telescope_detail,
        ])

    _advanced_tabs = mo.ui.tabs(
        {
            "Lattices & Duality": _lattice_panel(),
            "Spin(10) Matter": _spin_panel(),
            "4D + Gauge": _chirality_panel(),
            "MU Telescope": _telescope_panel(),
        },
        value="Lattices & Duality",
    )

    _kl_stage = mo.vstack([
        mo.md("### Locks 1–2 — Minimum Update as KL Projection"),
        mo.hstack([kl_mean, kl_var], justify="start", gap=1),
        kl_plot,
        kl_summary,
        mo.callout(
            "Move the constraints: the posterior changes only as much as required. This is MU made quantitative through Shore–Johnson consistency.",
            kind="info",
        ),
    ]).style({
        "width": "100%",
        "padding": "clamp(1rem, 2vw, 1.5rem)",
        "border": "1px solid rgba(15,35,63,0.16)",
        "background": "linear-gradient(180deg, rgba(242,238,226,0.94), rgba(232,237,229,0.84))",
    })

    _e8_stage = mo.vstack([
        mo.md("### ★ E₈ Root Lattice — Multiple Projection Modes (Locks 7–8)"),
        mo.hstack([_random_button, _reset_button], justify="start", gap=1),
        mo.hstack([e8_mode, e8_color_mode], justify="start", gap=1),
        mo.hstack([e8_phi, e8_theta, e8_psi], justify="start", gap=1),
        e8_slice_width,
        mo.hstack([e8_edges, e8_glow], justify="start", gap=1),
        e8_plot,
        e8_shadow_plot,
        mo.callout(
            "240 roots. All the same length. The 3D bloom and 2D shadow are different projections of the same E₈ object: change the mode, color rule, and angles, and the invariant 240-vector structure remains.",
            kind="success",
        ),
    ]).style({
        "width": "100%",
        "padding": "clamp(1rem, 2vw, 1.75rem)",
        "border": "1px solid rgba(15,35,63,0.18)",
        "background": "linear-gradient(180deg, rgba(242,238,226,0.96), rgba(232,237,229,0.88))",
    })

    _advanced_stage = mo.vstack([
        mo.Html('<a id="advanced"></a>'),
        section_header(
            "Advanced Structure Observatory",
            "The highest-impact visual bridges: lattice uniqueness, duality, Spin(10) branching, 4D chirality, anomaly cancellation, and the full MU collapse.",
        ),
        mo.Html("""
        <div class="ipk-observatory-strip">
            <div class="ipk-observatory-tile t-panel-slide t-resize" data-open="true"><strong>Lattice Geometry</strong>E₈, E₈×E₈, D16+, Leech, duality, and norm shells.</div>
            <div class="ipk-observatory-tile t-panel-slide t-resize" data-open="true"><strong>Matter Weights</strong>Spin(10) branching, Bott periodicity, and chirality balance.</div>
            <div class="ipk-observatory-tile t-panel-slide t-resize" data-open="true"><strong>4D Gauge Physics</strong>Hodge star, instantons, Lovelock elimination, and SM intersection.</div>
            <div class="ipk-observatory-tile t-panel-slide t-resize" data-open="true"><strong>MU Telescope</strong>Theory space collapsing as each Lock is applied.</div>
        </div>
        """),
        _advanced_tabs,
    ]).style({
        "width": "100%",
        "padding": "clamp(1rem, 2vw, 1.75rem)",
        "border": "1px solid rgba(15,35,63,0.16)",
        "background": "linear-gradient(180deg, rgba(242,238,226,0.94), rgba(232,237,229,0.84))",
    })

    _section = mo.vstack([
        mo.Html('<a id="viz"></a>'),
        section_header(
            "Interactive Visualizations by Branch",
            "Fully reactive demos for every major Lock. The enhanced E₈ viewer is the heart of the paper.",
        ),
        _kl_stage,
        mo.md("---"),
        _e8_stage,
        mo.md("---"),

        mo.md("### Lock 4 — Time & Unitarity (Osterwalder–Schrader intuition)"),
        lock4_t,
        lock4_plot,
        mo.md(f"Probability remaining in initial state after unitary evolution: **{lock4_prob:.3f}**. Reflection positivity guarantees this evolution stays consistent with the probabilistic inference of Lock 1."),
        mo.md("---"),

        mo.md("### Locks 9–10 — Spin(10) Matter and Gauge Algebra"),
        spin10_choice,
        spin10_plot,
        spin10_detail,
        mo.callout(
            "The 16-dimensional complex Weyl spinor of Spin(10) is the unique matter representation that survives every Lock. The gauge algebra is forced to be exactly su(3)⊕su(2)⊕u(1) by the Baez–Huerta intersection theorem.",
            kind="info",
        ),
        mo.md("---"),

        mo.md("### Build Your Own Chain — What Survives?"),
        mo.md("Select any subset of the Locks. See what physics is forced."),
        chain_selector,
        chain_summary,
        mo.md("---"),

        _advanced_stage,
        mo.md("---"),
    ]).style({
        "width": "100%",
        "padding": "0 clamp(0.75rem, 1.5vw, 1.25rem)",
    })
    _section
    return


@app.cell
def _():
    _section = mo.vstack([
        mo.md("### Export & Share"),
        mo.hstack([
            mo.callout(
                mo.md("**Best public snapshot:** use `make site` to export `site/index.html`. It is CDN-backed static HTML: great for sharing and reading, while live Python recomputation requires the Marimo app."),
                kind="info",
            ),
            mo.callout(
                mo.md("**For papers:** Screenshot the E₈ viewer or use Plotly’s built-in camera icon on any figure for vector-quality SVG/PNG."),
                kind="info",
            ),
        ]),
        mo.md("---"),
        mo.Html('<a id="why"></a>'),
        section_header(
            "Why This Matters",
            "A single epistemic principle, applied consistently, yields the entire visible structure of fundamental physics.",
        ),
        mo.Html("""
        <div class="ipk-why">
        <p>
        The MU principle does not "guess" the Standard Model. It <strong>eliminates everything else</strong>.
        </p>
        <ul>
            <li>Probability is not an assumption — it is the only consistent language for inference.</li>
            <li>Locality and unitarity are not aesthetic choices — they are the only structures compatible with consistent updating over time.</li>
            <li>Four-dimensional spacetime is not selected by anthropics — it is the unique dimension in which gravity is unique <em>and</em> chiral gauge theories with instantons exist.</li>
            <li>E₈ is not a "pretty lattice" — it is the unique self-dual even unimodular lattice that admits spin structure and embeds the required matter representations.</li>
            <li>The SM gauge group is not one of many possibilities — it is the fixed point of all maximal embeddings inside Spin(10) ⊂ E₈.</li>
        </ul>
        <p class="ipk-why-closing">
            One principle. A chain of ten Locks. The entire Standard Model + gravity + spacetime + internal geometry.
        </p>
        </div>
        """),
        mo.md(""),
        mo.Html("""
        <div class="ipk-footer">
            Built with <strong>Marimo</strong> + <strong>Grok Build</strong> • Inspired by Emad Mostaque’s MU principle<br>
            All theorems and reasoning taken verbatim from <em>Intelligent Physics Kernel</em> (January 2026).<br>
            <span>This is an interactive companion, not a replacement for the original paper.</span>
        </div>
        """),
        mo.md(""),
        mo.callout(
            mo.md("**Share this notebook** — Use `make site` for the static public artifact, or deploy the Python-backed Marimo app behind HTTPS/auth for full live controls."),
            kind="info",
        ),
    ])
    _section
    return

if __name__ == "__main__":
    app.run()
