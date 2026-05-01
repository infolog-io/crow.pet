# Public Export Obfuscation Pattern Adapter

## Purpose

Reduce casual disclosure in public exports.

## Runtime Target

Public skill packs, generated helpers, and adapter bundles.

## Capabilities

- Replace private names with aliases.
- Strip local paths from generated artifacts.
- Bundle generated helper scripts.
- Minify generated helper scripts.
- Remove comments that reveal private context.
- Keep private source maps out of public exports.

## Inputs

- Export profile.
- Alias map.
- Generated artifact list.
- Public target path.
- Privacy review checklist.

## Outputs

- Public-safe artifact set.
- Alias replacement report.
- Obfuscation report.
- Residual disclosure notes.

## Permissions

- Never store secrets in generated code.
- Never rely on obfuscation for security.
- Keep readable source in the private instance.
- Ask before publishing an export.

## Invocation

Run after target export generation.

Run before public package publishing.

Run again after any generated helper changes.

## Failure Modes

- Alias map misses a private identifier.
- Minification breaks a helper script.
- Source maps leak private paths.
- Obfuscation hides attribution or license text.

## Logging

Log alias count, generated file count, and skipped files.

Do not log private values replaced by aliases.

## Verification

Search exports for private paths.

Search exports for company-only names.

Run generated helper smoke tests.

Confirm license notices remain readable.

## Handoff Mapping

Map public artifact paths into `artifacts`.

Map residual disclosure notes into the handoff report.
