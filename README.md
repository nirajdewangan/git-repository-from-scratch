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
