# Telegram Adapter

## Purpose

Accept remote owner commands through Telegram.

## Runtime Target

Telegram bot API.

## Capabilities

- Receive text commands.
- Receive attachments.
- Send status replies.
- Send approval prompts.

## Inputs

- Telegram user ID.
- Message text.
- Files, images, or voice notes.

## Outputs

- Task records.
- Status messages.
- Approval requests.

## Permissions

- Allow only approved operators.
- Reject unknown users.

## Invocation

Map each message to the common task intake flow.

## Failure Modes

- Unknown user.
- Missing bot token.
- Attachment download failure.

## Logging

Log message ID, task ID, user ID, and redacted text.

## Verification

Send a test command and confirm task creation.

## Handoff Mapping

Map Telegram messages to task records.

Map task status back to Telegram replies.
