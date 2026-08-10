# authenticator-lifecycle-governance-pack

Governance for AAL, authenticator binding, activation, replacement, recovery, reset, revocation, failure controls, and authentication evidence.

## Package identity

- Pack ID: `pack:authenticator-lifecycle`
- PyPI distribution: `authenticator-lifecycle-governance-pack`
- Python import: `authenticator_lifecycle_governance_pack`
- Reservation owner: `extension-pack:authenticator-lifecycle-governance-pack`

## Normative ownership

This package is the canonical owner of the governance surfaces represented by its packaged ADRs and SPECs. Adjacent governance packs reference these documents rather than restating their requirements.

## Install

```bash
uv add authenticator-lifecycle-governance-pack
uv run ssot pack sync . authenticator_lifecycle_governance_pack --all --trust --yes
uv run ssot validate .
```

## Authority sources

- https://pages.nist.gov/800-63-4/sp800-63b.html
