# MAR updates

MAR files contain browser updates. Uwufox builds accept unsigned MAR files, so
the release workflow does not need signing keys.

## Create an update

The release workflow packages the browser, creates a complete MAR, and writes
an update manifest pointing to the GitHub Release asset. The updater checks the
manifest and MAR over HTTPS.

## Development updates

The default developer configuration accepts unsigned updates from
`http://127.0.0.1:8000/update.xml`. Updating with this configuration does not test
the HTTPS release path. Use a disposable profile and installation.
