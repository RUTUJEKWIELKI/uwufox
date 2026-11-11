# UwUfox CI — optional Cirun runners

Cirun is an **optional** runner backend for the six cross-platform build jobs.
The default remains `ubuntu-24.04` (GitHub-hosted) until you explicitly
choose Cirun in **Actions → Uwufox Build Pipeline → Run workflow → runner: cirun**.

## Important: cloud charges

Cirun Open Source is free to use, but it provisions virtual machines and disks
**in your cloud provider account**. Those resources can be billable. Nothing in
this branch automatically switches scheduled/push builds to paid cloud machines.

## Setup

1. In https://cirun.io, connect the GitHub App and activate `RUTUJEKWIELKI/uwufox`.
2. Connect an AWS/GCP/Azure/Oracle/etc. cloud account in the Cirun dashboard.
3. Create `.cirun.yml` in the repository root with **your actual provider's**
   `cloud`, `instance_type`, `machine_image`, `region`, and label
   `cirun-uwufox-build`. See `.cirun.yml.example` for a GCP example only.
   The GCP example requests an 8-vCPU / 32-GiB VM with a 200-GB root disk.
   These resources can incur cloud charges.
4. Run the `Uwufox Build Pipeline` **manually**, selecting `runner: cirun`.
5. Inspect runner startup and build artifacts. Only consider changing the
   default on push after a successful test and a cost review.

## How it works

Only the matrix `compile` job changes runner:

```yaml
runs-on: ${{ inputs.BUILD_RUNNER == 'cirun' && format('cirun-uwufox-build--{0}-{1}', github.run_id, matrix.platform) || 'ubuntu-24.04' }}
```

Each job gets a distinct suffix so it is assigned a separate Cirun VM.
Metadata and asset preparation stay on standard GitHub-hosted runners.
`maximize-build-space` is skipped on Cirun; configure enough disk in
`.cirun.yml` instead.

The current build cross-compiles all six platforms **from Linux x86_64**,
including Windows and macOS, so choose an x86_64 Ubuntu VM.
ARM64 runner support in Cirun does **not** mean these cross-compile jobs should
automatically run on ARM64 hardware.

Official docs:
- https://docs.cirun.io/quickstart
- https://docs.cirun.io/reference/yaml
- https://docs.cirun.io/reference/unique-runner-labels
