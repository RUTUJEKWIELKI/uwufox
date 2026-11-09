<p align="center">
  <img src="waterfox/browser/branding/default256.png" alt="Uwufox fox logo" width="112">
</p>

<h1 align="center">Uwufox</h1>

<p align="center">A desktop browser built on Mozilla Firefox.</p>

<p align="center">
  <a href="https://github.com/RUTUJEKWIELKI/uwufox/actions/workflows/uwufox.yml">
    <img src="https://github.com/RUTUJEKWIELKI/uwufox/actions/workflows/uwufox.yml/badge.svg" alt="Uwufox Build status">
  </a>
  <a href="https://github.com/RUTUJEKWIELKI/uwufox/releases/latest">
    <img src="https://img.shields.io/github/v/release/RUTUJEKWIELKI/uwufox?label=latest%20release" alt="Latest Uwufox release">
  </a>
</p>

<p align="center">
  <a href="#downloads">Downloads</a> ·
  <a href="#build-from-source">Build from source</a> ·
  <a href="https://github.com/RUTUJEKWIELKI/uwufox/issues">Report an issue</a>
</p>

## Downloads

Get the latest release from **[GitHub Releases](https://github.com/RUTUJEKWIELKI/uwufox/releases/latest)**.

| Platform | Release files |
| --- | --- |
| Linux x86-64 and ARM64 | `.tar.xz` packages |
| Windows x86-64 and ARM64 | Setup `.exe`, `.zip` package, and SHA-512 checksums |
| macOS Intel and Apple Silicon | `.tar.xz` archives containing the app bundle |

Each release also includes update packages and manifests. Build checksums are provided as `SHA512SUMS-*.txt` files.

## Releases and updates

The **Uwufox Build** workflow builds on pushes and pull requests. Actions artifacts are kept for 30 days. After a successful push to the default branch—including a merged pull request—the workflow creates a GitHub Release and a numeric version tag.

Tags increment the patch version and include the GitHub Actions run number to keep builds unique. For example, with `153.7.0` in `browser/config/version.txt`, an automatic tag looks like `153.7.1.<run-number>`.

To publish manually, run **Uwufox Release** from the Actions tab and enter a numeric release tag matching `browser/config/version.txt`.

Release builds use the latest GitHub Release for updates. Local development builds use a local test update URL instead.

## About unsigned builds

Uwufox releases do not require code-signing or MAR-signing credentials. Packages and update files are unsigned:

- Windows may show a SmartScreen warning. Updating an installation requires write access to its folder; the Windows maintenance service is disabled.
- macOS builds are not notarized, so Gatekeeper may ask you to approve the app the first time you open it.
- The updater accepts unsigned MAR files from this repository. Only publish trusted commits and protect release permissions.

## Build from source

The following commands prepare and build Uwufox on Linux:

```sh
./mach bootstrap --application-choice browser --no-interactive
scripts/fetch-clang-23.sh
./mach build
./mach package
```

The packaged application is written under `obj-*/dist/uwufox/`. See the [Firefox Source Docs](https://firefox-source-docs.mozilla.org/) for details about the shared Mozilla build system.

## Contributing

Bug reports and project questions are welcome in [GitHub Issues](https://github.com/RUTUJEKWIELKI/uwufox/issues). Uwufox-specific changes live alongside the Mozilla platform code in this repository.

---

Uwufox is an independent project built on Mozilla Firefox. Mozilla and Firefox are trademarks of the Mozilla Foundation.
