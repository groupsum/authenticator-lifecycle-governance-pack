"""Inspect the installed pack identity."""

from authenticator_lifecycle_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:authenticator-lifecycle"
print(metadata["origin"]["id"])
