# Introduction to AI-SDLC: demo and exercise files

One folder per implementation module. Each module folder has:

- `demos/`: the files shown in the module's two demo videos, a `README.md` describing them, and `demo-prompts.md` with every prompt pasted into Claude Code
- `<exercise>-starter/`: the exercise's `INSTRUCTIONS.md` and starter files
- `solution/`: the completed solution files

| Module | Folder | Exercise |
|---|---|---|
| Apply the Four Guiding Principles to AI-Assisted Workflows | `four-guiding-principles/` | Map the team's week and direct the release checklist |
| Apply AI Oversight in Planning | `ai-oversight-in-planning/` | Score a supplied plan and estimate |
| Evaluate AI-Generated Requirements Artifacts | `requirements-artifacts/` | Score the clinic's user stories, then direct your own |
| Evaluate AI-Generated Design Artifacts | `design-artifacts/` | Score the vendor's sketch, direct your own, and decide between two |
| Evaluate AI-Generated Code and Test Suites | `code-and-test-suites/` | Review pull request #412 |
| Apply Responsible Use Across Deployment and Maintenance | `deployment-and-maintenance/` | A late fee charged a day early |

The exercises reuse the lab materials from the instructor-led course AIC-1001: Alder Box (Lab 1), Cedar Clinic (Lab 2) and Ledgerline (Lab 3). The instructor answer keys are not included here.

---

# Purpose of This Repo

This repo is the source of truth for all exercises in this course.

> IMPORTANT!  Please remove these instructions before sharing this repo with learners.

## Folder Structure

This repo contains one folder for each module and each module folder contains subdirectories for exercises:

```bash
module-#-name/
├── exercise-name-starter/
│   └── INSTRUCTIONS.md
└── solution/
    └── .gitkeep
```

- `exercise-name-starter/` - Contains the starter files and instructions for the exercise (INSTRUCTIONS.md template provided)
- `solution/` - Contains the solution files for the exercise.

> **Note:** The `.gitkeep` file in the solution folder preserves the directory structure in the repository when the folder is empty. It should be removed when one or more solution files have been added to this folder.

Eight module folders have been provided as a template; However, you may need to add more or possibly use less than eight depending on what is needed. If you require an additional module folder, you can make a copy of an existing folder and paste it into the root directory.

As you build the exercises, the module and exercise folder names should be changed to reflect the content e.g.,

- python-basics/simple-calculator-starter
- object-oriented/classes-vs-instances-starter
- web-development/simple-api-starter
- error-handling/try-catch-practice-starter
- ai-agents/fact-checker-agent-starter

> ⚠️ **DO NOT NUMBER the exercises!**
> Our modular content may be used in more than one program where the order and number of exercises may differ from the order and number in the primary build.

## Resources for Building Exercises

The [Exercise Creation Resources](Exercise%20Creation%20Resources/) folder contains essential guidelines and standards for creating high-quality, accessible, and engaging exercises. These resources ensure consistency and help you follow best practices when developing course content.

### [Exercise Guidance.md](Exercise%20Creation%20Resources/Exercise%20Guidance.md)

Comprehensive guide covering exercise design principles, instruction writing, starter and solution code best practices, and requirements for solution videos and text. This is your primary resource for understanding what makes an effective exercise.

### [Accessibility Standards.md](Exercise%20Creation%20Resources/Accessibility%20Standards.md)

Details the WCAG 2.1 AA accessibility standards that all content must meet, including guidelines for headings, alt text, hyperlinks, color contrast, and avoiding images of text. Ensures exercises are accessible to all learners regardless of their abilities or use of assistive technology.

### [Real-World Content Guidelines.md](Exercise%20Creation%20Resources/Real-World%20Content%20Guidelines.md)

Guidelines for using real-world examples, company logos, trademarks, and references to people and organizations in exercises. Covers when it's appropriate to use actual brands versus creating fictitious examples and how to avoid legal and ethical issues.

### [Third Party Images and Datasets.md](Exercise%20Creation%20Resources/Third%20Party%20Images%20and%20Datasets.md)

Requirements for using third-party content including licensing requirements (Creative Commons, public domain), attribution standards, and approved sources for images, coding libraries, and datasets. Lists acceptable and unacceptable license types for commercial educational use.
