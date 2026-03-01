# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- John Wick Quotes: Added an option in Settings to show John Wick quotes instead of jokes on startup, or disable startup text entirely.
- Copy Note: Added a keyboard shortcut (`c`) in the "View All Notes" screen to copy a note's text to the clipboard.
- Clear All Notes: Users can now clear all saved notes from the "Settings" screen or via the CLI with `--clearnotes`.
- Edit Notes: Users can now edit existing notes by pressing `e` in the "View All Notes" screen.
- Pin Notes: Support for pinning important notes to the top of the list with the `p` key.
- Tagging/Categories: Automatic tag extraction (e.g., #work, #personal) from note text for better organization.
- Export Notes: Export all notes to a Markdown file with the `x` key.
- Expanded theme selection in Settings with 10+ new Textual themes (Nord, Dracula, Monokai, Tokyo Night, etc.)
- Follow XDG standards for writing app logs (Commit `392309a`)
- Add Dracula and all Catppuccin themes (Commit `5398ab7`)

dxd### Fixed
Fix wrong CLI version number (#82)
Make Itomori query lowercase for Github README support (`Commit` 8ba926e)

## [1.1.2] - 2026-02-01

### Added
- Add Changelog from (#58)
- Settings menu from (#55)
- Add new colorful badges and add many Python version support

## [1.1.1] - 2025-12-24

### Added
- Add 5 Recent Notes feature from (#52)


## [1.1.0] - 2025-12-03

### Added
- Add logging system
- Created a website for Itomori

### Changed
- Changed `Notes` page, it shows table view
- Improved documentation website, moved to `mk-docs`
- Improved `tcss` (styles) for Itomori

## [1.0.0] - 2025-11-19

### Added
- Multiple Themes support
- Live Notes Modal Screen for viewing saved notes [it shows raw `notes.json` file] and added `n` keybinding for viewing this page
- Version page for viewing the version and details for this app and added `v` keybinding for viewing this page
- Note input bar for adding notes, which also supports `enter` keybinding


[unreleased]: https://github.com/olivierlacan/keep-a-changelog/compare/v1.1.2`...HEAD
[1.1.1]: https://github.com/olivierlacan/keep-a-changelog/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/olivierlacan/keep-a-changelog/compare/v1.0.0...v1.1.0
[1.1.2]: https://github.com/olivierlacan/keep-a-changelog/compare/v1.1.1...v1.1.2
