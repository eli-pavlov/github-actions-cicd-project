<div align='center'>
<img src="https://raw.githubusercontent.com/eli-pavlov/github-actions-cicd-project/master/docs/githubactions2.png" width=320 />
<h1> GitHub Actions CI/CD Internship Project</h1>

<p> A complete GitOps-based Kubernetes CI/CD pipeline using GitHub Actions, Argo CD, Docker, SonarCloud, and Snyk. </p>

<h4> <span> · </span> <a href="https://github.com/eli-pavlov/github-actions-cicd-project/blob/master/README.md"> Documentation </a> <span> · </span> <a href="https://github.com/eli-pavlov/github-actions-cicd-project/issues"> Report Bug </a> <span> · </span> <a href="https://github.com/eli-pavlov/github-actions-cicd-project/issues"> Request Feature </a> </h4>

$\~\~\$

</div>

## \:world\_map: Project Diagram

<img src="https://github.com/eli-pavlov/github-actions-cicd-project/blob/master/docs/rtproject-diagram.png" width=1080 />

$\~\$

\:notebook\_with\_decorative\_cover: Table of Contents

* [Project Diagram](#world_map-project-diagram)
* [About the Project](#star2-about-the-project)
* [CI/CD Workflow Overview](#gear-workflow-overview)
* [How to Set It Up](#wrench-how-to-set-it-up)
* [Project Structure](#open_file_folder-files)
* [Secrets and Environments](#lock-secrets-and-environments)
* [License](#warning-license)
* [Contact](#handshake-contact)
* [Acknowledgements](#gem-acknowledgements)

$\~\~\$

## \:star2: About the Project

This project delivers a production-grade CI/CD pipeline for a Python Flask web app, as part of a DevOps internship assignment.

**Goals:**

* Implement modern CI/CD practices using GitHub Actions.
* Support both development and production deployment workflows.
* Enforce code quality and security via SonarCloud and Snyk.
* Deploy to Kubernetes clusters via GitOps using Argo CD.
* Apply semantic Docker image tagging based on branch.

**Key Decisions:**

* **CI Tool: GitHub Actions** — Tight integration with GitHub, cost-effective, strong ecosystem.

| Feature                  | Justification                                                                 |
|--------------------------|-------------------------------------------------------------------------------|
| 💰 **Cost-effective**     | Free for public repositories with generous free tier for private projects.    |
| 🔗 **Native GitHub Integration** | Directly integrates with pull requests, branches, and commits. No external setup needed. |
| 🧰 **Rich Ecosystem**       | Thousands of pre-built actions in the [GitHub Marketplace](https://github.com/marketplace/actions) for Docker, SonarCloud, Argo CD, and more. |
| 👨‍💻 **Developer-Friendly** | Clean YAML configuration with commit history, rollback, and branch-based logic. |
| 🔒 **Security**           | Secure handling of secrets and support for [GitHub Environments](https://docs.github.com/en/actions/deployment/targeting-different-environments) with required approvals. |
| ⚙️ **Scalability & Extensibility** | Supports parallel jobs, matrix builds, reusable workflows, and triggers on various GitHub events. |

GitHub Actions was therefore the best choice to deliver:
- A **fully automated CI/CD pipeline**,
- With **clear visibility in the GitHub UI**,
- And **minimal external tooling/setup** required.
$\~\$
**Other tools used:**

* **GitOps Tool: Argo CD** — Declarative Kubernetes deployment and version control.
* **Code Quality: SonarCloud** — Industry-standard static analysis.
* **Security: Snyk** — Detects vulnerabilities in IaC files.
$\~\$
* **Branching Strategy:**

  * `development`: Triggers full CI/CD pipeline and deploys automatically to dev.
  * `main`: Manual approval required, triggers deployment to production via Argo CD.

$\~\$

## \:gear: CI/CD Workflow Overview

### 1. **Lint-and-Test**

* Installs dependencies.
* Runs `flake8` for linting.
* Executes unit tests via `pytest` with coverage report.

### 2. **SonarCloud Analysis**

* Static code quality scan with full Git history.
* Uses SonarCloud GitHub action with secrets.

### 3. **Snyk IaC Scan**

* Analyzes Kubernetes manifests and Dockerfile.
* Ignores scan failures to allow developer review.

### 4. **Build and Push Docker Image**

* Builds multi-arch Docker images using QEMU and Buildx.
* Image tag:

  * `dev` for development branch
  * `latest` for production (main)
* Pushed to Docker Hub.

### 5. **Argo CD Deployment**

* Dev deploys automatically after push to `development`.
* Prod deploys automatically after push to `main`.
* Argo CD watches the corresponding overlay path:

  * `/manifests/overlays/development`
  * `/manifests/overlays/production`

### 6. **Slack Notification (Optional)**

* Posts status to Slack via webhook after build and deploy steps.

$\~\$

## \:wrench: How to Set It Up

### Prerequisites:

* GitHub repository
* DockerHub account
* SonarCloud and Snyk accounts (Optional)
* Kubernetes cluster with Argo CD installed and configured

### Steps:

1. **Fork or clone this repository**.
2. **Add GitHub Secrets** (see [Secrets and Environments](#lock-secrets-and-environments)).
3. **Install Argo CD** on your Kubernetes cluster (or use an existing instance).
4. **Apply the Argo CD applications**:

   ```bash
   kubectl apply -f manifests/argocd/application-dev.yaml
   kubectl apply -f manifests/argocd/application-prod.yaml
   ```
5. **Push to `development`** to auto-deploy to dev environment.
6. **Merge to `main`** and approve via GitHub environment to deploy to production.

$\~\$

## \:open\_file\_folder: Project Structure

```
github-actions-cicd-project/
├── Dockerfile
├── README.md
├── requirements.txt
├── src/
│   ├── app.py
│   ├── __init__.py
│   └── templates/index.html
├── tests/test_app.py
├── manifests/
│   ├── base/             # Base Kubernetes Deployment/Service
│   ├── overlays/
│   │   ├── development/  # Patched for dev (nodePort 30070)
│   │   └── production/   # Patched for prod (nodePort 30080)
│   └── argocd/           # Argo CD Application manifests
├── docs/
│   ├── *.png/pdf
└── .github/workflows/main.yml
```

$\~\$

## \:lock: Secrets and Environments

> Add these secrets under **GitHub repo settings** > **Secrets and variables** > **Actions**

| Secret Key           | Description                           |
| -------------------- | ------------------------------------- |
| `APP_NAME`           | Docker image/app name                 |
| `DOCKERHUB_USERNAME` | Docker Hub username                   |
| `DOCKERHUB_TOKEN`    | Docker Hub token                      |
| `SONAR_TOKEN`        | SonarCloud token                      |
| `SONAR_ORGANIZATION` | SonarCloud organization               |
| `SONAR_PROJECT_KEY`  | SonarCloud project key                |
| `SNYK_TOKEN`         | Snyk token                            |
| `SLACK_WEBHOOK_URL`  | (Optional) Slack Incoming Webhook URL |

**GitHub Environments**:

* **development**: Auto-deploys when code is pushed to `development`.
* **production**: Requires manual approval before executing workflow (set in GitHub).

$\~\$

## \:warning: License

Distributed under the Apache 2.0 License.

Please note: SonarCloud, Snyk, DockerHub, and Argo CD each have their own licensing terms.

$\~\$

## \:handshake: Contact

**Eli Pavlov**
[www.weblightenment.com](https://www.weblightenment.com)
[admin@weblightenment.com](mailto:admin@weblightenment.com)

Project Repo: [github-actions-cicd-project](https://github.com/eli-pavlov/github-actions-cicd-project)

$\~\$

## \:gem: Acknowledgements

* [Kubernetes.io](https://kubernetes.io/docs)
* [SonarCloud](https://www.sonarcloud.io)
* [Snyk](https://www.snyk.io)
* [DockerHub](https://hub.docker.com)
* [Argo CD](https://argo-cd.readthedocs.io/en/stable/)
* [Awesome GitHub README Generator](https://www.genreadme.cloud/)
