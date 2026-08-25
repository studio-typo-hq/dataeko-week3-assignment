# Week 3 assignment — build the pipeline, ship the image

**Due:** before Session 1 of Week 5.
**Time:** about 90 minutes. If you are past two hours, stop and message me.

Two halves. The first is written and tests whether the ideas landed. The second is
the real thing: **you take an API we give you, and you build everything around it
that makes it shippable.**

Everything uses only what we did in Week 3. Nothing new.

---

## What we give you

```
app/
  app.py             a small Flask API — do not change it
  test_app.py        five tests — do not change these either
  requirements.txt   flask and pytest
```

The API has three endpoints:

```
GET /health          -> {"status":"ok"}
GET /orders          -> all four orders
GET /orders/2        -> one order
GET /orders/99       -> 404
```

**You do not write any Python.** Your job is everything around it.

---

## Part 1 — the written half (30 marks)

Open **`QUIZ.md`**. It has ten multiple choice, ten fill-in-the-blanks, and two
short questions.

Copy it into your submission folder and fill in your answers there. Answer from
memory first, then check — you learn more that way, and I cannot tell the
difference anyway.

---

## Part 2 — the pipeline (60 marks)

### Step 1 — write a `Dockerfile`

In the root of your fork. It must:

- start from `python:3.13-slim`
- install from `app/requirements.txt`
- copy in `app/app.py`
- run the API when the container starts
- **order its layers so that changing `app.py` does not reinstall the dependencies**

That last point is worth marks on its own. Prove it to yourself: build, edit
`app.py`, build again, and look for `CACHED` on the pip line.

Check it works before you go near CI:

```bash
docker build -t coffee .
docker run --rm -p 9000:8080 coffee
curl localhost:9000/health
```

### Step 2 — write a workflow

`.github/workflows/ci.yml` in your fork. It must have **two jobs**:

**Job one — `test`**
- checks out the code
- sets up Python
- installs `app/requirements.txt`
- runs `pytest`

**Job two — `publish`**
- **only runs if `test` passed** — this is what `needs:` is for
- logs in to `ghcr.io` using the token that already exists in every run
- builds your image
- pushes it to `ghcr.io/<your-github-username>/dataeko-week3-assignment`,
  **tagged with your own GitHub username**

You will need a `permissions:` block. Work out which one from Week 3.

> **Registry names must be entirely lowercase.** If your GitHub username has any
> capital letters, `ghcr.io/YourName/...` is rejected outright with
> `invalid reference format: repository name must be lowercase`. Lowercase it in
> the workflow rather than typing it by hand:
>
> ```yaml
> - run: echo "IMAGE=ghcr.io/${GITHUB_REPOSITORY,,}" >> $GITHUB_ENV
> - run: docker build -t $IMAGE:<your-username-in-lowercase> .
> ```
>
> The `,,` is bash's lowercase expansion. Use the lowercase form in `LINK.md` too.

### Step 3 — make your package public

Your image lands on your GitHub **profile, under Packages** — not in the
repository. Open it, go to **Package settings**, and change visibility to
**public**.

**If you skip this I cannot pull your image and you lose the marks for it.**

### Step 4 — prove it works

From your own machine, pull your published image and run it:

```bash
docker pull ghcr.io/<your-username>/dataeko-week3-assignment:<your-username>
docker run --rm -p 9000:8080 ghcr.io/<your-username>/dataeko-week3-assignment:<your-username>
curl localhost:9000/orders/2
```

---

## What to hand in

Fork this repository, branch, and open a pull request adding **one folder**:

```
submissions/<your-github-username>/
  QUIZ.md          your answers
  Dockerfile       a copy of yours
  ci.yml           a copy of your workflow
  LINK.md          see below
```

`LINK.md` needs exactly three things:

```markdown
Image:    ghcr.io/<your-username>/dataeko-week3-assignment:<your-username>
Workflow: <link to a green run in your fork's Actions tab>
Package:  <link to your package page>
```

**Do not commit `venv/` or `__pycache__/`.** There is a `.gitignore` already.

### The Git bit

```bash
# 1. Fork this repo on GitHub

git clone https://github.com/<your-username>/dataeko-week3-assignment.git
cd dataeko-week3-assignment
git checkout -b week3-<your-username>

# 2. Add your Dockerfile and .github/workflows/ci.yml, and push —
#    the workflow only runs once it is on GitHub

# 3. Once it is green, add your submissions/<username>/ folder

git add .
git commit -m "Week 3 submission: <your name>"
git push origin week3-<your-username>

# 4. Open a pull request back to this repository
```

---
