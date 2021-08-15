# Contributing

## Commit Message Convention

> The main reference is [Conventional Commits website](https://www.conventionalcommits.org/en/v1.0.0/)

A commit message consists of a **header**, **body** and **footer**. The header
has a **type**, **scope** and **subject**:

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

The **header** is mandatory and the scope is **optional**.

### Type

Must be one of the following:

* **build**: Changes that affect the build system
* **ci**: Changes to our CI configuration files and scripts
* **chore**: Other changes that don't modify source or test files
* **docs**: Documentation only changes
* **feat**: A new feature
* **fix**: A bug fix
* **perf**: A code change that improves performance
* **refactor**: A code change that neither fixes a bug nor adds a feature
* **test**: Adding missing tests or correcting existing tests

### Scope

The scope specify the place of the commit change. Since we're working with C++,
it will often by the class concerned by the change. For example `mdBook`
, `problem_0001`, etc.

### Subject

The subject should be a quick summary in present tense. Do not capitalize the
first letter nor add a dot at the end.

### Body

As in **subject** use the imperative tense: "change" not "changed" nor
"changes". The body should include the motivation for the change.

### Footer

The footer should contain any information about **Breaking Changes**.
**Breaking Changes** should start with the work `BREAKING CHANGE:` with a space
or two newlines.

### Revert

If the commit reverts a previous commit, it should begin with revert followed by
the header of the reverted commit. The body should say: `This reverts commit
<hash>.`:

```
revert: <header of the reverted commit>

This reverts commit <hash>.
```

### Examples

```
ci: fix deploy issue when merging on main

chore(gitignore): ignore idea configuration files

docs(mdBook): add solution to problem 2

feat(0003): add naive solution

perf(0001): find the solution in O(1)

refactor(0005): replace list by list comprehension
```

## Branch Naming Convention

A branch name consists of a **type** and a **scope**, separated by dashes.

```
<type>-<scope>
```

## Pull Request Naming Convention

The pull request title consists of a **type**, **scope** and **subject**:

```
<type>(<scope>): <subject>
```

There's no requirement for the comment.

## Merge Commit Message Convention

The merge commit message should be the **same as the pull request title**,
followed by the **pull request number between parenthesis**.

```
type(<scope>): <subject> (#<pull request number>)
```

### Examples

```
chore(pre-commit): add pre-commit config and hooks (#42)
```

## Issues

There's no particular conventions for issues, provide as much information as
possible.

## Links and documentation

* [Conventional Commits website](https://www.conventionalcommits.org/en/v1.0.0/)
* [Commit Convention from discord.js](https://github.com/discordjs/discord.js-next/blob/master/.github/COMMIT_CONVENTION.md)
* [`CONTRIBUTING.md` from Angular](https://github.com/angular/angular/blob/master/CONTRIBUTING.md)
* [Conventional changelog from Angular](https://github.com/conventional-changelog/conventional-changelog/tree/master/packages/conventional-changelog-angular)