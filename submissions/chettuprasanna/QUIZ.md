# Part 1 — the written half

Copy this whole file into your submission folder as `QUIZ.md`, then fill in your
answers. Do not delete the questions.

For the multiple choice, **write the letter**. For the blanks, **write the exact
word, flag or command** — spelling matters, because half of these are things you
will type.

---

## A · Multiple choice (10 marks, 1 each)

**1.** Where must a GitHub Actions workflow file live?
- a) `.github/actions/`
- b) `workflows/` in the repository root
- c) `.github/workflows/`
- d) anywhere, as long as it ends in `.yml`

**Answer:c

**2.** Two jobs in the same workflow, with no `needs:` between them, will:
- a) run at the same time, on separate machines
- b) run one after the other, in the order written
- c) run at the same time, on the same machine
- d) fail, because every job needs a `needs:`

**Answer:a

**3.** A step writes a file. A **different job** in the same workflow tries to read it. What happens?
- a) it reads the file normally
- b) it reads an empty file
- c) it depends on the runner
- d) it fails — the file does not exist

**Answer:d

**4.** What does `actions/checkout` do, and why is it almost always the first step?
- a) it installs your dependencies
- b) it clones your repository onto the runner, which otherwise does not have your code
- c) it checks the workflow file for syntax errors
- d) it logs in to the container registry

**Answer:b

**5.** In `docker run -p 9000:8080`, which number is the port **inside** the container?
- a) 8080
- b) 9000
- c) both
- d) neither — they must always match

**Answer:a

**6.** You edit only `app.py` and rebuild. Your Dockerfile copies `requirements.txt`
**before** copying `app.py`. What happens to the `RUN pip install` layer?
- a) it runs again from scratch
- b) the build fails
- c) it is reused from cache
- d) it runs, but faster

**Answer:c

**7.** Which of these survives `docker rm -f mycontainer`?
- a) files written inside the container
- b) files written to a mounted named volume
- c) both
- d) neither

**Answer:b

**8.** `EXPOSE 8080` in a Dockerfile:
- a) publishes port 8080 to your machine
- b) is required, or `-p` will not work
- c) opens the port in your firewall
- d) is documentation only — it publishes nothing

**Answer:d

**9.** A container and its host report **different** boot IDs but the **same** kernel version. Why?
- a) containers share the host's kernel; only their view of the system differs
- b) the container booted its own kernel
- c) the kernel version is copied into the image at build time
- d) it is a bug in Docker

**Answer:a

**10.** In the image name `ghcr.io/rajbeer1/coffee-api:v1`, what is `v1`?
- a) the registry
- b) the tag
- c) the owner
- d) the digest

**Answer:b

---

## B · Fill in the blanks (10 marks, 1 each)

**11.** The two flags you need together to get an interactive shell in a container
are `-` ______ and `-` ______ .

**Answer:-i -t

**12.** A Dockerfile instruction that runs at **build** time is ____RUN________ .
An instruction that runs when the container **starts** is ________CMD____ .

**Answer:RUN , CMD

**13.** The command that shows every image on your machine is
`docker ___images_________` .

**Answer: docker images

**14.** To make a workflow runnable from a button in the Actions tab instead of on
every push, the trigger is `on: _workflow_dispatch___________` .

**Answer:workflow_dispatch

**15.** To give one job a dependency on another finishing first, you add
`____needs________: <job-id>` to it.

**Answer: needs

**16.** In a GitHub Actions step, a shell command uses the key `_____run_______:`
while borrowing a published action uses the key `____uses________:` .

**Answer:run , uses

**17.** The built-in secret that already exists in every workflow run, with no
setup, is `secrets.__ GITHUB_TOKEN__________` .

**Answer:GITHUB_TOKEN

**18.** To let that token push an image to the registry, you must add
`permissions:` with `__packages__________: write` .

**Answer:packages

**19.** The command to give an existing image a second name before pushing it is
`docker _____tag______` .

**Answer: tag

**20.** A green tick on a test job that actually ran **no tests** usually means the
workflow is missing the _____pytest_______ step.

**Answer:pytest

---

## C · Two sentences each (10 marks, 5 each)

**21.** Your colleague says "a container is basically a lightweight virtual
machine". In your own words, say what is wrong with that.

**Answer:containers are not virtual machines because they do not contain a guest operating system and instead share the host system's kernel.
 while a virtual machines hardware virtualizes and  entire os, a container onlyy isolates application processes at the software level.

**22.** Explain why a Dockerfile copies `requirements.txt` on its own line, before
copying the rest of the code.

**Answer:docker copies requirements.txt on its own line to leverage layer caching and speed up builds. By doing this, 
docker only reinstalls dependencies when the requriments.txt  changes, preventing slow downloads every time application code is modified.
