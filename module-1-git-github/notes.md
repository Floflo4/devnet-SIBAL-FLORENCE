# Module 1 — Git & GitHub

**Student:** [Florence Z. Sibal]
**Date:** [09/27/2026]

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

- first you need to learn first the basic like git add, commit, and push with that basics command you will had a basic knowledge about git command. and second I will not pressure you with the other commands because it will overwhelmed you from learning it.

[Write your own explanation here. What problem does Git actually solve? How is GitHub different from Git itself?]

-Git is like a time machine for your code. It keeps track of changes, so you can easily go back to an earlier version and work with others without losing your progress. GitHub, on the other hand, is an online platform that uses Git to store your projects and makes it easier to share and collaborate with other people over the internet.

---

## Key vocabulary (in your own words)

- repository: this is the folder where the changes made in my project.  
- commit: when you type commit in git terminal you are telling that you have a updated code or work bacause you need to updt the commit text everytime you have changes.
- branch: a separate version of your project where you can work on changes without affecting the main code.
- push / pull: sends your changes to the online repository, while pull gets the latest changes from it.
- pull request: a request to add your changes to the main project after others review them.
- merge conflict: a problem that happens when Git finds different changes in the same art of a file and doesn’t know which one to keep.

---

## Walking through what I did

[Describe, step by step, a real branch → commit → push → PR you did. Include the actual commands you used.]
- I create a branch because I'll work on a specific topic, and made changes un my project and commit it, and push the branch to Github.
```
# paste your actual commands here
```
git checkout -b flo/update-homework
git add .
git commit -m "Updated homework"
git push -u origin flo/update-homework

---

## A mistake I made (or one I want to avoid)

[What tripped you up? A confusing error message, committing to the wrong branch, a merge conflict — explain it so a classmate reading this avoids the same mistake.]

-The part that confused me was making sure I was on the correct branch before committing my changes. Next time, I’ll check my current branch with git branch before making a commit to avoid putting changes in the wrong place.

---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]

-Version control is similar to saving different versions of a file, but it makes it easier to track changes, work with others, and go back if something goes wrong.
