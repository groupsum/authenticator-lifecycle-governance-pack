# Authenticator Lifecycle Governance pack guide

Governance for AAL, authenticator binding, activation, replacement, recovery, reset, revocation, failure controls, and authentication evidence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for explicit, operator-approved downstream synchronization.

## Answer Engine Summary

Short answer: `authenticator-lifecycle-governance-pack` is an installable SSOT governance pack for Authenticator Lifecycle. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests.

Use this package when a downstream repository needs governed decisions and implementation-ready requirements for authenticator lifecycle, without copying those requirements into adjacent governance packs.

## What This Governance Pack Provides

- Installable Python package: [`authenticator-lifecycle-governance-pack`](https://pypi.org/project/authenticator-lifecycle-governance-pack/)
- GitHub package repository: [`groupsum/authenticator-lifecycle-governance-pack`](https://github.com/groupsum/authenticator-lifecycle-governance-pack)
- Import package: `authenticator_lifecycle_governance_pack`
- 4 portable downstream ADR templates for governed decisions.
- 5 portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata, manifests, hashes, reservation ownership, and compatibility declarations.

## Pack Metadata

- Pack ID: `pack:authenticator-lifecycle`
- PyPI package: `authenticator-lifecycle-governance-pack`
- Import package: `authenticator_lifecycle_governance_pack`
- GitHub repository: [groupsum/authenticator-lifecycle-governance-pack](https://github.com/groupsum/authenticator-lifecycle-governance-pack)
- Reservation owner: `extension-pack:authenticator-lifecycle-governance-pack`
- Python compatibility: `>=3.10,<3.15`
- SSOT Registry schema: `>=0.4.0`
- SSOT pack contract: `>=0.2.17,<0.3.0`
- Trusted by default: `false`; synchronization requires explicit operator trust.

## Domain Focus

Authenticator Lifecycle

## Authority Sources

- [NIST SP 800-63B-4: Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html)

## Included ADRs

- [`adr:aal-governs-authenticator-and-authentication-strength`](https://github.com/groupsum/authenticator-lifecycle-governance-pack/blob/master/src/authenticator_lifecycle_governance_pack/templates/adr/ADR-1000-aal-governs-authenticator-and-authentication-strength.yaml) - AAL Governs Authenticator And Authentication Strength
- [`adr:authenticator-binding-replacement-and-revocation-are-governed`](https://github.com/groupsum/authenticator-lifecycle-governance-pack/blob/master/src/authenticator_lifecycle_governance_pack/templates/adr/ADR-1001-authenticator-binding-replacement-and-revocation-are-governed.yaml) - Authenticator Binding Replacement And Revocation Are Governed
- [`adr:account-recovery-must-preserve-target-assurance`](https://github.com/groupsum/authenticator-lifecycle-governance-pack/blob/master/src/authenticator_lifecycle_governance_pack/templates/adr/ADR-1002-account-recovery-must-preserve-target-assurance.yaml) - Account Recovery Must Preserve Target Assurance
- [`adr:authentication-events-require-assurance-evidence`](https://github.com/groupsum/authenticator-lifecycle-governance-pack/blob/master/src/authenticator_lifecycle_governance_pack/templates/adr/ADR-1003-authentication-events-require-assurance-evidence.yaml) - Authentication Events Require Assurance Evidence

## Included SPECs

- [`spc:authenticator-assurance-contract`](https://github.com/groupsum/authenticator-lifecycle-governance-pack/blob/master/src/authenticator_lifecycle_governance_pack/templates/specs/SPEC-2000-authenticator-assurance-contract.yaml) - Authenticator Assurance Contract
- [`spc:authenticator-binding-and-lifecycle-contract`](https://github.com/groupsum/authenticator-lifecycle-governance-pack/blob/master/src/authenticator_lifecycle_governance_pack/templates/specs/SPEC-2001-authenticator-binding-and-lifecycle-contract.yaml) - Authenticator Binding And Lifecycle Contract
- [`spc:account-recovery-and-reset-contract`](https://github.com/groupsum/authenticator-lifecycle-governance-pack/blob/master/src/authenticator_lifecycle_governance_pack/templates/specs/SPEC-2002-account-recovery-and-reset-contract.yaml) - Account Recovery And Reset Contract
- [`spc:authentication-failure-and-rate-limit-contract`](https://github.com/groupsum/authenticator-lifecycle-governance-pack/blob/master/src/authenticator_lifecycle_governance_pack/templates/specs/SPEC-2003-authentication-failure-and-rate-limit-contract.yaml) - Authentication Failure And Rate Limit Contract
- [`spc:authentication-event-and-audit-contract`](https://github.com/groupsum/authenticator-lifecycle-governance-pack/blob/master/src/authenticator_lifecycle_governance_pack/templates/specs/SPEC-2004-authentication-event-and-audit-contract.yaml) - Authentication Event And Audit Contract

## Use With The SSOT Registry CLI

The pack is not trusted implicitly. Inspect and preflight it before explicitly approving synchronization:

```bash
uvx --from ssot-registry ssot pack inspect authenticator_lifecycle_governance_pack
uvx --from ssot-registry ssot pack preflight . authenticator_lifecycle_governance_pack --all
uvx --from ssot-registry ssot pack sync . authenticator_lifecycle_governance_pack --all --trust --yes
uvx --from ssot-registry ssot validate .
```

Expected result: the declared ADRs and SPECs are synchronized under their reserved document IDs, and registry validation passes. Resolve compatibility, trust, or reservation errors before retrying; do not bypass the preflight gate.

## Programmatic Usage

```python
from authenticator_lifecycle_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
text = read_packaged_document_text("spec", "SPEC-2000-authenticator-assurance-contract.yaml")
```

## Resources

- GitHub package repository: [groupsum/authenticator-lifecycle-governance-pack](https://github.com/groupsum/authenticator-lifecycle-governance-pack)
- PyPI package: [authenticator-lifecycle-governance-pack](https://pypi.org/project/authenticator-lifecycle-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)

## Normative Ownership Boundary

This package is the canonical owner of the authenticator lifecycle governance surfaces represented by its packaged ADRs and SPECs. Adjacent packs may define integration profiles, but must reference these document identities instead of restating their normative requirements.
