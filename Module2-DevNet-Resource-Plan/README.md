# IT0123 DevNet Resource Validation Plan

## Student and Project

- Name: Prince Myron B. Panlilio
- Section: TA31
- Repository name: `it0123-devnet-resource-plan`

## Purpose

Selecting the appropriate DevNet resource ensures that the available access, privileges, and learning materials match the requirements of a network-automation task. Making the correct selection also prevents unnecessary setup time and avoids using an environment that cannot safely support the intended activity.

## Validated Resource Decisions

### UC1 Quick Read Only API Exploration

- Selected resource: `always-on-sandbox`
- Decisive requirement: Immediate access to a shared environment for non-administrative API exploration
- Official evidence: https://developer.cisco.com/docs/sandbox/

An Always-On Sandbox fits because it provides immediate shared access without requiring a reservation or administrative privileges.

### UC2 Private Configuration Testing

- Selected resource: `reservation-sandbox`
- Decisive requirement: Private access and administrative privileges for testing configuration changes
- Official evidence: https://developer.cisco.com/docs/sandbox/

A Reservation Sandbox fits because it provides a private environment with administrative access. The team can also accept its reservation, VPN, and setup requirements.

### UC3 Guided API Concept Practice

- Selected resource: `learning-lab`
- Decisive requirement: Structured and guided learning for a beginner
- Official evidence: https://developer.cisco.com/learning/

A Learning Lab fits because the immediate objective is to learn API concepts through guided, step-by-step activities rather than independently configure devices.

### UC4 Reusable Automation Example

- Selected resource: `code-exchange`
- Decisive requirement: Access to existing repositories and network-automation examples
- Official evidence: https://developer.cisco.com/codeexchange/

Cisco Code Exchange fits because it allows the developer to examine existing Cisco and community code repositories before designing a new solution.

## AI Evaluation

I accepted ChatGPT's four resource classifications after comparing them with the official Cisco DevNet documentation. I modified the explanation for UC1 because the original reasoning did not clearly emphasize all its decisive requirements. The revised explanation identifies immediate access, a shared environment, and restricted administrative privileges as the reasons for selecting an Always-On Sandbox.

## AI Prompt Record

### UC1

**Prompt:** Which DevNet resource is suitable for immediate, shared, read-only API exploration without administrative changes or provisioning time?

**AI recommendation:** Use an Always-On Sandbox because it provides immediate shared access with restricted administrative privileges.

### UC2

**Prompt:** Which DevNet resource is suitable for private configuration testing that requires administrative access and permits reservation and VPN setup?

**AI recommendation:** Use a Reservation Sandbox because it provides a private environment with administrative access.

### UC3

**Prompt:** Which DevNet resource is suitable for a beginner who needs structured, step-by-step API instruction before working independently?

**AI recommendation:** Use a Learning Lab because it provides guided learning content for developing API knowledge and skills.

### UC4

**Prompt:** Which DevNet resource is suitable for finding existing Cisco and community network-automation code repositories?

**AI recommendation:** Use Cisco Code Exchange because it provides reusable code repositories and automation examples.

## Validation Evidence

- Validator result: `VALIDATION COMPLETE: 9/9 checks passed.`
- Command used: `python validate_plan.py`
- Official Cisco pages reviewed:
  - https://developer.cisco.com/docs/sandbox/
  - https://developer.cisco.com/learning/
  - https://developer.cisco.com/codeexchange/

## Git Evidence

- Initial commit message: `Set up initial DevNet Resource Plan`
- Validation commit message: `Complete and validate DevNet resource plan`
- Output of `git log --oneline`:

```text
046fa47 Complete and validate DevNet resource plan
9559076 Set up initial DevNet Resource Plan