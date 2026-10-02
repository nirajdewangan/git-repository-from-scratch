## Git Workflow – Step-by-Step Demonstration

This project demonstrates the complete Git workflow, from creating a local repository to publishing the commit history on GitHub.

### Step 1: Initialize Git

Open the project folder in VS Code Terminal.

```bash
git init
git branch -M main
git status
```

**Explanation:**

* `git init` initializes a new local Git repository.
* `git branch -M main` names the current branch `main`.
* `git status` shows the current working-tree state. Initially, project files appear as untracked because Git has not started tracking them.

### Step 2: Stage and Commit the Initial README

```bash
git add README.md
git status
git diff --staged
git commit -m "docs: initialize project with README"
```

**Expected observation:**

After `git add README.md`, Git displays README.md under **Changes to be committed**.

`git diff --staged` displays the README content being added.

### Step 3: Create Meaningful Commits

Track each Python module separately to demonstrate incremental development.

```bash
git add calculator.py
git commit -m "feat: add calculator operations"

git add student.py
git commit -m "feat: implement student management"

git add text_utils.py
git commit -m "feat: add text utility functions"

git add main.py
git commit -m "feat: integrate Python modules"
```

At this stage, five meaningful commits have been created, including the initial README commit.

### Step 4: Demonstrate git diff (Unstaged Changes)

Open `README.md` and temporarily add this line at the end:

```text
Learning Git helps developers track project changes.
```

Before staging the modification, run:

```bash
git status
git diff README.md
```

**Expected observation:**

`git status` shows README.md under **Changes not staged for commit**.

`git diff README.md` displays the newly added line with a `+` prefix.

This demonstrates how Git compares the working directory with the staging area.

### Step 5: Stage the Modification and Compare Again

```bash
git add README.md
git status
git diff
git diff --staged
```

**Expected observation:**

* `git status` now displays README.md under **Changes to be committed**.
* `git diff` shows no changes for README.md because its modification has been staged.
* `git diff --staged` displays the added line.

Now commit the change:

```bash
git commit -m "docs: demonstrate Git status and diff workflow"
```

### Step 6: Configure .gitignore

The `.gitignore` file prevents unnecessary generated files from being tracked.

Example:

```gitignore
__pycache__/
*.py[cod]
.venv/
venv/
.env
.DS_Store
*.log
```

Generate Python cache files by running:

```bash
python3 main.py
```

Verify the ignore rule:

```bash
git check-ignore __pycache__/
git status
```

The generated `__pycache__` directory should not appear among untracked files.

Commit the ignore rules:

```bash
git add .gitignore
git commit -m "chore: add Python gitignore configuration"
```

### Step 7: View Complete Commit History

```bash
git log
git log --oneline
```

`git log` displays detailed commit information, including commit hashes, authors, dates and messages.

`git log --oneline` displays a compact version of the history.

### Step 8: Publish the Repository on GitHub

Create an empty public GitHub repository named `git-repository-from-scratch`.

Do not initialize the remote repository with a separate README.

Connect your local repository:

```bash
git remote add origin https://github.com/YOUR_USERNAME/git-repository-from-scratch.git
```

Push the complete commit history:

```bash
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

### Step 9: Final Verification

```bash
git status
git log --oneline
git remote -v
```

**Expected result:**

* The working tree is clean.
* At least five meaningful commits are visible.
* The GitHub remote is correctly configured.
* The complete commit history is available in the public GitHub repository.


## Representative Git Terminal Transcript

The following is an **illustrative terminal session** showing the required command workflow and representative Git output. It demonstrates how to capture the workflow; it is not a recording of the original terminal session. Actual commit hashes may differ. The repository's published commit history can be checked using `git log --oneline`.

### Initialize and inspect the new repository

```console
$ git init
Initialized empty Git repository in .../git-repository-from-scratch/.git/
$ git branch -M main
$ git status
On branch main
No commits yet
Untracked files:
  README.md
  calculator.py
  student.py
  text_utils.py
  main.py
```

### Stage the README and make the initial commit

```console
$ git add README.md
$ git status
On branch main
No commits yet
Changes to be committed:
  new file:   README.md
$ git diff --staged -- README.md
diff --git a/README.md b/README.md
new file mode 100644
+... README content ...
$ git commit -m "docs: initialize project with README"
[main <commit-sha>] docs: initialize project with README
 1 file changed, ... insertions(+)
```

### Demonstrate an unstaged diff, then stage it

After creating the Python modules with separate commits, add this line temporarily to the end of README.md: `Learning Git helps developers track project changes.`

```console
$ git status
On branch main
Changes not staged for commit:
  modified:   README.md
$ git diff -- README.md
@@ ... @@
+Learning Git helps developers track project changes.
$ git add README.md
$ git status
On branch main
Changes to be committed:
  modified:   README.md
$ git diff -- README.md
# No output: the README change is staged, not unstaged.
$ git diff --staged -- README.md
@@ ... @@
+Learning Git helps developers track project changes.
$ git commit -m "docs: demonstrate Git status and diff workflow"
[main <commit-sha>] docs: demonstrate Git status and diff workflow
```

### Inspect actual history and publish

The repository contains these actual commits (abbreviated SHA, newest first as checked on GitHub):

```console
$ git log --oneline
76762c8 readme update
7aedbab chore: configure Python gitignore rules
4dacdc9 feat: integrate all Python modules
2ff6a4e feat: add reusable text utility functions
d1c169a feat: implement student management module
3d0fbd1 feat: add basic calculator operations
2976fea docs: initialize project with README
```

To push a local repository for the first time, connect the empty GitHub remote (skip `remote add` if already connected):

```console
$ git remote add origin https://github.com/nirajdewangan/git-repository-from-scratch.git
$ git push -u origin main
Enumerating objects: ...
Writing objects: 100% (.../...)
To https://github.com/nirajdewangan/git-repository-from-scratch.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
$ git status
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

**Note:** Output above is shortened for readability. The actual historical evidence accessible on GitHub is the commit graph and file diffs; local `status` and unstaged `diff` output cannot be reconstructed from published commits alone.